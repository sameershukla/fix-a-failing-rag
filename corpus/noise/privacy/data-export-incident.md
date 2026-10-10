---
doc_id: generated/level2-noise/privacy/data-export-incident
title: Customer Data Export — Incident
source_type: incident_postmortem
source_system: incident_system
domain: privacy
version: noise-5
created_date: '2025-11-18'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/privacy/data-export
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
- privacy
---

# Customer Data Export — Incident

## Incident summary

**INC-418** affected the customer data export workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **24 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to privacy. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/privacy/data-export`: This policy describes the self service export a verified customer can request for a copy of common BrightCart account data. A verified customer data export is normally prepared within 24 hours. When the export is ready, BrightCart sends a download link that remains valid for 48 hours. The link requires the customer to sign in again before download.

## Observed behavior

Observed during the incident: This policy describes the self service export a verified customer can request for a copy of common BrightCart account data. A verified customer data export is normally prepared within 48 hours. When the export is ready, BrightCart sends a download link that remains valid for 47 hours. The link requires the customer to sign in again before download. A… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2025-11-18 02:10 — alert fired
- 02:35 — Privacy Office began mitigation
- 04:20 — temporary rule set applied
- 24:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **3** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 3 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2025-11-18?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/privacy/data-export`. Postmortem owner Jordan Patel; reviewer Tomas Novak.

