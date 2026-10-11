"""A corpus overlay: change what the index THINKS the corpus contains, without editing the corpus (Lesson 8.4).

Rules come from corpus.overlay in the config. Each rule has a regex on the doc_id and one action:
  exclude: true                       the document is not in this world
  set: {status: active, retired_date: null}   override metadata (null removes the key)
It is applied by the indexer and by the retriever, so both always agree. It exists to build a "before world" for drift tests: the same corpus, as it was before a
new edition was published. The corpus files are never touched.
"""

import copy
import re


def apply_overlay(chunks, rules):
    if not rules:
        return list(chunks)
    compiled = [(re.compile(r["match"]), r) for r in rules]
    out = []
    for c in chunks:
        hit = [r for pat, r in compiled if pat.search(c["doc_id"])]
        if any(r.get("exclude") for r in hit):
            continue
        sets = {}
        for r in hit:
            sets.update(r.get("set") or {})
        if sets:
            c = copy.deepcopy(c)
            for key, value in sets.items():
                if value is None:
                    c["metadata"].pop(key, None)
                else:
                    c["metadata"][key] = value
        out.append(c)
    return out
