# Golden set changelog

Every change to `golden.yaml` gets an entry here and its own commit. The set changes only when a lesson deliberately adds questions, or when the missing label check finds another passage that also answers a question. It never changes to make a metric pass.

## 2026-10-10: first version, 360 questions

**What was added.** 360 questions: 314 answerable and 46 unanswerable. Ids `q001` to `q009` are the nine questions written for Module 0 (unchanged wording). The other ids follow a fixed shuffle (seed 360), so slices are mixed through the file.

**How it was made.** A model drafted every question and every evidence label. It read the passage first, then wrote the question in the loose words an on call engineer would type, and then reworded the 18 questions that sounded most like their evidence. This is less blind than the rule in CLAUDE.md ("write the question before opening the document"), so treat the wording as a draft. **No person has reviewed this set yet.** The author must review it, and the set should not be used for a published number until that is done.

**Evidence rule.** Evidence is a passage that states the correct current answer in an authoritative document (status `active`, authority `primary` or `implementation`). It is copied word for word from the normalized document. `validate.py` re-checks that every passage is found in its document.

These are not evidence, even when they repeat the right sentence:
- archived and retired copies, unless the question asks about a past period (5 questions do; 14 questions carry the `edition` tag in all)
- the 350 generated noise documents (release notes, incidents, draft FAQs, support cases, wiki copies, regional notes, Slack threads)
- secondary notes
- the human email, Slack, ticket and call copies

If these counted, the Module 0 failure (noise copies outranking the policy page) would show as a hit and disappear from the scorecard. **This is a judgement about what the course claims. The author should confirm it.** Flipping it later means relabelling, not rewriting questions.

**Not in the set.** The restricted documents, the fake PII and secret samples, and the prompt injection capture. Their answers are exactly what Module 5 must keep from being retrieved. Module 5 builds its own adversarial set (lesson 5.4).

**Missing label check, as done.**
1. For every answerable question, the answer's key phrase was searched in all 689 normalized documents. Any other authoritative document with the phrase was read and, where it answered, added as evidence. This is why 72 questions have two or more passages.
2. Every answerable question was run through the baseline index at K = 20. Authoritative documents that were not evidence but had a line close to the evidence were read and added or rejected.
3. For each unanswerable question, the key terms were searched in all 689 documents. Hits were read. Eight candidates were dropped because the corpus partly answers them.

Limits: the second step uses the baseline retriever, so an answer that the baseline cannot find and that uses different words from the evidence could still be missing. Repeat the check after each retrieval change (Module 3) and when new content is indexed.

**Questions whose first label was wrong.** Three Module 0 questions were first written as unanswerable:
- `q006` (API throttling limit) is answerable: 600 requests per minute per client, Retry After 20 (`brightcart/v1/api/rate-limits`).
- `q007` (ACH fallback idempotency key) is answerable: `return_record.refund_id` (`brightcart/v3/code/refunds/service.py`).
- `q008` (retention deletion cron) is answerable: `job_schedule: "0 3 * * *"` in `brightcart/v2/structured/privacy/retention-job-config`. The first check searched for the word "cron" and missed this.

`q009` ("Where I can find DE details") is the only Module 0 question that is truly unanswerable.

**Unanswerable set (46).** `q009` plus 45 more. 19 are about topics the corpus never mentions (`absent-topic`, for example Apple Pay, bitcoin, an uptime percentage). 26 are `near-miss`: the corpus covers the area but not the asked detail (for example the same day metro fee exists but its cutoff time does not). Each near miss has a `note` naming the closest document.

**Conflicts found between authoritative documents.** The corpus disagrees with itself in these places. Where the later effective date settles it, the later edition is the evidence and the question is tagged `authority-conflict`. Where it does not, the question avoids the disputed number.

| # | Topic | Documents and values | How handled |
|---|---|---|---|
| 1 | Account lockout | v1 article: 5 failures, 15 minute lock (effective 2026-09-01). v2 table and config: 6 failures in 15 minutes, 30 minute lock (effective 2026-10-01) | later edition wins (v2) |
| 2 | SEV 1 acknowledgement | v1 incident article: 15 minutes. v2 escalation table and incident config: 10 minutes. v2 escalation code and v1: 15. Production incident handbook: 5 minutes for the incident commander | no question asks the number |
| 3 | `POST /v1/admin/credits` limit | v2 table: 20 per minute. v2 rate limiter code: 5 | question asks about the key type only |
| 4 | `POST /v1/payments` limit | v2 table: 100 per minute. v2 rate limiter code: 90 | not asked |
| 5 | Order cancellation states | v1: received, picking, packed. v2 code: CREATED, PAID, ALLOCATED, PICKED | v1 question uses v1 words; code question uses code words |
| 6 | Limited edition SKU bulk cap | v2 table: 5 units. v2 code: review above 2 units | question asks only which team approves |
| 7 | Lost package clock | v1: 5 days (domestic) or 10 days (international) with no scan. v2: seven days no movement after the expected delivery date | question uses the v2 wording |
| 8 | Electronics return window (US) | v1 article: 14 days. v3 edition 2026.3 and the Spanish note: 30 days. Both effective 2026-09-01 | **unresolved**: the question follows v3, flagged for the author |
| 9 | Support transcript retention (non EU) | 730 days (v2 config), 24 months (v2 table), 365 days (v3 yaml). v3 editions: 730 retired, 365 retired, 180 EU only active | only the EU edition is asked as a number |
| 10 | Agent trace retention | v2 table: 90 days. v2 code and v3 yaml: 30 days | question asks the batch size only |
| 11 | API client retry base delay | v2 config: 500 ms. v3 yaml: 250 ms | question avoids the delay |
| 12 | Annual plan pause | v1: annual plans cannot be paused. v2 table: annual premium plan, 90 days maximum | question asks the premium plan row; note added |

Items 8 and 9 need the author's decision. The corpus does not say which document wins.

**Corpus findings that affect the course** (not changed here; the corpus is raw input):
- `corpus/failures/manifest.yaml` is indexed by the baseline. It is an authoring file, and its `expected_change` lines read like answers. It should be excluded from `corpus.include`, or CLAUDE.md should say it is deliberate.
- CLAUDE.md describes `corpus/brightcart/v1`, `v2`, `v3`, `archive`, `secondary` as the next release layout, with v2 held back until Module 8. The repo has these ids, but v2 and v3 documents are already `active` with effective dates before today, and the baseline indexes them. Several v1 facts are superseded by v2.
- 32 of the 50 v1 policies have an archived 2025 copy whose rule numbers differ from the current page (checked by comparing the numbers in the standard rule paragraph). Questions whose evidence line is missing from that copy are tagged `authority-conflict`.

**Counts.** 360 questions. Evidence passages per answerable question: 1 passage for 242, 2 for 61, 3 for 9, 4 for 1, 5 for 1. 185 distinct evidence documents. Slice tags overlap, so slice counts do not add up to 360. See `validate.py` for the live counts.
