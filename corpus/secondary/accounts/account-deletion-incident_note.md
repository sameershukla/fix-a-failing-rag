---
doc_id: brightcart/secondary/2026/accounts/account-deletion-incident_note
title: 'Working Note: Customer Account Deletion'
source_type: incident_note
source_system: incident_db
domain: accounts
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-deletion
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
- incident_note
---

# Working Note: Customer Account Deletion

## Context

This is an active team working note about customer account deletion. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with customer account deletion. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for customer account deletion, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 35 days. Certain transaction, tax, fraud, and legal records can be retained when required by law or legitimate business obligations even after the account is no longer active.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Identity verification is required before deletion starts.
- Active subscription renewal should be canceled before the account is closed.
- Open refunds or disputes may need to finish before some data is archived.

## Search terms

Useful search terms include customer account deletion, accounts, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/accounts/account-deletion` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Support should confirm the request date and explain that deletion is not the same as erasing every record immediately. Privacy questions beyond the standard process should be escalated to the privacy team. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The accounts operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
