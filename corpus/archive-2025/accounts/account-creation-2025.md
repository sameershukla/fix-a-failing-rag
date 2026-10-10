---
doc_id: brightcart/archive/2025/accounts/account-creation
title: 'Archived 2025 Copy: Creating a Customer Account'
source_type: archived_policy
source_system: legacy_confluence
domain: accounts
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/accounts/account-creation
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

# Archived 2025 Copy: Creating a Customer Account

## Purpose and scope

This archived guide covered creating a customer account before the 2026 policy consolidation. This guide describes the minimum information required for a BrightCart customer account. It is used by support when customers cannot finish registration.

## Archived rule

A customer account requires a unique email address, a password that meets the current password policy, and a verified phone number. One email address can be associated with only one active consumer account.

## Eligibility details

- The email verification link must be completed.
- The phone verification code expires after 15 minutes.
- Disposable email domains can be blocked by risk controls.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer enters an email already tied to an existing account. Registration stops and directs the customer to sign in or reset the existing account rather than creating a duplicate identity.

## Exceptions in the archived process

- Business organizations can have multiple users under one company profile while each user still has a unique email.
- Guest checkout does not automatically create a full account.
- Support cannot bypass phone verification for convenience.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the accounts operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about creating a customer account.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/accounts/account-creation`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
