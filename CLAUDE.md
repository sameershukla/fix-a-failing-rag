# CLAUDE.md

Guidance for Claude when working in this repository.

## What this repo is

The companion repo for the course **Fix a Failing RAG System: from "looks good" to measured, gated, production ready**.

Students start with a deliberately broken RAG system. Each module finds a real failure, measures it, fixes it, and proves the fix with numbers. The course is practical. Concepts are explained clearly and in plain English, then shown in code and real output.

**Running project: the BrightCart Assistant.** A RAG system that BrightCart support and engineering staff use to answer questions about refunds, payments, orders and APIs. Example question: "a high risk refund was not approved within its window. how long is the window and what happens on expiry?"

**The corpus is generated and fictional.** BrightCart is an invented company. Every name, value, email, phone number and secret in the corpus is fake. No downloaded datasets, no scraped docs, no client or employer data, ever (not even anonymized).

## Core principles (never break these)

1. **Every fix is proven by a scorecard delta.** No lesson or code change is complete until the eval shows the before and after numbers.
2. **Compare against the step before.** A lesson's delta is measured against the end state of the previous lesson, not only the frozen baseline. The baseline is shown for reference.
3. **One change per experiment.** If two settings change, the delta cannot be attributed. This includes settings that are easy to miss: output token limit, prompt persona line, judge prompt, index build.
4. **Evals come first.** The harness is built in Module 1. Every later change is judged against it.
5. **Never edit the golden set to make a metric pass.** The golden set changes only when a lesson deliberately adds questions, or when the missing-label check finds another passage that also answers a question. Each change gets its own commit and a note in `eval/golden/CHANGELOG.md`.
6. **Real outputs only.** Every number and output in a lesson comes from a saved run in `lessons/<module>/runs/`. Never invent, round in a way that changes meaning, or retype outputs.
7. **Say plainly what a number can and cannot prove.** If a metric is noisy, a judge is not calibrated, or a sample is small, the lesson says so next to the number.

## The two systems

```
baseline/   the broken system. Frozen. Never edited, never "fixed".
app/        the system students fix, one lesson at a time.
```

- `app/` starts as an exact copy of `baseline/`. Every fix lands in `app/`.
- Each system has its own data and index: `data/baseline/`, `data/app/`. The baseline collection is `baseline`; app collections are `app_<config_hash>`.
- `make eval` refuses to run against a stale index. `make clean-index` clears one system's index.
- Each module has a git tag for its start state (`module-03-start`) and end state (`module-03-end`). The `baseline` tag is the broken system from Module 0.

## Lesson template

Every lesson has an outcome, five content steps, and an exercise, in this order:

0. **Outcome**: one sentence, "After this lesson you can ___." A skill, not a topic.
1. **Symptom**: what the user sees going wrong
2. **Measure**: the metric that captures it, with the current number
3. **Root cause**: why it happens
4. **Fix**: the smallest change that addresses it
5. **Re-measure**: the new number and the delta
6. **Your turn**: an exercise the student does themselves, plus how they check they got it right

Module 0 has nothing to measure or fix yet. Its lessons use Outcome, Symptom, Root cause and Your turn. Every lesson from Module 1 on uses all seven parts.

Lesson files live in `lessons/<module>/<lesson>.md` (for example `lessons/module-03/3.1-chunk-size.md`). One idea per lesson. Real outputs used in a lesson are saved in `lessons/<module>/runs/`.

### How a lesson is made

1. **Run it.** Run the commands and save the real outputs to `lessons/<module>/runs/`.
2. **Write it** in the template, quoting only those saved outputs.
3. **Do the exercise** from a fresh clone. If it cannot be done as written, fix the lesson.
4. **One reader review.** Rewrite wherever the reader got lost.

Write the page first. Videos are recorded later, using the finished page as the script. Never write a lesson ahead of the code it describes.

## Writing style for lesson text

