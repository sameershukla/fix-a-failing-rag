---
doc_id: brightcart/secondary/2026/api/idempotency-ops_handoff
title: 'Working Note: Idempotency for Write Requests'
source_type: ops_handoff
source_system: ops_wiki
domain: api
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/idempotency
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
- api
- ops_handoff
---

# Working Note: Idempotency for Write Requests

## Context

This is an active team working note about idempotency for write requests. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with idempotency for write requests. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for idempotency for write requests, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 48 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second payment or refund.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The key should be unique for one intended business operation.
- A retry of the same operation must reuse the same key.
- Using the same key for different request bodies can return a conflict error.

## Search terms

Useful search terms include idempotency for write requests, api, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/api/idempotency` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Log the idempotency key alongside the client operation ID, but do not use secrets or customer payment data as the key value. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The api operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
