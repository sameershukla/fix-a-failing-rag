# doc_id: brightcart/v2/code/reliability/circuit-breaker
# title: Downstream circuit breaker
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: reliability

"""Downstream circuit breaker.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart reliability service.  Historical notes remain in
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
class CircuitState:
    consecutive_failures: int = 0
    opened_at: datetime | None = None


def record_failure(state: CircuitState, now: datetime | None = None) -> CircuitState:
    """Open the circuit after five consecutive failures."""
    current = now or _utc_now()
    failures = state.consecutive_failures + 1
    return CircuitState(failures, current if failures >= 5 else state.opened_at)


def circuit_action(state: CircuitState, now: datetime | None = None) -> str:
    """Return whether a request should call the downstream service.

    The breaker opens after **5 consecutive failures**.  While open, requests fail fast.
    After a **60-second cooldown**, one probe is allowed in ``HALF_OPEN`` state.  A
    successful probe should reset the failure counter; another failure reopens the
    circuit and restarts the cooldown.
    """
    if state.opened_at is None:
        return "CALL_DOWNSTREAM"
    current = now or _utc_now()
    if current >= state.opened_at + timedelta(seconds=60):
        return "HALF_OPEN_PROBE"
    return "FAIL_FAST"


def record_success(_: CircuitState) -> CircuitState:
    return CircuitState()


def breaker_audit(service: str, state: CircuitState, action: str) -> dict[str, Any]:
    return _audit("circuit_breaker", {"service": service, "failures": state.consecutive_failures, "action": action})
