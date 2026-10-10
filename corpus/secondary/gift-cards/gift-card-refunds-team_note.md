---
doc_id: brightcart/secondary/2026/gift-cards/gift-card-refunds-team_note
title: 'Working Note: Refunds for Gift Card and Mixed Payments'
source_type: team_note
source_system: confluence_teamspace
domain: gift-cards
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-refunds
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
- gift-cards
- team_note
---

# Working Note: Refunds for Gift Card and Mixed Payments

## Context

This is an active team working note about refunds for gift card and mixed payments. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with refunds for gift card and mixed payments. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for refunds for gift card and mixed payments, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> An amount originally paid by BrightCart gift card is refunded back to that gift card. For mixed payment orders, the refund is returned proportionally to the original payment methods until each method has received its share. Support cannot choose to move the entire refund to a credit card for convenience.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The original payment allocation is the source of truth.
- A gift card refund is normally available the same day it is issued.
- Card portions follow normal card posting times.

## Search terms

Useful search terms include refunds for gift card and mixed payments, gift-cards, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/gift-cards/gift-card-refunds` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

When explaining a mixed refund, show the customer each payment destination and amount. This prevents the customer from expecting the whole refund on one statement. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The gift-cards operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
