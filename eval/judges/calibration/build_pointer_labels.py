"""Builds labels_pointer.yaml: 14 DRAFT items about "where to look" pointers, for testing judge prompt v2 (Lesson 4.4).

Written by Claude. NOT human labels (labeled_by: claude-draft). They can test whether a prompt change behaves as the stated rule says; they cannot calibrate a judge.
The rule these labels follow:
  - A generic suggestion to consult another source ("check the policy", "ask the owning team") is NOT a claim about the corpus.
  - A pointer that names a specific document, page or team, or says something is found there, IS a claim and needs support in the chunks.
Questions were chosen so none appears in labels.yaml. Answers come from the 2000 token plain runs.
"""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
RUNS = {"S": ("gen-20261011-024453-33b32a", "claude-sonnet-5-5"), "H": ("gen-20261011-025155-63651e", "claude-haiku-5-5")}


def row(k, qid):
    for line in (ROOT / "eval/runs" / RUNS[k][0] / "answers.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        if r["id"] == qid:
            return r


# (run, qid, verdict, origin, reason, optional seeded edit (old, new))
ITEMS = [
    ("S", "q085", "faithful", "natural", "Generic pointer to documentation. Parameter names are offered as examples of what such docs might list. The rate limits quoted are in the chunks.", None),
    ("S", "q119", "faithful", "natural", "Generic pointer to eligibility rules or the policy owner. The exclusions quoted (oversize, hazmat) are in the chunks.", None),
    ("S", "q300", "faithful", "natural", "Generic pointer to consumer law guidance. The EU 2026.3 edition facts and the 14 day fallback are in the chunks.", None),
    ("S", "q215", "faithful", "natural", "Generic pointer to the returns operations team. The quote about a dated seasonal notice and the 30 and 14 day defaults are in the chunks.", None),
    ("H", "q061", "faithful", "natural", "Generic pointer to the team that owns fulfillment policy. The cancellation, address and backorder facts are in the chunks.", None),
    ("H", "q221", "faithful", "natural", "'gift cards remain valid' and 'promotional credits can have separate expiration rules' are in the chunks. The pointer is generic.", None),
    ("H", "q223", "faithful", "natural", "Generic pointer to the security or platform team and the processor docs. Tokenized references and processor handling are in the chunks.", None),
    ("H", "q304", "faithful", "natural", "Generic pointer to the process or the verification team. The exemption facts are in the chunks.", None),
    ("S", "q189", "faithful", "natural", "Names the Loyalty Points Conversion Matrix and the BrightPoints Loyalty Program Handbook. Both are in the chunks, and the chunks call the matrix the primary source.", None),
    ("S", "q208", "faithful", "natural", "Names B2B Subscriptions as an example owner. That team appears in the chunks as an owner. The rest is a generic pointer.", None),
    ("H", "q184", "unfaithful", "natural", "Says the current returns policy is available in 'the help center'. 'help center' does not appear in the chunks.", None),
    ("H", "q189", "unfaithful", "natural", "Says the relevant policy or registry is one that Loyalty Operations maintains. The chunks name Loyalty Operations as an owner of a redemption row and separately say thresholds live in a policy or registry. They do not link the two.", None),
    ("S", "q353", "unfaithful", "seeded_edit", "The generic pointer was replaced with a named internal page that 'lists Apple Pay and Google Pay as supported'. Neither the page nor the claim is in the chunks.",
     ("To get a definite answer, check the current checkout payment options or ask the payments team.",
      "To get a definite answer, see the Payments Integration Guide on the internal wiki, which lists Apple Pay and Google Pay as supported.")),
    ("H", "q222", "unfaithful", "seeded_edit", "The generic pointer was replaced with a named handbook and section. 'Account Security Handbook' is not in the chunks.",
     ("Check the current password policy document for the exact length requirement.",
      "The exact length requirement is in section 4 of the Account Security Handbook.")),
]

out = []
for n, (k, qid, verdict, origin, reason, edit) in enumerate(ITEMS, 1):
    r = row(k, qid)
    answer = r["answer"]
    extra = {}
    if edit:
        assert edit[0] in answer, qid
        answer = answer.replace(*edit)
        extra = {"original_text": edit[0], "edited_text": edit[1]}
    out.append({"id": f"P{n:02d}", "question_id": qid, "question": r["question"], "split": "pointer", "origin": origin, "answer_model": RUNS[k][1], "answer_run": RUNS[k][0],
                "chunk_ids": [c["chunk_id"] for c in r["chunks"]], "answer": answer.strip(), "verdict": verdict, "reason": reason, **extra,
                "labeled_by": "claude-draft", "status": "draft", "human_reviewed_by": None})
header = """# DRAFT pointer labels (Lesson 4.4). Written by Claude. NOT human labels: labeled_by is claude-draft on every item.
# Purpose: check that judge prompt v2 follows the pointer rule below. They cannot calibrate a judge.
# Rule: a generic suggestion to consult another source is not a claim. A pointer that names a specific document, page or team, or says something is found there, is a claim and needs support in the chunks.
# These questions do not appear in labels.yaml. A person should relabel them blind before any result from them is quoted as more than a rule check.
"""
(ROOT / "eval/judges/calibration/labels_pointer.yaml").write_text(header + yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=130), encoding="utf-8")
print(len(out), "items", sum(i["verdict"] == "unfaithful" for i in out), "unfaithful")
