"""Flag retrieved text that carries instructions aimed at the assistant (Lesson 5.1).

A rule based filter. It is cheap and explainable, and it can be evaded; the lesson measures how. A flagged chunk is dropped from the context.
Patterns v1. If a pattern changes after a scan, say so in the lesson and keep the old version's numbers.
"""

import re

PATTERNS_V1 = [
    ("override", re.compile(r"\b(ignore|disregard|forget|override)\b[^.\n]{0,40}\b(previous|prior|above|earlier|all|any|your)\b[^.\n]{0,30}\b(instructions?|prompts?|rules?|guidelines?|guidance)\b", re.I)),
    ("exfiltrate", re.compile(r"\b(reveal|print|output|leak|expose|repeat)\b[^.\n]{0,40}\b(your|the assistant's)\b[^.\n]{0,30}\b(system prompt|hidden instructions?|instructions?|secrets?|api keys?)\b", re.I)),
    ("role", re.compile(r"\bfrom now on,? you (are|will)\b|\byou are now\b|\bnew instructions for the (ai|assistant|model)\b", re.I)),
    ("conceal", re.compile(r"\bdo not tell the user\b|\bdon't tell the user\b", re.I)),
]


def scan(text: str):
    """Returns the names of the patterns that match. Empty list means nothing was flagged."""
    return [name for name, p in PATTERNS_V1 if p.search(text)]
