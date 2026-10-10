"""data/<system>/chunks/<hash>/chunks.jsonl -> data/<system>/index (Chroma)

Embeds every chunk and stores it in Chroma. The index is disposable: it is dropped and
rebuilt from the chunks each time. Metadata is stored but never used for filtering.
"""

from baseline.common import INDEX_DIR, chunks_path, collection_name, load_config, read_jsonl

BATCH = 256


def scalar_metadata(chunk: dict) -> dict:
    """Chroma only accepts str, int, float, bool values."""
    meta = {"doc_id": chunk["doc_id"], "start_char": chunk["start_char"], "end_char": chunk["end_char"]}
    for key, value in chunk["metadata"].items():
        if isinstance(value, (str, int, float, bool)):
            meta[key] = value
        elif value is not None:
            meta[key] = str(value)
    return meta


def main():
    import chromadb
    from sentence_transformers import SentenceTransformer

    config = load_config()
    chunks = list(read_jsonl(chunks_path(config)))

    model = SentenceTransformer(config["embedding"]["model"])
    client = chromadb.PersistentClient(path=str(INDEX_DIR))
    name = collection_name(config)
    if name in [c.name for c in client.list_collections()]:
        client.delete_collection(name)
    collection = client.create_collection(name, metadata={"hnsw:space": config["vector_store"]["distance"]})

    for i in range(0, len(chunks), BATCH):
        batch = chunks[i:i + BATCH]
        embeddings = model.encode([c["text"] for c in batch],
                                  normalize_embeddings=config["embedding"]["normalize"])
        collection.add(
            ids=[c["chunk_id"] for c in batch],
            documents=[c["text"] for c in batch],
            embeddings=embeddings.tolist(),
            metadatas=[scalar_metadata(c) for c in batch],
        )
        print(f"  indexed {min(i + BATCH, len(chunks))}/{len(chunks)}", flush=True)
    print(f"indexed {len(chunks)} chunks into collection '{name}'")


if __name__ == "__main__":
    main()
