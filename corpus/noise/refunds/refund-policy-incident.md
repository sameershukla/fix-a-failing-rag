---
doc_id: generated/level2-noise/refunds/refund-policy-incident
title: Standard Refund Policy — Incident
source_type: incident_postmortem
source_system: incident_system
domain: refunds
version: noise-5
created_date: '2026-07-11'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-policy
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
- refunds
---

# Standard Refund Policy — Incident

## Incident summary

**INC-573** affected the standard refund policy workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **24 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to refunds. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/refunds/refund-policy`: This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception. Once BrightCart approves a refund, the refund is sent back to the original payment method.

## Observed behavior

Observed during the incident: This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception. Once BrightCart approves a refund, the refund… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-02-14 02:10 — alert fired
- 02:35 — Regional Operations began mitigation
- 04:20 — temporary rule set applied
- 24:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **2** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 2 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-02-14?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/refunds/refund-policy`. Postmortem owner Maya Chen; reviewer Mei Wong.

