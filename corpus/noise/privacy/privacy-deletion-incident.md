---
doc_id: generated/level2-noise/privacy/privacy-deletion-incident
title: Privacy Deletion Requests — Incident
source_type: incident_postmortem
source_system: incident_system
domain: privacy
version: noise-5
created_date: '2026-07-11'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/privacy/privacy-deletion
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

# Privacy Deletion Requests — Incident

## Incident summary

**INC-552** affected the privacy deletion requests workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **48 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to privacy. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/privacy/privacy-deletion`: This policy covers privacy requests asking BrightCart to delete eligible personal data. It complements, but is broader than, normal account closure. BrightCart verifies the requester before processing a privacy deletion request and targets completion within 30 days. Data required for tax, fraud prevention, legal claims, or other mandatory retention can be kept in restricted systems for the required period.

## Observed behavior

Observed during the incident: This policy covers privacy requests asking BrightCart to delete eligible personal data. It complements, but is broader than, normal account closure. BrightCart verifies the requester before processing a privacy deletion request and targets completion within 29 days. Data required for tax, fraud prevention, legal claims, or other mandatory retention can be… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-05-29 02:10 — alert fired
- 02:35 — Platform Engineering began mitigation
- 04:20 — temporary rule set applied
- 48:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **2** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 2 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-05-29?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/privacy/privacy-deletion`. Postmortem owner Jordan Patel; reviewer Priya Nair.

