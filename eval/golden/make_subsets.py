"""Split the golden set into a dev half and a held out half. Writes eval/golden/subsets/dev.yaml and heldout.yaml (ids only).

Questions are grouped by their first slice tag, shuffled with a fixed seed inside each group, and dealt alternately to
dev and held out, so both halves have the same mix of slices. Run once. Rerunning with the same golden set gives the same files.
Use: choose settings on dev, then confirm on held out. The held out result is reported even when it is worse.
Run from the repo root:  .venv/bin/python eval/golden/make_subsets.py
"""
import collections
import random
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SEED = 2026
golden = yaml.safe_load((ROOT / "eval/golden/golden.yaml").read_text(encoding="utf-8"))
groups = collections.defaultdict(list)
for g in golden:
    stratum = "unanswerable" if not g["answerable"] else next(t for t in g["tags"] if not t.startswith("module-"))
    groups[stratum].append(g["id"])
dev, held = [], []
for stratum in sorted(groups):
    ids = sorted(groups[stratum])
    random.Random(f"{SEED}-{stratum}").shuffle(ids)
    dev += ids[0::2]
    held += ids[1::2]
header = ("# {name} half of the golden set, ids only. Made by eval/golden/make_subsets.py (seed %d, grouped by first slice tag).\n"
          "# Choose settings on dev. Confirm on heldout. Report heldout even when it is worse.\n" % SEED)
out = ROOT / "eval/golden/subsets"
for name, ids in (("dev", dev), ("heldout", held)):
    (out / f"{name}.yaml").write_text(header.format(name=name) + yaml.safe_dump({"ids": sorted(ids)}, width=100))
answerable = {g["id"] for g in golden if g["answerable"]}
print(f"dev: {len(dev)} questions ({len(set(dev) & answerable)} answerable), heldout: {len(held)} ({len(set(held) & answerable)} answerable)")
