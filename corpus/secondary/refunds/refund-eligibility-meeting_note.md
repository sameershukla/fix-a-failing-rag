---
doc_id: brightcart/secondary/2026/refunds/refund-eligibility-meeting_note
title: 'Working Note: Refund Eligibility Rules'
source_type: meeting_note
source_system: meeting_archive
domain: refunds
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-eligibility
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
- meeting_note
---

# Working Note: Refund Eligibility Rules

## Context

This is an active team working note about refund eligibility rules. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with refund eligibility rules. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for refund eligibility rules, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> Most unused physical items are eligible for a refund when the return is requested within 21 calendar days of delivery. Final sale items are not refundable. The item must include the parts and accessories that were shipped with it unless the item arrived damaged or incomplete.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- The 30 day clock starts on the carrier delivery date.
- Unused means the item has not been materially altered, consumed, or installed.
- A missing accessory can reduce the refund when the customer caused the loss.

## Search terms

Useful search terms include refund eligibility rules, refunds, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/refunds/refund-eligibility` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

Support should record the delivery date, reason for return, and item condition. If an agent cannot determine whether an item is final sale, the case should be escalated rather than approved by assumption. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The refunds operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
