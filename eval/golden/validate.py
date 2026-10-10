"""Check eval/golden/golden.yaml against the normalized corpus. No model, no index needed.

Run:  make golden-check   (or .venv/bin/python eval/golden/validate.py [--system baseline] [--golden path])
Checks: ids are unique, counts add up, every evidence passage appears word for word in its document,
answerable questions have evidence, unanswerable ones have none, every question has a module tag.
"""
import collections
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
system = sys.argv[sys.argv.index("--system") + 1] if "--system" in sys.argv else "baseline"
golden_path = ROOT / (sys.argv[sys.argv.index("--golden") + 1] if "--golden" in sys.argv else "eval/golden/golden.yaml")
docs = {}
with (ROOT / "data" / system / "normalized" / "docs.jsonl").open(encoding="utf-8") as fh:
    for line in fh:
        d = json.loads(line)
        docs[d["doc_id"]] = d["text"]

items = yaml.safe_load(golden_path.read_text(encoding="utf-8"))
errors = []
ids = [i["id"] for i in items]
if len(ids) != len(set(ids)):
    errors.append("duplicate ids")
for it in items:
    if it["answerable"] and not it["evidence"]:
        errors.append(f"{it['id']}: answerable without evidence")
    if not it["answerable"] and it["evidence"]:
        errors.append(f"{it['id']}: unanswerable with evidence")
    if not any(t.startswith("module-") for t in it["tags"]):
        errors.append(f"{it['id']}: no module tag")
    for e in it["evidence"]:
        if e["doc_id"] not in docs:
            errors.append(f"{it['id']}: unknown doc_id {e['doc_id']}")
        elif e["text"] not in docs[e["doc_id"]]:
            errors.append(f"{it['id']}: evidence text not found in {e['doc_id']}")

n_ans = sum(i["answerable"] for i in items)
print(f"{len(items)} questions: {n_ans} answerable, {len(items) - n_ans} unanswerable")
print("evidence passages per answerable question:", dict(sorted(collections.Counter(len(i["evidence"]) for i in items if i["answerable"]).items())))
print("distinct evidence documents:", len({e["doc_id"] for i in items for e in i["evidence"]}))
print("slices:", dict(collections.Counter(t for i in items for t in i["tags"] if not t.startswith("module-")).most_common()))
if errors:
    print(f"{len(errors)} problems:")
    print("\n".join(errors[:20]))
    sys.exit(1)
print("ok")
