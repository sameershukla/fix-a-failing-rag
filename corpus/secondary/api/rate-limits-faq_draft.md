---
doc_id: brightcart/secondary/2026/api/rate-limits-faq_draft
title: 'Working Note: API Rate Limits'
source_type: faq_draft
source_system: draft_kb
domain: api
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/rate-limits
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
- faq_draft
---

# Working Note: API Rate Limits

## Context

This is an active team working note about api rate limits. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with api rate limits. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for api rate limits, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> The default public API limit is 450 requests per minute per client. When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The limit is measured per registered client.
- Short traffic bursts can consume the available window quickly.
- Repeated 429 responses can indicate a design problem in polling or retry logic.

## Search terms

Useful search terms include api rate limits, api, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/api/rate-limits` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Record rate limit headers in client telemetry. If normal traffic consistently needs more capacity, request a limit review instead of ignoring 429 responses. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The api operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
