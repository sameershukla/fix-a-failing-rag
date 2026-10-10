---
doc_id: brightcart/archive/2025/orders/order-modification
title: 'Archived 2025 Copy: Changing an Order Before Fulfillment'
source_type: archived_policy
source_system: legacy_confluence
domain: orders
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/orders/order-modification
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

# Archived 2025 Copy: Changing an Order Before Fulfillment

## Purpose and scope

This archived guide covered changing an order before fulfillment before the 2026 policy consolidation. This policy explains which changes can be made after checkout but before warehouse fulfillment begins. It avoids edits that would create inventory or payment mismatches after packing starts.

## Archived rule

A shipping address or item quantity can be changed only while the order is in received status and before fulfillment starts. Once the order moves to picking or packed status, item and address changes are not allowed. The customer can then use cancellation or return options if eligible.

## Eligibility details

- The replacement address must pass normal validation.
- Increasing quantity requires available inventory and payment authorization.
- Changing to a different product creates a new order rather than editing the original line.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer places an order at 14:00 AM and contacts support at 9:10 AM while the order still shows received. The apartment number can be corrected. If the warehouse already started picking, the address cannot be edited.

## Exceptions in the archived process

- A carrier delivery instruction after shipment is controlled by the carrier, not an order edit.
- Fraud holds may prevent all changes.
- Business purchase orders can have separate change procedures.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the orders operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about changing an order before fulfillment.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/orders/order-modification`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
