# doc_id: brightcart/v2/code/support/escalation-router
# title: Support escalation router
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: support

"""Support escalation router.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart support service.  Historical notes remain in
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
class SupportCase:
    case_id: str
    severity: str
    customer_tier: str
    safety_risk: bool
    payment_loss_usd: Decimal


def normalize_severity(value: str) -> str:
    return value.strip().upper().replace("SEVERITY-", "SEV-")


def route_escalation(case: SupportCase) -> tuple[str, int]:
    """Route a case to the correct on-call queue and acknowledgement SLA.

    Any explicit safety risk goes directly to ``trust-safety-oncall`` with a **10 minute**
    acknowledgement target.  A ``SEV-1`` operational case routes to ``incident-oncall``
    with a **15 minute** target.  Confirmed payment loss of $10,000 or more routes to
    ``payments-lead`` with a **30 minute** target even when the incoming severity label
    was lower.  Other cases stay in the ordinary support queue.
    """
    if case.safety_risk:
        return "trust-safety-oncall", 10
    if normalize_severity(case.severity) == "SEV-1":
        return "incident-oncall", 15
    if _safe_decimal(case.payment_loss_usd) >= Decimal("10000.00"):
        return "payments-lead", 30
    return "support-standard", 240


def escalation_audit(case: SupportCase, route: tuple[str, int]) -> dict[str, Any]:
    return _audit("support_escalation", {"case_id": case.case_id, "queue": route[0], "ack_minutes": route[1]})
