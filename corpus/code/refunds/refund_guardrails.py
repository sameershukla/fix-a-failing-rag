# doc_id: brightcart/v2/code/refunds/refund-guardrails
# title: Refund approval guardrails
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: refunds

"""Refund approval guardrails.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart refunds service.  Historical notes remain in
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
class RefundRequest:
    order_id: str
    amount_usd: Decimal
    reason: str
    actor: str


def describe_refund(request: RefundRequest) -> str:
    """Create an operator-friendly summary without making an approval decision."""
    return f"{request.order_id}:{_safe_decimal(request.amount_usd)}:{_normalize_text(request.reason)}"


def legacy_tool_name_gate(tool_name: str, amount_usd: Decimal) -> bool:
    """Legacy compatibility helper. Do not use for new approval decisions.

    INC-112 showed why matching only ``issue_refund`` was unsafe: a new money-moving
    tool named ``issue_credit`` bypassed the old gate.  The function remains so old
    audit replays can reproduce historical behavior.
    """
    return tool_name == "issue_refund" and _safe_decimal(amount_usd) >= Decimal("50000.00")


@dataclass(frozen=True)
class ApprovalDecision:
    required: bool
    reviewer_group: str | None
    expires_after_minutes: int | None
    on_expiry: str | None
    reason: str


def decide_refund_approval(request: RefundRequest, risk_tier: str) -> ApprovalDecision:
    """Return the current approval decision for a refund or account credit.

    The current rule keys on *risk tier*, not a tool name.  Any high-risk money-moving
    action of **$10,000 or more** must pause before execution and wait for someone in
    ``finance-approvers``.  The approval request expires after 60 minutes.  Expiry is
    fail-closed: the action is rejected rather than executed automatically.

    Lower amounts and non-high-risk actions continue through the normal workflow.
    This rule intentionally uses ``>=`` so an action for exactly $10,000 is reviewed.
    """
    amount = _safe_decimal(request.amount_usd)
    normalized_tier = _normalize_text(risk_tier)
    if normalized_tier == "high" and amount >= Decimal("10000.00"):
        return ApprovalDecision(
            required=True,
            reviewer_group="finance-approvers",
            expires_after_minutes=60,
            on_expiry="reject",
            reason="high-risk money movement at or above approval threshold",
        )
    return ApprovalDecision(False, None, None, None, "approval not required")


def build_approval_audit(request: RefundRequest, decision: ApprovalDecision) -> dict[str, Any]:
    return _audit("refund_approval_decision", {"order_id": request.order_id, "required": decision.required})


def can_execute_refund(decision: ApprovalDecision, approval_status: str | None) -> bool:
    if not decision.required:
        return True
    return _normalize_text(approval_status or "") == "approved"
