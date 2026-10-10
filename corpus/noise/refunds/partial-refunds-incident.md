---
doc_id: generated/level2-noise/refunds/partial-refunds-incident
title: Partial Refunds and Deductions — Incident
source_type: incident_postmortem
source_system: incident_system
domain: refunds
version: noise-5
created_date: '2026-05-29'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/refunds/partial-refunds
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: incident
tags:
- level-2
- messy
- noise
- incident
- refunds
---

# Partial Refunds and Deductions — Incident

## Incident summary

**INC-283** affected the partial refunds and deductions workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **72 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to refunds. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/refunds/partial-refunds`: Partial refunds are used when the customer is owed money but not the full original item price. This guide explains the allowed reasons for deductions and the information that must be shown to the customer. A partial refund may be issued when returned merchandise is missing customer removable parts, shows customer caused damage, or only part of a multi item order is being refunded. The deduction must be tied to a…

## Observed behavior

Observed during the incident: Partial refunds are used when the customer is owed money but not the full original item price. This guide explains the allowed reasons for deductions and the information that must be shown to the customer. A partial refund may be issued when returned merchandise is missing customer removable parts, shows customer caused damage, or only part of a multi item… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-08-22 02:10 — alert fired
- 02:35 — Regional Operations began mitigation
- 04:20 — temporary rule set applied
- 72:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **15** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 15 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-08-22?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/refunds/partial-refunds`. Postmortem owner Maya Chen; reviewer Ifeoma Okafor.

