---
doc_id: brightcart/archive/2025/refunds/refund-timelines
title: 'Archived 2025 Copy: Refund Timelines by Payment Method'
source_type: archived_policy
source_system: legacy_confluence
domain: refunds
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/refunds/refund-timelines
company: BrightCart
audience:
- support
- operations
tags:
- level-2
- stale
- near-duplicate
- refunds
- archived
---

# Archived 2025 Copy: Refund Timelines by Payment Method

## Purpose and scope

This archived guide covered refund timelines by payment method before the 2026 policy consolidation. This reference separates BrightCart processing time from the time a bank or card issuer may take to display the credit. Use it when a refund is already in issued status and the customer wants to know when the money will appear.

## Archived rule

After a refund is issued, card refunds usually appear within 5 to 8 business days, ACH refunds usually appear within 7 to 10 business days, and gift card refunds are normally available the same day. These are posting estimates after BrightCart has issued the refund.

## Eligibility details

- The refund must show issued, not pending.
- Issuer or bank posting time is controlled by the financial institution.
- The estimate is counted in business days.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

BrightCart issues a Visa refund on Wednesday. The customer should normally see the credit between the following Monday and Wednesday, depending on bank holidays and the card issuer.

## Exceptions in the archived process

- A failed refund does not follow the normal posting estimate.
- Closed bank accounts may cause a refund to be rejected and returned.
- Chargeback credits follow the issuer dispute process, not this timeline.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the refunds operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about refund timelines by payment method.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/refunds/refund-timelines`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
