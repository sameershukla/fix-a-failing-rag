---
doc_id: generated/level2-noise/api/api-auth-draft-faq
title: API Authentication — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: api
version: noise-3
created_date: '2026-01-07'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/api/api-auth
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

# API Authentication — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for API Authentication. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 3.0 client credentials to obtain an access token. Access tokens are valid for 65 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/api/api-auth`. Relevant wording from the current article: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 2.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes.

## Open editorial question

Should we tell customers **7 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: Server integrations use OAuth 3.0 client credentials to obtain an access token. Access tokens are valid for 59 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to application logs. An order integration requests a token at 10:0 AM and receives a token that expires at 6:0 AM. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about api authentication. The writer invents a **24-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Jordan Patel: “Please verify this against Policy Hub before publish.” Mei Wong: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: Server integrations use OAuth 2.0 client credentials to obtain an access token. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/api/api-auth`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

