"""One trace per request (Lesson 8.2): enough to debug a bad answer without reproducing it.

A trace stores what the system DID, in order: the question and who asked, what retrieval returned (chunk ids and scores), what the security stages removed or masked,
the exact prompt the model saw (after access control and redaction, so a trace never holds text the caller could not see), the answer, tokens, timings, and the system version.
Written as one JSON line to data/app/traces/traces.jsonl. Nothing in a trace is needed to run the system; turn it off with tracing.enabled: false.

    python -m app.trace list [N]      the last N traces, one line each
    python -m app.trace show <id>     one trace, in the order things happened
"""

import hashlib
import json
import secrets
import sys
import time
from datetime import datetime, timezone
from functools import lru_cache

from app.common import DATA

TRACE_PATH = DATA / "traces" / "traces.jsonl"


@lru_cache(maxsize=1)
def system_version() -> str:
    from ops.versioning import manifest
    return manifest()["system_version"]


def new_id() -> str:
    return f"tr-{datetime.now(timezone.utc):%Y%m%d-%H%M%S}-{secrets.token_hex(3)}"


def prompt_hash(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def write(record: dict, path=None) -> None:
    p = path or TRACE_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_all(path=None) -> list:
    p = path or TRACE_PATH
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.exists() else []


def show(t: dict) -> str:
    L = [f"trace {t['trace_id']}   {t['time']}   system {t['system_version']}   caller {t['caller']}",
         f"question: {t['question']}"]
    c = t.get("cache") or {}
    if c.get("hit"):
        L.append(f"CACHE HIT (similarity {c['similarity']:.3f}) matched: {c['matched_question']}; no retrieval, no model call")
    else:
        L.append("retrieved:")
        for r in t.get("retrieved", []):
            L.append(f"  {r['score']:8.3f}  {r['chunk_id']}")
        if t.get("removed"):
            L.append("removed by security:")
            for r in t["removed"]:
                L.append(f"  {r['chunk_id']}  ({r['why']})")
        if t.get("denied_groups"):
            L.append("access groups this caller may not read (removed before ranking): " + ", ".join(t["denied_groups"]))
        if t.get("redactions"):
            L.append(f"redactions: {t['redactions']}")
        L.append(f"prompt {t['prompt_hash']} ({t['prompt_style']}, {len(t['prompt'])} characters); last 200: ...{t['prompt'][-200:]!r}" if t.get("prompt") else f"prompt {t['prompt_hash']} (text not stored)")
        L.append(f"model {t['model']}: {t['usage']['input_tokens']} in, {t['usage']['output_tokens']} out, stop {t['usage']['stop_reason']}")
    L.append(f"answer: {t['answer'][:400]}{'...' if len(t['answer']) > 400 else ''}" if t.get("answer") is not None else f"ERROR: {t.get('error')}")
    L.append("timings ms: " + ", ".join(f"{k} {v:.0f}" for k, v in t["timings_ms"].items()))
    return "\n".join(L)


def _main(argv):
    ts = read_all()
    if not argv or argv[0] == "list":
        n = int(argv[1]) if len(argv) > 1 else 10
        for t in ts[-n:]:
            print(f"{t['trace_id']}  {t['caller']:14s} {'CACHE' if (t.get('cache') or {}).get('hit') else 'model'}  {t['timings_ms'].get('total', 0):7.0f} ms  {t['question'][:70]}")
    elif argv[0] == "show":
        match = [t for t in ts if t["trace_id"] == argv[1]]
        print(show(match[0]) if match else f"no trace {argv[1]}")


if __name__ == "__main__":
    _main(sys.argv[1:])
