---
doc_id: brightcart/secondary/2026/shipping/delayed-packages-meeting_note
title: 'Working Note: Delayed Package Handling'
source_type: meeting_note
source_system: meeting_archive
domain: shipping
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/delayed-packages
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
- meeting_note
---

# Working Note: Delayed Package Handling

## Context

This is an active team working note about delayed package handling. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with delayed package handling. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for delayed package handling, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> A package is considered delayed when it is more than 4 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless there is evidence of loss or damage.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- Use the latest promised date shown on the order.
- Check for carrier exception scans and address problems.
- Confirm that the package was not delivered to a mailroom, parcel locker, or household member.

## Search terms

Useful search terms include delayed package handling, shipping, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/shipping/delayed-packages` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Open a carrier trace when required and record the promised date, last scan, and customer confirmation. Do not issue duplicate replacements while an earlier replacement is already in transit. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The shipping operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
