"""Retrieval metrics for one question, from a ranked list of chunks and the located evidence.

Definitions (R = number of evidence passages for the question, K = cutoff):
  Hit@K        1 if any of the top K chunks finds a passage, else 0
  Recall@K     passages found by the top K chunks / R
  Precision@K  chunks among the top K that find at least one passage / K
  RR@K         1 / rank of the first chunk that finds a passage, 0 if none in the top K. Its mean is MRR@K.
  nDCG@K       gain of 1 for a chunk that finds a passage no earlier chunk found, discounted by log2(rank + 1),
               divided by the best possible score min(R, K) gains at the top.

nDCG gives gain only for new passages, so two overlapping chunks that both hold the same passage
are not counted twice and the score stays between 0 and 1.
"""
import math

from eval.metrics.relevance import MIN_COVER, chunk_finds


def rank_table(ranked: list, passages: list, min_cover: float = MIN_COVER) -> list:
    """For each chunk in rank order: the set of passage indexes it finds."""
    return [{i for i, p in enumerate(passages) if chunk_finds(c, p, min_cover)} for c in ranked]


def question_metrics(found_by_rank: list, n_passages: int, ks: list) -> dict:
    out = {}
    for k in ks:
        top = found_by_rank[:k]
        found = set().union(*top) if top else set()
        relevant_chunks = sum(1 for s in top if s)
        first = next((i + 1 for i, s in enumerate(found_by_rank) if s), None)
        seen, dcg = set(), 0.0
        for i, s in enumerate(top, 1):
            if s - seen:
                dcg += 1 / math.log2(i + 1)
            seen |= s
        ideal = sum(1 / math.log2(i + 1) for i in range(1, min(n_passages, k) + 1))
        out[k] = {
            "hit": 1.0 if found else 0.0,
            "recall": len(found) / n_passages,
            "precision": relevant_chunks / k,
            "rr": (1 / first) if first and first <= k else 0.0,
            "ndcg": dcg / ideal if ideal else 0.0,
        }
    return out


def first_relevant_rank(found_by_rank: list):
    return next((i + 1 for i, s in enumerate(found_by_rank) if s), None)
