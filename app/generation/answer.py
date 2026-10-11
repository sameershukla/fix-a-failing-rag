"""Answer a question from the retrieved chunks.

Two prompts, chosen by generation.prompt in the config:
  plain   the Module 0 prompt. No citations, no refusal rule, no grounding check.
  cited   Lesson 4.4. Numbered context, use only the context, every factual sentence ends with [n: "exact quote"].
Nothing else differs, so a run with one and a run with the other differ in the prompt only.
"""

import sys
from datetime import datetime, timezone

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
def call_llm_full(system: str, user: str) -> dict:
    import time

    import anthropic

    llm = load_config()["llm"]
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
    t0 = time.perf_counter()
    response = client.messages.create(
        model=llm["model"],
        max_tokens=llm["max_tokens"],
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return {"text": "".join(block.text for block in response.content if block.type == "text"), "stop_reason": response.stop_reason,
            "input_tokens": response.usage.input_tokens, "output_tokens": response.usage.output_tokens, "latency_ms": (time.perf_counter() - t0) * 1000}


def call_llm(system: str, user: str) -> str:
    return call_llm_full(system, user)["text"]


def _semantic_cache(cfg: dict) -> SemanticCache:
    from app.common import DATA
    from app.retrieval.search import _load

    st = _load()
    c = cfg["cache"]["semantic"]
    embed = lambda xs: st["model"].encode(xs, normalize_embeddings=st["config"]["embedding"]["normalize"])
    return SemanticCache(DATA / "semantic_cache" / "entries.jsonl", embed, c["threshold"], c.get("ttl_days"))


def answer(question: str, caller: str = None, llm=None, trace_path=None) -> dict:
    """llm: a function (system, user) -> {text, stop_reason, input_tokens, output_tokens, latency_ms}; defaults to the real model. Used by tests.
    Writes one trace per request when tracing.enabled is true (Lesson 8.2), including requests that fail."""
    import time

    from app import trace

    cfg = load_config()
    caller = caller or cfg.get("security", {}).get("caller", "staff-all")
    tracing = (cfg.get("tracing") or {}).get("enabled", False)
    t_start = time.perf_counter()
    tr = {"trace_id": trace.new_id(), "time": datetime.now(timezone.utc).isoformat(timespec="seconds"), "system_version": trace.system_version() if tracing else None,
          "question": question, "caller": caller, "timings_ms": {}}
    try:
        cache_cfg = (cfg.get("cache") or {}).get("semantic") or {}
        cache, scope = None, None
        if cache_cfg.get("enabled"):           # Lesson 6.3: a hit skips retrieval and the model
            cache, scope = _semantic_cache(cfg), scope_key(cfg, caller)
            entry, sim = cache.lookup(question, scope)
            if entry:
                tr.update(cache={"hit": True, "similarity": sim, "matched_question": entry["question"]}, answer=entry["answer"])
                return {"question": question, "answer": entry["answer"], "chunks": [], "cache": tr["cache"], "trace_id": tr["trace_id"]}
        tr["cache"] = {"hit": False}
        timings = {}
        ctx = build_context(question, caller, timings=timings)   # applies the security controls the config turns on (Module 5)
        chunks = ctx["chunks"]
        style = cfg.get("generation", {}).get("prompt", "plain")
        system, template, fmt = prompt_for(style)
        user = template.format(context=fmt(chunks), question=question)
        full_prompt = system + "\n\n" + user   # the hash and the stored prompt use this same string
        res = (llm or call_llm_full)(system, user)
        text = res["text"]
        tr.update(retrieved=[{"chunk_id": c["chunk_id"], "score": round(c["score"], 4)} for c in chunks],
                  removed=[{"chunk_id": c["chunk_id"], "why": "injection filter: " + ",".join(c.get("injection_rules", [])) if c.get("injection_rules") else "access control"} for c in ctx["removed"]],
                  redactions=ctx["redactions"], denied_groups=ctx["denied_groups"], prompt_style=style, prompt_hash=trace.prompt_hash(full_prompt),
                  prompt=full_prompt if (cfg.get("tracing") or {}).get("store_prompt", True) else None, model=cfg["llm"]["model"],
                  usage={"input_tokens": res.get("input_tokens"), "output_tokens": res.get("output_tokens"), "stop_reason": res.get("stop_reason")}, answer=text)
        tr["timings_ms"] = {**{k: round(v, 1) for k, v in timings.items()}, "model": round(res.get("latency_ms") or 0, 1)}
        if cache is not None:
            cache.store(question, scope, text, [c["chunk_id"] for c in chunks])
        return {"question": question, "answer": text, "chunks": chunks, "cache": {"hit": False}, "trace_id": tr["trace_id"]}
    except Exception as e:
        tr["error"] = f"{type(e).__name__}: {e}"
        raise
    finally:
        tr["timings_ms"]["total"] = round((time.perf_counter() - t_start) * 1000, 1)
        if tracing:
            trace.write(tr, trace_path)


if __name__ == "__main__":
    result = answer(" ".join(sys.argv[1:]))
    print(result["answer"])
    print("\n--- retrieved ---")
    for c in result["chunks"]:
        print(f"{c['score']:.3f}  {c['chunk_id']}")
