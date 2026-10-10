"""data/<system>/normalized/docs.jsonl -> data/<system>/chunks/<chunk_config_hash>/chunks.jsonl

Naive on purpose: a fixed size window of tokens slides over the text. It does not know about
functions, tables, headings or Slack messages, so it cuts through all of them.
"""

import json
import shutil

import yaml

from baseline.common import NORMALIZED, ROOT, chunks_path, load_config, read_jsonl


def split_fixed(text: str, tokenizer, size: int, overlap: int):
    """Yield (start_char, end_char) for each window of `size` tokens, stepping `size - overlap`."""
    spans = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True,
                      truncation=False, verbose=False)["offset_mapping"]
    step = size - overlap
    start = 0
    while start < len(spans):
        end = min(start + size, len(spans))
        yield spans[start][0], spans[end - 1][1]
        if end == len(spans):
            break
        start += step


def main():
    config = load_config()
    from transformers import AutoTokenizer

    size = config["chunking"]["size_tokens"]
    overlap = config["chunking"]["overlap_tokens"]
    tokenizer = AutoTokenizer.from_pretrained(config["chunking"]["tokenizer"])
    out = chunks_path(config)
    out.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with out.open("w", encoding="utf-8") as fh:
        for doc in read_jsonl(NORMALIZED):
            for i, (start, end) in enumerate(split_fixed(doc["text"], tokenizer, size, overlap)):
                record = {
                    "chunk_id": f"{doc['doc_id']}::{i}",
                    "doc_id": doc["doc_id"],
                    "start_char": start,
                    "end_char": end,
                    "text": doc["text"][start:end],
                    "metadata": doc["metadata"],
                }
                fh.write(json.dumps(record, ensure_ascii=False) + "\n")
                count += 1

    (out.parent / "config.yaml").write_text(yaml.safe_dump(config["chunking"]))
    print(f"wrote {count} chunks -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
