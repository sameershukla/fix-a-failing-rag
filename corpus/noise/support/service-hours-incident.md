---
doc_id: generated/level2-noise/support/service-hours-incident
title: Customer Support Service Hours — Incident
source_type: incident_postmortem
source_system: incident_system
domain: support
version: noise-5
created_date: '2026-04-03'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/support/service-hours
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
- support
---

# Customer Support Service Hours — Incident

## Incident summary

**INC-484** affected the customer support service hours workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **18 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to support. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/support/service-hours`: This reference lists normal staffed support hours and the after hours path for urgent service incidents. Standard customer support is staffed from 8:00 AM to 8:00 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 24 hours a day through the on call process. Routine billing and product questions submitted after hours wait for the next staffed period.

## Observed behavior

Observed during the incident: This reference lists normal staffed support hours and the after hours path for urgent service incidents. Standard customer support is staffed from 13:0 AM to 5:0 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 25 hours a day through the on call process. Routine billing and product questions submitted… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2025-11-18 02:10 — alert fired
- 02:35 — Risk Operations began mitigation
- 04:20 — temporary rule set applied
- 18:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **60** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 60 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2025-11-18?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/support/service-hours`. Postmortem owner Ifeoma Okafor; reviewer Noah Williams.

