"""Check citations with code. No model is involved.

An answer cites with [n: "exact quote"]. A citation passes when chunk n exists AND the quote appears in that chunk.
Matching rule, stated once: both sides are lowercased, markdown emphasis marks (* ` #) are removed and table bars (|) become spaces, and runs of whitespace become one space.
Nothing else is forgiven: a changed word or number fails.

An "uncited sentence" is a sentence of at least 6 words that has no citation and is not a lead-in (ends with a colon), a refusal, a pointer ("check ...", "ask ...") or an offer
("I can ..."). That rule is rough, and the report says so.
"""

import re

CITATION = re.compile(r"\[(\d+)\s*:\s*[\"“]([^\"”\]]+)[\"”]\s*\]")
SKIP = re.compile(r"context (doesn.t|does not)|doesn.t (say|state|specify|mention|include|list|give|contain|cover)|does not (say|state|specify|mention|include|list|give|contain|cover)|"
                  r"not (mentioned|specified|stated|provided)|\b(check|ask|share|confirm|contact|escalate to)\b|\bI can\b|\bI.d\b|\bI can.t\b", re.I)


def normalize(text: str) -> str:
    # emphasis and code marks are removed (so "**US**." matches "US."); table bars become spaces
    return re.sub(r"\s+", " ", re.sub(r"[*`#]", "", text).replace("|", " ")).strip().lower()


def sentences(answer: str):
    body = CITATION.sub(lambda m: "[c]", answer)           # a quote can contain a full stop; hide it before splitting
    for part in re.split(r"(?<=[.!?:])\s+|\n+", body):
        part = part.strip(" -*#>")
        if part:
            yield part


def check(answer: str, chunks: list) -> dict:
    texts = [normalize(c["text"]) for c in chunks]
    cites, failures = [], []
    for m in CITATION.finditer(answer):
        n, quote = int(m.group(1)), m.group(2)
        if not 1 <= n <= len(texts):
            ok, why = False, "chunk number does not exist"
        elif normalize(quote) in texts[n - 1]:
            ok, why = True, ""
        else:
            ok, why = False, "quote not found in that chunk"
        cites.append(ok)
        if not ok:
            failures.append({"chunk": n, "quote": quote, "why": why})
    uncited = [s for s in sentences(answer) if "[c]" not in s and len(s.split()) >= 6 and not s.endswith(":") and not SKIP.search(s)]
    return {"citations": len(cites), "passed": sum(cites), "failed": len(failures), "failures": failures, "uncited_sentences": uncited}
