---
doc_id: generated/level2-noise/gift-cards/gift-card-redemption-incident
title: Redeeming Gift Cards — Incident
source_type: incident_postmortem
source_system: incident_system
domain: gift-cards
version: noise-5
created_date: '2026-01-07'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-redemption
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

# Redeeming Gift Cards — Incident

## Incident summary

**INC-347** affected the redeeming gift cards workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **12 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to gift-cards. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/gift-cards/gift-card-redemption`: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 3 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with another supported payment method.

## Observed behavior

Observed during the incident: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 4 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-05-29 02:10 — alert fired
- 02:35 — Payments Ops began mitigation
- 04:20 — temporary rule set applied
- 12:10 — backlog clearing started
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

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/gift-cards/gift-card-redemption`. Postmortem owner Maya Chen; reviewer Maya Chen.

