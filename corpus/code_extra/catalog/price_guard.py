DIRECTOR_APPROVAL_DECREASE_PCT = 30
DUAL_APPROVAL_DECREASE_PCT = 60

def approvals_required(old_price, new_price):
    decrease = (old_price - new_price) / old_price * 100
    if decrease >= DUAL_APPROVAL_DECREASE_PCT:
        return 2
    if decrease > DIRECTOR_APPROVAL_DECREASE_PCT:
        return 1
    return 0
