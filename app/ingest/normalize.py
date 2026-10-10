"""corpus/ -> data/<system>/normalized/docs.jsonl

Naive on purpose: read each file as plain text, split off the front matter, keep it as
metadata, and use none of it. No table handling, no cleanup, no dedupe, no edition logic.
"""

import json
import re
from pathlib import Path

import yaml

from app.common import CORPUS, NORMALIZED, ROOT, load_config

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
# Plain text readers only. Scanned PDFs are left out on purpose: they need OCR, which the baseline does not have.
EXTENSIONS = {".md", ".py", ".ts", ".sql", ".txt", ".eml", ".log", ".html", ".csv", ".json", ".yaml", ".diff"}
CODE_EXTENSIONS = {".py", ".ts", ".sql"}
SIDECAR_SUFFIX = ".meta.yaml"   # corpus/formats, human and code_extra files carry their metadata (and doc_id) here
CODE_HEADER = re.compile(r"\A((?:(?:#|//|--) [a-z_]+: .*\n)+)")   # code files carry their metadata in a comment header


def doc_id_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix().split("/", 1)[1]  # drop the corpus folder
    return rel[:-3] if rel.endswith(".md") else rel  # keep .py, drop .md


def source_for(doc_id: str) -> str:
    return doc_id.split("/")[0]  # book, repo, generated, brightcart


def normalize_file(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    metadata = {}
    sidecar = path.with_name(path.name + SIDECAR_SUFFIX)
    if sidecar.exists():
        metadata = yaml.safe_load(sidecar.read_text(encoding="utf-8")) or {}
    match = FRONT_MATTER.match(raw)
    if match:
        metadata.update(yaml.safe_load(match.group(1)) or {})
        raw = raw[match.end():]
    header = CODE_HEADER.match(raw) if path.suffix in CODE_EXTENSIONS else None
    if header:   # the header stays in the text, so character offsets are unchanged
        for line in header.group(1).splitlines():
            key, value = line.split(": ", 1)
            metadata[key.lstrip("#/- ").strip()] = value.strip()
    doc_id = metadata.get("doc_id") or doc_id_for(path)  # corpus docs carry their own doc_id
    metadata.pop("retrieval_hazard", None)   # an authoring note about why a doc is hard: never part of the indexed record
    metadata["source"] = source_for(doc_id)
    if metadata["source"] == "repo":
        metadata["program"] = path.parent.name
    return {"doc_id": doc_id, "text": raw.lstrip("\n"), "metadata": metadata}


def collect_files(config: dict) -> list:
    files = []
    for folder in config["corpus"]["include"]:
        base = ROOT / folder
        files += [p for p in base.rglob("*") if p.is_file() and p.suffix in EXTENSIONS and not p.name.endswith(SIDECAR_SUFFIX)]
    excluded = [(ROOT / e).resolve() for e in config["corpus"].get("exclude", [])]
    files = [p for p in files if not any(e in p.resolve().parents for e in excluded)]
    return sorted(files)  # sorted, so the same corpus always gives the same output


def main():
    config = load_config()
    files = collect_files(config)
    NORMALIZED.parent.mkdir(parents=True, exist_ok=True)
    with NORMALIZED.open("w", encoding="utf-8") as fh:
        for path in files:
            fh.write(json.dumps(normalize_file(path), ensure_ascii=False, default=str) + "\n")
    print(f"normalized {len(files)} docs -> {NORMALIZED.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
