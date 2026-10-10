---
doc_id: brightcart/archive/2025/refunds/refund-status
title: 'Archived 2025 Copy: Refund Status and Failed Refunds'
source_type: archived_policy
source_system: legacy_confluence
domain: refunds
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/refunds/refund-status
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

# Archived 2025 Copy: Refund Status and Failed Refunds

## Purpose and scope

This archived guide covered refund status and failed refunds before the 2026 policy consolidation. This runbook explains the refund lifecycle visible to support and the action to take when a refund fails. It is intended for customer support and payment operations.

## Archived rule

Refunds move through pending, issued, or failed status. A failed refund is retried automatically one time. If the retry also fails, the case must be sent to payment operations for manual review. Support must not create a second independent refund.

## Eligibility details

- Pending means BrightCart has accepted the request but the processor has not confirmed it.
- Issued means the processor accepted the refund.
- Failed means the processor rejected the request or the refund could not be completed.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A refund fails because the card account is closed. The platform retries once and receives the same failure. The support agent opens a payment operations case with the order ID and refund reference instead of pressing refund again.

## Exceptions in the archived process

- Processor outages can leave a refund pending longer than usual without marking it failed.
- Fraud holds are reviewed by risk and should not be bypassed by support.
- Manual payment methods may require finance rather than payment operations.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the refunds operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about refund status and failed refunds.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/refunds/refund-status`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
