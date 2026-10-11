"""System version: one id for everything that can change what the system does (Lesson 8.1).

The old config hash covered only the yaml config. A prompt edited in code, the judge settings, the caller rules or the golden set could change a result
and leave that hash unchanged. The manifest hashes each behavior input on its own, so a run record can say WHICH part changed between two runs.
system_version is a short hash of the behavior parts. The git commit and dirty flag are recorded beside it, not inside it.
"""

import hashlib
import json
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _sha(text) -> str:
    return hashlib.sha1(text.encode("utf-8") if isinstance(text, str) else text).hexdigest()[:8]


def _file(rel: str) -> str:
    p = ROOT / rel
    return _sha(p.read_bytes()) if p.exists() else "absent"


def behavior_parts() -> dict:
    """Every input that can change an answer, a retrieval result or a score. Name -> short content hash."""
    from app.common import load_config
    from app.generation import answer as gen
    from app.retrieval import rewrite
    from eval.metrics import relevance

    return {
        "config": _sha(yaml.safe_dump(load_config(), sort_keys=True)),          # the active app config (after CONFIG= is applied)
        "prompt.system": _sha(gen.SYSTEM),
        "prompt.plain": _sha(gen.PROMPT),
        "prompt.cited": _sha(gen.PROMPT_CITED),
        "prompt.hyde": _sha(rewrite.PROMPT),
        "judge": _file("config/judge.yaml"),                                      # model, prompt text, max tokens
        "security.callers": _file("config/security.yaml"),
        "pricing": _file("config/pricing.yaml"),
        "relevance_rule": _sha(str(relevance.MIN_COVER)),
        "golden": _file("eval/golden/golden.yaml"),
    }


def git_state() -> dict:
    def run(*a):
        return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return {"commit": run("rev-parse", "--short", "HEAD") or None, "dirty": bool(run("status", "--porcelain", "--", "app", "eval", "config", "ops"))}


def manifest() -> dict:
    parts = behavior_parts()
    return {"system_version": _sha(json.dumps(parts, sort_keys=True)), "parts": parts, "git": git_state()}


def stamp(record: dict) -> dict:
    """Adds the manifest to a run record. Call it where the record is built."""
    m = manifest()
    record["system_version"] = m["system_version"]
    record["manifest"] = {"parts": m["parts"], "git": m["git"]}
    return record


def changed_parts(a: dict, b: dict) -> list:
    """Which behavior parts differ between two manifests (each is a record's 'manifest')."""
    pa, pb = a["parts"], b["parts"]
    return sorted(k for k in set(pa) | set(pb) if pa.get(k) != pb.get(k))
