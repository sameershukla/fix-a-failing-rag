"""Mask fake PII and secrets in the text sent to the model (Lesson 5.2).

Rules come from a census of the FAKE_ values in the indexed chunks (lessons/module-05/runs/fake_token_census.txt), not from a guess:
  secret   FAKE_SECRET_...                 -> [REDACTED_SECRET]
  email    FAKE_..@example.<tld>           -> [REDACTED_EMAIL]
  phone    FAKE_555_010_NNNN               -> [REDACTED_PHONE]
  address  FAKE_N_..._STREET               -> [REDACTED_ADDRESS]
  name     FAKE_WORD_WORD (letters only)   -> [REDACTED_NAME]
Operational ids are NOT redacted on purpose, because engineers need them and golden questions use them:
  FAKE_USER_882, FAKE_ACCT_0005, FAKE_EVT_10028, FAKE_REFUND_8821, FAKE_RMA_712, FAKE_IDEMP_aa81.
That is a policy choice: an account id can be personal data in a real system.
Order matters: secrets first, so a secret is never read as a name.
"""

import re

RULES = [
    ("secret", re.compile(r"FAKE_SECRET_[A-Za-z0-9_]+"), "[REDACTED_SECRET]"),
    ("email", re.compile(r"FAKE_[\w.\-]+@example\.\w+"), "[REDACTED_EMAIL]"),
    ("phone", re.compile(r"FAKE_555_\d{3}_\d{4}"), "[REDACTED_PHONE]"),
    ("address", re.compile(r"FAKE_\d+_[A-Z_]+_STREET"), "[REDACTED_ADDRESS]"),
    ("name", re.compile(r"FAKE_[A-Z]+_[A-Z]+\b"), "[REDACTED_NAME]"),
]


def redact(text: str):
    """Returns (redacted text, {category: count})."""
    counts = {}
    for name, pattern, mask in RULES:
        text, n = pattern.subn(mask, text)
        if n:
            counts[name] = n
    return text, counts
