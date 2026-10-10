---
doc_id: brightcart/secondary/2026/subscriptions/subscription-pause-team_note
title: 'Working Note: Pausing and Resuming Membership'
source_type: team_note
source_system: confluence_teamspace
domain: subscriptions
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-pause
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
- team_note
---

# Working Note: Pausing and Resuming Membership

## Context

This is an active team working note about pausing and resuming membership. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with pausing and resuming membership. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for pausing and resuming membership, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> A monthly BrightCart Plus subscription can be paused for 1, 2, 3, or 4 full billing months. Annual plans cannot be paused. During a pause, recurring charges stop and membership benefits are inactive. The subscription resumes automatically after the selected pause period.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The plan must be monthly and in good standing.
- A pause starts at the end of the current paid billing period.
- Only one active pause can exist at a time.

## Search terms

Useful search terms include pausing and resuming membership, subscriptions, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/subscriptions/subscription-pause` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Support should confirm the resume date in the case notes and tell the customer that billing will restart automatically on that date unless the plan is canceled. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The subscriptions operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
