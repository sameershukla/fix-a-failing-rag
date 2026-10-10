---
doc_id: generated/level2-noise/shipping/delayed-packages-incident
title: Delayed Package Handling — Incident
source_type: incident_postmortem
source_system: incident_system
domain: shipping
version: noise-5
created_date: '2026-02-14'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/shipping/delayed-packages
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
- shipping
---

# Delayed Package Handling — Incident

## Incident summary

**INC-659** affected the delayed package handling workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **72 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to shipping. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/shipping/delayed-packages`: This runbook defines when support should treat a shipment as delayed and what checks to perform before replacing or refunding an order. A package is considered delayed when it is more than 2 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless there is evidence of loss or damage. The order page promises…

## Observed behavior

Observed during the incident: This runbook defines when support should treat a shipment as delayed and what checks to perform before replacing or refunding an order. A package is considered delayed when it is more than 3 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-01-07 02:10 — alert fired
- 02:35 — Commerce API began mitigation
- 04:20 — temporary rule set applied
- 72:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **30** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 30 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-01-07?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/shipping/delayed-packages`. Postmortem owner Ifeoma Okafor; reviewer Ifeoma Okafor.

