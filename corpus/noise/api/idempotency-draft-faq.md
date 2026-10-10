---
doc_id: generated/level2-noise/api/idempotency-draft-faq
title: Idempotency for Write Requests — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: api
version: noise-3
created_date: '2026-01-07'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/api/idempotency
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
- api
---

# Idempotency for Write Requests — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Idempotency for Write Requests. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 25 hours. Repeating the same request with the same key during that period returns the… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/api/idempotency`. Relevant wording from the current article: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 24 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second…

## Open editorial question

Should we tell customers **45 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: BrightCart remembers the result for 25 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second payment or refund. A client submits a refund and the network connection drops before the response arrives. The client retries the same refund with the same idempotency key. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about idempotency for write requests. The writer invents a **48-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Priya Nair: “Please verify this against Policy Hub before publish.” Tomas Novak: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: BrightCart remembers the result for 24 hours. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/api/idempotency`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

