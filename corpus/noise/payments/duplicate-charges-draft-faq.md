---
doc_id: generated/level2-noise/payments/duplicate-charges-draft-faq
title: Duplicate Charge Investigation — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: payments
version: noise-3
created_date: '2026-05-29'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/payments/duplicate-charges
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: draft-faq
tags:
- level-2
- messy
- noise
- draft-faq
- payments
---

# Duplicate Charge Investigation — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Duplicate Charge Investigation. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists. Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/payments/duplicate-charges`. Relevant wording from the current article: This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists. Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment.

## Open editorial question

Should we tell customers **7 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment. If two captured charges exist for the same order and amount, payments should void or refund the extra capture. A bank app shows one $76 pending amount and one $150 posted amount for the same order. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about duplicate charge investigation. The writer invents a **72-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Jordan Patel: “Please verify this against Policy Hub before publish.” Priya Nair: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: Before refunding a reported duplicate charge, verify whether both entries are captured transactions. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/payments/duplicate-charges`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

