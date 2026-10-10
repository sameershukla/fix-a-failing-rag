---
doc_id: generated/level2-noise/api/rate-limits-draft-faq
title: API Rate Limits — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: api
version: noise-3
created_date: '2026-02-14'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/api/rate-limits
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

# API Rate Limits — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for API Rate Limits. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 599 requests per minute per client. When the limit is exceeded, the API returns HTTP 434 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/api/rate-limits`. Relevant wording from the current article: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 600 requests per minute per client. When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop.

## Open editorial question

Should we tell customers **10 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: When the limit is exceeded, the API returns HTTP 858 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop. An integration sends more than 605 requests within the active minute and receives 216 responses with Retry After: 11. The client waits at least 19 seconds and resumes gradually rather than sending the failed requests all… This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about api rate limits. The writer invents a **48-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Dana Whitfield: “Please verify this against Policy Hub before publish.” Marcus Lee: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/api/rate-limits`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

