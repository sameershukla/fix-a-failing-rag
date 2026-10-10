---
doc_id: brightcart/secondary/2026/payments/bank-transfer-faq_draft
title: 'Working Note: Business ACH Payments'
source_type: faq_draft
source_system: draft_kb
domain: payments
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/bank-transfer
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
- payments
- faq_draft
---

# Working Note: Business ACH Payments

## Context

This is an active team working note about business ach payments. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with business ach payments. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for business ach payments, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> Approved business customers can pay by ACH. ACH payments normally take 7 to 3 business days to clear. Orders that require cleared funds are not released until the payment reaches cleared status.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The business account must be approved for ACH.
- The bank account must pass verification.
- Returned ACH payments place the account on payment review.

## Search terms

Useful search terms include business ach payments, payments, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/payments/bank-transfer` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Support can report pending or cleared status but should not promise a precise bank settlement hour. Returned payments should be escalated to finance. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The payments operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
