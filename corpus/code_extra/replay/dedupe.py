SEEN = set()
def seen(event_id):
    if event_id in SEEN:
        return True
    SEEN.add(event_id)
    return False
