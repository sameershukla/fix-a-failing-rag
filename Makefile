# Fix a Failing RAG System: Makefile
# Recipe lines must start with a TAB, not spaces.

VENV := .venv
# Which system package ingest, ask and retrieve use: baseline (frozen) or app (working copy).
SYSTEM ?= baseline
PY   := $(VENV)/bin/python
# Optional: run SYSTEM=app with another config file instead of app/config.yaml (baseline is frozen and ignores it).
#   make ingest SYSTEM=app CONFIG=config/experiments/m3-fixed_256.yaml   |   make eval SYSTEM=app CONFIG=config/experiments/m3-fixed_256.yaml
ifdef CONFIG
export RAG_CONFIG := $(CONFIG)
endif


.PHONY: golden-check show-chunk setup generate-corpus generate-corpus-dry hello normalize chunk index ingest ask retrieve eval eval-gen judge-sample judge-sheet judge-calibrate dashboard compare test

# Create a local virtual environment and install the generator's dependencies.
$(PY):
	python3 -m venv $(VENV)
	$(PY) -m pip install --quiet --upgrade pip
	$(PY) -m pip install --quiet -r requirements.txt

setup: $(PY)

# AUTHOR ONLY. Generate new docs listed in authoring/generator/plan.yaml (needs ANTHROPIC_API_KEY).
generate-corpus: $(PY)
	$(PY) authoring/generator/generate.py

# Print the prompts without calling the API. Free, and a good first check.
generate-corpus-dry: $(PY)
	$(PY) authoring/generator/generate.py --dry-run

hello:
	@echo "make works"

# ---- Baseline RAG system (see baseline/README.md) ----

# corpus/ -> data/$(SYSTEM)/normalized/docs.jsonl
normalize: $(PY)
	$(PY) -m $(SYSTEM).ingest.normalize

# normalized docs -> data/$(SYSTEM)/chunks/<chunk_config_hash>/
chunk: $(PY)
	$(PY) -m $(SYSTEM).ingest.chunk

# chunks -> data/$(SYSTEM)/index/ (Chroma)
index: $(PY)
	$(PY) -m $(SYSTEM).ingest.index

# normalize + chunk + index
ingest: normalize chunk index

# Ask one question. Needs ANTHROPIC_API_KEY.  Usage: make ask Q="why did the agent skip approval?"
ask: $(PY)
	@test -n "$(Q)" || (echo 'Usage: make ask Q="your question"'; exit 1)
	$(PY) -m $(SYSTEM).generation.answer "$(Q)"

# Show only what retrieval returns for one question: score, chunk id, and where the chunk ends.
#   make retrieve Q="..."   |   make retrieve Q="..." K=20   (K = how many chunks to show)
retrieve: $(PY)
	@test -n "$(Q)" || (echo 'Usage: make retrieve Q="your question"'; exit 1)
	$(PY) -m $(SYSTEM).retrieval.search "$(Q)" $(if $(K),--k $(K))

# Show where one chunk ends and the next begins.  Usage: make show-chunk DOC=book/v1/Ch02 N=0
show-chunk: $(PY)
	@test -n "$(DOC)" -a -n "$(N)" || (echo 'Usage: make show-chunk DOC=book/v1/Ch02 N=0'; exit 1)
	@SYSTEM=$(SYSTEM) $(PY) lessons/module-00/runs/0.1/show_chunks.py $(DOC) $(N)

# Check eval/golden/golden.yaml: ids, counts, and that every evidence passage appears word for word in its document.
#   make golden-check   |   make golden-check SYSTEM=app   |   make golden-check GOLDEN=<another golden file>
golden-check: $(PY)
	$(PY) eval/golden/validate.py --system $(SYSTEM) $(if $(GOLDEN),--golden $(GOLDEN))

# ---- Eval harness ----

