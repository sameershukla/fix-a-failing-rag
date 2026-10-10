---
doc_id: brightcart/archive/2025/accounts/password-reset
title: 'Archived 2025 Copy: Password Reset Process'
source_type: archived_policy
source_system: legacy_confluence
domain: accounts
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/accounts/password-reset
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

# Archived 2025 Copy: Password Reset Process

## Purpose and scope

This archived guide covered password reset process before the 2026 policy consolidation. This runbook explains the self service password reset flow and how support should handle expired or already used links.

## Archived rule

A password reset link is valid for 60 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid.

## Eligibility details

- The reset request is sent to the verified account email.
- The new password must meet the active password policy.
- Support never asks the customer to reveal the new password.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer requests a reset at 12:00 PM and again at 2:10 PM. The first link becomes invalid when the second request is created. The second link remains valid until 2:40 PM unless it is used earlier.

## Exceptions in the archived process

- Security can force an immediate password reset after suspicious activity.
- Accounts under legal hold can still reset passwords.
- A locked account may require the lockout timer or security review in addition to a password reset.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the accounts operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about password reset process.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/accounts/password-reset`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
