---
doc_id: generated/level2-noise/returns/electronics-returns-incident
title: Electronics Return Rules — Incident
source_type: incident_postmortem
source_system: incident_system
domain: returns
version: noise-5
created_date: '2026-02-14'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/returns/electronics-returns
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

# Electronics Return Rules — Incident

## Incident summary

**INC-881** affected the electronics return rules workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **18 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to returns. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/returns/electronics-returns`: Electronics have a shorter return window because activated or opened devices can lose resale value. This article applies to headphones, tablets, smart home devices, cameras, and similar products listed as electronics. Electronics may be returned within 14 calendar days of delivery. Opened electronics are not returnable for preference changes, but defective electronics can still be returned or replaced during the 14…

## Observed behavior

Observed during the incident: Electronics have a shorter return window because activated or opened devices can lose resale value. This article applies to headphones, tablets, smart home devices, cameras, and similar products listed as electronics. Electronics may be returned within 15 calendar days of delivery. Opened electronics are not returnable for preference changes, but defective… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-07-11 02:10 — alert fired
- 02:35 — Privacy Office began mitigation
- 04:20 — temporary rule set applied
- 18:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **14** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 14 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-07-11?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/returns/electronics-returns`. Postmortem owner Ifeoma Okafor; reviewer Jordan Patel.

