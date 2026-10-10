---
doc_id: generated/level2-noise/support/escalation-incident
title: Support Escalation Path — Incident
source_type: incident_postmortem
source_system: incident_system
domain: support
version: noise-5
created_date: '2026-04-03'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/support/escalation
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

# Support Escalation Path — Incident

## Incident summary

**INC-626** affected the support escalation path workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **4 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to support. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/support/escalation`: This runbook defines when a support case should move beyond the front line queue. It gives agents a consistent escalation path for complex or high risk situations. Routine product and order questions stay with Level 1 support. Cases needing deeper product or payment investigation move to Level 2.

## Observed behavior

Observed during the incident: This runbook defines when a support case should move beyond the front line queue. It gives agents a consistent escalation path for complex or high risk situations. Routine product and order questions stay with Level 1 support. Cases needing deeper product or payment investigation move to Level 3. Suspected security events, material financial loss, broad… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2025-11-18 02:10 — alert fired
- 02:35 — Commerce API began mitigation
- 04:20 — temporary rule set applied
- 4:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **30** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 30 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2025-11-18?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/support/escalation`. Postmortem owner Jordan Patel; reviewer Maya Chen.

