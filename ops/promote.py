"""Turn bad production traces into REVIEWED golden cases (Lesson 8.5). Nothing here writes golden.yaml.

    make promote ARGS="flag <trace id> <reason>"        mark a trace as bad (a sidecar file next to the traces)
    make promote ARGS="candidates"                      build a review file from the flagged traces
    make promote ARGS="check <review file>"             validate a reviewed file and print the golden.yaml snippet and CHANGELOG line

The order is the point. A bad trace is a QUESTION, not a label. Before it can become a golden case, the missing label check (CLAUDE.md) comes first:
  1. is the question already in the golden set (exact, or a very close paraphrase)? Then it is not new.
  2. what does the system's own retrieval put in the top 20 from authoritative documents? Those are leads for the evidence, never the label.
  3. does the answer also live in other authoritative documents? List them, so the reviewer labels every passage that answers, not only the first one found.
A person then reads and fills the review block. `check` refuses a case with no named reviewer, no evidence, or a passage that is not verbatim in its document.
The golden change itself is made by hand, in its own commit, with a note in eval/golden/CHANGELOG.md (CLAUDE.md principle 5).
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
STOP = set("the a an and or of to in on for with is are was be do does did how what when where which who why can i we you it its this that these those at by from as if not no any there their they them our your my me about after before into than then so also have has had will would should could may might must per get got just".split())
AUTH_STATUS, AUTH_AUTHORITY = {"active"}, {"primary", "implementation", "observational"}


def words(s):
    return {w for w in re.findall(r"[a-z][a-z0-9_.]{3,}", s.lower()) if w not in STOP}


def paths(args):
    from app.trace import TRACE_PATH
    traces = Path(args.traces) if args.traces else TRACE_PATH
    return traces, traces.with_name("feedback.jsonl")


def flag(args):
    traces, fb = paths(args)
    ids = {t["trace_id"] for t in map(json.loads, traces.read_text().splitlines()) if t}
    if args.rest[0] not in ids:
        sys.exit(f"no trace {args.rest[0]} in {traces}")
    with fb.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"trace_id": args.rest[0], "label": "bad", "reason": " ".join(args.rest[1:]) or "unspecified", "time": datetime.now(timezone.utc).isoformat(timespec="seconds")}) + "\n")
    print(f"flagged {args.rest[0]}")


def candidates(args):
    from app.retrieval.search import _load, search
    from app.security.access import denied_groups, load_callers
    from app.retrieval.search import access_groups

    traces, fb = paths(args)
    bad = {}
    for l in fb.read_text().splitlines() if fb.exists() else []:
        r = json.loads(l); bad[r["trace_id"]] = r
    ts = [t for t in map(json.loads, traces.read_text().splitlines()) if t and t["trace_id"] in bad]
    golden = yaml.safe_load((ROOT / "eval/golden/golden.yaml").read_text(encoding="utf-8"))
    st = _load(); model = st["model"]; norm = st["config"]["embedding"]["normalize"]
    gvec = model.encode([g["question"] for g in golden], normalize_embeddings=norm)
    items = []
    for n, t in enumerate(ts, 1):
        q = t["question"]
        vec = model.encode([q], normalize_embeddings=norm)[0]
        sims = gvec @ vec
        best = int(sims.argmax())
        dup = {"golden_id": golden[best]["id"], "similarity": round(float(sims[best]), 3), "question": golden[best]["question"]} if sims[best] >= 0.85 else None
        caller = load_callers()[t["caller"]]
        hits = search(q, k=20, deny_groups=denied_groups(caller, access_groups()))      # what this caller could see, top 20
        auth = [h for h in hits if h["metadata"].get("status") in AUTH_STATUS and h["metadata"].get("authority") in AUTH_AUTHORITY]
        top = auth[0] if auth else None
        also = []
        if top:
            tw = words(top["text"])
            for h in auth[1:]:
                if h["doc_id"] != top["doc_id"] and tw and len(tw & words(h["text"])) / len(tw) >= 0.5:
                    also.append({"doc_id": h["doc_id"], "chunk_id": h["chunk_id"], "excerpt": h["text"][:200].replace("\n", " ")})
        items.append({"id": f"cand-{n:03d}", "question": q, "source": {"trace_id": t["trace_id"], "caller": t["caller"], "why_bad": bad[t["trace_id"]]["reason"]},
                      "possible_duplicate_of": dup,
                      "suggested_evidence": [{"doc_id": h["doc_id"], "chunk_id": h["chunk_id"], "score": round(h["score"], 2), "excerpt": h["text"][:300].replace("\n", " ")} for h in auth[:6]],
                      "also_check_other_documents": also,
                      "review": {"decision": None, "answerable": None, "evidence": [], "tags": [], "labeled_by": None, "note": ""}})
    out = ROOT / "eval/golden/candidates"; out.mkdir(parents=True, exist_ok=True)
    f = out / f"candidates-{datetime.now(timezone.utc):%Y%m%d-%H%M%S}.yaml"
    f.write_text("# Review file. Candidates are leads, not labels. Fill the review block, then run: make promote ARGS=\"check <this file>\"\n"
                 "# decision: approve | reject | duplicate. evidence: list of {doc_id, text} with the EXACT passage (every authoritative passage that answers).\n"
                 + yaml.safe_dump(items, sort_keys=False, allow_unicode=True, width=140), encoding="utf-8")
    print(f"{len(items)} candidates from {len(bad)} flagged traces -> {f.relative_to(ROOT)}")
    for it in items:
        d = it["possible_duplicate_of"]
        print(f"  {it['id']} {'DUPLICATE? ' + d['golden_id'] + ' (' + str(d['similarity']) + ')' if d else 'new':28s} suggested docs {len(it['suggested_evidence'])}, also check {len(it['also_check_other_documents'])}  | {it['question'][:60]}")


def check(args):
    f = ROOT / args.rest[0]
    items = yaml.safe_load(f.read_text(encoding="utf-8"))
    docs = {}
    for l in (ROOT / "data/app/normalized/docs.jsonl").open(encoding="utf-8"):
        d = json.loads(l); docs[d["doc_id"]] = d["text"]
    golden = {g["question"].strip().lower() for g in yaml.safe_load((ROOT / "eval/golden/golden.yaml").read_text(encoding="utf-8"))}
    ok, snippet = 0, []
    for it in items:
        r = it["review"]; problems = []
        if r["decision"] != "approve":
            print(f"  {it['id']}: decision {r['decision']!r}: not promoted"); continue
        if not r["labeled_by"]:
            problems.append("no named reviewer in labeled_by")
        if r["answerable"] and not r["evidence"]:
            problems.append("answerable but no evidence")
        for e in r["evidence"]:
            if e["doc_id"] not in docs:
                problems.append(f"document not found: {e['doc_id']}")
            elif e["text"] not in docs[e["doc_id"]]:
                problems.append(f"passage is not verbatim in {e['doc_id']}")
        if it["question"].strip().lower() in golden:
            problems.append("question is already in golden.yaml")
        if problems:
            print(f"  {it['id']}: REFUSED: " + "; ".join(problems)); continue
        ok += 1
        snippet.append({"id": "qNEW", "question": it["question"], "evidence": r["evidence"], "answerable": bool(r["answerable"]), "tags": r["tags"] + ["module-08"], "note": r["note"] or f"from trace {it['source']['trace_id']}"})
    print(f"{ok} of {len(items)} candidates ready")
    if snippet:
        print("\n--- add to eval/golden/golden.yaml (give each a real id), in its own commit ---")
        print(yaml.safe_dump(snippet, sort_keys=False, allow_unicode=True, width=140))
        print(f"--- add to eval/golden/CHANGELOG.md ---\n- add {ok} question(s) promoted from production traces; missing-label check run on each before approval (ops/promote.py)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["flag", "candidates", "check"])
    ap.add_argument("rest", nargs="*")
    ap.add_argument("--traces")
    args = ap.parse_args()
    {"flag": flag, "candidates": candidates, "check": check}[args.cmd](args)


if __name__ == "__main__":
    main()
