---
doc_id: brightcart/secondary/2026/payments/card-payments-analytics_note
title: 'Working Note: Card Payment Authorization and Capture'
source_type: analytics_note
source_system: analytics_wiki
domain: payments
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/card-payments
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
- analytics_note
---

# Working Note: Card Payment Authorization and Capture

## Context

This is an active team working note about card payment authorization and capture. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with card payment authorization and capture. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for card payment authorization and capture, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. The authorization reserves funds but is not the final settled charge. If the order is canceled before capture, BrightCart releases the authorization request.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Visa, Mastercard, American Express, and Discover are supported for standard consumer checkout.
- A bank can continue showing a released authorization as pending for several days.
- Split shipments may create more than one capture up to the authorized total.

## Search terms

Useful search terms include card payment authorization and capture, payments, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/payments/card-payments` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

When a customer reports two card entries, determine whether one is an authorization and one is a capture before labeling the situation a duplicate charge. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The payments operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
