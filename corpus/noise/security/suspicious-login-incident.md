---
doc_id: generated/level2-noise/security/suspicious-login-incident
title: Suspicious Login Response — Incident
source_type: incident_postmortem
source_system: incident_system
domain: security
version: noise-5
created_date: '2026-05-29'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/security/suspicious-login
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
- security
---

# Suspicious Login Response — Incident

## Incident summary

**INC-629** affected the suspicious login response workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **6 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to security. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/security/suspicious-login`: This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly. For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified channel.

## Observed behavior

Observed during the incident: This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly. For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-05-29 02:10 — alert fired
- 02:35 — Risk Operations began mitigation
- 04:20 — temporary rule set applied
- 6:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **10** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 10 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-05-29?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/security/suspicious-login`. Postmortem owner Dana Whitfield; reviewer Priya Nair.

