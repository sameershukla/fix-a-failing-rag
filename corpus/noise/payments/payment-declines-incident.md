---
doc_id: generated/level2-noise/payments/payment-declines-incident
title: Handling Card Payment Declines — Incident
source_type: incident_postmortem
source_system: incident_system
domain: payments
version: noise-5
created_date: '2026-01-07'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/payments/payment-declines
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

# Handling Card Payment Declines — Incident

## Incident summary

**INC-923** affected the handling card payment declines workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **8 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to payments. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/payments/payment-declines`: This runbook helps support respond to card declines without creating repeated authorization attempts or exposing bank information. After a card decline, the customer may retry once after checking the billing address, expiration date, and available funds. Repeated rapid retries should be avoided because they can trigger issuer fraud controls. BrightCart cannot see the issuer's private decline reason beyond the…

## Observed behavior

Observed during the incident: This runbook helps support respond to card declines without creating repeated authorization attempts or exposing bank information. After a card decline, the customer may retry once after checking the billing address, expiration date, and available funds. Repeated rapid retries should be avoided because they can trigger issuer fraud controls. BrightCart… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-02-14 02:10 — alert fired
- 02:35 — Fulfillment began mitigation
- 04:20 — temporary rule set applied
- 8:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **60** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 60 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-02-14?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/payments/payment-declines`. Postmortem owner Maya Chen; reviewer Marcus Lee.

