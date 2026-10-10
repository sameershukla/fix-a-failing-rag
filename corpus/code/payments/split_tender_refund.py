# doc_id: brightcart/v2/code/payments/split-tender-refund
# title: Split tender refund allocation
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: payments

"""Split tender refund allocation.

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
class Tender:
    kind: str
    original_amount: Decimal


def allocate_split_tender_refund(tenders: Sequence[Tender], refund_amount: Decimal) -> dict[str, Decimal]:
    """Allocate a refund back to the original tenders without converting gift-card value.

    Refunds are returned in the **same proportions as the original payment**.  Gift-card
    value must go back to ``gift_card`` and may never be moved to cash or a bank card.
    The final tender receives any one-cent rounding remainder so allocations sum exactly
    to the requested refund amount.
    """
    total = sum((t.original_amount for t in tenders), Decimal("0.00"))
    if total <= 0:
        raise ValueError("original_tender_total_must_be_positive")
    remaining = _safe_decimal(refund_amount)
    allocation: dict[str, Decimal] = {}
    for index, tender in enumerate(tenders):
        if index == len(tenders) - 1:
            share = remaining
        else:
            share = _safe_decimal(refund_amount * tender.original_amount / total)
            remaining -= share
        allocation[tender.kind] = allocation.get(tender.kind, Decimal("0.00")) + share
    return allocation


def validate_gift_card_allocation(tenders: Sequence[Tender], allocation: Mapping[str, Decimal]) -> bool:
    original_has_gift_card = any(t.kind == "gift_card" and t.original_amount > 0 for t in tenders)
    return not original_has_gift_card or allocation.get("gift_card", Decimal("0.00")) > 0


def allocation_audit(order_id: str, allocation: Mapping[str, Decimal]) -> dict[str, Any]:
    return _audit("split_tender_refund", {"order_id": order_id, "allocation": {k: str(v) for k, v in allocation.items()}})
