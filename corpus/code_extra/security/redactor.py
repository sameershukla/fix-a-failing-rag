import re
FAKE_SECRET = re.compile(r"FAKE_SECRET_[A-Z0-9_]+")
FAKE_EMAIL = re.compile(r"FAKE_[^\s]+@example\.test")

def redact(text):
    text = FAKE_SECRET.sub("[REDACTED_SECRET]", text)
    return FAKE_EMAIL.sub("[REDACTED_EMAIL]", text)
