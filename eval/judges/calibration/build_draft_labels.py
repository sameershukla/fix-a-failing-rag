"""Builds labels.yaml (DRAFT) from saved generation runs.

Every verdict here was written by Claude while reading the answer next to its retrieved chunks. None of it is human.
labeled_by says so on every item, and status stays "draft" until a person has relabeled the items blind and the two sets
of verdicts have been compared (CLAUDE.md: a model may draft labels only if marked as a draft and reviewed blind by a person).

Two origins:
  natural      an answer a model really wrote for the question, read and judged as it is.
  seeded_edit  a natural answer that was judged faithful, with exactly one claim changed. The error is known by construction,
               so the verdict does not depend on anyone's judgment. These exist only because natural unfaithful answers are rare.
Run once: python eval/judges/calibration/build_draft_labels.py
"""

import json
import random
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
RUNS = {"A": "gen-20261011-010241-2ab232",    # claude-sonnet-5-5, sample seed 1
        "B": "gen-20261011-010839-eb1c14",    # claude-haiku-5-5, same 60 questions
        "C": "gen-20261011-011240-eb1c14"}    # claude-haiku-5-5, sample seed 2
MODEL = {"A": "claude-sonnet-5-5", "B": "claude-haiku-5-5", "C": "claude-haiku-5-5"}


def load(run):
    return {r["id"]: r for r in map(json.loads, (ROOT / "eval/runs" / run / "answers.jsonl").open(encoding="utf-8"))}


ANS = {k: load(v) for k, v in RUNS.items()}

# (run, question id, split, reason)
FAITHFUL = [
    ("A", "q013", "tune", "Zero charge and MANUAL_HAZMAT_REVIEW are in the code. The $18 hazmat ground row and the docstring quote are in the matrix and code chunks."),
    ("A", "q112", "tune", "Day 30 rule, next renewal credit, annual to monthly row, 48 hour accidental renewal rule and enterprise order form row are all in chunks. '42 days' is arithmetic on six weeks."),
    ("A", "q137", "tune", "Login disabled 04:11, revocation 04:19, 04:11:08Z timeout and the 5 and 15 minute SLAs are all in the chunks. '8 minutes' is arithmetic."),
    ("A", "q091", "tune", "A refusal. Both quoted facts (24 hours, 48 hours, 15 minutes) are in the chunks. Naming CSV, JSON or ZIP is only a list of formats that are NOT mentioned."),
    ("A", "q171", "tune", "Hard case. 10 percent for 60 days, Tuesday, 20 percent for 90 days and the 12 percent electronics commission are in chunks. 'Weekly' is read from a Tuesday payout day. The suggested deck wording is a rewrite, not a new fact."),
    ("C", "q103", "tune", "Thresholds 30 and 60, return values 0, 1 and 2 and the test name are in the code chunks. 35 percent is above 30 and below 60."),
    ("C", "q279", "tune", "A refusal. DFW-RET-1, PHX-RET-2 and the 85 percent overflow are in the us_central chunk. Nothing is claimed about us_east."),
    ("C", "q065", "tune", "12 months of account inactivity, not 12 months after each purchase, is stated. Tier thresholds over a rolling 12 months are in the CSV chunk."),
    ("C", "q023", "tune", "standard_support_limit_usd 250 and supervisor_limit_usd 1000 are in the config chunk. 'Above 250 needs a supervisor' is the plain reading of those limits."),
    ("A", "q114", "test", "$25 for zone 5 to 8 over 48 inches, $45 Alaska, the hazmat zero charge, and the rural and signature rows are all in chunks. The answer says the context does not define is_oversized in the matrix and relies on the 48 inch row."),
    ("A", "q254", "test", "Proportional split, same day gift card refund, 'card portions follow normal card posting times' and the $100 order example are in the chunk. 25 and 25 follow from 50 and 50."),
    ("A", "q192", "test", "Hard case. A refusal that lists real ENTER-xxx rules from the chunks. SAML, OIDC and SCIM appear only in an offer to help if the user shares more, not as a claim about BrightCart."),
    ("A", "q130", "test", "The ATP formula, the Failure recovery heading, the stale context sentence and the BACKORDER_REVIEW code are all in chunks."),
    ("B", "q182", "test", "Hard case. 24 hours a day SEV 1 cover, 8 to 8 weekday support hours and the SEV 1 definition are in chunks. '7 days a week' and 'Sunday 3 AM is covered' follow from 24 hours a day."),
    ("C", "q008", "test", "job_schedule '0 3 * * *' is in the config chunk. The answer says the time zone is not specified, which is true."),
    ("C", "q044", "test", "A refusal. 'SMS availability depends on supported phone regions' and 'authenticator app or SMS' are in the chunk."),
    ("C", "q358", "test", "The Alaska over 50 lb $45 row and is_oversized (longer than 48 or heavier than 50) are in the chunks."),
    ("C", "q170", "test", "Divide by 30, rounded price difference times days remaining, are in the docstring and code chunks. The $10 example is arithmetic on that formula."),
]

