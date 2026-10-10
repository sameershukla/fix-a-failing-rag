---
doc_id: brightcart/secondary/2026/shipping/domestic-shipping-ops_handoff
title: 'Working Note: Domestic Shipping Service Levels'
source_type: ops_handoff
source_system: ops_wiki
domain: shipping
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/domestic-shipping
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
- ops_handoff
---

# Working Note: Domestic Shipping Service Levels

## Context

This is an active team working note about domestic shipping service levels. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with domestic shipping service levels. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for domestic shipping service levels, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> Standard domestic shipping normally arrives in 4 to 7 business days after the order ships. The estimate begins when the carrier accepts the package, not when the customer places the order. Processing time before shipment is separate.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Business days exclude weekends and federal holidays.
- The delivery estimate can vary for Alaska, Hawaii, and remote postal codes.
- A tracking number is created before the carrier may show the first scan.

## Search terms

Useful search terms include domestic shipping service levels, shipping, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/shipping/domestic-shipping` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Support should quote the tracking based estimate when available. If the shipment is more than two business days beyond the promised date, use the delayed package runbook. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The shipping operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
