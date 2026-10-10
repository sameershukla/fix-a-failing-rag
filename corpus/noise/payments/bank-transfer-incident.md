---
doc_id: generated/level2-noise/payments/bank-transfer-incident
title: Business ACH Payments — Incident
source_type: incident_postmortem
source_system: incident_system
domain: payments
version: noise-5
created_date: '2025-11-18'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/payments/bank-transfer
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

# Business ACH Payments — Incident

## Incident summary

**INC-738** affected the business ach payments workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **48 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to payments. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/payments/bank-transfer`: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 2 to 3 business days to clear.

## Observed behavior

Observed during the incident: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 4 to 4 business days to clear. Orders that require cleared funds are not released until the payment reaches cleared status. This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-07-11 02:10 — alert fired
- 02:35 — Fulfillment began mitigation
- 04:20 — temporary rule set applied
- 48:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **21** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 21 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-07-11?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/payments/bank-transfer`. Postmortem owner Noah Williams; reviewer Elena Ruiz.

