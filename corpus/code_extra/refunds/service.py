"""Refund orchestration."""
from .policy import choose_refund_route
from .payments import send_refund

def process_refund(order, return_record):
    route = choose_refund_route(order, return_record)
    if route == "ACH_FALLBACK":
        if not return_record.identity_verified:
            raise ValueError("identity verification required")
        if not return_record.supervisor_approved:
            raise PermissionError("supervisor approval required")
    return send_refund(order, route, idempotency_key=return_record.refund_id)
