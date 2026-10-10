---
doc_id: brightcart/secondary/2026/subscriptions/subscription-plans-slack_summary
title: 'Working Note: Subscription Plans and Pricing'
source_type: slack_summary
source_system: slack_export
domain: subscriptions
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-plans
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
- subscriptions
- slack_summary
---

# Working Note: Subscription Plans and Pricing

## Context

This is an active team working note about subscription plans and pricing. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with subscription plans and pricing. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for subscription plans and pricing, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> BrightCart Plus is offered as a monthly plan and an annual plan. The annual plan is priced 20 percent lower than paying the standard monthly price for twelve months. Both plans provide the same core member benefits unless a promotion explicitly adds a temporary benefit.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Taxes may apply based on customer location.
- Promotional discounts are applied separately from the standard annual savings.
- Plan changes take effect according to the billing change shown at checkout.

## Search terms

Useful search terms include subscription plans and pricing, subscriptions, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/subscriptions/subscription-plans` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Support should quote the price currently shown on the customer account and explain the annual savings rule instead of promising that a temporary promotion will renew. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The subscriptions operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
