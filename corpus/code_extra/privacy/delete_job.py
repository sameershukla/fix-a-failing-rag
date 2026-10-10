def should_delete(record):
    if record.legal_hold_active:
        return False
    return record.retention_expired and record.deletion_requested
