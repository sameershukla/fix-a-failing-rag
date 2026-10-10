---
doc_id: brightcart/secondary/2026/refunds/partial-refunds-training_note
title: 'Working Note: Partial Refunds and Deductions'
source_type: training_note
source_system: enablement_wiki
domain: refunds
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/partial-refunds
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
- refunds
- training_note
---

# Working Note: Partial Refunds and Deductions

## Context

This is an active team working note about partial refunds and deductions. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with partial refunds and deductions. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for partial refunds and deductions, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> A partial refund may be issued when returned merchandise is missing customer removable parts, shows customer caused damage, or only part of a multi item order is being refunded. The deduction must be tied to a documented reason and the customer must be told the amount before the refund is finalized.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Shipping fees are refunded only when the shipping service itself failed or the return was caused by BrightCart.
- Tax is recalculated based on the refunded merchandise amount.
- Agents cannot invent a restocking fee when no published fee applies.

## Search terms

Useful search terms include partial refunds and deductions, refunds, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/refunds/partial-refunds` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

The case note should identify the original price, deduction reason, deduction amount, tax adjustment, and final refund. The customer should be able to understand the calculation without contacting finance. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The refunds operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
