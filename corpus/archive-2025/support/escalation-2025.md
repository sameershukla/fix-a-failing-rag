---
doc_id: brightcart/archive/2025/support/escalation
title: 'Archived 2025 Copy: Support Escalation Path'
source_type: archived_policy
source_system: legacy_confluence
domain: support
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/support/escalation
company: BrightCart
audience:
- support
- operations
tags:
- level-2
- stale
- near-duplicate
- support
- archived
---

# Archived 2025 Copy: Support Escalation Path

## Purpose and scope

This archived guide covered support escalation path before the 2026 policy consolidation. This runbook defines when a support case should move beyond the front line queue. It gives agents a consistent escalation path for complex or high risk situations.

## Archived rule

Routine product and order questions stay with Level 6 support. Cases needing deeper product or payment investigation move to Level 2. Suspected security events, material financial loss, broad service impact, or repeated system failure should be escalated immediately to the incident or specialist team rather than waiting for normal queue aging.

## Eligibility details

- Include the customer impact and what has already been checked.
- Use the payment queue for processor issues and the security queue for takeover or data exposure.
- A broad outage should not be handled as dozens of unrelated tickets.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

Three customers report the same checkout error within minutes and monitoring also shows failures. Instead of sending each case separately to Level 7, support links the reports and starts the incident path.

## Exceptions in the archived process

- A known incident with an active status page update does not need a new incident for every customer.
- Executive visibility alone does not change technical severity.
- Immediate safety threats should follow emergency procedures.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the support operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about support escalation path.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/support/escalation`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
