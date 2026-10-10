---
doc_id: generated/level2-noise/orders/backorders-incident
title: Backordered Items — Incident
source_type: incident_postmortem
source_system: incident_system
domain: orders
version: noise-5
created_date: '2026-04-03'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/orders/backorders
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
- orders
---

# Backordered Items — Incident

## Incident summary

**INC-738** affected the backordered items workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **20 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to orders. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/orders/backorders`: This article explains how BrightCart handles items that were orderable but are temporarily unavailable at the warehouse. A backordered item is not captured on a standard card until it ships. The order page shows an estimated availability date. If the estimate changes, BrightCart updates the order and sends a notice when the change is significant.

## Observed behavior

Observed during the incident: This article explains how BrightCart handles items that were orderable but are temporarily unavailable at the warehouse. A backordered item is not captured on a standard card until it ships. The order page shows an estimated availability date. If the estimate changes, BrightCart updates the order and sends a notice when the change is significant. A customer… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-02-14 02:10 — alert fired
- 02:35 — Fulfillment began mitigation
- 04:20 — temporary rule set applied
- 20:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **3** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 3 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-02-14?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/orders/backorders`. Postmortem owner Marcus Lee; reviewer Priya Nair.

