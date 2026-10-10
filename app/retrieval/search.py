"""Vector only search, top K. No filters, no BM25, no reranker, no access control."""

import sys

from app.common import INDEX_DIR, collection_name, load_config

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
    return _cache


def search(query: str, k: int = None) -> list:
    state = _load()
    config = state["config"]
    k = k or config["retrieval"]["k"]
    embedding = state["model"].encode([query], normalize_embeddings=config["embedding"]["normalize"])
    result = state["collection"].query(query_embeddings=embedding.tolist(), n_results=k)
    return [
        {"chunk_id": cid, "doc_id": meta["doc_id"], "text": text, "score": 1 - dist, "metadata": meta}
        for cid, text, meta, dist in zip(result["ids"][0], result["documents"][0],
                                         result["metadatas"][0], result["distances"][0])
    ]


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