# Score a system on the golden questions in eval/golden/golden.yaml and write eval/runs/<run id>/.
#   make eval LABEL="what changed"  (a note saved in the run record)   |   make eval BUILDS=10  (more index builds, for a wider noise band; the default is 3)
#   make eval   |   make eval SYSTEM=app   |   make eval SYSTEM=app KS=2,7,15,20,30  (more cut offs, for the K curve)   |   make eval SYSTEM=app BASE=<older run id>  (adds deltas to the dashboard)
# Retrieval metrics only for now. No API key needed, no cost. Also builds the dashboard.
eval: $(PY)
	$(PY) -m eval.run --system $(SYSTEM) $(if $(KS),--ks $(KS)) $(if $(BUILDS),--builds $(BUILDS)) $(if $(LABEL),--label "$(LABEL)") $(if $(GOLDEN),--golden $(GOLDEN)) $(if $(RESCORE),--rescore $(RESCORE)) $(if $(COVER),--min-cover $(COVER)) $(if $(NOREBUILD),--no-rebuild)
	$(PY) -m dashboard.build $(if $(BASE),--baseline $(BASE))

# Score the ANSWERS: faithfulness of each answer to the chunks it was given (Module 4). Needs ANTHROPIC_API_KEY and costs model calls.
#   make eval-gen SYSTEM=app CONFIG=config/experiments/g-plain.yaml   |   add LIMIT=20 to try 20 questions first   |   SUBSET=gen50 for the 50 question set in eval/golden/subsets/   |   NOCACHE=1 to ignore the call cache
# Compare two of these runs with make compare, the same as for retrieval runs.
eval-gen: $(PY)
	$(PY) -m eval.generate --system $(SYSTEM) $(if $(SUBSET),--subset $(SUBSET)) $(if $(LIMIT),--limit $(LIMIT)) $(if $(NOCACHE),--no-cache)

# Lesson 4.2: calibrate the judge against human labels. One file, eval/judges/calibration/labels.yaml; each item is split=tune or split=test.
#   make judge-sample RUNS="<run id> <run id>" SPLIT=test N=30 SEED=1   draws 30 more answers (stratified, repeatable, never a question already labeled) and adds them (free)
#   make judge-sheet                                                    writes eval/judges/calibration/sheet.md with the items still to label; type the verdicts there
#   make judge-calibrate SPLIT=tune                                     runs the judge on that split: agreement, kappa, precision, recall (needs ANTHROPIC_API_KEY)
# A judge is calibrated only when the TEST split passes. Score test once the prompt is final.
judge-sample: $(PY)
	@test -n "$(RUNS)" -a -n "$(SPLIT)" || (echo 'Usage: make judge-sample RUNS="<run id> <run id>" SPLIT=tune|test [N=30] [SEED=0]'; exit 1)
	$(PY) -m eval.judges.calibrate sample $(RUNS) --split $(SPLIT) $(if $(N),--n $(N)) $(if $(SEED),--seed $(SEED))

judge-sheet: $(PY)
	$(PY) -m eval.judges.calibrate sheet

judge-calibrate: $(PY)
	$(PY) -m eval.judges.calibrate score $(if $(SPLIT),--split $(SPLIT))

# Unit tests. No API key, no index needed.
test: $(PY)
	$(PY) -m unittest discover -s tests -v

# Rebuild the static HTML report from a saved run. Default is the latest run.
#   make dashboard   |   make dashboard RUN=<run id>   |   make dashboard RUN=<new> BASE=<older>
dashboard: $(PY)
	$(PY) -m dashboard.build $(if $(RUN),--run $(RUN)) $(if $(BASE),--baseline $(BASE))

# Two runs side by side: metric deltas, then which questions got better or worse. A is before, B is after.
#   make compare RUN_A=<run id> RUN_B=<run id>
compare: $(PY)
	@test -n "$(RUN_A)" -a -n "$(RUN_B)" || (echo 'Usage: make compare RUN_A=<run id> RUN_B=<run id>'; exit 1)
	$(PY) -m eval.compare $(RUN_A) $(RUN_B)
