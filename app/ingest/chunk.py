"""data/<system>/normalized/docs.jsonl -> data/<system>/chunks/<chunk_config_hash>/chunks.jsonl

Fixed windows by default, exactly as the baseline. Module 2 adds structure aware chunkers. Each one is switched on by
a flag under `chunking.structure` in the config, so one lesson changes one thing:

    tables     markdown tables: whole rows, with the title and header row repeated in every chunk
    config     fenced YAML blocks: one chunk per group of sibling settings, with the key path in front
    code       Python files: one chunk per function or class, with the file and symbol name in front
    title_prefix   the document title in front of every remaining fixed window (needs strategy: router)
    headings   markdown prose: one chunk per section, with the heading trail in front.
               `headings: long` applies it only to documents of at least `heading_min_chars` characters

A chunk's `text` is what gets embedded: the prefix plus a slice of the document. `start_char` and `end_char` point at
the slice only, so the golden set's evidence passages still line up with the chunk (lesson 1.3).
Token counts use the embedder's own tokenizer. The embedder reads at most WINDOW tokens, so the script reports how much
chunk text lies beyond it.
"""

import ast
import json
import re

import yaml

from app.common import NORMALIZED, ROOT, chunks_path, load_config, read_jsonl

WINDOW = 254   # all-MiniLM-L6-v2 reads 256 tokens, two of them are special tokens


class Counter:
    def __init__(self, tokenizer):
        self.tok = tokenizer

    def n(self, text: str) -> int:
        return len(self.tok(text, add_special_tokens=False, verbose=False)["input_ids"])


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


def fixed_chunks(text, offset, tokenizer, size, overlap, prefix=""):
    """Fixed windows over text, shifted so the offsets point into the whole document."""
    return [{"start": offset + s, "end": offset + e, "prefix": prefix} for s, e in split_fixed(text, tokenizer, size, overlap)]


def lines_with_offsets(text):
    pos = 0
    for line in text.split("\n"):
        yield pos, line
        pos += len(line) + 1


def doc_title(doc):
    return str(doc["metadata"].get("title") or doc["doc_id"])


# ---------------------------------------------------------------- markdown regions

def markdown_regions(text):
    """Split a document into ('prose' | 'table' | 'fence', start, end) regions that cover the whole text."""
    lines = list(lines_with_offsets(text))
    regions, i, prose_start = [], 0, 0

    def close_prose(upto):
        if upto > prose_start:
            regions.append(("prose", prose_start, upto))

    while i < len(lines):
        pos, line = lines[i]
        if line.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j][1].startswith("```"):
                j += 1
            if j < len(lines):
                close_prose(pos)
                end = lines[j][0] + len(lines[j][1])
                regions.append(("fence", pos, end))
                prose_start = end + 1
                i = j + 1
                continue
        if line.startswith("|"):
            j = i
            while j < len(lines) and lines[j][1].startswith("|"):
                j += 1
            if j - i >= 3 and re.match(r"^\|[\s:\-|]+\|?$", lines[i + 1][1]):
                close_prose(pos)
                end = lines[j - 1][0] + len(lines[j - 1][1])
                regions.append(("table", pos, end))
                prose_start = end + 1
                i = j
                continue
        i += 1
    close_prose(len(text))
    return regions


# ---------------------------------------------------------------- tables

def table_chunks(doc, start, end, cnt, size):
    """Whole rows only. Every chunk starts with the document title, the header row and the separator row."""
    rows = list(lines_with_offsets(doc["text"][start:end]))
    header, sep, body = rows[0][1], rows[1][1], rows[2:]
    prefix = f"{doc_title(doc)}\n{header}\n{sep}"
    base = cnt.n(prefix)
    chunks, cur_start, cur_end, cur_tokens = [], None, None, base
    for off, line in body:
        row_tokens = cnt.n(line)
        if cur_start is not None and cur_tokens + row_tokens > size:
            chunks.append({"start": cur_start, "end": cur_end, "prefix": prefix})
            cur_start, cur_tokens = None, base
        if cur_start is None:
            cur_start = start + off
        cur_end = start + off + len(line)
        cur_tokens += row_tokens
    if cur_start is not None:
        chunks.append({"start": cur_start, "end": cur_end, "prefix": prefix})
    return chunks


# ---------------------------------------------------------------- config blocks

KEY_LINE = re.compile(r"^(\s*)(- )?([\w\-\"'.]+)\s*:(.*)$")


def looks_like_yaml(lines):
    body = [l for _, l in lines if l.strip()]
    return bool(body) and sum(1 for l in body if KEY_LINE.match(l) or l.strip().startswith("- ")) / len(body) > 0.6


