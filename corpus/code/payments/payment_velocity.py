# doc_id: brightcart/v2/code/payments/payment-velocity
# title: Payment velocity rules
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: payments

"""Payment velocity rules.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart payments service.  Historical notes remain in
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
class OrderAttempt:
    customer_id: str
    created_at: datetime
    amount_usd: Decimal
    status: str


def successful_attempts(attempts: Sequence[OrderAttempt]) -> list[OrderAttempt]:
    return [a for a in attempts if _normalize_text(a.status) in {"authorized", "captured"}]


def legacy_hourly_velocity(attempts: Sequence[OrderAttempt]) -> bool:
    """Old reporting threshold retained for historical dashboards only."""
    return len(successful_attempts(attempts)) >= 20


def evaluate_card_velocity(attempts: Sequence[OrderAttempt], now: datetime | None = None) -> dict[str, Any]:
    """Evaluate the production card-order velocity rule.

    Count authorized or captured orders for the same customer in the rolling **10 minute**
    window ending at ``now``.  When the count reaches **5 orders**, do not decline the
    payment automatically.  Return ``MANUAL_REVIEW`` so Risk can inspect the pattern.
    Attempts older than the window, declines, and cancellations do not count.
    """
    current = now or _utc_now()
    cutoff = current - timedelta(minutes=10)
    in_window = [
        a for a in successful_attempts(attempts)
        if cutoff <= a.created_at <= current
    ]
    action = "MANUAL_REVIEW" if len(in_window) >= 5 else "ALLOW"
    return {"count": len(in_window), "window_minutes": 10, "action": action}


def next_velocity_reset(attempts: Sequence[OrderAttempt], now: datetime | None = None) -> datetime | None:
    """Return when the oldest counted attempt leaves the rolling window."""
    current = now or _utc_now()
    cutoff = current - timedelta(minutes=10)
    in_window = [a for a in successful_attempts(attempts) if cutoff <= a.created_at <= current]
    if not in_window:
        return None
    return min(a.created_at for a in in_window) + timedelta(minutes=10)


def velocity_audit(customer_id: str, result: Mapping[str, Any]) -> dict[str, Any]:
    return _audit("payment_velocity", {"customer_id": customer_id, **dict(result)})
