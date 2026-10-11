"""The faithfulness judge. Sees only the retrieved chunks and the answer.

The model lists the claims and marks each supported or not. The VERDICT is computed here, not by the model: an answer is
unfaithful when at least one claim is unsupported. An answer with no claims, or a reply that is not valid JSON, gets no verdict
(verdict None) and is counted separately. Every call is cached on disk; the key holds model, prompt, max tokens, thinking and input.
Needs ANTHROPIC_API_KEY on a cache miss.
"""

import hashlib
import json
import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / os.environ.get("JUDGE_CONFIG", "config/judge.yaml")   # JUDGE_CONFIG=config/judge_v1.yaml reruns the frozen v1 prompt
CACHE = ROOT / "data/app/llm_cache/judge"
CITATION = re.compile(r"\[\d+\s*:\s*[\"“][^\"”\]]+[\"”]\s*\]|\[(?:\d+|[^\]\s]*::\d+)\]|\(\s*source:[^)]*\)", re.I)   # [n: "quote"] (Lesson 4.4), [n], [doc::n], (source: ...)


def load_config():
    return yaml.safe_load(CONFIG.read_text())


def strip_citations(answer):
    return CITATION.sub("", answer)


def build_prompt(cfg, chunks, answer):
    context = "\n\n".join(f"[Chunk {i}]\n{t}" for i, t in enumerate(chunks, 1))
    return cfg["prompt"].replace("{context}", context).replace("{answer}", strip_citations(answer))


def cache_key(cfg, prompt):
    payload = json.dumps({"version": cfg["prompt_version"], "model": cfg["model"], "max_tokens": cfg["max_tokens"],
                          "thinking": cfg["thinking"], "prompt": prompt}, sort_keys=True)
    return hashlib.sha1(payload.encode()).hexdigest()


def call_model(cfg, prompt):
    import anthropic

    r = anthropic.Anthropic().messages.create(model=cfg["model"], max_tokens=cfg["max_tokens"], messages=[{"role": "user", "content": prompt}])
    return "".join(b.text for b in r.content if b.type == "text"), r.stop_reason


def parse(text):
    """Use the LAST complete JSON object that has a claims list: a model sometimes writes one, then corrects itself and writes another."""
    dec, found = json.JSONDecoder(), None
    for m in re.finditer(r"\{", text):
        try:
            obj, _ = dec.raw_decode(text[m.start():])
        except ValueError:
            continue
        if isinstance(obj, dict) and isinstance(obj.get("claims"), list):
            found = obj["claims"]
    if found is None:
        return None
    try:
        return [{"claim": str(c["claim"]), "supported": bool(c["supported"]), "evidence": str(c.get("evidence", ""))} for c in found]
    except (KeyError, TypeError):
        return None


def judge(chunks, answer, cfg=None, use_cache=True):
    cfg = cfg or load_config()
    prompt = build_prompt(cfg, chunks, answer)
    path = CACHE / (cache_key(cfg, prompt) + ".json")
    if use_cache and path.exists():
        raw = json.loads(path.read_text())
    else:
        text, stop = call_model(cfg, prompt)
        raw = {"text": text, "stop_reason": stop}
        CACHE.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(raw, ensure_ascii=False))
    claims = parse(raw["text"])
    if not claims:
        return {"verdict": None, "claims": claims or [], "problem": "unparseable reply" if claims is None else "no claims", "stop_reason": raw["stop_reason"]}
    return {"verdict": "unfaithful" if any(not c["supported"] for c in claims) else "faithful", "claims": claims, "stop_reason": raw["stop_reason"]}
