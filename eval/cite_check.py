"""make cite-check RUN=<generation run id>

Checks every citation in a generation run with code (app/generation/citations.py): does the chunk exist, is the quote in it. Also counts uncited sentences.
Works on any run. On a run made with the plain prompt it finds no citations, which is the point of the comparison.
No model is called.
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.generation.citations import check  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    args = ap.parse_args()
    rows = [json.loads(l) for l in (ROOT / "eval/runs" / args.run / "answers.jsonl").open(encoding="utf-8")]
    out, tot = [], {"answers": len(rows), "with_citations": 0, "citations": 0, "passed": 0, "failed": 0, "answers_with_failed": 0, "answers_with_uncited": 0, "uncited_sentences": 0}
    for r in rows:
        c = check(r["answer"], r["chunks"])
        out.append({"id": r["id"], "answerable": r["answerable"], **c})
        tot["with_citations"] += c["citations"] > 0
        tot["citations"] += c["citations"]; tot["passed"] += c["passed"]; tot["failed"] += c["failed"]
        tot["answers_with_failed"] += c["failed"] > 0
        tot["answers_with_uncited"] += bool(c["uncited_sentences"]); tot["uncited_sentences"] += len(c["uncited_sentences"])
    (ROOT / "eval/runs" / args.run / "citation_check.json").write_text(json.dumps({"summary": tot, "answers": out}, indent=1, ensure_ascii=False))
    print(f"run {args.run}")
    print(f"answers {tot['answers']}, with at least one citation {tot['with_citations']}")
    pct = f"{tot['passed'] / tot['citations']:.3f}" if tot["citations"] else "n/a"
    print(f"citations {tot['citations']}: quote found in the cited chunk {tot['passed']} ({pct}), failed {tot['failed']} in {tot['answers_with_failed']} answers")
    print(f"uncited sentences (rough rule): {tot['uncited_sentences']} in {tot['answers_with_uncited']} answers, {tot['uncited_sentences'] / tot['answers']:.2f} per answer")
    for a in out:
        for f in a["failures"]:
            print(f"  FAIL {a['id']}: chunk {f['chunk']}: {f['why']}: \"{f['quote'][:90]}\"")


if __name__ == "__main__":
    main()