def config_chunks(doc, start, end, cnt, size, tokenizer, overlap):
    """One chunk per run of lines that share a parent key. The prefix is the key path. None if not a YAML like block."""
    block = list(lines_with_offsets(doc["text"][start:end]))
    inner = block[1:-1] if len(block) >= 3 else []
    if not inner or not looks_like_yaml(inner):
        return None
    stack, groups = [], []   # groups: [path, first line index, last line index]
    for idx, (_, line) in enumerate(inner):
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        m = KEY_LINE.match(line)
        is_parent = bool(m) and m.group(4).strip() == "" and not line.strip().startswith("- ")
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if is_parent:
            stack.append((indent, m.group(3).strip("\"'")))
        path = [k for _, k in stack]
        if groups and groups[-1][0] == path and not is_parent:
            groups[-1][2] = idx
        else:
            groups.append([path, idx, idx])
    chunks, title = [], doc_title(doc)
    for path, a, b in groups:
        prefix = f"{title}\nconfig path: {' > '.join(path) if path else 'top level'}"
        s = start + inner[a][0]
        e = start + inner[b][0] + len(inner[b][1])
        if cnt.n(prefix) + cnt.n(doc["text"][s:e]) <= size:
            chunks.append({"start": s, "end": e, "prefix": prefix})
        else:
            chunks += fixed_chunks(doc["text"][s:e], s, tokenizer, max(32, size - cnt.n(prefix)), overlap, prefix)
    return chunks


# ---------------------------------------------------------------- code

def python_chunks(doc, cnt, size, tokenizer, overlap):
    """One chunk per top level function or class. Code between two definitions goes with the next one."""
    text = doc["text"]
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return None
    kinds = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
    defs = [n for n in tree.body if isinstance(n, kinds)]
    if not defs:
        return None
    line_starts = [0]
    for line in text.split("\n"):
        line_starts.append(line_starts[-1] + len(line) + 1)

    def span(node):
        first = min([node.lineno] + [d.lineno for d in node.decorator_list])
        return line_starts[first - 1], min(line_starts[node.end_lineno], len(text))

    chunks, first_start = [], span(defs[0])[0]
    if text[:first_start].strip():
        chunks += code_unit(doc, "module header", 0, first_start, cnt, size, tokenizer, overlap)
    prev = first_start
    for node in defs:
        _, e = span(node)
        label = ("class " if isinstance(node, ast.ClassDef) else "function ") + node.name
        chunks += code_unit(doc, label, prev, e, cnt, size, tokenizer, overlap)
        prev = e
    if text[prev:].strip():
        chunks += code_unit(doc, "module footer", prev, len(text), cnt, size, tokenizer, overlap)
    return chunks


def code_unit(doc, label, s, e, cnt, size, tokenizer, overlap):
    prefix = f"{doc['doc_id']}\n{label}"
    body = doc["text"][s:e]
    if cnt.n(prefix) + cnt.n(body) <= size:
        return [{"start": s, "end": e, "prefix": prefix}]
    return fixed_chunks(body, s, tokenizer, max(32, size - cnt.n(prefix)), overlap, prefix)


# ---------------------------------------------------------------- headings

HEADING = re.compile(r"^(#{1,6}) +(.*)$")


def heading_chunks(doc, start, end, cnt, size, tokenizer, overlap):
    """One chunk per section. The prefix is the document title and the heading trail. None if fewer than two headings."""
    text = doc["text"]
    region = list(lines_with_offsets(text[start:end]))
    if sum(1 for _, l in region if HEADING.match(l)) < 2:
        return None
    sections, trail = [], []
    cur_start, cur_names = start, []
    for off, line in region:
        m = HEADING.match(line)
        if m:
            pos = start + off
            if pos > cur_start and text[cur_start:pos].strip():
                sections.append((list(cur_names), cur_start, pos))
            level = len(m.group(1))
            trail = [t for t in trail if t[0] < level] + [(level, m.group(2).strip())]
            cur_names, cur_start = [n for _, n in trail], pos
    if end > cur_start and text[cur_start:end].strip():
        sections.append((list(cur_names), cur_start, end))
    chunks, title = [], doc_title(doc)
    for names, s, e in sections:
        names = names[1:] if names and names[0] == title else names
        prefix = f"{title}\n{' > '.join(names)}" if names else title
        e = s + len(text[s:e].rstrip("\n"))
        if cnt.n(prefix) + cnt.n(text[s:e]) <= size:
            chunks.append({"start": s, "end": e, "prefix": prefix})
        else:
            chunks += fixed_chunks(text[s:e], s, tokenizer, max(32, size - cnt.n(prefix)), overlap, prefix)
    return chunks


