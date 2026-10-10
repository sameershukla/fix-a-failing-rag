---
doc_id: brightcart/archive/2025/support/incident-response
title: 'Archived 2025 Copy: Incident Response Process'
source_type: archived_policy
source_system: legacy_confluence
domain: support
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/support/incident-response
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

# Archived 2025 Copy: Incident Response Process

## Purpose and scope

This archived guide covered incident response process before the 2026 policy consolidation. This runbook describes the first response steps for service incidents and the follow up expected after restoration.

## Archived rule

A SEV 1 incident should be acknowledged within 30 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 10 business days after a SEV 1 or qualifying SEV 2 incident is resolved.

## Eligibility details

- The incident commander coordinates work and communication.
- A timeline should record meaningful changes and decisions.
- Customer facing communication should be updated as impact changes.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

Monitoring detects checkout failure at 6:00 AM. The on call engineer acknowledges the SEV 1 by 1:10 AM, starts the incident channel, and names an incident commander. After recovery, the team schedules the postmortem for the same week.

## Exceptions in the archived process

- A false alarm closed before customer impact is confirmed may not require a full postmortem.
- Security incidents can have restricted communication channels.
- Regulatory notification timelines can add separate obligations.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the support operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about incident response process.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/support/incident-response`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
