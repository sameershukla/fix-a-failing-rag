"""make judge-run RUN="<generation run id> [<second run id>]"

Judges every answer in a generation run with the faithfulness judge (config/judge.yaml): only chunks and answer, claims listed, code decides the verdict.
THE JUDGE IS NOT CALIBRATED (Lesson 4.2). Every number printed here says so.
With two runs, also prints the paired comparison per question: better (unfaithful -> faithful), worse, same, with a bootstrap 95% interval for the change
in unfaithful answers per 100. Answers with no verdict are left out of the faithfulness numbers and counted. Refusals are counted next to faithfulness.
Needs ANTHROPIC_API_KEY on a cache miss.
"""

import argparse
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from eval.judges.judge import judge, load_config  # noqa: E402

REFUSE = re.compile(r"(context|documents?|material|excerpts?) (doesn.t|does not|don.t|do not) (say|state|specify|mention|include|list|give|contain|cover|address|show)|"
                    r"(doesn.t|does not) (say|state|specify|mention|include|list|give|contain|cover|address)|not (mentioned|specified|stated|provided)|no (information|mention)|"
                    r"can.t (find|tell|say|give)|cannot (find|tell|say|give)", re.I)


def judge_run(run):
    cfg = load_config()
    rows = [json.loads(l) for l in (ROOT / "eval/runs" / run / "answers.jsonl").open(encoding="utf-8")]
    out = []
    for r in rows:
        j = judge([c["text"] for c in r["chunks"]], r["answer"], cfg)
        out.append({"id": r["id"], "answerable": r["answerable"], "verdict": j["verdict"], "problem": j.get("problem"), "refused": bool(REFUSE.search(r["answer"][:500])),
                    "truncated": r["stop_reason"] == "max_tokens", "output_tokens": r["output_tokens"],
                    "unsupported": [c["claim"] for c in j["claims"] if not c["supported"]]})
    (ROOT / "eval/runs" / run / "judged.json").write_text(json.dumps(__import__("ops.versioning", fromlist=["stamp"]).stamp({"judge": cfg["prompt_version"], "model": cfg["model"], "calibrated": False, "answers": out}), indent=1, ensure_ascii=False))
    return out


def summary(run, out):
    scored = [o for o in out if o["verdict"]]
    unf = [o for o in scored if o["verdict"] == "unfaithful"]
    ans = [o for o in out if o["answerable"]]
    print(f"{run}  (judge NOT CALIBRATED)")
    print(f"  answers {len(out)}, judged {len(scored)}, no verdict {len(out) - len(scored)}, unfaithful {len(unf)} ({100 * len(unf) / max(len(scored), 1):.1f} per 100 judged)")
    print(f"  refused: {sum(o['refused'] for o in out)} of {len(out)}; answerable questions refused: {sum(o['refused'] for o in ans)} of {len(ans)}; unanswerable refused: "
          f"{sum(o['refused'] for o in out if not o['answerable'])} of {sum(not o['answerable'] for o in out)}")
    print(f"  hit the output token limit: {sum(o['truncated'] for o in out)}; mean output tokens {sum(o['output_tokens'] for o in out) / len(out):.0f}")


def paired(a, b, name_a, name_b):
    A = {o["id"]: o for o in a}
    pairs = [(A[o["id"]], o) for o in b if o["id"] in A and A[o["id"]]["verdict"] and o["verdict"]]
    better = sum(x["verdict"] == "unfaithful" and y["verdict"] == "faithful" for x, y in pairs)
    worse = sum(x["verdict"] == "faithful" and y["verdict"] == "unfaithful" for x, y in pairs)
    same = len(pairs) - better - worse
    diffs = [(y["verdict"] == "unfaithful") - (x["verdict"] == "unfaithful") for x, y in pairs]
    rng = random.Random(0)
    boots = sorted(100 * sum(rng.choice(diffs) for _ in diffs) / len(diffs) for _ in range(2000))
    print(f"paired, {len(pairs)} questions judged in both: {name_a} -> {name_b}")
    print(f"  unfaithful: {better} better, {worse} worse, {same} same; change in unfaithful per 100 answers {100 * sum(diffs) / len(diffs):+.1f}, bootstrap 95% interval [{boots[50]:+.1f}, {boots[1949]:+.1f}]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("runs", nargs="+")
    args = ap.parse_args()
    results = [(r, judge_run(r)) for r in args.runs]
    for r, o in results:
        summary(r, o)
    if len(results) == 2:
        paired(results[0][1], results[1][1], results[0][0], results[1][0])


if __name__ == "__main__":
    main()
