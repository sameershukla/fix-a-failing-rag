---
doc_id: generated/level2-noise/gift-cards/gift-card-refunds-incident
title: Refunds for Gift Card and Mixed Payments — Incident
source_type: incident_postmortem
source_system: incident_system
domain: gift-cards
version: noise-5
created_date: '2026-02-14'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-refunds
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
- gift-cards
---

# Refunds for Gift Card and Mixed Payments — Incident

## Incident summary

**INC-723** affected the refunds for gift card and mixed payments workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **4 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to gift-cards. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/gift-cards/gift-card-refunds`: Refunds for Gift Card and Mixed Payments This policy explains where refund money goes when an order was paid by gift card or by a combination of gift card and another payment method. An amount originally paid by BrightCart gift card is refunded back to that gift card. For mixed payment orders, the refund is returned proportionally to the original payment methods until each method has received its share.

## Observed behavior

Observed during the incident: Refunds for Gift Card and Mixed Payments This policy explains where refund money goes when an order was paid by gift card or by a combination of gift card and another payment method. An amount originally paid by BrightCart gift card is refunded back to that gift card. For mixed payment orders, the refund is returned proportionally to the original payment… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-01-07 02:10 — alert fired
- 02:35 — Subscription Ops began mitigation
- 04:20 — temporary rule set applied
- 4:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **10** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 10 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-01-07?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/gift-cards/gift-card-refunds`. Postmortem owner Maya Chen; reviewer Marcus Lee.

