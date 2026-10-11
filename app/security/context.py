"""Build the context the model sees: retrieve, then apply the security controls the config turns on.

Three controls, each off at the start of Module 5 and each added by one lesson:
  acl               5.3  remove chunks the caller may not read, before ranking, and check again after
  redact            5.2  mask fake PII and secrets in the text
  injection_filter  5.1  drop chunks that carry instructions aimed at the assistant
With all three off this returns exactly what search() returns, so nothing about earlier modules changes.
"""

from app.common import load_config
from app.retrieval.search import access_groups, search
from app.security.access import can_read, denied_groups, load_callers
from app.security.injection import scan
from app.security.redact import redact


def build_context(question: str, caller_name: str = None, k: int = None) -> dict:
    cfg = load_config()
    sec = cfg.get("security", {})
    caller_name = caller_name or sec.get("caller", "staff-all")
    caller = load_callers()[caller_name]
    deny = denied_groups(caller, access_groups()) if sec.get("acl") else None
    chunks = search(question, k=k, deny_groups=deny)
    removed = []
    if sec.get("acl"):   # belt and braces: the pre-filter should already have done this, so nothing should be removed here
        kept = []
        for c in chunks:
            (kept if can_read(c["metadata"].get("access_group"), caller) else removed).append(c)
        chunks = kept
    if sec.get("injection_filter"):
        kept = []
        for c in chunks:
            hits = scan(c["text"])
            if hits:
                removed.append(dict(c, injection_rules=hits))
            else:
                kept.append(c)
        chunks = kept
    redactions = {}
    if sec.get("redact"):
        masked = []
        for c in chunks:
            text, counts = redact(c["text"])
            for name, n in counts.items():
                redactions[name] = redactions.get(name, 0) + n
            masked.append(dict(c, text=text))
        chunks = masked
    return {"caller": caller_name, "chunks": chunks, "removed": removed, "denied_groups": deny or [], "redactions": redactions}
