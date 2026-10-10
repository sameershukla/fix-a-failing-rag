---
doc_id: brightcart/secondary/2026/accounts/email-change-slack_summary
title: 'Working Note: Changing the Account Email Address'
source_type: slack_summary
source_system: slack_export
domain: accounts
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/email-change
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- secondary
- distractor
- semantic-overlap
- accounts
- slack_summary
---

# Working Note: Changing the Account Email Address

## Context

This is an active team working note about changing the account email address. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with changing the account email address. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for changing the account email address, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change. The new email becomes the sign in identifier only after verification succeeds.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The new email cannot already belong to another active consumer account.
- The verification code expires after 15 minutes.
- A recently recovered account can be temporarily blocked from email changes.

## Search terms

Useful search terms include changing the account email address, accounts, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/accounts/email-change` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

If a customer reports an email change they did not make, treat it as suspicious account activity and follow the session revocation process. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The accounts operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
