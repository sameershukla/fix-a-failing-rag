"""Score a system on the golden set and write a run record to eval/runs/<run_id>/.

    python -m eval.run --system baseline [--ks 1,3,5,10,20] [--builds 3] [--golden PATH] [--label TEXT] [--no-rebuild]

Each build re-creates the index from the saved chunks, retrieves the top max(K) chunks for every question,
and scores them with the relevance rule in eval/metrics/relevance.py. With --builds 3 the headline numbers are
the mean over three index builds, with the min to max band.
"""
import argparse
import hashlib
import json
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

from eval.metrics import relevance
from eval.metrics.retrieval import first_relevant_rank, question_metrics, rank_table

ROOT = Path(__file__).resolve().parents[1]
METRICS = ["hit", "recall", "precision", "rr", "ndcg"]
ALIAS = {"rr": "mrr"}


def sha(text: str, n: int = 8) -> str:
    return hashlib.sha1(text.encode()).hexdigest()[:n]


def git_state() -> dict:
    def run(*a):
        r = subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None
    return {"commit": run("rev-parse", "--short", "HEAD"), "dirty": bool(run("status", "--porcelain", "--", "baseline", "app", "eval", "Makefile"))}


def guard_system(system: str):
    """app/ starts as a copy of baseline/. Refuse to score it while it still imports baseline."""
    if system == "baseline":
        return
    src = (ROOT / system / "retrieval" / "search.py").read_text()
    if "baseline." in src and f"{system}." not in src:
        sys.exit(f"{system}/retrieval/search.py still imports baseline.*, so it would read the baseline index. Fix the imports first.")