- **Explain the concept and the flow in detail first.** Say what the idea is, why it matters here, and how the pieces connect, step by step. Use simple, plain English and short sentences.
- **Crisp and to the point.** No filler, no hype, no "In this lesson we will…" openers.
- **Code comes below the concept explanation.** First the explanation, then the command, config or code, then the real output.
- **Avoid hyphens in lesson prose** where a plain phrasing works ("structure aware", not "structure-aware").

Rules that apply to every lesson:

1. **Annotate outputs.** Use `←` arrows and inline comments on the lines that matter.
2. **Every fix is shown as a diff** (code or config), followed by the before and after scorecard.
3. **Every table of numbers has a Source line** naming the run ids or the saved file in `runs/`.
4. **State the noise.** Retrieval numbers are the mean of three index builds, with the min to max band. Say what one question is worth (1 / number of questions). A difference inside the band is "no measurable difference".
5. **Use the same names everywhere.** A metric, file or config is named the same way in every lesson.
6. **Use only the student commands** listed under Commands. No `python -m …` in lessons.

### Who writes what

- **Claude drafts the full lesson**: runs the commands, saves outputs to `runs/`, writes the explanation, places the code and real outputs, adds `←` annotations, and checks the draft against this file.
- **The author reviews and edits** every lesson before it is published, and has the final word on wording and on what the course claims.
- Never leave placeholder lines in a lesson. If an output or number is missing, run the command. If it cannot be run, stop and report what is missing instead of writing around it.
- When reviewing a draft, Claude checks: all seven template parts (or the Module 0 subset), the writing style rules, every output traceable to a file in `runs/`, and every number consistent with the lessons before it. It reports problems as a list.

## Course modules and lessons

| # | Module | Adds to the dashboard |
|---|---|---|
| 0 | Meet the broken system | Baseline run |
| 1 | Build the eval harness first | Retrieval scorecard, dashboard v1 |
| 2 | Ingestion failures | Ingestion stats panel |
| 3 | Retrieval failures | Retrieval panel with deltas |
| 4 | Generation failures | Generation panel, calibrated judge |
| 5 | Securing the assistant | Security eval panel |
| 6 | Latency and cost | Cost and latency panel |
| 7 | Eval gating in CI/CD | Gate status, PR comment |
| 8 | Minimal LLMOps and drift | Run comparison, trend view |
| 9 | Capstone: mystery breakage | Full report |

**Module 0: Meet the broken system**
1. Clone, index, ask 10 questions. It looks fine.
2. Five questions an on call engineer would ask, five kinds of failure.
3. Eyeballing is not an eval. Vector search always returns K results, even when nothing is relevant.

**Module 1: Build the eval harness first**
1. Meet the golden set: what is in `golden.yaml` and why
2. Writing a good question: human words, not doc words
3. Evidence is a passage, not a chunk
4. The missing-label trap, and the quick check that avoids it
5. Hit Rate@K
6. Recall@K and Precision@K
7. MRR and nDCG
8. Scorecard to dashboard v1

**Module 2: Ingestion failures**
1. A refund approval function split in half by fixed size chunks: code aware chunking with the Python AST
2. Long policy tables cut mid row: table aware chunking that repeats the header
3. (planned) A policy, its ops handoff note and its archived copy saying the same thing: dedupe or decide which wins
4. (planned) A retired edition competing with the current one: edition metadata
5. Wrap up: Module 2 scorecard, both chunkers together

**Module 3: Retrieval failures**
1. Chunk size and the embedder window: test several sizes, pick with data
2. Picking K: the Recall@K elbow (the method; the final K is picked in 3.8)
3. Exact names missed (`legacy_hourly_velocity`): hybrid search with BM25
4. Look alike functions and near duplicate docs ranked above the answer: reranker
5. Vague questions, and names the user never typed: query rewriting (HyDE)
6. Archived or secondary docs returned for a "what is the rule now" question: metadata filters
7. Swapping the embedding model, decided by evals
8. The final K on the final stack, then the missing-label check

