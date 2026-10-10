---
doc_id: brightcart/archive/2025/orders/preorders
title: 'Archived 2025 Copy: Preorder Fulfillment and Payment'
source_type: archived_policy
source_system: legacy_confluence
domain: orders
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/orders/preorders
company: BrightCart
audience:
- support
- operations
tags:
- level-2
- stale
- near-duplicate
- orders
- archived
---

# Archived 2025 Copy: Preorder Fulfillment and Payment

## Purpose and scope

This archived guide covered preorder fulfillment and payment before the 2026 policy consolidation. This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled.

## Archived rule

For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier schedule changes.

## Eligibility details

- The customer must keep a valid payment method on the order.
- An authorization check can expire before the ship date without being a final charge.
- BrightCart sends an update when the expected ship date changes materially.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer preorders a console in May for an expected July shipment. The card is verified in May, but the final capture occurs when the console ships in July. If the supplier moves the date, BrightCart sends an updated estimate.

## Exceptions in the archived process

- Gift cards can reserve value immediately because they do not use card authorization holds.
- Limited release items can have quantity limits.
- Business purchase orders can follow contract terms.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the orders operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about preorder fulfillment and payment.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/orders/preorders`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
