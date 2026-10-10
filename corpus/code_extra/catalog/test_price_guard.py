from .price_guard import approvals_required

def test_35_percent_cut_needs_director():
    assert approvals_required(100,65) == 1

def test_60_percent_cut_needs_dual_approval():
    assert approvals_required(100,40) == 2