**Module 4: Generation failures**
1. Faithfulness: good retrieval, wrong answer
2. LLM as judge: calibrate it against human labels before trusting its score
3. Lost in the middle
4. Answers nobody can audit: enforce citations and verify them with code
5. Refusal: a minimum relevance score plus a refusal rule
6. A secondary note contradicts the current policy: choose the authoritative source and cite it
7. Answer relevance: correct but useless

**Module 5: Securing the assistant**
1. Prompt injection hidden in a Slack export: filter retrieved text before it reaches the model
2. Fake PII and secrets in support cases and logs: redact them before they reach the answer
3. Restricted documents: access control and a test that proves it
4. Turning attacks into an adversarial eval set

**Module 6: Latency and cost**
1. The latency budget
2. Cost per query, measured
3. Semantic caching, and the eval that proves quality held
4. The quality vs cost trade off table

**Module 7: Eval gating in CI/CD**
1. Thresholds that are not arbitrary
2. Evals on every PR with GitHub Actions
3. Break it on purpose: a bad chunking PR gets blocked
4. Noisy judges: tolerance bands and retries
5. The gate report: PR comment plus dashboard link
6. Smoke evals vs nightly evals

**Module 8: Minimal LLMOps and drift**
1. Config versioning and run ids
2. Tracing you can actually debug
3. Run comparison: proving a fix across configs
4. Drift for real: the v2 policy release is indexed and the old golden set breaks
5. Production traces to new golden cases, checked for missing labels first
6. The same thing with an open source tool

**Module 9: Capstone, mystery breakage**
A new build with three hidden failures. Diagnose with the harness and dashboard, fix, prove, pass the gate, and write a one page incident report per fix.

## The corpus

About 560 generated BrightCart documents plus source code. It is built to be hard in realistic ways: versions that disagree, near duplicates, long tables, look alike code, and noisy team chatter.

```
corpus/
  brightcart/
    v1/                  current policies and docs (primary)
    v2/                  the next policy release; indexed only in Module 8
    archive/2025/        retired editions
    secondary/2026/      ops handoff notes and other non authoritative copies
  structure_sensitive/   docs with long Markdown tables
  code/                  Python, TypeScript and SQL (refunds, payments, api, ...)
  generated/
    level2-noise/        Slack threads, support cases, release notes, draft FAQs
```

If this tree and the repo disagree, the repo wins. Update this file in the same commit.

**Front matter.** Docs carry `status`, `authority`, `version`, `effective_date`, `retired_date`, `canonical_doc_id` and `retrieval_hazard`.

- `status`, `authority`, `effective_date`, `retired_date` and `canonical_doc_id` are real document metadata. Ingestion may use them (Module 2.4, Module 3.6).
- `retrieval_hazard` is an authoring note about what makes the doc hard. It must never reach chunk text, embeddings, BM25, or retrievable metadata. Strip it at normalize. It may be used only in analysis.

**Rules for the corpus**
- `corpus/` is raw input. The pipeline never edits it. Ingestion fixes happen in code.
- Regenerating or changing the corpus is an explicit, versioned author action, never a side effect of another command.
- Never index `corpus/brightcart/v2/` before Module 8.
- All fake data stays obviously fake: emails at `example.com`, phones `555-01xx`, secrets and ids prefixed `FAKE_`.

## Data flow and storage

```
corpus/                                   1. Raw: never modified by the pipeline
   ↓  make normalize
data/<system>/normalized/docs.jsonl       2. Normalized: one doc per line
   ↓  make chunk
data/<system>/chunks/<chunk_config_hash>/ 3. Chunks: one folder per chunking config
   ↓  make index
data/<system>/index/                      4. Index: disposable, rebuilt from chunks
```

- **Normalized** records have a stable `doc_id` derived from the source path, `text` (code and tables kept intact), and `metadata`. Normalization is deterministic.
- **Chunks** have `chunk_id`, `doc_id`, `start_char`, `end_char`, `text`, and inherited metadata. Several chunking configs live side by side; never overwrite one with another.
- **Token counts** for chunk sizes use the embedder's own tokenizer. Chunks longer than the embedder window are allowed, but the lesson must say how much text is truncated for embedding.
- `data/` is gitignored and always rebuildable.

