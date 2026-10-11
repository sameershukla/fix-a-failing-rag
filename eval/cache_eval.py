"""make eval-cache

Lesson 6.3, step one: how well can question similarity tell a paraphrase (reuse the stored answer) from a near miss (do not)? No model call.
For each pair in eval/cache/pairs.yaml: embed the base question, its paraphrase and its near miss with the retrieval embedder, take the cosine similarity,
and sweep a threshold. Pairs are split into dev (even positions) and held out (odd positions). Pick the threshold on dev; read it on held out.
Also reports whether the paraphrase's OWN retrieval finds the base question's evidence document, so a cache hit would not hand back an answer built on other evidence.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main():
    from app.common import load_config
    from app.retrieval.search import _load
    from app.security.context import build_context

    pairs = yaml.safe_load((ROOT / "eval/cache/pairs.yaml").read_text())["pairs"]
    golden = {g["id"]: g for g in yaml.safe_load((ROOT / "eval/golden/golden.yaml").read_text(encoding="utf-8"))}
    st = _load(); model = st["model"]; norm = st["config"]["embedding"]["normalize"]
    enc = lambda xs: model.encode(xs, normalize_embeddings=norm)
    rows = []
    for i, p in enumerate(pairs):
        base_q = golden[p["base"]]["question"]
        eb, ep, en = enc([base_q, p["paraphrase"], p["near_miss"]])
        evidence = {e["doc_id"] for e in golden[p["base"]]["evidence"]}
        own = {c["doc_id"] for c in build_context(p["paraphrase"], "staff-all")["chunks"]}
        rows.append({"base": p["base"], "split": "dev" if i % 2 == 0 else "heldout", "paraphrase_sim": float(eb @ ep), "near_miss_sim": float(eb @ en),
                     "paraphrase_finds_base_evidence": bool(evidence & own)})
    for split in ("dev", "heldout", "all"):
        rs = [r for r in rows if split == "all" or r["split"] == split]
        ps = sorted(r["paraphrase_sim"] for r in rs); ns = sorted(r["near_miss_sim"] for r in rs)
        print(f"\n{split.upper()}  pairs {len(rs)}")
        print(f"  paraphrase similarity: min {ps[0]:.3f}  median {ps[len(ps) // 2]:.3f}  max {ps[-1]:.3f}")
        print(f"  near miss similarity:  min {ns[0]:.3f}  median {ns[len(ns) // 2]:.3f}  max {ns[-1]:.3f}")
        print("  threshold | paraphrase hits | near miss false hits")
        for t in (0.70, 0.75, 0.80, 0.85, 0.88, 0.90, 0.92, 0.94, 0.96):
            print(f"  {t:9.2f} | {sum(r['paraphrase_sim'] >= t for r in rs):2d} of {len(rs)} = {sum(r['paraphrase_sim'] >= t for r in rs) / len(rs):.2f} | {sum(r['near_miss_sim'] >= t for r in rs):2d} of {len(rs)} = {sum(r['near_miss_sim'] >= t for r in rs) / len(rs):.2f}")
    ok = sum(r["paraphrase_finds_base_evidence"] for r in rows)
    print(f"\nparaphrases whose own retrieval finds the base question's evidence document: {ok} of {len(rows)}")
    print("\nper pair (similarity of paraphrase / near miss), pairs where a threshold can not separate them (near miss >= paraphrase):")
    for r in rows:
        if r["near_miss_sim"] >= r["paraphrase_sim"]:
            print(f"  {r['base']}: paraphrase {r['paraphrase_sim']:.3f}  near miss {r['near_miss_sim']:.3f}")
    run_id = f"cache-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
    out = ROOT / "eval/runs" / run_id; out.mkdir(parents=True)
    from ops.versioning import stamp
    (out / "record.json").write_text(json.dumps(stamp({"run_id": run_id, "kind": "cache-eval", "model_calls": 0, "pairs": len(rows), "embedder": load_config()["embedding"]["model"], "rows": rows}), indent=1))
    print(f"\nsaved eval/runs/{run_id}/")


if __name__ == "__main__":
    main()
