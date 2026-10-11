"""make drift-check [GOLDEN=eval/golden/golden.yaml] [CONFIG=...]

Label health: a golden set is only valid for the corpus state it was written against. For every answerable question this checks, in the index the config points at
(overlay applied), whether each evidence document still exists and is still active. It does not retrieve and calls no model, so it can run on every corpus change.
  missing   the evidence document is not in this index at all
  retired   the document exists but its status is not active (the Module 3 status filter will hide it from retrieval)
A question is "broken" when NONE of its evidence documents is both present and active. "Degraded" means some are, some are not.
"""

import argparse
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--golden", default="eval/golden/golden.yaml")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    from app.common import load_config
    from app.retrieval.search import _chunks

    cfg = load_config()
    docs = {}
    for c in _chunks()["chunks"]:
        docs.setdefault(c["doc_id"], c["metadata"].get("status"))
    golden = yaml.safe_load((ROOT / args.golden).read_text(encoding="utf-8"))
    overlay = (cfg.get("corpus") or {}).get("overlay") or []
    print(f"index world: collection {cfg['vector_store']['collection']}, overlay rules {len(overlay)}, documents in this index {len(docs)}")
    print(f"golden file: {args.golden}")
    broken, degraded, rows = [], [], []
    for g in golden:
        if not g.get("answerable", True):
            continue
        ev = [e["doc_id"] for e in g.get("evidence") or []]
        state = [("missing" if d not in docs else ("ok" if docs[d] == "active" else "retired")) for d in ev]
        good = state.count("ok")
        if ev and good == 0:
            broken.append(g["id"]); rows.append((g["id"], "BROKEN", Counter(state)))
        elif good < len(ev):
            degraded.append(g["id"]); rows.append((g["id"], "degraded", Counter(state)))
    n = sum(1 for g in golden if g.get("answerable", True))
    print(f"answerable questions {n}: broken {len(broken)}, degraded {len(degraded)}, healthy {n - len(broken) - len(degraded)}")
    reasons = Counter(k for _, _, c in rows for k in c if k != "ok")
    print(f"evidence documents not usable by reason: {dict(reasons)}")
    if args.list or len(rows) <= 25:
        for qid, kind, c in rows:
            print(f"  {kind:8s} {qid}  {dict(c)}")


if __name__ == "__main__":
    main()