## The golden set

Retrieval metrics come from relevance labels: for each question, which passages are correct evidence. The golden set creates those labels.

```
corpus  →  eval/golden/golden.yaml (written by hand)  →  make eval  →  scorecard
```

- 360 questions: 314 answerable and 46 unanswerable. Each item has `id`, `question`, `evidence` (empty for unanswerable), `answerable`, `tags` (slice, module) and an optional `note`.
- Slices include table, code, exact name, authority conflict, multi evidence, long form, messy input, everyday policy, format aware, human source and terse query.
- Named subsets list ids only and live in `eval/golden/subsets/` (for example `gen50.yaml`, `gen100.yaml`). The questions and evidence stay in `golden.yaml`.
- When a lesson uses a subset or an earlier, smaller version of the set, it says which one and how many questions.

### Writing a good question

Write the question the way an on call engineer would type it, **before** opening the document that answers it. Vague, abbreviated, missing context is fine. Copying the doc's wording is not: it makes retrieval look better than it is.

```yaml
- id: q224
  question: "high risk refund approval not decided in time. how long is the window and what happens on expiry"
  evidence:
    - doc_id: <doc_id of the BrightCart code file>
      text: "<exact evidence passage>"
  answerable: true
  tags: [code, module-02]
```

**Evidence references documents, never chunks.** Each item is a `doc_id` plus the evidence text (or a `start_char`/`end_char` span). Keep it to the 1 to 3 sentences that actually answer; for a table, the answering row. The overlap rule that decides whether a retrieved chunk counts as relevant lives in `eval/metrics/relevance.py` and is the same for every run.

### The missing-label check

The same answer often lives in several places. If only one is listed, a retriever that returns another correct passage is scored as wrong.

1. Search the corpus for the answer's key terms (`grep -ri`) and run `make retrieve` with K = 20.
2. Read anything that looks like it answers the question.
3. Add every passage that does to `evidence`, and log it in `CHANGELOG.md` as a `missing-label:` entry.

For unanswerable questions, the same check confirms nothing in the corpus answers them. Repeat the check when new content is indexed (Module 8) or when a lesson shows a "wrong" retrieval that was actually right.

## Eval harness

**Retrieval:** `make eval` writes a run record to `eval/runs/<run_id>/` with run id, git commit, config hash, Hit Rate@K, Recall@K, Precision@K, MRR, nDCG, per slice results and per question results.

**Generation:** `make eval-gen` retrieves, answers, judges, and records retrieval recall, faithfulness (mean and strict), unsupported claims per answer, output tokens, and per question results.

### Measurement rules

- **Noise.** Report retrieval numbers as the mean of three index builds with the min to max band. Name individual questions that improved or got worse.
- **Paired comparisons.** Generation deltas are paired per question, with a bootstrap 95% interval and counts of better, worse and same.
- **Precision with one evidence item.** When every question has one evidence item, Precision@K equals Recall@K divided by K, and Hit Rate equals Recall. Say so instead of treating them as separate findings.
- **Edge cases, one rule everywhere.** An answer with no claims and a judge reply that cannot be parsed are both left out of faithfulness averages and counted separately. Report refusals and answer coverage next to faithfulness, so a prompt cannot score well by saying less.
- **Truncation.** Report how many answers hit the output token limit. A run where answers were cut off cannot be compared with one where they were not.
- **Cache keys.** Every setting that can change a model output (model, prompts, max tokens, temperature) is part of the cache key.
- **Tuning on the test set.** A setting picked on the same questions it is scored on (for example a fusion weight) is reported as an upper bound until checked on held out questions.

### LLM judges

