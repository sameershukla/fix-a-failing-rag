"""Judge calibration tools (Lesson 4.2).

sheet    write eval/judges/calibration/sheet.md: every labeled item with the question, the chunks and the answer, and NO
         verdict, reason, origin or model name. A person types a verdict under each item without seeing the draft.
compare  read the verdicts typed in the sheet and compare them with the draft labels: agreement, kappa, and every disagreement.
sample, score  come later in the lesson (the judge itself is not built yet).
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CAL = ROOT / "eval/judges/calibration"
LABELS = CAL / (os.environ.get("JUDGE_LABELS", "labels") + ".yaml")   # JUDGE_LABELS=labels_pointer scores the pointer drafts
SHEET = CAL / "sheet.md"
MARK = "Your verdict (faithful or unfaithful):"


def load_labels():
    return yaml.safe_load(LABELS.read_text(encoding="utf-8"))


def chunk_texts(item):
    path = ROOT / "eval/runs" / item["answer_run"] / "answers.jsonl"
    for line in path.open(encoding="utf-8"):
        row = json.loads(line)
        if row["id"] == item["question_id"]:
            return {c["chunk_id"]: c["text"] for c in row["chunks"]}
    raise SystemExit(f"{item['id']}: question {item['question_id']} not found in {item['answer_run']}")


def sheet():
    items = load_labels()
    lines = ["# Faithfulness labeling sheet", "",
             "For each item, read the chunks, then the answer. Decide whether every claim in the answer is supported by the chunks.", "",
             "- **faithful**: every claim is stated in the chunks or follows directly from them (arithmetic, a plain reading). "
             "A true statement that the context does not cover something is faithful.",
             "- **unfaithful**: at least one claim is not supported by the chunks, or contradicts them.",
             "- Judge support only, not whether the source is the right one to trust. Do not use outside knowledge.",
             "- Do not open `labels.yaml` before you finish. Type one word after each `" + MARK + "` line, then run `make judge-compare`.", ""]
    for it in items:
        lines += ["---", "", f"## {it['id']}", "", f"**Question:** {it['question']}", "", "**Chunks the assistant was given:**", ""]
        for n, (cid, text) in enumerate(chunk_texts(it).items(), 1):
            lines += [f"Chunk {n} (`{cid}`)", "", "```", text.strip(), "```", ""]
        lines += ["**Answer:**", "", *["> " + l if l else ">" for l in it["answer"].split("\n")], "", f"**{MARK}** ", "",
                  "Unsupported claim, if any (optional, helps when we compare):", ""]
    SHEET.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {SHEET.relative_to(ROOT)}: {len(items)} items. Type your verdicts there, then run make judge-compare.")


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    cats = {c for p in pairs for c in p}
    pe = sum((sum(a == c for a, _ in pairs) / n) * (sum(b == c for _, b in pairs) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")


def compare():
    text = SHEET.read_text(encoding="utf-8")
    human = {}
    for block in re.split(r"\n---\n", text)[1:]:
        m_id = re.search(r"^## (L\d+)", block, re.M)
        m_v = re.search(re.escape(MARK) + r"\*\*\s*(\S+)", block)
        if m_id and m_v and m_v.group(1).lower() in ("faithful", "unfaithful"):
            human[m_id.group(1)] = m_v.group(1).lower()
    items = load_labels()
    missing = [i["id"] for i in items if i["id"] not in human]
    if missing:
        sys.exit(f"{len(missing)} items have no verdict yet: {', '.join(missing)}")
    pairs = [(human[i["id"]], i["verdict"]) for i in items]
    agree = sum(a == b for a, b in pairs)
    print(f"human vs claude draft on {len(items)} items: agreement {agree}/{len(items)} = {agree/len(items):.2f}, kappa {kappa(pairs):.2f}")
    print(f"human counts: {sum(a == 'unfaithful' for a, _ in pairs)} unfaithful, {sum(a == 'faithful' for a, _ in pairs)} faithful; "
          f"draft counts: {sum(b == 'unfaithful' for _, b in pairs)} unfaithful, {sum(b == 'faithful' for _, b in pairs)} faithful")
    for it in items:
        h = human[it["id"]]
        if h != it["verdict"]:
            print(f"\nDISAGREE {it['id']} ({it['question_id']}, {it['origin']}): human={h}, draft={it['verdict']}\n  draft reason: {it['reason']}")
    print("\nThis compares a person with the draft. It says nothing about the judge yet.")


def score(split):
    from datetime import datetime, timezone

    from eval.judges.judge import judge, load_config

    cfg = load_config()
    items = [i for i in load_labels() if i["split"] == split]
    rows = []
    for it in items:
        res = judge(list(chunk_texts(it).values()), it["answer"], cfg)
        rows.append({"id": it["id"], "question_id": it["question_id"], "origin": it["origin"], "human": it["verdict"], "judge": res["verdict"],
                     "claims": res["claims"], "problem": res.get("problem"), "stop_reason": res["stop_reason"]})
    scored = [r for r in rows if r["judge"]]
    tp = sum(r["human"] == "unfaithful" and r["judge"] == "unfaithful" for r in scored)
    fn = sum(r["human"] == "unfaithful" and r["judge"] == "faithful" for r in scored)
    fp = sum(r["human"] == "faithful" and r["judge"] == "unfaithful" for r in scored)
    tn = sum(r["human"] == "faithful" and r["judge"] == "faithful" for r in scored)
    agree = (tp + tn) / len(scored) if scored else float("nan")
    k = kappa([(r["human"], r["judge"]) for r in scored]) if scored else float("nan")
    recall = tp / (tp + fn) if tp + fn else float("nan")
    precision = tp / (tp + fp) if tp + fp else float("nan")
    print(f"judge {cfg['model']} prompt {cfg['prompt_version']} on {split}: NOT CALIBRATED (needs the test split to pass, with >= 15 human unfaithful labels)")
    print(f"items {len(rows)}, scored {len(scored)}, no verdict {len(rows) - len(scored)}; human unfaithful {tp + fn}, human faithful {fp + tn}")
    print(f"agreement {agree:.2f}  kappa {k:.2f}  unfaithful recall {recall:.2f} ({tp}/{tp + fn})  unfaithful precision {precision:.2f} ({tp}/{tp + fp})")
    for origin in ("natural", "seeded_edit"):
        sub = [r for r in scored if r["origin"] == origin and r["human"] == "unfaithful"]
        if sub:
            print(f"  caught {sum(r['judge'] == 'unfaithful' for r in sub)}/{len(sub)} {origin} unfaithful")
    for r in rows:
        if r["judge"] != r["human"]:
            print(f"\nDISAGREE {r['id']} ({r['question_id']}, {r['origin']}): human={r['human']}, judge={r['judge']} {r['problem'] or ''}")
            for c in r["claims"]:
                if not c["supported"] or r["human"] == "unfaithful":
                    print(f"   {'UNSUPPORTED' if not c['supported'] else 'supported  '}: {c['claim']}")
    out = CAL / "results"
    out.mkdir(exist_ok=True)
    name = f"{split}-{cfg['prompt_version']}-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}.json"
    (out / name).write_text(json.dumps({"split": split, "prompt_version": cfg["prompt_version"], "model": cfg["model"], "agreement": agree,
                                        "kappa": k, "recall": recall, "precision": precision, "counts": {"tp": tp, "fn": fn, "fp": fp, "tn": tn},
                                        "items": rows}, indent=1))
    print(f"\nsaved {(out / name).relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["sheet", "compare", "sample", "score"])
    ap.add_argument("rest", nargs="*")
    args, extra = ap.parse_known_args()
    args.rest = args.rest + extra
    if args.cmd == "sample":
        sys.exit("'sample' is not built yet.")
    if args.cmd == "score":
        split = args.rest[args.rest.index("--split") + 1] if "--split" in args.rest else "tune"
        return score(split)
    {"sheet": sheet, "compare": compare}[args.cmd]()


if __name__ == "__main__":
    main()
