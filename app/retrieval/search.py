"""Retrieval for the app. What it does is set by `retrieval` and `embedding` in the config:

  mode        vector (embedding search), bm25 (keyword search) or hybrid (both, fused by reciprocal rank fusion)
  candidates  how many chunks each retriever contributes before fusion
  rerank      optional cross encoder that re-orders the top_n fused candidates
  filters     optional metadata filter, for example {status: [active]}; keys are ANDed, values in a list are ORed
  rewrite     optional query rewriting (HyDE): a model writes a passage that would answer the question; apply_to is vector or both
  query_prefix / passage_prefix (under embedding) for embedding models that expect them
"""

import sys

from app.common import INDEX_DIR, chunks_path, collection_name, load_config, read_jsonl
from app.retrieval.bm25 import BM25, rrf

_cache = {}


def _load():
    if not _cache:
        import chromadb
        from sentence_transformers import SentenceTransformer

        config = load_config()
        client = chromadb.PersistentClient(path=str(INDEX_DIR))
        _cache["config"] = config
        _cache["model"] = SentenceTransformer(config["embedding"]["model"])
        _cache["collection"] = client.get_collection(collection_name(config))
        _cache["chunks"] = None
    return _cache


def _chunks():
    state = _load()
    if state["chunks"] is None:
        chunks = list(read_jsonl(chunks_path(state["config"])))
        state["chunks"] = chunks
        state["by_id"] = {c["chunk_id"]: i for i, c in enumerate(chunks)}
        state["bm25"] = BM25([c["text"] for c in chunks])
    return state


def _reranker(name):
    state = _load()
    if "reranker" not in state:
        from sentence_transformers import CrossEncoder
        state["reranker"] = CrossEncoder(name)
    return state["reranker"]


def matches(meta: dict, filters: dict) -> bool:
    return all(str(meta.get(key)) in [str(v) for v in values] for key, values in filters.items())


def chroma_where(filters: dict):
    clauses = [{key: {"$in": list(values)}} for key, values in filters.items()]
    if not clauses:
        return None
    return clauses[0] if len(clauses) == 1 else {"$and": clauses}


def _hit(chunk, score):
    meta = dict(chunk["metadata"])
    meta.update({"doc_id": chunk["doc_id"], "start_char": chunk["start_char"], "end_char": chunk["end_char"]})
    return {"chunk_id": chunk["chunk_id"], "doc_id": chunk["doc_id"], "text": chunk["text"], "score": score, "metadata": meta}


import time
from contextlib import contextmanager


@contextmanager
def _timed(timings, name):
    """Adds the milliseconds spent in the block to timings[name]. Does nothing when timings is None."""
    if timings is None:
        yield
        return
    t0 = time.perf_counter()
    try:
        yield
    finally:
        timings[name] = timings.get(name, 0.0) + (time.perf_counter() - t0) * 1000


def access_groups() -> set:
    """Every access_group value present in the indexed chunks."""
    return {c["metadata"].get("access_group") for c in _chunks()["chunks"]} - {None, ""}


def search(query: str, k: int = None, deny_groups=None, timings: dict = None) -> list:
    """deny_groups: access groups the caller may not read. Chunks in them are removed BEFORE ranking, in both the vector and the keyword search (Lesson 5.3)."""
    state = _load()
    config = state["config"]
    rcfg = config["retrieval"]
    k = k or rcfg["k"]
    mode = rcfg.get("mode", "vector")
    filters = rcfg.get("filters") or {}
    rerank = rcfg.get("rerank") or {}
    candidates = max(rcfg.get("candidates", 50), k)
    depth = max(rerank.get("top_n", 30), k) if rerank.get("enabled") else k

    vector_text, keyword_text = query, query
    rewrite = rcfg.get("rewrite") or {}
    if rewrite.get("enabled"):
        from app.retrieval.rewrite import hypothetical_passage
        passage = hypothetical_passage(query, rewrite)
        if rewrite.get("apply_to", "vector") in ("vector", "both"):
            vector_text = passage if rewrite.get("replace", True) else query + "\n" + passage
        if rewrite.get("apply_to", "vector") == "both":
            keyword_text = query + "\n" + passage

    vector_ids, vector_scores = [], {}
    if mode in ("vector", "hybrid"):
        prefix = config["embedding"].get("query_prefix", "")
        with _timed(timings, "embed_query"):
            emb = state["model"].encode([prefix + vector_text], normalize_embeddings=config["embedding"]["normalize"])
        n = max(candidates, depth) if mode == "hybrid" else depth
        where = chroma_where(filters)
        if deny_groups:
            acl = {"access_group": {"$nin": list(deny_groups)}}   # chunks with no access_group are open and are kept by $nin
            where = acl if where is None else {"$and": [where, acl]}
        kwargs = {"where": where} if where else {}
        with _timed(timings, "vector_search"):
            res = state["collection"].query(query_embeddings=emb.tolist(), n_results=n, **kwargs)
        vector_ids = res["ids"][0]
        vector_scores = {cid: 1 - d for cid, d in zip(res["ids"][0], res["distances"][0])}

    bm25_ids, bm25_scores = [], {}
    if mode in ("bm25", "hybrid"):
        st = _chunks()
        allowed = None
        if filters or deny_groups:
            allowed = {i for i, c in enumerate(st["chunks"]) if matches(c["metadata"], filters) and c["metadata"].get("access_group") not in (deny_groups or ())}
        with _timed(timings, "keyword_search"):
            top = st["bm25"].top(keyword_text, max(candidates, depth), allowed)
        bm25_ids = [st["chunks"][i]["chunk_id"] for i, _ in top]
        bm25_scores = {st["chunks"][i]["chunk_id"]: s for i, s in top}

    if mode == "vector":
        ordered = [(cid, vector_scores[cid]) for cid in vector_ids]
    elif mode == "bm25":
        ordered = [(cid, bm25_scores[cid]) for cid in bm25_ids]
    else:
        ordered = rrf([vector_ids, bm25_ids], [rcfg.get("vector_weight", 1.0), rcfg.get("bm25_weight", 1.0)], rcfg.get("rrf_k", 60))
    ordered = ordered[:depth]

    st = _chunks()
    pool = [(st["chunks"][st["by_id"][cid]], score) for cid, score in ordered]
    if rerank.get("enabled") and pool:
        with _timed(timings, "rerank"):
            model = _reranker(rerank["model"])
            scores = model.predict([(query, c["text"]) for c, _ in pool])
        pool = sorted(((c, float(s)) for (c, _), s in zip(pool, scores)), key=lambda p: -p[1])
    return [_hit(c, s) for c, s in pool[:k]]


if __name__ == "__main__":
    args = sys.argv[1:]
    k = None
    if "--k" in args:  # optional: how many chunks to show, for example --k 20
        i = args.index("--k")
        k = int(args[i + 1])
        args = args[:i] + args[i + 2:]
    for hit in search(" ".join(args), k):
        tail = hit["text"][-50:].replace("\n", " ")
        print(f"{hit['score']:.3f}  {hit['chunk_id']}   \"...{tail}\"")
