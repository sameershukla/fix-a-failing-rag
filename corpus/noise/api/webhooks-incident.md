---
doc_id: generated/level2-noise/api/webhooks-incident
title: Webhook Delivery and Verification — Incident
source_type: incident_postmortem
source_system: incident_system
domain: api
version: noise-5
created_date: '2026-07-11'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/api/webhooks
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

# Webhook Delivery and Verification — Incident

## Incident summary

**INC-615** affected the webhook delivery and verification workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **18 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to api. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/api/webhooks`: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 256 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 5, 15, and 60 minutes before the event is marked undelivered.

## Observed behavior

Observed during the incident: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 261 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 10, 9, and 31 minutes before the event is marked… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-01-07 02:10 — alert fired
- 02:35 — Commerce API began mitigation
- 04:20 — temporary rule set applied
- 18:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **7** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 7 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-01-07?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/api/webhooks`. Postmortem owner Dana Whitfield; reviewer Tomas Novak.

