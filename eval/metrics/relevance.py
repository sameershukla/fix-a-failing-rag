"""The relevance rule: when does a retrieved chunk count as correct evidence?

One rule, used by every run. The golden set names a document and the exact evidence passage.
It never names a chunk, so the labels stay valid when the chunk size changes.

A passage is "found" by a chunk when the chunk is in the same document and covers at least
MIN_COVER of the passage's characters. A chunk that holds only a sliver of the passage does not count.
"""

MIN_COVER = 0.5


def passage_spans(doc_text: str, passage: str) -> list:
    """Every (start, end) character span where the passage occurs in the document text."""
    spans, start = [], doc_text.find(passage)
    while start != -1:
        spans.append((start, start + len(passage)))
        start = doc_text.find(passage, start + 1)
    return spans


def locate_evidence(docs: dict, evidence: list) -> list:
    """Turn a question's evidence items into passages with spans. docs maps doc_id to normalized text."""
    located = []
    for item in evidence:
        text = docs[item["doc_id"]]
        spans = passage_spans(text, item["text"])
        if not spans:
            raise ValueError(f"evidence not found in {item['doc_id']}: {item['text'][:60]!r}")
        located.append({"doc_id": item["doc_id"], "spans": spans})
    return located


def chunk_finds(chunk: dict, passage: dict, min_cover: float = MIN_COVER) -> bool:
    """Does this chunk (doc_id, start_char, end_char) find this located passage?"""
    if chunk["doc_id"] != passage["doc_id"]:
        return False
    for ps, pe in passage["spans"]:
        overlap = min(chunk["end_char"], pe) - max(chunk["start_char"], ps)
        if overlap >= min_cover * (pe - ps):
            return True
    return False
