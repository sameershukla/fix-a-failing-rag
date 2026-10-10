def choose_refund_route(order, return_record):
    """Use original payment unless a closed-card fallback is approved."""
    if order.payment_method == "CARD" and return_record.card_closed:
        return "ACH_FALLBACK"
    return order.payment_method
