---
doc_id: brightcart/archive/2025/orders/backorders
title: 'Archived 2025 Copy: Backordered Items'
source_type: archived_policy
source_system: legacy_confluence
domain: orders
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/orders/backorders
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

# Archived 2025 Copy: Backordered Items

## Purpose and scope

This archived guide covered backordered items before the 2026 policy consolidation. This article explains how BrightCart handles items that were orderable but are temporarily unavailable at the warehouse.

## Archived rule

A backordered item is not captured on a standard card until it ships. The order page shows an estimated availability date. If the estimate changes, BrightCart updates the order and sends a notice when the change is significant.

## Eligibility details

- In stock items on the same order can ship separately.
- The card must remain valid when the backordered item becomes ready.
- Customers can cancel an unshipped backordered line.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer orders two items, one in stock and one backordered. The in stock item ships and is charged first. The backordered item remains open and is captured only when it later ships.

## Exceptions in the archived process

- Gift card value can be reserved differently from a credit card capture.
- Supplier cancellation can cause BrightCart to cancel and refund the line.
- Made to order products follow their own lead time terms.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the orders operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about backordered items.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/orders/backorders`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