NATURAL_UNFAITHFUL = [
    ("B", "q297", "tune",
     ["Tell the customer not to use or charge it, keep it away from heat and flammable materials, and not to repair or open it",
      "If there is smoke, fire or heat, contact emergency services first"],
     "The chunks say only: escalate leaking batteries immediately, quarantine, no restock, BATTERY_SWELL with 3 photos. The customer safety advice is not in them."),
    ("B", "q226", "tune",
     ["The URL can be found in the Production Incident Command Handbook (reason code RELIA-155)"],
     "The chunks contain RELIA-155 only as a reason code at the end of a generic sentence. Nothing says the status page URL is in any handbook."),
    ("B", "q168", "test",
     ["A payout request shortly after a password change can be a warning sign of account takeover"],
     "The answer correctly says the payout policy is not in the context, then states this warning sign as a fact. The only matching rule (reset then payout is high risk) was not retrieved for this question."),
]

# (run, question id, split, old text, new text, what was changed)
SEEDED = [
    ("A", "q058", "tune", "**Required action:** Pause gift-card issuance and review the funding source.",
     "**Required action:** Permanently close the account and refund all 12 gift card orders.", "required action changed to an action the matrix does not give"),
    ("A", "q128", "tune", "**$39 per month**", "**$49 per month**", "fee changed from $39 to $49"),
    ("A", "q196", "tune", "valid for **30 minutes**", "valid for **60 minutes**", "link lifetime changed from 30 to 60 minutes"),
    ("A", "q016", "tune",
     "It's tracked **per account**, not per device. So failed attempts from a phone, a laptop, or any other device all count toward the same counter.",
     "It's tracked **per device**, not per account. So each phone or laptop has its own counter.", "scope reversed: per account became per device"),
    ("A", "q328", "test", "- **Idle timeout:** 15 minutes", "- **Idle timeout:** 30 minutes", "enterprise idle timeout changed to the consumer value"),
    ("A", "q203", "test", "It returns `MANUAL_REVIEW` so Risk can inspect the pattern.",
     "It returns `MANUAL_REVIEW` so Risk can inspect the pattern, and the customer's card is also blocked for 24 hours.", "invented consequence added"),
    ("A", "q164", "test", "so the order is processed the next business day.", "so the order still ships the same day for a $15 rush fee.", "after cutoff rule contradicted and a fee invented"),
    ("A", "q074", "test", "normally take **2 to 3 business days** to clear.", "normally clear **the same day** for orders under $5,000.", "clearing time replaced with an invented rule"),
    ("A", "q175", "test", "No. BrightCart systems must not store card CVV values after authorization, and the policy allows no support exception for CVV storage.",
     "Yes, but only for 30 days. BrightCart systems may keep card CVV values for 30 days after authorization to handle chargeback disputes.", "policy reversed"),
]


def item(run, qid, split, verdict, origin, answer, **extra):
    row = ANS[run][qid]
    base = {"question_id": qid, "question": row["question"], "split": split, "origin": origin,
            "answer_model": MODEL[run], "answer_run": RUNS[run], "chunk_ids": [c["chunk_id"] for c in row["chunks"]],
            "answer": answer.strip(), "verdict": verdict}
    base.update(extra)
    return base


items = []
for run, qid, split, reason in FAITHFUL:
    items.append(item(run, qid, split, "faithful", "natural", ANS[run][qid]["answer"], reason=reason))
for run, qid, split, claims, reason in NATURAL_UNFAITHFUL:
    items.append(item(run, qid, split, "unfaithful", "natural", ANS[run][qid]["answer"], unsupported_claims=claims, reason=reason))
for run, qid, split, old, new, what in SEEDED:
    text = ANS[run][qid]["answer"]
    assert old in text, (qid, old)
    items.append(item(run, qid, split, "unfaithful", "seeded_edit", text.replace(old, new), edit=what, original_text=old, edited_text=new,
                      reason=f"The original answer was faithful. One claim was changed: {what}."))

rng = random.Random(7)
out = []
for split in ("tune", "test"):
    part = [i for i in items if i["split"] == split]
    rng.shuffle(part)
    out += part
for n, it in enumerate(out, 1):
    it["id"] = f"L{n:02d}"
    it["labeled_by"] = "claude-draft"
    it["status"] = "draft"
    it["human_reviewed_by"] = None
    out[n - 1] = {"id": it.pop("id"), **it}

header = """# DRAFT calibration labels for the faithfulness judge (Lesson 4.2).
# Written by Claude, not by a person. labeled_by is claude-draft and status is draft on every item.
# These do NOT count as human labels (CLAUDE.md). They count only after a person labels the same items blind
# (without seeing verdict or reason) and the two sets are compared.
# origin: natural      = an answer a model really wrote, judged as it is.
# origin: seeded_edit  = a faithful natural answer with exactly one claim changed (see edit). Known unfaithful by construction.
# Context for an item = the chunks listed in chunk_ids, from the saved run in answer_run (eval/runs/<answer_run>/answers.jsonl).
# Rule used: a claim is faithful if the chunks state it or it follows directly from them (arithmetic, a plain reading).
# Authority is not judged here: a claim stated in a chunk is supported even if the chunk is a secondary source.
# A true statement that the context does not cover something is faithful.
"""
path = ROOT / "eval/judges/calibration/labels.yaml"
if path.exists() and "human_labeled" in path.read_text(encoding="utf-8"):
    raise SystemExit("labels.yaml already holds the author's labels. Refusing to overwrite them with the draft.")
path.write_text(header + yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=130), encoding="utf-8")
from collections import Counter
print(path.relative_to(ROOT), len(out), "items")
print(Counter((i["split"], i["verdict"], i["origin"]) for i in out))
