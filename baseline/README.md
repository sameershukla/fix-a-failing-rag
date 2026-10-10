# Baseline: the failing RAG system

This system is broken on purpose. Never edit it.

It is what a team plausibly builds first: fixed size chunks, vector only search, K = 5, one plain prompt. Every later module fixes one failure and proves the fix with `make eval`. The `baseline` tag marks the frozen state.

| Part | File | What it does |
|---|---|---|
| Normalize | `ingest/normalize.py` | Reads text, splits off front matter, keeps it as metadata and uses none of it |
| Chunk | `ingest/chunk.py` | Fixed 500 token windows, overlap 50, ignores code, tables and messages |
| Index | `ingest/index.py` | Embeds chunks, stores them in Chroma under `data/baseline/index/` |
| Retrieve | `retrieval/search.py` | Vector only, top 5. No filters, no BM25, no reranker, no access control |
| Answer | `generation/answer.py` | "Answer the question using this context." No citations, no refusal rule |

Settings live in `config.yaml`. Only `corpus/book/v1`, `corpus/repo` and `corpus/generated` are indexed.
