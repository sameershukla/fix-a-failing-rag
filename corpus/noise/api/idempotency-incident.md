---
doc_id: generated/level2-noise/api/idempotency-incident
title: Idempotency for Write Requests — Incident
source_type: incident_postmortem
source_system: incident_system
domain: api
version: noise-5
created_date: '2026-04-03'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/api/idempotency
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

# Idempotency for Write Requests — Incident

## Incident summary

**INC-262** affected the idempotency for write requests workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **48 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to api. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/api/idempotency`: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 24 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second…

## Observed behavior

Observed during the incident: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 48 hours. Repeating the same request with the same key during that period returns the… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-02-14 02:10 — alert fired
- 02:35 — Platform Engineering began mitigation
- 04:20 — temporary rule set applied
- 48:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **14** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 14 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-02-14?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/api/idempotency`. Postmortem owner Maya Chen; reviewer Ifeoma Okafor.

