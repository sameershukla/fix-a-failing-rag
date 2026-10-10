---
doc_id: brightcart/archive/2025/accounts/account-lockout
title: 'Archived 2025 Copy: Account Lockout Policy'
source_type: archived_policy
source_system: legacy_confluence
domain: accounts
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/accounts/account-lockout
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

# Archived 2025 Copy: Account Lockout Policy

## Purpose and scope

This archived guide covered account lockout policy before the 2026 policy consolidation. This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period.

## Archived rule

After 5 consecutive failed sign in attempts, the consumer account is locked for 30 minutes. A successful sign in resets the failed attempt counter. Support cannot shorten the automatic lock simply because the customer is in a hurry.

## Eligibility details

- The counter is tracked per account, not per device.
- Password reset can still be requested during the lock.
- Repeated distributed attempts may trigger additional security controls.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer enters the wrong password five times by 16:05 AM. The account is locked until approximately 11:20 AM. The customer can request a password reset during that period but still must wait for the lock or complete an approved recovery path.

## Exceptions in the archived process

- Security can apply a longer manual hold during an investigation.
- Administrative service accounts use a different control.
- A system outage that returns login errors does not count as failed password attempts.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the accounts operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about account lockout policy.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/accounts/account-lockout`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