def mean(xs):
    return statistics.fmean(xs) if xs else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--system", default="baseline")
    ap.add_argument("--ks", default="1,3,5,10,20")
    ap.add_argument("--builds", type=int, default=3)
    ap.add_argument("--golden", default="eval/golden/golden.yaml")
    ap.add_argument("--label", default="")
    ap.add_argument("--no-rebuild", action="store_true")
    ap.add_argument("--min-cover", type=float, default=relevance.MIN_COVER)
    ap.add_argument("--rescore", default="", help="re-score the saved retrieved lists of this run id: no index build, no retrieval")
    args = ap.parse_args()
    ks = sorted({int(k) for k in args.ks.split(",")})
    guard_system(args.system)

    import importlib
    config_text = yaml.safe_dump(importlib.import_module(f"{args.system}.common").load_config(), sort_keys=True)
    cfg_hash = sha(config_text)
    golden_path = ROOT / args.golden
    golden = yaml.safe_load(golden_path.read_text(encoding="utf-8"))
    golden_hash = sha(golden_path.read_text(encoding="utf-8"))
    docs = {}
    with (ROOT / "data" / args.system / "normalized" / "docs.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            d = json.loads(line)
            docs[d["doc_id"]] = d["text"]
    answerable = [g for g in golden if g["answerable"]]
    passages = {g["id"]: relevance.locate_evidence(docs, g["evidence"]) for g in answerable}

    source_record = None
    if args.rescore:   # a rescored run keeps the config of the run whose retrieved lists it reuses
        source_record = json.loads((ROOT / "eval" / "runs" / args.rescore / "run.json").read_text())
        cfg_hash = source_record["config_hash"]
        config_text = yaml.safe_dump(source_record["config"], sort_keys=True)
    now = datetime.now(timezone.utc)
    base_id = f"{now:%Y%m%d-%H%M%S}-{args.system}-{cfg_hash[:6]}"
    run_id, n = base_id, 1
    while (ROOT / "eval" / "runs" / run_id).exists():
        n += 1
        run_id = f"{base_id}-{n}"
    out_dir = ROOT / "eval" / "runs" / run_id
    out_dir.mkdir(parents=True)

    builds, timings = [], []
    source = None
    if args.rescore:
        source = ROOT / "eval" / "runs" / args.rescore
        files = sorted(source.glob("retrieved_build_*.jsonl"))
        if not files:
            sys.exit(f"no saved retrieved lists in {source}")
        args.builds = len(files)
    for b in range(1, args.builds + 1):
        t0 = time.time()
        if source:
            retrieved_path = source / f"retrieved_build_{b}.jsonl"
        else:
            if not args.no_rebuild:
                log = subprocess.run([sys.executable, "-m", f"{args.system}.ingest.index"], cwd=ROOT, capture_output=True, text=True)
                (out_dir / f"index_build_{b}.log").write_text(log.stdout + log.stderr)
                if log.returncode:
                    sys.exit(f"index build {b} failed, see {out_dir}/index_build_{b}.log")
            t1 = time.time()
            retrieved_path = out_dir / f"retrieved_build_{b}.jsonl"
            r = subprocess.run([sys.executable, "-m", "eval.retrieve_all", "--system", args.system, "--golden", args.golden,
                                "--k", str(max(ks)), "--out", str(retrieved_path)], cwd=ROOT, capture_output=True, text=True)
            if r.returncode:
                sys.exit(r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "retrieval failed")
            timings.append({"build": b, "index_seconds": round(t1 - t0, 1), "retrieve_seconds": round(time.time() - t1, 1)})
        retrieved = {}
        for line in retrieved_path.open(encoding="utf-8"):
            rec = json.loads(line)
            retrieved[rec["id"]] = rec["retrieved"]
        per_q = {}
        for g in answerable:
            found = rank_table(retrieved[g["id"]], passages[g["id"]], args.min_cover)
            per_q[g["id"]] = {"metrics": question_metrics(found, len(passages[g["id"]]), ks), "first_rank": first_relevant_rank(found)}
        builds.append({"retrieved": retrieved, "per_q": per_q})

    # headline metrics: mean over questions, per build, then mean/min/max over builds
    def over_questions(build, ids, metric, k):
        return mean([build["per_q"][i]["metrics"][k][metric] for i in ids])

    all_ids = [g["id"] for g in answerable]
    metrics = {}
    for m in METRICS:
        for k in ks:
            vals = [over_questions(bd, all_ids, m, k) for bd in builds]
            metrics[f"{ALIAS.get(m, m)}@{k}"] = {"mean": mean(vals), "min": min(vals), "max": max(vals)}

    slice_tags = sorted({t for g in answerable for t in g["tags"] if not t.startswith("module-")})
    slices = {}
    for tag in slice_tags:
        ids = [g["id"] for g in answerable if tag in g["tags"]]
        slices[tag] = {"n": len(ids)}
        for m in METRICS:
            for k in ks:
                vals = [over_questions(bd, ids, m, k) for bd in builds]
                slices[tag][f"{ALIAS.get(m, m)}@{k}"] = {"mean": mean(vals), "min": min(vals), "max": max(vals)}

    subsets = {}
    sub_dir = ROOT / "eval" / "golden" / "subsets"
    for f in sorted(sub_dir.glob("*.yaml")) if sub_dir.exists() else []:
        ids = [i for i in (yaml.safe_load(f.read_text()) or {}).get("ids", []) if i in passages]
        if not ids:
            continue
        subsets[f.stem] = {"n": len(ids)}
        for m in METRICS:
            for k in ks:
                vals = [over_questions(bd, ids, m, k) for bd in builds]
                subsets[f.stem][f"{ALIAS.get(m, m)}@{k}"] = {"mean": mean(vals), "min": min(vals), "max": max(vals)}

    unans = [g for g in golden if not g["answerable"]]
    top1 = lambda bd, ids: mean([bd["retrieved"][i][0]["score"] for i in ids])
    descriptive = {
        "top1_score_answerable": mean([top1(bd, all_ids) for bd in builds]),
        "top1_score_unanswerable": mean([top1(bd, [g["id"] for g in unans]) for bd in builds]),
    }

    with (out_dir / "questions.jsonl").open("w", encoding="utf-8") as fh:
        for g in golden:
            rec = {"id": g["id"], "question": g["question"], "tags": g["tags"], "answerable": g["answerable"]}
            first = builds[0]["retrieved"][g["id"]]
            rec["top_retrieved"] = [{"chunk_id": h["chunk_id"], "doc_id": h["doc_id"], "score": h["score"]} for h in first]
            if g["answerable"]:
                rec["evidence_docs"] = [e["doc_id"] for e in g["evidence"]]
                rec["n_passages"] = len(g["evidence"])
                rec["first_rank_by_build"] = [bd["per_q"][g["id"]]["first_rank"] for bd in builds]
                rec["metrics"] = {str(k): {ALIAS.get(m, m): mean([bd["per_q"][g["id"]]["metrics"][k][m] for bd in builds]) for m in METRICS} for k in ks}
                rec["stable_across_builds"] = len({tuple(bd["per_q"][g["id"]]["metrics"][k]["hit"] for k in ks) for bd in builds}) == 1
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    record = {
        "run_id": run_id, "created_at": now.isoformat(timespec="seconds"), "system": args.system, "label": args.label,
        "git": git_state(), "config_hash": cfg_hash, "golden": {"path": args.golden, "hash": golden_hash, "questions": len(golden),
        "answerable": len(answerable), "unanswerable": len(unans)},
        "relevance_rule": {"min_cover": args.min_cover}, "rescored_from": args.rescore or None, "ks": ks, "builds": args.builds, "timings": timings,
        "one_question_is_worth": 1 / len(answerable), "metrics": metrics, "slices": slices, "subsets": subsets, "descriptive": descriptive,
        "unstable_questions": [g["id"] for g in answerable if not all(bd["per_q"][g["id"]]["metrics"][k]["hit"] == builds[0]["per_q"][g["id"]]["metrics"][k]["hit"] for bd in builds for k in ks)],
        "config": yaml.safe_load(config_text),
    }
    if source_record is not None:
        if "chunk_stats" in source_record:
            record["chunk_stats"] = source_record["chunk_stats"]
    else:
        stats_file = importlib.import_module(f"{args.system}.common").chunks_path(importlib.import_module(f"{args.system}.common").load_config()).parent / "stats.json"
        if stats_file.exists():
            record["chunk_stats"] = json.loads(stats_file.read_text())
    from ops.versioning import stamp
    stamp(record)   # Lesson 8.1: system_version and the behavior parts behind it
    (out_dir / "run.json").write_text(json.dumps(record, indent=2, ensure_ascii=False))
    with (ROOT / "eval" / "runs" / "index.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"run_id": run_id, "created_at": record["created_at"], "system": args.system, "label": args.label,
                             "builds": args.builds, "rescored_from": args.rescore or None, "golden_hash": golden_hash, "min_cover": args.min_cover,
                             "hit@5": metrics.get("hit@5", {}).get("mean"), "recall@5": metrics.get("recall@5", {}).get("mean"),
                             "mrr@5": metrics.get("mrr@5", {}).get("mean")}) + "\n")

    print(f"run {run_id}  ({args.builds} index builds, {len(answerable)} answerable questions, one question = {100/len(answerable):.2f} points)")
    print(f"{'K':>3}  {'Hit':>14}  {'Recall':>14}  {'Precision':>14}  {'MRR':>14}  {'nDCG':>14}")
    for k in ks:
        def cell(m):
            v = metrics[f"{ALIAS.get(m, m)}@{k}"]
            return f"{v['mean']:.3f} [{v['min']:.3f}-{v['max']:.3f}]".rjust(14) if v["max"] != v["min"] else f"{v['mean']:.3f}".rjust(14)
        print(f"{k:>3}  " + "  ".join(cell(m) for m in METRICS))
    hist = {}
    for g in answerable:
        r = builds[0]["per_q"][g["id"]]["first_rank"]
        key = "not in top %d" % max(ks) if r is None else (str(r) if r <= 5 else ("6 to 10" if r <= 10 else "11 to 20"))
        hist[key] = hist.get(key, 0) + 1
    order = ["1", "2", "3", "4", "5", "6 to 10", "11 to 20", "not in top %d" % max(ks)]
    print("rank of the first relevant chunk (build 1): " + ", ".join(f"{k}: {hist.get(k, 0)}" for k in order))
    if 5 in ks:
        print(f"{'slice':<20}{'n':>4}  {'Hit@5':>6} {'Recall@5':>9} {'Prec@5':>7} {'MRR@5':>6}")
        for tag, s in sorted(slices.items(), key=lambda ts: -ts[1]["hit@5"]["mean"]):
            print(f"{tag:<20}{s['n']:>4}  {s['hit@5']['mean']:>6.3f} {s['recall@5']['mean']:>9.3f} {s['precision@5']['mean']:>7.3f} {s['mrr@5']['mean']:>6.3f}")
    for name, s in subsets.items():
        if "hit@5" in s:
            print(f"subset {name:<8} n={s['n']:>3}  Hit@5 {s['hit@5']['mean']:.3f} [{s['hit@5']['min']:.3f}-{s['hit@5']['max']:.3f}]  Recall@5 {s['recall@5']['mean']:.3f}  MRR@5 {s['mrr@5']['mean']:.3f}")
    print(f"unstable questions across builds: {len(record['unstable_questions'])}" + (f" ({', '.join(record['unstable_questions'])})" if record['unstable_questions'] else ""))
    print(f"mean top 1 score: answerable {descriptive['top1_score_answerable']:.3f}, unanswerable {descriptive['top1_score_unanswerable']:.3f}")
    print(f"saved eval/runs/{run_id}/")


if __name__ == "__main__":
    main()
