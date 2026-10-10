# doc_id: brightcart/v2/code/api/idempotency-store
# title: API idempotency store
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: api

"""API idempotency store.

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


@dataclass
class IdempotencyRecord:
    key: str
    payload_hash: str
    response_status: int
    response_body: dict[str, Any]
    created_at: datetime


class IdempotencyConflict(RuntimeError):
    status_code = 409


def is_expired(record: IdempotencyRecord, now: datetime | None = None) -> bool:
    current = now or _utc_now()
    return current >= record.created_at + timedelta(hours=24)


def resolve_idempotent_request(
    existing: IdempotencyRecord | None,
    key: str,
    payload_hash: str,
    now: datetime | None = None,
) -> tuple[str, int | None, dict[str, Any] | None]:
    """Resolve a request before the endpoint performs its side effect.

    An idempotency record remains valid for **24 hours**.  Repeating the same key with
    the same payload hash returns the stored response and must not execute the side
    effect again.  Reusing a live key with a *different* payload is a conflict and the
    API returns **HTTP 409**.  Once the record has expired, the key may be used again.
    """
    if existing is None or is_expired(existing, now):
        return "EXECUTE", None, None
    if existing.key != key:
        return "EXECUTE", None, None
    if existing.payload_hash == payload_hash:
        return "REPLAY", existing.response_status, existing.response_body
    return "CONFLICT", 409, {"error": "idempotency_key_reused_with_different_payload"}


def ttl_seconds() -> int:
    return 24 * 60 * 60


def idempotency_audit(key: str, outcome: str) -> dict[str, Any]:
    return _audit("idempotency_resolved", {"key": key, "outcome": outcome})
