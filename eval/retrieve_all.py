"""Retrieve the top K chunks for every golden question and save them. Needs the index.

    python -m eval.retrieve_all --system baseline --golden eval/golden/golden.yaml --k 20 --out file.jsonl

Runs in its own process so a freshly rebuilt index is always read from disk.
"""
import argparse
import importlib
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--system", default="baseline")
    ap.add_argument("--golden", default="eval/golden/golden.yaml")
    ap.add_argument("--k", type=int, default=20)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    search = importlib.import_module(f"{args.system}.retrieval.search")
    common = importlib.import_module(f"{args.system}.common")
    config = common.load_config()
    chunks_file = common.chunks_path(config)
    if not chunks_file.exists() or not common.NORMALIZED.exists():
        sys.exit(f"missing chunks or normalized docs for {args.system}. Run: make ingest SYSTEM={args.system}")
    n_chunks = sum(1 for _ in chunks_file.open(encoding="utf-8"))
    n_indexed = search._load()["collection"].count()
    if n_chunks != n_indexed:
        sys.exit(f"stale index: {n_indexed} chunks indexed, {n_chunks} in {chunks_file.name}. Run: make ingest SYSTEM={args.system}")

    golden = yaml.safe_load((ROOT / args.golden).read_text(encoding="utf-8"))
    with Path(args.out).open("w", encoding="utf-8") as fh:
        for item in golden:
            hits = search.search(item["question"], args.k)
            rec = {"id": item["id"], "retrieved": [
                {"chunk_id": h["chunk_id"], "doc_id": h["doc_id"], "start_char": h["metadata"]["start_char"],
                 "end_char": h["metadata"]["end_char"], "score": round(h["score"], 4)} for h in hits]}
            fh.write(json.dumps(rec) + "\n")
    print(f"retrieved top {args.k} for {len(golden)} questions -> {args.out}")


if __name__ == "__main__":
    main()
