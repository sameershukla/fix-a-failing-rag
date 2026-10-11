"""Missing label check with the system's own retrieval (CLAUDE.md, "The missing label check").

For every answerable question, retrieve the top K chunks. A chunk is a candidate when it does not hold the labelled
evidence, comes from an authoritative document (status active, authority primary, implementation or observational) and
contains a line that shares at least half of its content words with an evidence passage. A person reads each candidate and
decides whether it also answers the question. Candidates are leads, not labels.

Run from the repo root:  .venv/bin/python eval/golden/missing_labels.py [--system app] [--k 20] [--min-overlap 0.5]
"""
import argparse
import importlib
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from eval.metrics.relevance import chunk_finds, locate_evidence  # noqa: E402

STOP = set("""the a an and or of to in on for with is are was be do does did how what when where which who why can i we you it its this that
these those at by from as if not no any there their they them our your my me about after before into than then so also have has had
will would should could may might must per get got just""".split())


def toks(s):
    return {w for w in re.findall(r"[a-z][a-z0-9_.]{3,}", s.lower()) if w not in STOP}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--system", default="app")
    ap.add_argument("--k", type=int, default=20)
    ap.add_argument("--min-overlap", type=float, default=0.5)
    args = ap.parse_args()
    search = importlib.import_module(f"{args.system}.retrieval.search")
    common = importlib.import_module(f"{args.system}.common")
    docs, meta = {}, {}
    for line in common.NORMALIZED.open(encoding="utf-8"):
        d = json.loads(line)
        docs[d["doc_id"]] = d["text"]
        meta[d["doc_id"]] = d["metadata"]
    golden = yaml.safe_load((ROOT / "eval/golden/golden.yaml").read_text(encoding="utf-8"))
    total = 0
    for n, g in enumerate(golden, 1):
        if not g["answerable"]:
            continue
        passages = locate_evidence(docs, g["evidence"])
        et = toks(" ".join(e["text"] for e in g["evidence"]))
        seen = set()
        for rank, h in enumerate(search.search(g["question"], args.k), 1):
            chunk = {"doc_id": h["doc_id"], "start_char": h["metadata"]["start_char"], "end_char": h["metadata"]["end_char"]}
            m = meta[h["doc_id"]]
            if any(chunk_finds(chunk, p) for p in passages):
                continue
            if m.get("status") != "active" or m.get("authority") not in ("primary", "implementation", "observational"):
                continue
            best, best_line = 0.0, ""
            for ln in docs[h["doc_id"]][chunk["start_char"]:chunk["end_char"]].split("\n"):
                lt = toks(ln)
                if len(lt) < 6:
                    continue
                o = len(lt & et) / len(lt)
                if o > best:
                    best, best_line = o, ln.strip()
            key = (h["doc_id"], best_line)
            if best >= args.min_overlap and key not in seen:
                seen.add(key)
                if total == 0 or True:
                    print(f"{g['id']}  rank {rank:>2}  {h['doc_id']}  overlap {best:.2f}\n      question: {g['question'][:90]}\n      line: {best_line[:170]}")
                total += 1
    print(f"\n{total} candidates for review")


if __name__ == "__main__":
    main()
