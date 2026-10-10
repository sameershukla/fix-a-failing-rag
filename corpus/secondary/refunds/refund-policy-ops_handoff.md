---
doc_id: brightcart/secondary/2026/refunds/refund-policy-ops_handoff
title: 'Working Note: Standard Refund Policy'
source_type: ops_handoff
source_system: ops_wiki
domain: refunds
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-policy
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
- ops_handoff
---

# Working Note: Standard Refund Policy

## Context

This is an active team working note about standard refund policy. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with standard refund policy. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for standard refund policy, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> Once BrightCart approves a refund, the refund is sent back to the original payment method. BrightCart normally issues the refund within 7 business days after the return is accepted or the cancellation is confirmed. Bank processing time can add additional days after BrightCart sends the money.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The return or cancellation must already be approved.
- The original payment method should be used unless a separate policy explicitly says otherwise.
- Business days exclude weekends and United States federal holidays.

## Search terms

Useful search terms include standard refund policy, refunds, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/refunds/refund-policy` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Support should confirm the return or cancellation status before promising a date. If the refund has not moved to issued status after 5 business days, open a payment investigation instead of creating a second refund. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The refunds operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
