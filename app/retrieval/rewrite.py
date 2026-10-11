"""Query rewriting with a language model (HyDE: hypothetical document embeddings).

The model writes a short passage that would answer the question, in the style of the internal docs. That passage is used
as the search text instead of, or beside, the raw question. Every model call is cached on disk. The cache key includes every
setting that can change the output: model, prompt, max tokens, the thinking setting and the question. This SDK version has no temperature
argument, so the model's default sampling applies and there is nothing to record.
Needs ANTHROPIC_API_KEY on a cache miss.
"""

import hashlib
import json

from app.common import DATA

CACHE_DIR = DATA / "llm_cache"
PROMPT = ("You are helping a search engine find passages in BrightCart's internal support and engineering documentation. Write a short "
          "passage (two or three sentences) in the style of an internal policy, runbook or config note that would answer the question below. "
          "The passage is only used as a search query to find the real document. It is never shown to anyone and is never treated as fact, "
          "so it does not need to be accurate: guess the wording, names and numbers such a document would likely contain. "
          "Write only the passage.\n\nQuestion: {question}\n\nPassage:")
THINKING = {"type": "disabled"}   # with thinking on, the model can spend the whole token limit before writing any text


def cache_key(model: str, prompt: str, max_tokens: int, question: str) -> str:
    payload = json.dumps({"model": model, "prompt": prompt, "max_tokens": max_tokens, "thinking": THINKING, "question": question}, sort_keys=True)
    return hashlib.sha1(payload.encode()).hexdigest()


def call_model(model: str, prompt_text: str, max_tokens: int) -> str:
    import anthropic

    client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY
    response = client.messages.create(model=model, max_tokens=max_tokens, thinking=THINKING,
                                      messages=[{"role": "user", "content": prompt_text}])
    text = "".join(b.text for b in response.content if b.type == "text").strip()
    if not text:   # never cache or search with an empty passage
        raise RuntimeError(f"the model returned no text (stop_reason={response.stop_reason}, blocks={[b.type for b in response.content]})")
    return text


def hypothetical_passage(question: str, cfg: dict, caller=call_model) -> str:
    model, max_tokens = cfg["model"], cfg.get("max_tokens", 150)
    key = cache_key(model, PROMPT, max_tokens, question)
    path = CACHE_DIR / f"{key}.json"
    if path.exists():
        return json.loads(path.read_text())["text"]
    text = caller(model, PROMPT.format(question=question), max_tokens)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"model": model, "question": question, "text": text}, ensure_ascii=False))
    return text
