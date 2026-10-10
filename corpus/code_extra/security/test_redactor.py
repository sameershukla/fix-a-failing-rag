from .redactor import redact

def test_fake_secret_is_redacted():
    assert redact("FAKE_SECRET_ABC") == "[REDACTED_SECRET]"
