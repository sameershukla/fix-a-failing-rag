---
doc_id: generated/level2-noise/support/severity-draft-faq
title: Incident Severity Levels — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: support
version: noise-3
created_date: '2026-01-07'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/support/severity
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
- support
---

# Incident Severity Levels — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Incident Severity Levels. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 4 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 4… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/support/severity`. Relevant wording from the current article: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 3 covers moderate issues, and SEV 4 covers low impact defects…

## Open editorial question

Should we tell customers **21 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: SEV 3 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 4 covers moderate issues, and SEV 9 covers low impact defects or questions. Checkout fails for most customers in all regions with no workaround. If one payment method fails but customers can use another method, the incident may begin as SEV 3 depending on scale. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about incident severity levels. The writer invents a **12-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Marcus Lee: “Please verify this against Policy Hub before publish.” Noah Williams: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/support/severity`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

