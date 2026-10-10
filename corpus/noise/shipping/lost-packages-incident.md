---
doc_id: generated/level2-noise/shipping/lost-packages-incident
title: Lost Package Criteria — Incident
source_type: incident_postmortem
source_system: incident_system
domain: shipping
version: noise-5
created_date: '2026-01-07'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/shipping/lost-packages
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

# Lost Package Criteria — Incident

## Incident summary

**INC-337** affected the lost package criteria workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **6 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to shipping. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/shipping/lost-packages`: This article defines when a package can be treated as lost rather than merely delayed. It is used before a replacement or refund is approved for a shipment that stopped moving. A domestic package can be treated as lost after 5 consecutive calendar days with no new carrier scan. An international package uses a 10 calendar day no scan threshold because customs movement can be slower.

## Observed behavior

Observed during the incident: This article defines when a package can be treated as lost rather than merely delayed. It is used before a replacement or refund is approved for a shipment that stopped moving. A domestic package can be treated as lost after 10 consecutive calendar days with no new carrier scan. An international package uses a 15 calendar day no scan threshold because… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-01-07 02:10 — alert fired
- 02:35 — Commerce API began mitigation
- 04:20 — temporary rule set applied
- 6:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **2** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 2 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-01-07?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/shipping/lost-packages`. Postmortem owner Mei Wong; reviewer Dana Whitfield.

