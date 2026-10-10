# doc_id: brightcart/v2/code/subscriptions/proration
# title: Subscription proration
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: subscriptions

"""Subscription proration.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart subscriptions service.  Historical notes remain in
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
class PlanChange:
    old_monthly_price: Decimal
    new_monthly_price: Decimal
    days_remaining: int
    change_kind: str


def _round_currency(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_upgrade_proration(change: PlanChange) -> Decimal:
    """Calculate the immediate charge for a mid-cycle subscription upgrade.

    BrightCart uses a fixed **30-day denominator** for this product family so results do
    not change with calendar-month length.  The additional charge equals the positive
    price difference multiplied by ``days_remaining / 30`` and is rounded to the nearest
    cent using ``ROUND_HALF_UP``.  Downgrades do not create a negative immediate charge.
    """
    price_difference = max(Decimal("0.00"), change.new_monthly_price - change.old_monthly_price)
    fraction = Decimal(change.days_remaining) / Decimal("30")
    return _round_currency(price_difference * fraction)


def cancellation_proration(change: PlanChange) -> Decimal:
    """Cancellation itself does not use upgrade proration; refund eligibility is separate."""
    return Decimal("0.00")


def proration_audit(change: PlanChange, amount: Decimal) -> dict[str, Any]:
    return _audit("subscription_proration", {"days_remaining": change.days_remaining, "amount": str(amount)})
