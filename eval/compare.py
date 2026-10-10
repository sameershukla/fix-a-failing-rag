"""Compare two run records. A is before, B is after.

    python -m eval.compare RUN_A RUN_B [--k 5]

A difference is only called a change when the min to max bands of the two runs do not overlap.
Per question changes are paired: the same question in both runs.
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = ["hit", "recall", "precision", "mrr", "ndcg"]


def load(run_id):
    d = ROOT / "eval" / "runs" / run_id
    if not d.exists():
        sys.exit(f"no such run: {run_id}")
    rec = json.loads((d / "run.json").read_text())
    qs = {}
    for line in (d / "questions.jsonl").open(encoding="utf-8"):
        q = json.loads(line)
        qs[q["id"]] = q
    return rec, qs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_a")
    ap.add_argument("run_b")
    ap.add_argument("--k", type=int, default=5)
    args = ap.parse_args()
    a, qa = load(args.run_a)
    b, qb = load(args.run_b)

    print(f"A  {a['run_id']}  {a['label'] or ''}")
    print(f"B  {b['run_id']}  {b['label'] or ''}")
    if a["golden"]["hash"] != b["golden"]["hash"] or a["relevance_rule"] != b["relevance_rule"]:
        print("WARNING: the golden set or the relevance rule differs between A and B. The delta below is a change in the measurement, not in the system.")
    if a["config_hash"] != b["config_hash"]:
        print(f"config changed: {a['config_hash']} -> {b['config_hash']}")
    print()
    print(f"{'metric':<14}{'A':>8}{'B':>8}{'delta':>9}   verdict")
    common = sorted(set(a["ks"]) & set(b["ks"]))
    for k in common:
        for m in NAMES:
            key = f"{m}@{k}"
            ma, mb = a["metrics"][key], b["metrics"][key]
            delta = mb["mean"] - ma["mean"]
            overlap = not (mb["min"] > ma["max"] or ma["min"] > mb["max"])
            band = "inside the band: no measurable difference" if overlap and (ma["max"] > ma["min"] or mb["max"] > mb["min"]) else \
                   ("identical" if abs(delta) < 1e-12 else ("improved" if delta > 0 else "declined"))
            print(f"{key:<14}{ma['mean']:>8.3f}{mb['mean']:>8.3f}{delta:>+9.3f}   {band}")
    print()

    ids = [i for i in qa if i in qb and qa[i]["answerable"]]
    k = str(args.k)
    better = [i for i in ids if qb[i]["metrics"][k]["hit"] > qa[i]["metrics"][k]["hit"]]
    worse = [i for i in ids if qb[i]["metrics"][k]["hit"] < qa[i]["metrics"][k]["hit"]]
    same = len(ids) - len(better) - len(worse)
    print(f"Hit@{k} per question (paired, {len(ids)} questions; one question = {100/len(ids):.2f} points): {len(better)} better, {len(worse)} worse, {same} same")
    for name, group in (("got better", better), ("got worse", worse)):
        for i in group[:5]:
            print(f"  {name:<10} {i}  {qb[i]['question'][:80]}")
        if len(group) > 5:
            print(f"  ... and {len(group) - 5} more {name}")


if __name__ == "__main__":
    main()
