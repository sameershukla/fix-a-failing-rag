"""Shared paths and config loading. data goes to data/<system>/. app/ also honors CONFIG= for experiment configs."""

import hashlib
import json
import os
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
SYSTEM = Path(__file__).resolve().parent.name   # "baseline" or "app": each system owns its own data folder
DATA = ROOT / "data" / SYSTEM
NORMALIZED = DATA / "normalized" / "docs.jsonl"
CHUNKS_DIR = DATA / "chunks"
INDEX_DIR = DATA / "index"      # Chroma persist directory
_override = os.environ.get("RAG_CONFIG")   # make ... CONFIG=config/experiments/<file>.yaml sets this
CONFIG_PATH = (ROOT / _override) if _override else Path(__file__).resolve().parent / "config.yaml"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text())


def chunk_config_hash(config: dict) -> str:
    """Folder name for one chunking config. Same settings, same hash."""
    canonical = json.dumps(config["chunking"], sort_keys=True)
    return hashlib.sha1(canonical.encode()).hexdigest()[:10]


def collection_name(config: dict) -> str:
    """Chroma collection for this config. "auto" gives one collection per index-relevant config
    (chunking, embedding, distance), so two configs can sit side by side and be compared."""
    name = config["vector_store"]["collection"]
    if name != "auto":
        return name
    parts = {k: config[k] for k in ("chunking", "embedding")}
    parts["distance"] = config["vector_store"]["distance"]
    digest = hashlib.sha1(json.dumps(parts, sort_keys=True).encode()).hexdigest()[:6]
    return f"{SYSTEM}_{digest}"


def chunks_path(config: dict) -> Path:
    return CHUNKS_DIR / chunk_config_hash(config) / "chunks.jsonl"


def read_jsonl(path: Path):
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)
