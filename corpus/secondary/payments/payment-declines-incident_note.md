---
doc_id: brightcart/secondary/2026/payments/payment-declines-incident_note
title: 'Working Note: Handling Card Payment Declines'
source_type: incident_note
source_system: incident_db
domain: payments
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/payment-declines
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
- incident_note
---

# Working Note: Handling Card Payment Declines

## Context

This is an active team working note about handling card payment declines. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with handling card payment declines. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for handling card payment declines, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> After a card decline, the customer may retry once after checking the billing address, expiration date, and available funds. Repeated rapid retries should be avoided because they can trigger issuer fraud controls. BrightCart cannot see the issuer's private decline reason beyond the processor code returned to us.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Do not ask the customer to send a full card number in chat or email.
- A corrected billing address can justify one new attempt.
- A hard processor code such as stolen card should not be retried.

## Search terms

Useful search terms include handling card payment declines, payments, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/payments/payment-declines` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Record the processor code and whether a retry occurred. Never copy sensitive card data into case notes. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The payments operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
