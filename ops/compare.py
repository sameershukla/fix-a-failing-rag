"""make compare-runs A=<run id> B=<run id>

Compares two runs of the SAME kind (retrieval, generation, security, latency). A is before, B is after.
First it says what changed in the system: the behavior parts from the manifest (Lesson 8.1) when both runs have one, otherwise only whether the config hash differs.
Then it compares the results. Where there is a result per question it is paired (same question in both runs): better, worse, same, and a bootstrap 95% interval
for the change. A change is only a finding when that interval excludes zero; with few events, say so.
"""

import argparse
import json
import random
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ops.versioning import changed_parts  # noqa: E402


def load(run_id):
    d = ROOT / "eval" / "runs" / run_id
    if not d.exists():
        sys.exit(f"no such run: {run_id}")
    if (d / "record.json").exists():
        rec = json.loads((d / "record.json").read_text()); return d, rec, rec.get("kind")
    if (d / "run.json").exists():
        return d, json.loads((d / "run.json").read_text()), "retrieval"
    sys.exit(f"{run_id} has no record")


def jsonl(path):
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def bootstrap(diffs, n=2000):
    rng = random.Random(0)
    b = sorted(100 * sum(rng.choice(diffs) for _ in diffs) / len(diffs) for _ in range(n))
    return b[int(0.025 * n)], b[int(0.975 * n) - 1]


def what_changed(ra, rb):
    if ra.get("manifest") and rb.get("manifest"):
        parts = changed_parts(ra["manifest"], rb["manifest"])
        print(f"system version {ra['system_version']} -> {rb['system_version']}; parts that changed: {', '.join(parts) if parts else 'none'}")
        ga, gb = ra["manifest"]["git"], rb["manifest"]["git"]
        if ga["commit"] != gb["commit"]:
            print(f"git commit {ga['commit']} -> {gb['commit']}")
    else:
        ca, cb = ra.get("config_hash"), rb.get("config_hash")
        print(f"no manifest on {'A' if not ra.get('manifest') else ''}{' and ' if not ra.get('manifest') and not rb.get('manifest') else ''}{'B' if not rb.get('manifest') else ''} "
              f"(run made before Lesson 8.1): only the config hash is known: {ca} -> {cb} ({'same' if ca == cb else 'different'}). A prompt, judge or golden set change would not show.")


def paired(label, pa, pb, higher_is_better):
    ids = [i for i in pa if i in pb]
    better = sum((pb[i] > pa[i]) == higher_is_better and pb[i] != pa[i] for i in ids)
    worse = sum((pb[i] < pa[i]) == higher_is_better and pb[i] != pa[i] for i in ids)
    diffs = [pb[i] - pa[i] for i in ids]
    lo, hi = bootstrap(diffs)
    mean = 100 * sum(diffs) / len(diffs)
    verdict = "interval excludes 0" if lo > 0 or hi < 0 else "interval includes 0: no measurable change"
    print(f"  {label}: {better} better, {worse} worse, {len(ids) - better - worse} same over {len(ids)} questions; change {mean:+.1f} points [{lo:+.1f}, {hi:+.1f}] ({verdict})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"); ap.add_argument("b")
    args = ap.parse_args()
    da, ra, ka = load(args.a); db, rb, kb = load(args.b)
    if ka != kb:
        sys.exit(f"different kinds: {ka} and {kb}. Compare runs of the same kind.")
    print(f"A {args.a}\nB {args.b}\nkind {ka}")
    what_changed(ra, rb)
    if ka == "security":
        sa = {r["id"]: r for r in jsonl(da / "results.jsonl")}; sb = {r["id"]: r for r in jsonl(db / "results.jsonl")}
        print(f"attacks that LEAK {ra['leak']} of {ra['attacks']} -> {rb['leak']} of {rb['attacks']}; blocked {ra['blocked']} -> {rb['blocked']}; not reached {ra['not_reached']} -> {rb['not_reached']}; "
              f"controls failed {ra['controls_failed']} -> {rb['controls_failed']}")
        for i in sa:
            if i in sb and sa[i]["status"] != sb[i]["status"]:
                print(f"  {i}: {sa[i]['status']} -> {sb[i]['status']}")
    elif ka == "generation":
        print(f"model {ra['model']} -> {rb['model']}; prompt {ra.get('prompt')} -> {rb.get('prompt')}")
        for key in ("latency_ms", "tokens_per_answer"):
            if ra.get(key) and rb.get(key):
                print(f"  {key}: {ra[key]} -> {rb[key]}")
        ja, jb = da / "judged.json", db / "judged.json"
        if ja.exists() and jb.exists():
            A = {a["id"]: a for a in json.loads(ja.read_text())["answers"]}; B = {a["id"]: a for a in json.loads(jb.read_text())["answers"]}
            ids = [i for i in A if i in B and A[i]["verdict"] and B[i]["verdict"]]
            paired("unfaithful (judge NOT CALIBRATED)", {i: A[i]["verdict"] == "unfaithful" for i in ids}, {i: B[i]["verdict"] == "unfaithful" for i in ids}, higher_is_better=False)
        else:
            print("  one or both runs are not judged (make judge-run): no faithfulness comparison.")
    elif ka == "latency":
        for tag, r, d in (("A", ra, da), ("B", rb, db)):
            calls = jsonl(d / "calls.jsonl")[r["warmup_calls_not_counted"] + 1:]
            print(f"  {tag}: median total {statistics.median(c['total_ms'] for c in calls):.1f} ms over {len(calls)} warm calls; first call {r['cold_first_call_ms']:.0f} ms")
        print("  one run each on one machine: a few milliseconds is noise.")
    elif ka == "retrieval":
        qa = {q["id"]: q for q in jsonl(da / "questions.jsonl") if q["answerable"]}; qb = {q["id"]: q for q in jsonl(db / "questions.jsonl") if q["answerable"]}
        for name in ("hit", "recall", "mrr"):
            paired(f"{name}@5", {i: qa[i]["metrics"]["5"][name] for i in qa if i in qb}, {i: qb[i]["metrics"]["5"][name] for i in qa if i in qb}, higher_is_better=True)
        print(f"  index builds: A {ra['builds']}, B {rb['builds']}; per question values are from the saved per question record")
    else:
        sys.exit(f"no comparison for kind {ka}")


if __name__ == "__main__":
    main()
