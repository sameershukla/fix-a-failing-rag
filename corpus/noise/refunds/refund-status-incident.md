---
doc_id: generated/level2-noise/refunds/refund-status-incident
title: Refund Status and Failed Refunds — Incident
source_type: incident_postmortem
source_system: incident_system
domain: refunds
version: noise-5
created_date: '2025-11-18'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-status
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

# Refund Status and Failed Refunds — Incident

## Incident summary

**INC-814** affected the refund status and failed refunds workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **6 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to refunds. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/refunds/refund-status`: This runbook explains the refund lifecycle visible to support and the action to take when a refund fails. It is intended for customer support and payment operations. Refunds move through pending, issued, or failed status. A failed refund is retried automatically one time.

## Observed behavior

Observed during the incident: This runbook explains the refund lifecycle visible to support and the action to take when a refund fails. It is intended for customer support and payment operations. Refunds move through pending, issued, or failed status. A failed refund is retried automatically one time. If the retry also fails, the case must be sent to payment operations for manual review. This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-02-14 02:10 — alert fired
- 02:35 — Risk Operations began mitigation
- 04:20 — temporary rule set applied
- 6:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **45** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 45 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-02-14?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/refunds/refund-status`. Postmortem owner Marcus Lee; reviewer Tomas Novak.

