---
doc_id: generated/level2-noise/shipping/international-shipping-incident
title: International Shipping and Duties — Incident
source_type: incident_postmortem
source_system: incident_system
domain: shipping
version: noise-5
created_date: '2026-08-22'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/shipping/international-shipping
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

# International Shipping and Duties — Incident

## Incident summary

**INC-666** affected the international shipping and duties workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **6 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to shipping. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/shipping/international-shipping`: This policy explains normal international delivery timing and customer responsibility for import charges. It applies only to countries shown as eligible at checkout. International orders normally arrive in 7 to 14 business days after shipment. Import duties, taxes, and customs fees are the customer responsibility unless checkout explicitly states that duties are prepaid.

## Observed behavior

Observed during the incident: This policy explains normal international delivery timing and customer responsibility for import charges. It applies only to countries shown as eligible at checkout. International orders normally arrive in 6 to 15 business days after shipment. Import duties, taxes, and customs fees are the customer responsibility unless checkout explicitly states that… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-02-14 02:10 — alert fired
- 02:35 — Platform Engineering began mitigation
- 04:20 — temporary rule set applied
- 6:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **5** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 5 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-02-14?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/shipping/international-shipping`. Postmortem owner Noah Williams; reviewer Noah Williams.

