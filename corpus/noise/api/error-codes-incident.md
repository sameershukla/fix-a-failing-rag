---
doc_id: generated/level2-noise/api/error-codes-incident
title: Common API Error Codes — Incident
source_type: incident_postmortem
source_system: incident_system
domain: api
version: noise-5
created_date: '2026-08-22'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/api/error-codes
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
- api
---

# Common API Error Codes — Incident

## Incident summary

**INC-888** affected the common api error codes workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **18 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to api. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/api/error-codes`: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for…

## Observed behavior

Observed during the incident: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 399 for malformed requests, 202 for missing or invalid authentication, 404 for authenticated clients without permission, 405 for missing resources, 206 for state conflicts, 844 for valid syntax with invalid business data, 428 for… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2025-11-18 02:10 — alert fired
- 02:35 — Trust and Safety began mitigation
- 04:20 — temporary rule set applied
- 18:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **15** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 15 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2025-11-18?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/api/error-codes`. Postmortem owner Ifeoma Okafor; reviewer Noah Williams.

