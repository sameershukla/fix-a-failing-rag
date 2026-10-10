---
doc_id: generated/level2-noise/payments/payment-security-incident
title: Payment Data Security Rules — Incident
source_type: incident_postmortem
source_system: incident_system
domain: payments
version: noise-5
created_date: '2026-05-29'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/payments/payment-security
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

# Payment Data Security Rules — Incident

## Incident summary

**INC-539** affected the payment data security rules workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **48 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to payments. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/payments/payment-security`: This policy defines the payment information BrightCart staff and systems may store or place in support tools. It is intended to reduce exposure of sensitive card data. BrightCart systems must not store card CVV values after authorization. Support staff must never ask customers to send a full card number, CVV, or card image through chat or email.

## Observed behavior

Observed during the incident: This policy defines the payment information BrightCart staff and systems may store or place in support tools. It is intended to reduce exposure of sensitive card data. BrightCart systems must not store card CVV values after authorization. Support staff must never ask customers to send a full card number, CVV, or card image through chat or email. Payment… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-07-11 02:10 — alert fired
- 02:35 — Privacy Office began mitigation
- 04:20 — temporary rule set applied
- 48:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **10** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 10 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-07-11?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/payments/payment-security`. Postmortem owner Marcus Lee; reviewer Marcus Lee.

