---
doc_id: brightcart/archive/2025/payments/duplicate-charges
title: 'Archived 2025 Copy: Duplicate Charge Investigation'
source_type: archived_policy
source_system: legacy_confluence
domain: payments
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/payments/duplicate-charges
company: BrightCart
audience:
- support
- operations
tags:
- level-2
- stale
- near-duplicate
- payments
- archived
---

# Archived 2025 Copy: Duplicate Charge Investigation

## Purpose and scope

This archived guide covered duplicate charge investigation before the 2026 policy consolidation. This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists.

## Archived rule

Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment. If two captured charges exist for the same order and amount, payments should void or refund the extra capture.

## Eligibility details

- Compare transaction IDs, status, amount, and order reference.
- Pending bank entries may disappear after the issuer releases the authorization.
- A split shipment can legitimately create multiple captures with different amounts.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A bank app shows one $100 pending amount and one $75 posted amount for the same order. BrightCart finds one authorization and one capture. Support explains the pending authorization instead of issuing a second refund.

## Exceptions in the archived process

- Two settled charges with distinct transaction IDs require payment operations action.
- A customer may have placed two separate identical orders.
- Chargebacks are not handled as duplicate capture refunds.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the payments operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about duplicate charge investigation.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/payments/duplicate-charges`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
