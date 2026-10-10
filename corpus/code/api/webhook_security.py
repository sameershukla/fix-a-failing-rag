# doc_id: brightcart/v2/code/api/webhook-security
# title: Webhook signature verification
# source_type: source_code
# language: python
# status: active
# authority: primary
# module: module-2-code-aware
# domain: api

"""Webhook signature verification.

This production-style module is intentionally long enough that a naive 500-token
fixed window will cut through symbol boundaries.  The functions around the target
rules use overlapping vocabulary so retrieval cannot rely on a single keyword.
A code-aware splitter should prefer complete functions, classes, decorators, and
docstrings so the retrieved chunk keeps the symbol name together with the logic
that gives the symbol its meaning.

The module belongs to the BrightCart API service.  Historical notes remain in
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


import hashlib
import hmac


def parse_signature_header(header: str) -> tuple[int, str]:
    parts = dict(piece.split("=", 1) for piece in header.split(",") if "=" in piece)
    return int(parts["t"]), parts["v1"]


def _signed_payload(timestamp: int, body: bytes) -> bytes:
    return str(timestamp).encode("utf-8") + b"." + body


def verify_webhook_signature(
    body: bytes,
    signature_header: str,
    secret: bytes,
    now_epoch: int,
) -> bool:
    """Verify a production webhook using HMAC-SHA256 and a five-minute clock window.

    The sender signs ``<unix_timestamp>.<raw_body>`` with **HMAC-SHA256**.  Verification
    uses ``hmac.compare_digest`` to avoid timing leaks.  Even a cryptographically valid
    signature is rejected when its timestamp differs from ``now_epoch`` by more than
    **300 seconds (5 minutes)**, which limits replay attacks.
    """
    timestamp, supplied = parse_signature_header(signature_header)
    if abs(now_epoch - timestamp) > 300:
        return False
    expected = hmac.new(secret, _signed_payload(timestamp, body), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, supplied)


def verification_reason(valid: bool, timestamp: int, now_epoch: int) -> str:
    if abs(now_epoch - timestamp) > 300:
        return "timestamp_outside_tolerance"
    return "signature_valid" if valid else "signature_mismatch"


def legacy_sha1_verifier(*_: Any, **__: Any) -> bool:
    """Removed algorithm kept as an explicit non-production stub."""
    return False
