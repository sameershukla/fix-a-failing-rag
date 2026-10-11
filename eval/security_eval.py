"""make eval-security [CONFIG=...]

Scores the security controls with no model call. For each case in eval/security/attacks.yaml it builds the context exactly as the assistant does
(app/security/context.py, with the controls the config turns on) and checks what reached it.

For an attack case the result is one of:
  LEAK         the sensitive content reached the context (the attack worked)
  blocked      the target document was retrieved by the retriever and the controls kept it out, or hid the value
  not reached  the target document never came up for this question, so nothing was tested
For a control case: ok, or FAILED (a fix that blocks too much shows up here).
"""

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="")
    args = ap.parse_args()
    from app.common import load_config
    from app.retrieval.search import search
    from app.security.context import build_context

    cfg = load_config()
    cases = yaml.safe_load((ROOT / "eval/security/attacks.yaml").read_text(encoding="utf-8"))["cases"]
    golden = {g["id"]: g for g in yaml.safe_load((ROOT / "eval/golden/golden.yaml").read_text(encoding="utf-8"))}
    results = []
    for c in cases:
        ctx = build_context(c["question"], c["caller"])
        docs = {x["doc_id"] for x in ctx["chunks"]}
        text = "\n".join(x["text"] for x in ctx["chunks"])
        r = {"id": c["id"], "category": c["category"], "caller": c["caller"], "question": c["question"], "docs_in_context": sorted(docs)}
        if c["category"].startswith("control"):
            wanted = set(c.get("must_include_docs", [])) or {e["doc_id"] for e in golden[c["must_include_golden"]]["evidence"]}
            ok = bool(wanted & docs)
            r.update(status="ok" if ok else "FAILED", wanted=sorted(wanted))
        else:
            # what the retriever alone would have put in front of the model, to tell "blocked" from "never retrieved"
            raw_docs = {x["doc_id"] for x in search(c["question"])}
            reached_raw = c["target_doc"] in raw_docs
            leak = (any(d in docs for d in c.get("forbid_docs", [])) or any(s in text for s in c.get("forbid_strings", []))
                    or (c.get("forbid_regex") and re.search(c["forbid_regex"], text)))
            r.update(status="LEAK" if leak else ("blocked" if reached_raw else "not reached"), target_retrieved_by_search=reached_raw)
        results.append(r)

    cfg_hash = hashlib.sha1(yaml.safe_dump(cfg, sort_keys=True).encode()).hexdigest()[:6]
    from ops.versioning import manifest
    run_id = f"sec-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-{manifest()['system_version'][:6]}"
    out = ROOT / "eval/runs" / run_id; out.mkdir(parents=True)
    sec = cfg.get("security", {})
    attack = [r for r in results if not r["category"].startswith("control")]
    ctrl = [r for r in results if r["category"].startswith("control")]
    cnt = Counter(r["status"] for r in attack)
    record = {"run_id": run_id, "kind": "security", "config_hash": cfg_hash, "label": args.label, "security": sec,
              "authority_filter": (cfg["retrieval"].get("filters") or {}).get("authority"), "attacks": len(attack),
              "leak": cnt["LEAK"], "blocked": cnt["blocked"], "not_reached": cnt["not reached"],
              "controls": len(ctrl), "controls_failed": sum(r["status"] == "FAILED" for r in ctrl)}
    from ops.versioning import stamp
    stamp(record)
    (out / "record.json").write_text(json.dumps(record, indent=1)); (out / "results.jsonl").write_text("\n".join(json.dumps(r) for r in results))

    print(f"run {run_id}  security controls: acl={sec.get('acl')} redact={sec.get('redact')} injection_filter={sec.get('injection_filter')}  authority filter: {record['authority_filter']}")
    print(f"{'category':24s} {'cases':>5s} {'LEAK':>5s} {'blocked':>8s} {'not reached':>12s}")
    for cat in dict.fromkeys(r["category"] for r in attack):
        rs = [r for r in attack if r["category"] == cat]; k = Counter(r["status"] for r in rs)
        print(f"{cat:24s} {len(rs):5d} {k['LEAK']:5d} {k['blocked']:8d} {k['not reached']:12d}")
    print(f"{'ALL ATTACKS':24s} {len(attack):5d} {cnt['LEAK']:5d} {cnt['blocked']:8d} {cnt['not reached']:12d}")
    print(f"controls: {len(ctrl) - record['controls_failed']} ok, {record['controls_failed']} FAILED of {len(ctrl)}")
    for r in results:
        if r["status"] in ("LEAK", "FAILED", "not reached"):
            print(f"  {r['status']:11s} {r['id']} ({r['caller']}): {r['question'][:70]}")
    print(f"saved eval/runs/{run_id}/")


if __name__ == "__main__":
    main()
