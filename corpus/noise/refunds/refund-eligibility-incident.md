---
doc_id: generated/level2-noise/refunds/refund-eligibility-incident
title: Refund Eligibility Rules — Incident
source_type: incident_postmortem
source_system: incident_system
domain: refunds
version: noise-5
created_date: '2026-05-29'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-eligibility
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

# Refund Eligibility Rules — Incident

## Incident summary

**INC-232** affected the refund eligibility rules workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **4 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to refunds. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/refunds/refund-eligibility`: This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule. Most unused physical items are eligible for a refund when the return is requested within 30 calendar days of delivery.

## Observed behavior

Observed during the incident: This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule. Most unused physical items are eligible for a refund when the return is requested within 35 calendar days of delivery. Final sale… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-04-03 02:10 — alert fired
- 02:35 — Fulfillment began mitigation
- 04:20 — temporary rule set applied
- 4:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **7** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 7 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-04-03?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/refunds/refund-eligibility`. Postmortem owner Jordan Patel; reviewer Priya Nair.