- The faithfulness judge sees only the retrieved chunks and the answer. It checks support, not authority: a claim stated in a chunk is supported even if the chunk is a secondary or archived source. Authority is handled by retrieval and by Lesson 4.6.
- A true statement that the context does not cover something is faithful.
- Strip citation markers from an answer before judging it.
- **A judge is not trusted until it is calibrated** against human labels in `eval/judges/calibration/labels.yaml`:
  - Labels are written by a person. `labeled_by` always records who wrote each label. A model may draft labels only if the draft is marked as a draft and reviewed blind by a person before it counts.
  - Two splits: tune (read disagreements, change the judge prompt) and test (score once, after the judge is frozen).
  - Each split needs at least 15 human unfaithful labels before recall and kappa are reported as results.
  - Pass rule: kappa ≥ 0.60 and unfaithful recall ≥ 0.80 on the test split. Report agreement and precision too, with the class counts.
- Until a judge is calibrated, every lesson that uses it marks its scores as not calibrated, next to the numbers.

## Dashboard

A static HTML report generated from a run record. No server, no vendor. It must answer "why did the gate fail?" within 30 seconds.

Sections, in order:
1. Gate status: each metric vs threshold vs baseline
2. Retrieval panel with deltas
3. Generation panel with deltas
4. Cost and latency panel
5. **Failing questions table**: question, expected evidence, retrieved chunks, judge reason
6. Trend across recent runs

## CI/CD gate

- Thresholds live in `ci/thresholds.yaml`, each with a one line reason.
- The gate compares against the last passing run, not only fixed thresholds.
- Judge based metrics use tolerance bands.
- A short summary is posted as a PR comment with a link to the full dashboard.

## Minimal LLMOps

- Every behavior setting (prompts, chunking, embedding model, K, reranker, judge prompt, model, max tokens) lives in `config/` and contributes to the config hash. Experiment configs live in `config/experiments/`.
- Every request can be traced: query, retrieved chunks, prompt, answer, tokens, latency.
- Bad production traces can be promoted into golden set cases through a reviewed step.

## Commands

Student commands (the only ones used in lessons):

```
make setup                                   # install dependencies
make ingest SYSTEM=app CONFIG=...            # normalize + chunk + index
make clean-index SYSTEM=...                  # clear one system's index
make ask SYSTEM=... Q="..."                  # ask one question
make retrieve SYSTEM=... Q="..." K=20        # show retrieved chunks
make eval SYSTEM=... [CONFIG=...] [BASE=<run_id>] [KS=...]
make eval-gen SYSTEM=app CONFIG=... [SUBSET=...] [LIMIT=...]
make compare RUN_A=... RUN_B=...
make judge-sample RUNS="..." SPLIT=tune|test N=... SEED=...
make judge-sheet
make judge-calibrate SPLIT=tune|test
make dashboard RUN=...
make eval-smoke                              # fast subset for PRs
make test                                    # unit tests
```

If a lesson needs a step that has no make target, add a thin make target for it first, and tell the author.

## Working rules for Claude

- Before changing ingestion, retrieval or generation code, run the eval and record the run id. After the change, run it again and report the delta. If a metric drops, say so plainly.
- Keep changes small and tied to one lesson.
- Never edit anything under `baseline/`.
- Never commit anything under `data/`. Change the code or config that generates it instead.
- Never write golden set evidence as chunk ids.
- Never add a question to the golden set without running the missing-label check on it.
- Never write a calibration label as human unless a person wrote or reviewed it.
- Do not add dependencies without noting why in the PR description.
- Do not commit real secrets. Fake secrets in the corpus are prefixed `FAKE_`.
- Keep the system runnable on a laptop: indexing the full corpus should take minutes, not hours.
- When writing lesson text, follow the lesson template and writing style above.

## Open decisions

- Whether Modules 2 and 3 are re-scored on the full 360 question golden set, or Module 1 explains when the set grows from 80.
- Lessons 2.3 and 2.4: write duplicate and staleness questions first, then build the fixes.
- Module 5: confirm the corpus has the injected Slack export, fake PII and secrets, and restricted documents.
- Module 4: human review of the draft calibration labels.
- Course platform and delivery format.
