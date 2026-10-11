"""make eval-latency [LIMIT=60] [CONFIG=...]

Times the retrieval side of one request, stage by stage, with no model call: embed the query, vector search, keyword search, rerank, then the security stages.
The first call in a fresh process is reported on its own (cold start: it loads the embedder, the reranker and the index). The rest are warm.
Uses the same seeded question sample as make eval-gen, so the runs line up. One machine, one run: read the numbers as this laptop's, not as a benchmark.
"""

import argparse
import json
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
STAGES = ["embed_query", "vector_search", "keyword_search", "rerank", "acl_check", "injection_filter", "redact"]


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, round(p * (len(xs) - 1)))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=60)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--warmup", type=int, default=3)
    args = ap.parse_args()
    t_import = time.perf_counter()
    from app.common import load_config
    from app.security.context import build_context
    from eval.generate import pick
    import_ms = (time.perf_counter() - t_import) * 1000

    golden = yaml.safe_load((ROOT / "eval/golden/golden.yaml").read_text(encoding="utf-8"))
    questions = pick(golden, None, args.limit, args.seed)
    rows = []
    for i, q in enumerate(questions):
        timings = {}
        t0 = time.perf_counter()
        build_context(q["question"], timings=timings)
        total = (time.perf_counter() - t0) * 1000
        rows.append({"id": q["id"], "total_ms": total, "stages": timings, "cold": i == 0})
    cold, warm = rows[0], rows[args.warmup + 1:]       # the first call is cold; the next few warm up caches and are not counted
    cfg = load_config()
    run_id = f"lat-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
    out = ROOT / "eval/runs" / run_id; out.mkdir(parents=True)
    (out / "record.json").write_text(json.dumps({"run_id": run_id, "kind": "latency", "model_calls": 0, "questions": len(rows), "warmup_calls_not_counted": args.warmup,
                                                 "import_ms": import_ms, "cold_first_call_ms": cold["total_ms"], "security": cfg.get("security"),
                                                 "retrieval": {k: cfg["retrieval"].get(k) for k in ("mode", "k", "candidates")}, "rerank": cfg["retrieval"].get("rerank")}, indent=1))
    (out / "calls.jsonl").write_text("\n".join(json.dumps(r) for r in rows))
    print(f"run {run_id}  retrieval side only, no model call. {len(warm)} warm calls measured ({args.warmup} warm up calls not counted)")
    print(f"import {import_ms:.0f} ms; first call in a fresh process (cold start) {cold['total_ms']:.0f} ms")
    tot = [r["total_ms"] for r in warm]
    print(f"{'stage':18s} {'median':>8s} {'p95':>8s} {'mean':>8s}   share of median total")
    med_total = statistics.median(tot)
    for s in STAGES:
        xs = [r["stages"].get(s, 0.0) for r in warm]
        if any(xs):
            print(f"{s:18s} {statistics.median(xs):7.1f}ms {pct(xs, .95):7.1f}ms {statistics.mean(xs):7.1f}ms   {100 * statistics.median(xs) / med_total:5.1f}%")
    other = [r["total_ms"] - sum(r["stages"].values()) for r in warm]
    print(f"{'other (fusion etc)':18s} {statistics.median(other):7.1f}ms {pct(other, .95):7.1f}ms {statistics.mean(other):7.1f}ms   {100 * statistics.median(other) / med_total:5.1f}%")
    print(f"{'TOTAL retrieval':18s} {med_total:7.1f}ms {pct(tot, .95):7.1f}ms {statistics.mean(tot):7.1f}ms")
    print(f"saved eval/runs/{run_id}/")


if __name__ == "__main__":
    main()
