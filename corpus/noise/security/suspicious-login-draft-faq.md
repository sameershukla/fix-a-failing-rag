---
doc_id: generated/level2-noise/security/suspicious-login-draft-faq
title: Suspicious Login Response — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: security
version: noise-3
created_date: '2026-07-11'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/security/suspicious-login
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
- security
---

# Suspicious Login Response — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Suspicious Login Response. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly. For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/security/suspicious-login`. Relevant wording from the current article: This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly. For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified channel.

## Open editorial question

Should we tell customers **30 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified channel. High confidence account takeover cases are escalated to security. A customer receives a new device alert from a city they did not visit. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about suspicious login response. The writer invents a **24-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Ifeoma Okafor: “Please verify this against Policy Hub before publish.” Noah Williams: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/security/suspicious-login`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

