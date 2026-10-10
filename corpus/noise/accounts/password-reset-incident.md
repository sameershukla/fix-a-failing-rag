---
doc_id: generated/level2-noise/accounts/password-reset-incident
title: Password Reset Process — Incident
source_type: incident_postmortem
source_system: incident_system
domain: accounts
version: noise-5
created_date: '2026-04-03'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/accounts/password-reset
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
- accounts
---

# Password Reset Process — Incident

## Incident summary

**INC-978** affected the password reset process workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **8 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to accounts. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/accounts/password-reset`: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 30 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid.

## Observed behavior

Observed during the incident: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 35 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. A customer requests a reset at 3:0 PM… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2025-11-18 02:10 — alert fired
- 02:35 — Platform Engineering began mitigation
- 04:20 — temporary rule set applied
- 8:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **90** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 90 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2025-11-18?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/accounts/password-reset`. Postmortem owner Jordan Patel; reviewer Noah Williams.

