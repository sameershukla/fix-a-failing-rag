from .dedupe import seen

def replay(events, environment, approvers):
    if environment == "prod" and len(events) > 1_000_000 and len(approvers) < 2:
        raise PermissionError("two Data Platform approvers required")
    for event in events:
        if seen(event["event_id"]):
            continue
        yield event
