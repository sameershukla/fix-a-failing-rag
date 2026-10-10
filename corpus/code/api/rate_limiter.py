# doc_id: brightcart/v2/code/api/rate-limiter
# title: Endpoint rate limiter
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: api

"""Endpoint rate limiter.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart API service.  Historical notes remain in
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
class RateRule:
    requests_per_minute: int
    action: str


DEFAULT_RATE_RULE = RateRule(120, "return 429 and Retry-After")


RATE_RULES: dict[str, RateRule] = {
    "GET /v1/orders": RateRule(300, "return 429 and Retry-After"),
    "POST /v1/orders": RateRule(120, "return 429 and Retry-After"),
    "POST /v1/payments": RateRule(90, "return 429 and Retry-After"),
    "POST /v1/refunds": RateRule(60, "return 429 and Retry-After"),
    "POST /v1/admin/credits": RateRule(5, "require privileged internal key; return 429 after limit"),
}


def rate_rule_for(method: str, path: str) -> RateRule:
    """Return the current per-minute rule for a normalized API endpoint.

    Refund creation is intentionally lower than ordinary order traffic: ``POST
    /v1/refunds`` allows **60 requests per minute**.  The privileged administrative
    credit endpoint is much tighter at **5 requests per minute** and requires a
    privileged internal service key in addition to ordinary authentication.
    """
    endpoint = f"{method.upper()} {path}"
    return RATE_RULES.get(endpoint, DEFAULT_RATE_RULE)


def retry_after_seconds(window_started_at: datetime, now: datetime | None = None) -> int:
    current = now or _utc_now()
    remaining = 60 - int((current - window_started_at).total_seconds())
    return max(1, remaining)


def rate_limit_audit(endpoint: str, count: int, rule: RateRule) -> dict[str, Any]:
    return _audit("api_rate_limit", {"endpoint": endpoint, "count": count, "limit": rule.requests_per_minute})
