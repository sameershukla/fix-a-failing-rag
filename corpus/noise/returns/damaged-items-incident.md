---
doc_id: generated/level2-noise/returns/damaged-items-incident
title: Damaged Item Claims — Incident
source_type: incident_postmortem
source_system: incident_system
domain: returns
version: noise-5
created_date: '2026-05-29'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/returns/damaged-items
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
- returns
---

# Damaged Item Claims — Incident

## Incident summary

**INC-643** affected the damaged item claims workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **8 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to returns. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/returns/damaged-items`: This runbook covers merchandise that arrives physically damaged. It helps support distinguish delivery damage from customer caused damage and collect enough information for a replacement or refund decision. Customers should report visible delivery damage within 7 calendar days of delivery. Support should request clear photos of the item and shipping package when practical.

## Observed behavior

Observed during the incident: This runbook covers merchandise that arrives physically damaged. It helps support distinguish delivery damage from customer caused damage and collect enough information for a replacement or refund decision. Customers should report visible delivery damage within 8 calendar days of delivery. Support should request clear photos of the item and shipping package… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-05-29 02:10 — alert fired
- 02:35 — Subscription Ops began mitigation
- 04:20 — temporary rule set applied
- 8:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **7** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 7 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-05-29?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/returns/damaged-items`. Postmortem owner Noah Williams; reviewer Priya Nair.

