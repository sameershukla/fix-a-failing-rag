def send_refund(order, route, idempotency_key):
    if not idempotency_key:
        raise ValueError("idempotency key required")
    return {"status": "submitted", "route": route, "key": idempotency_key}
