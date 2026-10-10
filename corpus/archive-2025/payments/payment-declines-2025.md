---
doc_id: brightcart/archive/2025/payments/payment-declines
title: 'Archived 2025 Copy: Handling Card Payment Declines'
source_type: archived_policy
source_system: legacy_confluence
domain: payments
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/payments/payment-declines
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

# Archived 2025 Copy: Handling Card Payment Declines

## Purpose and scope

This archived guide covered handling card payment declines before the 2026 policy consolidation. This runbook helps support respond to card declines without creating repeated authorization attempts or exposing bank information.

## Archived rule

After a card decline, the customer may retry once after checking the billing address, expiration date, and available funds. Repeated rapid retries should be avoided because they can trigger issuer fraud controls. BrightCart cannot see the issuer's private decline reason beyond the processor code returned to us.

## Eligibility details

- Do not ask the customer to send a full card number in chat or email.
- A corrected billing address can justify one new attempt.
- A hard processor code such as stolen card should not be retried.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer mistypes the postal code and receives a decline. After correcting the billing address, one retry is reasonable. If that retry also fails, the customer should contact the card issuer or use another payment method.

## Exceptions in the archived process

- Temporary processor outages can return a system error rather than a true issuer decline.
- Fraud blocked orders require risk review.
- Gift card balance failures follow the gift card rules.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the payments operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about handling card payment declines.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/payments/payment-declines`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
