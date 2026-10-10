---
doc_id: brightcart/secondary/2026/shipping/lost-packages-support_case
title: 'Working Note: Lost Package Criteria'
source_type: support_case
source_system: zendesk_export
domain: shipping
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/lost-packages
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
- shipping
- support_case
---

# Working Note: Lost Package Criteria

## Context

This is an active team working note about lost package criteria. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with lost package criteria. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for lost package criteria, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> A domestic package can be treated as lost after 10 consecutive calendar days with no new carrier scan. An international package uses a 10 calendar day no scan threshold because customs movement can be slower. An explicit carrier lost status overrides these waiting periods.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Count from the timestamp of the last meaningful carrier scan.
- A label created event without carrier possession is handled as a fulfillment issue.
- A customs hold message is a scan and resets the international no movement clock.

## Search terms

Useful search terms include lost package criteria, shipping, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/shipping/lost-packages` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

When resolving a lost package, record the last scan time, destination, item value, and whether the customer wants replacement or refund. A replacement shipment should have a new tracking number. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The shipping operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
