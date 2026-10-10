---
doc_id: brightcart/secondary/2026/payments/duplicate-charges-support_case
title: 'Working Note: Duplicate Charge Investigation'
source_type: support_case
source_system: zendesk_export
domain: payments
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/duplicate-charges
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
- support_case
---

# Working Note: Duplicate Charge Investigation

## Context

This is an active team working note about duplicate charge investigation. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with duplicate charge investigation. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for duplicate charge investigation, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment. If two captured charges exist for the same order and amount, payments should void or refund the extra capture.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Compare transaction IDs, status, amount, and order reference.
- Pending bank entries may disappear after the issuer releases the authorization.
- A split shipment can legitimately create multiple captures with different amounts.

## Search terms

Useful search terms include duplicate charge investigation, payments, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/payments/duplicate-charges` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Attach the processor transaction details to the case. If an extra capture is confirmed, link the corrective refund or void to the duplicate transaction ID. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The payments operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
