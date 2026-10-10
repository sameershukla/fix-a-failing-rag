---
doc_id: brightcart/archive/2025/security/suspicious-login
title: 'Archived 2025 Copy: Suspicious Login Response'
source_type: archived_policy
source_system: legacy_confluence
domain: security
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/security/suspicious-login
company: BrightCart
audience:
- support
- operations
tags:
- level-2
- stale
- near-duplicate
- security
- archived
---

# Archived 2025 Copy: Suspicious Login Response

## Purpose and scope

This archived guide covered suspicious login response before the 2026 policy consolidation. This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly.

## Archived rule

For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified channel. High confidence account takeover cases are escalated to security.

## Eligibility details

- Confirm the customer identity before discussing account details.
- Review recent email, phone, shipping address, and saved payment changes.
- Check whether MFA was added, removed, or challenged.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A customer receives a new device alert from a city they did not visit. After identity verification, support revokes sessions and starts a password reset. The account shows an unauthorized shipping address change, so the case is escalated to security.

## Exceptions in the archived process

- Travel or VPN use can create a false positive alert.
- A failed login attempt alone is not proof of takeover.
- Active fraud or payment theft can require immediate order cancellation.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the security operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about suspicious login response.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/security/suspicious-login`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
