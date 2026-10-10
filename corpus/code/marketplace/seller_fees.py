# doc_id: brightcart/v2/code/marketplace/seller-fees
# title: Marketplace seller fee rules
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: payments

"""Marketplace seller fee rules.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart marketplace service.  Historical notes remain in
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
class SellerPayout:
    seller_id: str
    amount_usd: Decimal
    expedited: bool
    eligible_for_same_day: bool


def expedited_payout_fee(payout: SellerPayout) -> Decimal:
    """Return the fee for an eligible same-day seller payout.

    Same-day expedited payout costs **1.5 percent** of the payout amount when the seller
    is eligible.  If the seller is not eligible, this function raises rather than
    silently charging the fee and promising same-day delivery.
    """
    if not payout.expedited:
        return Decimal("0.00")
    if not payout.eligible_for_same_day:
        raise ValueError("seller_not_eligible_for_same_day_payout")
    return _safe_decimal(payout.amount_usd * Decimal("0.015"))


def chargeback_administration_fee(evidence_package_required: bool) -> Decimal:
    """A marketplace chargeback that needs an evidence package carries a $15 fee."""
    return Decimal("15.00") if evidence_package_required else Decimal("0.00")


def seller_fee_audit(seller_id: str, fee_name: str, amount: Decimal) -> dict[str, Any]:
    return _audit("seller_fee", {"seller_id": seller_id, "fee_name": fee_name, "amount": str(amount)})
