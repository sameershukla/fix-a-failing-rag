"""A semantic cache for answers (Lesson 6.3).

If a new question is close enough to an earlier one, return the stored answer and skip retrieval and the model.
Similarity is not the same as "same question": a near miss can be very close and still need a different answer. So:
  - an entry is only reused inside its SCOPE. The scope is a hash of everything that can change an answer: who is asking (the caller), the security
    switches, the prompt style, the answer model, max tokens and the retrieval settings. A staff answer is never served to a support agent.
  - the threshold is a setting in the config and is chosen with eval/cache_eval.py, not guessed.
  - entries expire after ttl_days, because documents change.
"""

import hashlib
import json
import time
from pathlib import Path

import numpy as np


def scope_key(cfg: dict, caller: str) -> str:
    parts = {"caller": caller, "security": cfg.get("security"), "prompt": (cfg.get("generation") or {}).get("prompt", "plain"),
             "llm": cfg.get("llm"), "retrieval": cfg.get("retrieval"), "embedding": cfg.get("embedding"), "chunking": cfg.get("chunking")}
    return hashlib.sha1(json.dumps(parts, sort_keys=True, default=str).encode()).hexdigest()[:12]


class SemanticCache:
    def __init__(self, path: Path, embed, threshold: float, ttl_days: float = None, now=time.time):
        self.path, self.embed, self.threshold, self.ttl_days, self.now = Path(path), embed, threshold, ttl_days, now
        self.entries = []   # {"scope", "question", "vec", "answer", "chunk_ids", "created"}
        if self.path.exists():
            for line in self.path.read_text(encoding="utf-8").splitlines():
                e = json.loads(line); e["vec"] = np.array(e["vec"], dtype=float); self.entries.append(e)

    def _alive(self, e) -> bool:
        return self.ttl_days is None or (self.now() - e["created"]) <= self.ttl_days * 86400

    def lookup(self, question: str, scope: str):
        """Returns (entry, similarity) for the most similar live entry in this scope if it reaches the threshold, else (None, best similarity or None)."""
        vec = np.asarray(self.embed([question])[0], dtype=float)
        best, best_sim = None, None
        for e in self.entries:
            if e["scope"] != scope or not self._alive(e):
                continue
            sim = float(vec @ e["vec"])
            if best_sim is None or sim > best_sim:
                best, best_sim = e, sim
        if best is not None and best_sim >= self.threshold:
            return best, best_sim
        return None, best_sim

    def store(self, question: str, scope: str, answer: str, chunk_ids: list):
        e = {"scope": scope, "question": question, "vec": np.asarray(self.embed([question])[0], dtype=float), "answer": answer, "chunk_ids": chunk_ids, "created": self.now()}
        self.entries.append(e)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({**e, "vec": e["vec"].tolist()}, ensure_ascii=False) + "\n")
