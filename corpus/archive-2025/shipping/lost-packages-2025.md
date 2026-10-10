---
doc_id: brightcart/archive/2025/shipping/lost-packages
title: 'Archived 2025 Copy: Lost Package Criteria'
source_type: archived_policy
source_system: legacy_confluence
domain: shipping
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/shipping/lost-packages
company: BrightCart
audience:
- support
- operations
tags:
- level-2
- stale
- near-duplicate
- shipping
- archived
---

# Archived 2025 Copy: Lost Package Criteria

## Purpose and scope

This archived guide covered lost package criteria before the 2026 policy consolidation. This article defines when a package can be treated as lost rather than merely delayed. It is used before a replacement or refund is approved for a shipment that stopped moving.

## Archived rule

A domestic package can be treated as lost after 10 consecutive calendar days with no new carrier scan. An international package uses a 10 calendar day no scan threshold because customs movement can be slower. An explicit carrier lost status overrides these waiting periods.

## Eligibility details

- Count from the timestamp of the last meaningful carrier scan.
- A label created event without carrier possession is handled as a fulfillment issue.
- A customs hold message is a scan and resets the international no movement clock.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A domestic package has its last carrier movement scan on June 6 and there are no later scans. On June 6 it reaches the five day no scan threshold and support can start the lost package resolution process.

## Exceptions in the archived process

- High value items may require a carrier investigation before replacement.
- Fraud flagged orders require risk review.
- An explicit carrier confirmation of loss allows immediate resolution.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the shipping operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about lost package criteria.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/shipping/lost-packages`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
