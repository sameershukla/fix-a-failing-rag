"""Generation run: retrieve, answer, and save everything a judge or a person needs to read.

make eval-gen SYSTEM=app [SUBSET=dev] [LIMIT=40]

Without SUBSET it uses the whole golden set. LIMIT takes a seeded sample that keeps the answerable and unanswerable mix
(40% unanswerable, because the plain prompt fails most often there). Each answer is cached on disk. The cache key holds every
setting that can change the output: model, system prompt, prompt, max tokens and the exact context text.
Needs ANTHROPIC_API_KEY on a cache miss. This step does not judge anything; judging is Lesson 4.2.
"""

import argparse
import hashlib
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def cache_key(model, system, prompt, max_tokens, context):
    payload = json.dumps({"model": model, "system": system, "prompt": prompt, "max_tokens": max_tokens, "context": context}, sort_keys=True)
    return hashlib.sha1(payload.encode()).hexdigest()


def call_model(model, system, user, max_tokens):
    import anthropic

    client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY
    r = client.messages.create(model=model, max_tokens=max_tokens, system=system, messages=[{"role": "user", "content": user}])
    text = "".join(b.text for b in r.content if b.type == "text")
    return {"text": text, "stop_reason": r.stop_reason, "output_tokens": r.usage.output_tokens}


def pick(golden, ids, limit, seed):
    items = [q for q in golden if ids is None or q["id"] in ids]
    if not limit or limit >= len(items):
        return items
    rng = random.Random(seed)
    un = [q for q in items if not q["answerable"]]
    an = [q for q in items if q["answerable"]]
    n_un = min(len(un), round(limit * 0.4))
    chosen = rng.sample(un, n_un) + rng.sample(an, limit - n_un)
    return sorted(chosen, key=lambda q: q["id"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--system", default="app")
    ap.add_argument("--subset", default="")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--no-cache", action="store_true")
    args = ap.parse_args()
    if args.system != "app":
        sys.exit("eval-gen runs the app system only (the baseline is frozen and has no Module 4 changes).")

    from app.common import DATA, load_config
    from app.generation.answer import prompt_for
    from app.retrieval.search import search

    cfg = load_config()
    llm = cfg["llm"]
    style = cfg.get("generation", {}).get("prompt", "plain")
    SYSTEM, PROMPT, fmt = prompt_for(style)
    golden = yaml.safe_load((ROOT / "eval/golden/golden.yaml").read_text(encoding="utf-8"))
    ids = None
    if args.subset:
        ids = set(yaml.safe_load((ROOT / f"eval/golden/subsets/{args.subset}.yaml").read_text())["ids"])
    questions = pick(golden, ids, args.limit, args.seed)

    cache_dir = DATA / "llm_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    cfg_hash = hashlib.sha1(yaml.safe_dump(cfg, sort_keys=True).encode()).hexdigest()[:6]
    run_id = f"gen-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-{cfg_hash}"
    out_dir = ROOT / "eval" / "runs" / run_id
    out_dir.mkdir(parents=True)

    rows, calls = [], 0
    for i, q in enumerate(questions, 1):
        chunks = search(q["question"])
        context = fmt(chunks)
        user = PROMPT.format(context=context, question=q["question"])
        path = cache_dir / (cache_key(llm["model"], SYSTEM, PROMPT, llm["max_tokens"], context + "\n" + q["question"]) + ".json")
        if path.exists() and not args.no_cache:
            res = json.loads(path.read_text())
        else:
            res = call_model(llm["model"], SYSTEM, user, llm["max_tokens"])
            path.write_text(json.dumps(res, ensure_ascii=False))
            calls += 1
        rows.append({"id": q["id"], "question": q["question"], "answerable": q["answerable"], "tags": q.get("tags", []),
                     "chunks": [{"chunk_id": c["chunk_id"], "doc_id": c["doc_id"], "text": c["text"]} for c in chunks],
                     "answer": res["text"], "stop_reason": res["stop_reason"], "output_tokens": res["output_tokens"]})
        print(f"{i}/{len(questions)} {q['id']}", end="\r")

    with (out_dir / "answers.jsonl").open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    truncated = sum(r["stop_reason"] == "max_tokens" for r in rows)
    record = {"run_id": run_id, "kind": "generation", "config_hash": cfg_hash, "model": llm["model"], "max_tokens": llm["max_tokens"], "prompt": style,
              "subset": args.subset or "all", "limit": args.limit, "seed": args.seed, "questions": len(rows),
              "answerable": sum(r["answerable"] for r in rows), "unanswerable": sum(not r["answerable"] for r in rows),
              "truncated_answers": truncated, "model_calls": calls, "judged": False}
    (out_dir / "record.json").write_text(json.dumps(record, indent=2))
    print(f"\nrun {run_id}: {len(rows)} answers ({record['answerable']} answerable, {record['unanswerable']} unanswerable), "
          f"{calls} model calls, {truncated} hit the output token limit")
    print(f"saved eval/runs/{run_id}/answers.jsonl   (not judged yet: faithfulness is Lesson 4.2)")


if __name__ == "__main__":
    main()
