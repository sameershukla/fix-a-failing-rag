---
doc_id: brightcart/archive/2025/support/severity
title: 'Archived 2025 Copy: Incident Severity Levels'
source_type: archived_policy
source_system: legacy_confluence
domain: support
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/support/severity
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

# Archived 2025 Copy: Incident Severity Levels

## Purpose and scope

This archived guide covered incident severity levels before the 2026 policy consolidation. This reference defines BrightCart incident severity so teams use the same language when deciding response urgency.

## Archived rule

SEV 6 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 3 covers moderate issues, and SEV 4 covers low impact defects or questions.

## Eligibility details

- Severity is based on customer and business impact, not the job title of the reporter.
- Security can raise severity based on data risk even when few customers are affected.
- Severity can change as new evidence appears.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

Checkout fails for most customers in all regions with no workaround. That is SEV 6. If one payment method fails but customers can use another method, the incident may begin as SEV 2 depending on scale.

## Exceptions in the archived process

- Planned maintenance is not automatically an incident.
- A single high value customer does not automatically make an issue SEV 6.
- A confirmed sensitive data exposure can be SEV 1 despite limited traffic impact.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the support operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about incident severity levels.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/support/severity`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
