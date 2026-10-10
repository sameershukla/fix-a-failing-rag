---
doc_id: brightcart/secondary/2026/orders/order-modification-meeting_note
title: 'Working Note: Changing an Order Before Fulfillment'
source_type: meeting_note
source_system: meeting_archive
domain: orders
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/orders/order-modification
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
- orders
- meeting_note
---

# Working Note: Changing an Order Before Fulfillment

## Context

This is an active team working note about changing an order before fulfillment. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with changing an order before fulfillment. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for changing an order before fulfillment, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> A shipping address or item quantity can be changed only while the order is in received status and before fulfillment starts. Once the order moves to picking or packed status, item and address changes are not allowed. The customer can then use cancellation or return options if eligible.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The replacement address must pass normal validation.
- Increasing quantity requires available inventory and payment authorization.
- Changing to a different product creates a new order rather than editing the original line.

## Search terms

Useful search terms include changing an order before fulfillment, orders, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/orders/order-modification` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Check the live fulfillment status before making any promise. If the order crosses into picking while the case is open, stop the edit and explain the available next action. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The orders operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
