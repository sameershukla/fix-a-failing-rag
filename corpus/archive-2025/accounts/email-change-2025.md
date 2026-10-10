---
doc_id: brightcart/archive/2025/accounts/email-change
title: 'Archived 2025 Copy: Changing the Account Email Address'
source_type: archived_policy
source_system: legacy_confluence
domain: accounts
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/accounts/email-change
company: BrightCart
audience:
- support
- operations
tags:
- level-2
- stale
- near-duplicate
- accounts
- archived
---

# Archived 2025 Copy: Changing the Account Email Address

## Purpose and scope

This archived guide covered changing the account email address before the 2026 policy consolidation. This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account.

## Archived rule

To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change. The new email becomes the sign in identifier only after verification succeeds.

## Eligibility details

- The new email cannot already belong to another active consumer account.
- The verification code expires after 30 minutes.
- A recently recovered account can be temporarily blocked from email changes.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A signed in customer enters a new email but does not complete verification. The account continues using the old email. Once the verification code is completed, the new address becomes active and the old address receives a change notice.

## Exceptions in the archived process

- Customers who no longer control the old account credentials must use account recovery rather than a normal email change.
- Security can freeze profile changes during an active takeover investigation.
- Business administrator changes follow organization controls.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the accounts operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about changing the account email address.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/accounts/email-change`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
