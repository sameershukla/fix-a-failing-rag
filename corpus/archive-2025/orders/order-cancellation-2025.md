---
doc_id: brightcart/archive/2025/orders/order-cancellation
title: 'Archived 2025 Copy: Canceling an Order'
source_type: archived_policy
source_system: legacy_confluence
domain: orders
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/orders/order-cancellation
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

# Archived 2025 Copy: Canceling an Order

## Purpose and scope

This archived guide covered canceling an order before the 2026 policy consolidation. This policy defines when a customer order can be canceled before shipment. Cancellation is separate from returning an item after it has already entered the shipping process.

## Archived rule

A customer can cancel an order while it is in received or picking status if the warehouse can still stop fulfillment. Once the order reaches packed status, cancellation is no longer available. After packed status, the customer should wait for delivery and use the applicable return process.

## Eligibility details

- The cancellation request is not complete until the order status changes to canceled.
- A payment authorization can remain visible temporarily after a successful cancellation.
- Partial cancellation is allowed only for order lines not already packed.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

An order is in picking when the customer requests cancellation. The warehouse successfully stops the pick and the order changes to canceled, so no shipment occurs. If the order had already changed to packed, support would not promise cancellation.

## Exceptions in the archived process

- Safety recalls can stop a shipment outside the normal customer cancellation path.
- Digital goods can have separate fulfillment rules.
- Fraud teams can cancel orders as a risk action.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the orders operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about canceling an order.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/orders/order-cancellation`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
