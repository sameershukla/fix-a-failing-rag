def cancel(order, approval_token=None):
    if order.total_usd > 5000 and not approval_token:
        raise PermissionError("X-Approval-Token required above $5,000")
    if order.state in {"SHIPPED", "DELIVERED"}:
        raise ValueError("order can no longer be cancelled")
    order.state = "CANCELLED"
