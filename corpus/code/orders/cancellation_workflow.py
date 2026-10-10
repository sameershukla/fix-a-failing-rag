# doc_id: brightcart/v2/code/orders/cancellation-workflow
# title: Order cancellation workflow
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: orders

"""Order cancellation workflow.

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


CANCELLABLE_STATES = {"CREATED", "PAID", "ALLOCATED"}


def normalize_order_state(state: str) -> str:
    return state.strip().upper().replace(" ", "_")


def decide_cancellation(state: str, carrier_intercept_available: bool) -> tuple[str, str]:
    """Decide whether an order can still be cancelled.

    Orders in ``CREATED``, ``PAID``, or ``ALLOCATED`` can be cancelled normally.  Once
    the warehouse reports ``PICKED``, ordinary cancellation is no longer allowed.  If
    carrier intercept is available, return ``REQUEST_INTERCEPT``; otherwise return
    ``DENY_CANCELLATION`` and direct the customer to the return workflow after delivery.
    Shipped orders follow the same return-after-delivery rule.
    """
    normalized = normalize_order_state(state)
    if normalized in CANCELLABLE_STATES:
        return "CANCEL", "order has not crossed the warehouse pick boundary"
    if normalized == "PICKED" and carrier_intercept_available:
        return "REQUEST_INTERCEPT", "warehouse already picked; attempt carrier intercept"
    if normalized in {"PICKED", "SHIPPED", "DELIVERED"}:
        return "DENY_CANCELLATION", "use return workflow after delivery"
    return "REVIEW", "unknown state requires operations review"


def cancellation_audit(order_id: str, state: str, decision: tuple[str, str]) -> dict[str, Any]:
    return _audit("order_cancellation", {"order_id": order_id, "state": state, "decision": decision[0]})
