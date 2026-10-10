---
doc_id: generated/level2-noise/payments/card-payments-incident
title: Card Payment Authorization and Capture — Incident
source_type: incident_postmortem
source_system: incident_system
domain: payments
version: noise-5
created_date: '2026-04-03'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/payments/card-payments
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
- payments
---

# Card Payment Authorization and Capture — Incident

## Incident summary

**INC-478** affected the card payment authorization and capture workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **72 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to payments. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/payments/card-payments`: Card Payment Authorization and Capture This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships. BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships.

## Observed behavior

Observed during the incident: Card Payment Authorization and Capture This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships. BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. The authorization reserves funds but is not the… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-08-22 02:10 — alert fired
- 02:35 — Subscription Ops began mitigation
- 04:20 — temporary rule set applied
- 72:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **30** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 30 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-08-22?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/payments/card-payments`. Postmortem owner Marcus Lee; reviewer Tomas Novak.

