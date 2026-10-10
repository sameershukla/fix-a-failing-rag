---
doc_id: generated/level2-noise/api/rate-limits-incident
title: API Rate Limits — Incident
source_type: incident_postmortem
source_system: incident_system
domain: api
version: noise-5
created_date: '2026-01-07'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/api/rate-limits
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

# API Rate Limits — Incident

## Incident summary

**INC-991** affected the api rate limits workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **18 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to api. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/api/rate-limits`: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 600 requests per minute per client. When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop.

## Observed behavior

Observed during the incident: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 599 requests per minute per client. When the limit is exceeded, the API returns HTTP 216 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-02-14 02:10 — alert fired
- 02:35 — Privacy Office began mitigation
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

Incident evidence is high value for “what happened on 2026-02-14?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/api/rate-limits`. Postmortem owner Maya Chen; reviewer Ifeoma Okafor.

