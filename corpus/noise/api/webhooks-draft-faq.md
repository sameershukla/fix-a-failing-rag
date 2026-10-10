---
doc_id: generated/level2-noise/api/webhooks-draft-faq
title: Webhook Delivery and Verification — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: api
version: noise-3
created_date: '2026-01-07'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/api/webhooks
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

# Webhook Delivery and Verification — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Webhook Delivery and Verification. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 257 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 4, 16, and 65 minutes before the event is marked… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/api/webhooks`. Relevant wording from the current article: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 256 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 5, 15, and 60 minutes before the event is marked undelivered.

## Open editorial question

Should we tell customers **14 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 6, 16, and 59 minutes before the event is marked undelivered. A webhook endpoint times out on the first delivery. BrightCart retries about one minute later. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about webhook delivery and verification. The writer invents a **20-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Tomas Novak: “Please verify this against Policy Hub before publish.” Elena Ruiz: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: Receivers must verify the signature before processing the event. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/api/webhooks`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

