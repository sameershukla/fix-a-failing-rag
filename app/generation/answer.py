"""Answer a question from the retrieved chunks.

Two prompts, chosen by generation.prompt in the config:
  plain   the Module 0 prompt. No citations, no refusal rule, no grounding check.
  cited   Lesson 4.4. Numbered context, use only the context, every factual sentence ends with [n: "exact quote"].
Nothing else differs, so a run with one and a run with the other differ in the prompt only.
"""

import sys

from app.common import load_config
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


def answer(question: str) -> dict:
    chunks = build_context(question)["chunks"]   # applies the security controls the config turns on (Module 5)
    system, template, fmt = prompt_for(load_config().get("generation", {}).get("prompt", "plain"))
    text = call_llm(system, template.format(context=fmt(chunks), question=question))
    return {"question": question, "answer": text, "chunks": chunks}


if __name__ == "__main__":
    result = answer(" ".join(sys.argv[1:]))
    print(result["answer"])
    print("\n--- retrieved ---")
    for c in result["chunks"]:
        print(f"{c['score']:.3f}  {c['chunk_id']}")
