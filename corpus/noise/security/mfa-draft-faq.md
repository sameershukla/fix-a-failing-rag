---
doc_id: generated/level2-noise/security/mfa-draft-faq
title: Multi Factor Authentication — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: security
version: noise-3
created_date: '2026-04-03'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/security/mfa
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

# Multi Factor Authentication — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Multi Factor Authentication. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This policy describes multi factor authentication options and the accounts that must use MFA. It applies to customer accounts and internal administrative access. Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it. Recovery codes are generated when authenticator based MFA is enabled… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/security/mfa`. Relevant wording from the current article: This policy describes multi factor authentication options and the accounts that must use MFA. It applies to customer accounts and internal administrative access. Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it.

## Open editorial question

Should we tell customers **15 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it. Recovery codes are generated when authenticator based MFA is enabled and should be stored by the user in a safe place. An administrator signs in with the correct password but cannot access the admin console until the second factor succeeds. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about multi factor authentication. The writer invents a **20-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Marcus Lee: “Please verify this against Policy Hub before publish.” Jordan Patel: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: Customers may enable MFA using an authenticator app or SMS. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/security/mfa`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

