# doc_id: brightcart/v2/code/privacy/retention-jobs
# title: Privacy retention jobs
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: privacy

"""Privacy retention jobs.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart privacy service.  Historical notes remain in
comments and helper functions because real repositories accumulate compatibility
paths, operational helpers, and instrumentation beside business logic.  Those
nearby symbols are useful distractors for the Module 2 evaluation.
"""


from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any, Iterable, Mapping, Sequence


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _audit(event: str, details: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Return a small audit record used by examples in this module.

    Production sends this data to the central audit stream.  Keeping the helper in
    the corpus makes the file look like normal service code rather than a tiny toy
    function written solely for retrieval.
    """
    return {"event": event, "details": dict(details or {}), "recorded_at": _utc_now()}


def _normalize_text(value: str) -> str:
    return " ".join(value.strip().lower().split())


def _safe_decimal(value: Decimal | int | str) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class RetentionRule:
    dataset: str
    days: int
    batch_size: int


RETENTION_RULES = {
    "prod_agent_traces": RetentionRule("prod_agent_traces", 30, 500),
    "support_transcripts": RetentionRule("support_transcripts", 365, 250),
    "security_audit": RetentionRule("security_audit", 730, 100),
}


def deletion_cutoff(rule: RetentionRule, now: datetime | None = None) -> datetime:
    current = now or _utc_now()
    return current - timedelta(days=rule.days)


def purge_expired_agent_traces(rows: Sequence[Mapping[str, Any]], now: datetime | None = None) -> list[str]:
    """Select production agent traces that are old enough for deletion.

    ``prod_agent_traces`` are retained for **30 days**.  The worker deletes no more than
    **500 records per batch** so the privacy job does not create a large database lock.
    Rows on or newer than the cutoff remain.  Legal-hold rows are always skipped even
    when their creation time is older than the ordinary retention window.
    """
    rule = RETENTION_RULES["prod_agent_traces"]
    cutoff = deletion_cutoff(rule, now)
    candidates = [
        str(row["trace_id"]) for row in rows
        if row.get("created_at") < cutoff and not row.get("legal_hold", False)
    ]
    return candidates[: rule.batch_size]


def retention_audit(dataset: str, deleted: int) -> dict[str, Any]:
    return _audit("retention_purge", {"dataset": dataset, "deleted": deleted})
