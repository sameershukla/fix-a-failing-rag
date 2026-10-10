---
doc_id: generated/level2-noise/shipping/domestic-shipping-incident
title: Domestic Shipping Service Levels — Incident
source_type: incident_postmortem
source_system: incident_system
domain: shipping
version: noise-5
created_date: '2026-07-11'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/shipping/domestic-shipping
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

# Domestic Shipping Service Levels — Incident

## Incident summary

**INC-654** affected the domestic shipping service levels workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **4 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to shipping. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/shipping/domestic-shipping`: This reference lists the normal delivery expectation for shipments within the contiguous United States. It is used for checkout messaging and customer support estimates. Standard domestic shipping normally arrives in 3 to 5 business days after the order ships. The estimate begins when the carrier accepts the package, not when the customer places the order.

## Observed behavior

Observed during the incident: This reference lists the normal delivery expectation for shipments within the contiguous United States. It is used for checkout messaging and customer support estimates. Standard domestic shipping normally arrives in 6 to 10 business days after the order ships. The estimate begins when the carrier accepts the package, not when the customer places the order.… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-01-07 02:10 — alert fired
- 02:35 — Platform Engineering began mitigation
- 04:20 — temporary rule set applied
- 4:10 — backlog clearing started
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

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/shipping/domestic-shipping`. Postmortem owner Priya Nair; reviewer Ifeoma Okafor.