# ---------------------------------------------------------------- router

def is_code(doc):
    meta = doc["metadata"]
    return meta.get("source_type") == "source_code" or doc["doc_id"].rsplit(".", 1)[-1] in ("py", "ts", "sql")


def is_python(doc):
    return doc["metadata"].get("language") == "python" or doc["doc_id"].endswith(".py")


def plan(doc, cfg, tokenizer, cnt):
    """Chunk spans for one document: a list of {start, end, prefix, strategy}."""
    size, overlap = cfg["size_tokens"], cfg["overlap_tokens"]
    flags = cfg.get("structure", {}) if cfg.get("strategy") == "router" else {}
    text = doc["text"]
    tag = lambda cs, name: [{**c, "strategy": name} for c in cs]
    if is_code(doc):
        if flags.get("code") and is_python(doc):
            got = python_chunks(doc, cnt, size, tokenizer, overlap)
            if got is not None:
                return tag(got, "code")
        return tag(fixed_chunks(text, 0, tokenizer, size, overlap), "fixed")
    if not flags:
        return tag(fixed_chunks(text, 0, tokenizer, size, overlap), "fixed")
    out = []
    title_prefix = doc_title(doc) if flags.get("title_prefix") else ""
    window = size - cnt.n(title_prefix) if title_prefix else size
    for kind, s, e in markdown_regions(text):
        piece = None
        if kind == "table" and flags.get("tables"):
            piece = tag(table_chunks(doc, s, e, cnt, size), "table")
        elif kind == "fence" and flags.get("config"):
            got = config_chunks(doc, s, e, cnt, size, tokenizer, overlap)
            piece = tag(got, "config") if got is not None else None
        elif kind == "prose" and flags.get("headings") and (flags["headings"] != "long" or len(text) >= cfg.get("heading_min_chars", 20000)):
            got = heading_chunks(doc, s, e, cnt, size, tokenizer, overlap)
            piece = tag(got, "headings") if got is not None else None
        if piece is None:
            piece = tag(fixed_chunks(text[s:e], s, tokenizer, window, overlap, title_prefix), "fixed")
        out += piece
    return out


def main():
    config = load_config()
    from transformers import AutoTokenizer

    cfg = config["chunking"]
    tokenizer = AutoTokenizer.from_pretrained(cfg["tokenizer"])
    cnt = Counter(tokenizer)
    window = cfg.get("window_tokens", WINDOW)   # set it when the embedding model reads a different number of tokens
    out = chunks_path(config)
    out.parent.mkdir(parents=True, exist_ok=True)

    count, strategies = 0, {}
    n_over = tokens_total = tokens_cut = 0
    with out.open("w", encoding="utf-8") as fh:
        for doc in read_jsonl(NORMALIZED):
            for i, c in enumerate(plan(doc, cfg, tokenizer, cnt)):
                body = doc["text"][c["start"]:c["end"]]
                text = (c["prefix"] + "\n" + body) if c["prefix"] else body
                record = {
                    "chunk_id": f"{doc['doc_id']}::{i}",
                    "doc_id": doc["doc_id"],
                    "start_char": c["start"],
                    "end_char": c["end"],
                    "text": text,
                    "metadata": doc["metadata"],
                }
                fh.write(json.dumps(record, ensure_ascii=False) + "\n")
                count += 1
                strategies[c["strategy"]] = strategies.get(c["strategy"], 0) + 1
                n = cnt.n(text)
                tokens_total += n
                if n > window:
                    n_over += 1
                    tokens_cut += n - window

    stats = {"chunks": count, "by_strategy": strategies, "chunks_over_window": n_over,
             "share_chunks_over_window": round(n_over / count, 3), "tokens": tokens_total,
             "tokens_beyond_window": tokens_cut, "share_tokens_beyond_window": round(tokens_cut / tokens_total, 3)}
    (out.parent / "config.yaml").write_text(yaml.safe_dump(cfg))
    (out.parent / "stats.json").write_text(json.dumps(stats, indent=2))
    print(f"wrote {count} chunks -> {out.relative_to(ROOT)}")
    print(f"by strategy: {strategies}")
    print(f"chunks longer than the embedder window: {n_over} ({100*n_over/count:.0f}%); "
          f"tokens beyond it: {tokens_cut} of {tokens_total} ({100*tokens_cut/tokens_total:.0f}%)")


if __name__ == "__main__":
    main()
