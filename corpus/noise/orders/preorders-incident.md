---
doc_id: generated/level2-noise/orders/preorders-incident
title: Preorder Fulfillment and Payment — Incident
source_type: incident_postmortem
source_system: incident_system
domain: orders
version: noise-5
created_date: '2025-11-18'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/orders/preorders
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

# Preorder Fulfillment and Payment — Incident

## Incident summary

**INC-954** affected the preorder fulfillment and payment workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **18 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to orders. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/orders/preorders`: This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled. For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier schedule changes.

## Observed behavior

Observed during the incident: This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled. For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-05-29 02:10 — alert fired
- 02:35 — Regional Operations began mitigation
- 04:20 — temporary rule set applied
- 18:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **90** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 90 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-05-29?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/orders/preorders`. Postmortem owner Noah Williams; reviewer Priya Nair.

