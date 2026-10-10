"""Answer a question from the retrieved chunks. One plain prompt.

No citations, no refusal rule, no grounding check, no guardrails.
"""

import sys

from app.common import load_config
from app.retrieval.search import search

SYSTEM = "You are a helpful assistant for an AI platform team."
PROMPT = "Answer the question using this context.\n\nContext:\n{context}\n\nQuestion: {question}"


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
    chunks = search(question)
    context = "\n\n".join(c["text"] for c in chunks)
    text = call_llm(SYSTEM, PROMPT.format(context=context, question=question))
    return {"question": question, "answer": text, "chunks": chunks}


if __name__ == "__main__":
    result = answer(" ".join(sys.argv[1:]))
    print(result["answer"])
    print("\n--- retrieved ---")
    for c in result["chunks"]:
        print(f"{c['score']:.3f}  {c['chunk_id']}")
