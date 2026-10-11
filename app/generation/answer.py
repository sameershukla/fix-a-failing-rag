"""Answer a question from the retrieved chunks.

Two prompts, chosen by generation.prompt in the config:
  plain   the Module 0 prompt. No citations, no refusal rule, no grounding check.
  cited   Lesson 4.4. Numbered context, use only the context, every factual sentence ends with [n: "exact quote"].
Nothing else differs, so a run with one and a run with the other differ in the prompt only.
"""

import sys

from app.common import load_config
from app.cache.semantic import SemanticCache, scope_key
from app.security.context import build_context

SYSTEM = "You are a helpful assistant for an AI platform team."
PROMPT = "Answer the question using this context.\n\nContext:\n{context}\n\nQuestion: {question}"

PROMPT_CITED = (
    "Answer the question using ONLY the numbered context below.\n\n"
    "Rules:\n"
    "1. Every sentence that states a fact must end with one or more citations in the form [n: \"exact quote\"], where n is the chunk number "
    "and the quote is copied word for word from that chunk (at most 25 words).\n"
    "2. Do not cite a chunk for something it does not say.\n"
    "3. Do not add advice, numbers or facts that are not in the context.\n"
    "4. If the context does not contain the answer, say so in one sentence. You may then say what the context does cover, with citations.\n\n"
    "Context:\n{context}\n\nQuestion: {question}"
)


def prompt_for(style: str):
    """Returns (system, prompt template, how to format the chunks) for a prompt style."""
    if style == "plain":
        return SYSTEM, PROMPT, lambda chunks: "\n\n".join(c["text"] for c in chunks)
    if style == "cited":
        return SYSTEM, PROMPT_CITED, lambda chunks: "\n\n".join(f"[{i}] {c['text']}" for i, c in enumerate(chunks, 1))
    raise ValueError(f"unknown generation.prompt: {style}")


# The only function that talks to a model. To switch providers, change only this.
def call_llm(system: str, user: str) -> str:
    import anthropic

    llm = load_config()["llm"]
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
    response = client.messages.create(
        model=llm["model"],
        max_tokens=llm["max_tokens"],
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(block.text for block in response.content if block.type == "text")


def _semantic_cache(cfg: dict) -> SemanticCache:
    from app.common import DATA
    from app.retrieval.search import _load

    st = _load()
    c = cfg["cache"]["semantic"]
    embed = lambda xs: st["model"].encode(xs, normalize_embeddings=st["config"]["embedding"]["normalize"])
    return SemanticCache(DATA / "semantic_cache" / "entries.jsonl", embed, c["threshold"], c.get("ttl_days"))


def answer(question: str, caller: str = None) -> dict:
    cfg = load_config()
    caller = caller or cfg.get("security", {}).get("caller", "staff-all")
    cache_cfg = (cfg.get("cache") or {}).get("semantic") or {}
    cache, scope = None, None
    if cache_cfg.get("enabled"):           # Lesson 6.3: a hit skips retrieval and the model
        cache, scope = _semantic_cache(cfg), scope_key(cfg, caller)
        entry, sim = cache.lookup(question, scope)
        if entry:
            return {"question": question, "answer": entry["answer"], "chunks": [], "cache": {"hit": True, "similarity": sim, "matched_question": entry["question"]}}
    chunks = build_context(question, caller)["chunks"]   # applies the security controls the config turns on (Module 5)
    system, template, fmt = prompt_for(cfg.get("generation", {}).get("prompt", "plain"))
    text = call_llm(system, template.format(context=fmt(chunks), question=question))
    if cache is not None:
        cache.store(question, scope, text, [c["chunk_id"] for c in chunks])
    return {"question": question, "answer": text, "chunks": chunks, "cache": {"hit": False}}


if __name__ == "__main__":
    result = answer(" ".join(sys.argv[1:]))
    print(result["answer"])
    print("\n--- retrieved ---")
    for c in result["chunks"]:
        print(f"{c['score']:.3f}  {c['chunk_id']}")
