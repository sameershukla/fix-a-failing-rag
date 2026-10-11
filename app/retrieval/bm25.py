"""BM25 keyword search over the chunk texts. Written by hand so the course adds no dependency.

Tokens keep identifiers whole and also split them into parts, so `evaluate_card_velocity` is found by that exact
name and by the word `velocity`. Scores follow the usual BM25 formula with k1 = 1.5 and b = 0.75.
"""

import math
import re

TOKEN = re.compile(r"[a-z0-9_]+(?:[.\-/][a-z0-9_]+)*")
SPLIT = re.compile(r"[_.\-/]+")


def tokenize(text: str) -> list:
    tokens = []
    for tok in TOKEN.findall(text.lower()):
        tokens.append(tok)
        parts = [p for p in SPLIT.split(tok) if p]
        if len(parts) > 1:
            tokens.extend(parts)
    return tokens


class BM25:
    def __init__(self, texts, k1: float = 1.5, b: float = 0.75):
        self.k1, self.b = k1, b
        self.postings = {}   # term -> list of (doc index, term frequency)
        self.lengths = []
        for i, text in enumerate(texts):
            counts = {}
            toks = tokenize(text)
            for t in toks:
                counts[t] = counts.get(t, 0) + 1
            self.lengths.append(len(toks))
            for t, c in counts.items():
                self.postings.setdefault(t, []).append((i, c))
        self.n = len(texts)
        self.avg = sum(self.lengths) / max(1, self.n)

    def idf(self, term: str) -> float:
        df = len(self.postings.get(term, ()))
        return math.log(1 + (self.n - df + 0.5) / (df + 0.5))

    def top(self, query: str, k: int, allowed=None) -> list:
        """Return [(doc index, score)] best first. `allowed` is an optional set of doc indexes."""
        scores = {}
        for term in set(tokenize(query)):
            posting = self.postings.get(term)
            if not posting:
                continue
            idf = self.idf(term)
            for i, tf in posting:
                if allowed is not None and i not in allowed:
                    continue
                norm = tf + self.k1 * (1 - self.b + self.b * self.lengths[i] / self.avg)
                scores[i] = scores.get(i, 0.0) + idf * tf * (self.k1 + 1) / norm
        return sorted(scores.items(), key=lambda kv: -kv[1])[:k]


def rrf(rankings: list, weights: list, k: int = 60) -> list:
    """Reciprocal rank fusion. rankings is a list of ranked id lists. Returns [(id, score)] best first."""
    fused = {}
    for ranking, w in zip(rankings, weights):
        for rank, item in enumerate(ranking, 1):
            fused[item] = fused.get(item, 0.0) + w / (k + rank)
    return sorted(fused.items(), key=lambda kv: -kv[1])
