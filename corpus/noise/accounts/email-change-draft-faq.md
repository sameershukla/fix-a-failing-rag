---
doc_id: generated/level2-noise/accounts/email-change-draft-faq
title: Changing the Account Email Address — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: accounts
version: noise-3
created_date: '2026-04-03'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/accounts/email-change
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
- accounts
---

# Changing the Account Email Address — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Changing the Account Email Address. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/accounts/email-change`. Relevant wording from the current article: This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change.

## Open editorial question

Should we tell customers **90 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change. The new email becomes the sign in identifier only after verification succeeds. A signed in customer enters a new email but does not complete verification. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about changing the account email address. The writer invents a **12-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Ifeoma Okafor: “Please verify this against Policy Hub before publish.” Mei Wong: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: To change the account email, the customer must enter the current password and verify the new email address. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/accounts/email-change`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

