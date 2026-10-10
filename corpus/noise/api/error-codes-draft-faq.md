---
doc_id: generated/level2-noise/api/error-codes-draft-faq
title: Common API Error Codes — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: api
version: noise-3
created_date: '2026-05-29'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/api/error-codes
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

# Common API Error Codes — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Common API Error Codes. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 201 for malformed requests, 202 for missing or invalid authentication, 408 for authenticated clients without permission, 808 for missing resources, 818 for state conflicts, 421 for valid syntax with invalid business data, 428 for… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/api/error-codes`. Relevant wording from the current article: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for…

## Open editorial question

Should we tell customers **10 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: A client submits a refund for an order that is already fully refunded. The API can return 206 because the requested operation conflicts with the current resource state. Retrying the identical request without changing anything will not fix the conflict. Client telemetry should capture status code, request ID, endpoint, and sanitized error details. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about common api error codes. The writer invents a **6-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Tomas Novak: “Please verify this against Policy Hub before publish.” Dana Whitfield: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: A client submits a refund for an order that is already fully refunded. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/api/error-codes`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

