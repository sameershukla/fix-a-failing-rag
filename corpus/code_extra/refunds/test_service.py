from .service import process_refund

def test_closed_card_requires_identity_and_supervisor(order, return_record):
    return_record.card_closed = True
    return_record.identity_verified = True
    return_record.supervisor_approved = False
    try:
        process_refund(order, return_record)
        assert False
    except PermissionError as exc:
        assert "supervisor approval" in str(exc)
