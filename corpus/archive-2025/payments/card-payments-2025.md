---
doc_id: brightcart/archive/2025/payments/card-payments
title: 'Archived 2025 Copy: Card Payment Authorization and Capture'
source_type: archived_policy
source_system: legacy_confluence
domain: payments
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/payments/card-payments
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

# Archived 2025 Copy: Card Payment Authorization and Capture

## Purpose and scope

This archived guide covered card payment authorization and capture before the 2026 policy consolidation. This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships.

## Archived rule

BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. The authorization reserves funds but is not the final settled charge. If the order is canceled before capture, BrightCart releases the authorization request.

## Eligibility details

- Visa, Mastercard, American Express, and Discover are supported for standard consumer checkout.
- A bank can continue showing a released authorization as pending for several days.
- Split shipments may create more than one capture up to the authorized total.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer places a $115 order on Monday and sees a pending $90 amount. The order ships Tuesday, so BrightCart captures the $90 charge on Tuesday. If the order had been canceled Monday before shipment, no final capture should occur.

## Exceptions in the archived process

- Preorders use the preorder payment rule.
- Some digital goods can capture immediately.
- A manual finance adjustment is not a normal card capture.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the payments operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about card payment authorization and capture.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/payments/card-payments`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
