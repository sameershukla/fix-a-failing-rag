# doc_id: brightcart/v2/code/orders/bulk-approval
# title: Bulk order approval
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: orders

"""Bulk order approval.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart orders service.  Historical notes remain in
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
class BulkOrder:
    sku: str
    quantity: int
    limited_edition: bool
    inventory_available: bool
    account_type: str


def classify_bulk_order(order: BulkOrder) -> str:
    if order.limited_edition:
        return "controlled_release"
    if order.quantity >= 100:
        return "high_volume"
    return "standard"


def decide_bulk_order(order: BulkOrder) -> tuple[str, str]:
    """Return the approval threshold outcome for a bulk order.

    Controlled-release or limited-edition SKUs require review when quantity is **more
    than 2 units**; the action is ``MERCHANDISING_APPROVAL``.  If inventory is not
    currently available, a bulk request does not get promised stock: it returns
    ``BACKORDER_REVIEW`` regardless of customer account type.
    """
    if not order.inventory_available:
        return "BACKORDER_REVIEW", "inventory unavailable; do not promise allocation"
    if order.limited_edition and order.quantity > 2:
        return "MERCHANDISING_APPROVAL", "controlled release quantity above 2"
    if order.quantity >= 100:
        return "SALES_OPS_APPROVAL", "high-volume order"
    return "APPROVE", "within standard quantity rules"


def bulk_order_audit(order: BulkOrder, decision: tuple[str, str]) -> dict[str, Any]:
    return _audit("bulk_order_decision", {"sku": order.sku, "quantity": order.quantity, "decision": decision[0]})
