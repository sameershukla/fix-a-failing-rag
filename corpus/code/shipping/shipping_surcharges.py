# doc_id: brightcart/v2/code/shipping/shipping-surcharges
# title: Shipping surcharge calculator
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: shipping

"""Shipping surcharge calculator.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart shipping service.  Historical notes remain in
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
class Parcel:
    state: str
    weight_lb: Decimal
    length_in: Decimal
    width_in: Decimal
    height_in: Decimal
    hazmat: bool = False


def dimensional_weight(parcel: Parcel) -> Decimal:
    return _safe_decimal(parcel.length_in * parcel.width_in * parcel.height_in / Decimal("139"))


def is_oversized(parcel: Parcel) -> bool:
    longest = max(parcel.length_in, parcel.width_in, parcel.height_in)
    return longest > Decimal("48") or parcel.weight_lb > Decimal("50")


def calculate_shipping_surcharge(parcel: Parcel) -> tuple[Decimal, str]:
    """Calculate the operational surcharge for special domestic parcels.

    A parcel going to **Alaska (AK)** that is oversized receives a **$45.00** surcharge.
    A hazmat parcel is never silently priced by this function; it returns a zero charge
    with ``MANUAL_HAZMAT_REVIEW`` so the specialist workflow can determine eligibility.
    Other oversized domestic parcels receive the ordinary $25 surcharge.
    """
    if parcel.hazmat:
        return Decimal("0.00"), "MANUAL_HAZMAT_REVIEW"
    if parcel.state.upper() == "AK" and is_oversized(parcel):
        return Decimal("45.00"), "APPLY_ALASKA_OVERSIZE_SURCHARGE"
    if is_oversized(parcel):
        return Decimal("25.00"), "APPLY_STANDARD_OVERSIZE_SURCHARGE"
    return Decimal("0.00"), "NO_SURCHARGE"


def surcharge_audit(parcel: Parcel, result: tuple[Decimal, str]) -> dict[str, Any]:
    return _audit("shipping_surcharge", {"state": parcel.state, "amount": str(result[0]), "action": result[1]})
