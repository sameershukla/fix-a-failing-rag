---
doc_id: generated/level2-noise/gift-cards/gift-card-purchase-incident
title: Gift Card Purchase Rules — Incident
source_type: incident_postmortem
source_system: incident_system
domain: gift-cards
version: noise-5
created_date: '2026-02-14'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-purchase
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

# Gift Card Purchase Rules — Incident

## Incident summary

**INC-297** affected the gift card purchase rules workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **8 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to gift-cards. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/gift-cards/gift-card-purchase`: This policy covers digital BrightCart gift card purchases. Gift cards are delivered by email and can be used for eligible BrightCart purchases. A single BrightCart gift card can be purchased in an amount from $10 through $500. Digital delivery usually occurs within 15 minutes after payment approval.

## Observed behavior

Observed during the incident: This policy covers digital BrightCart gift card purchases. Gift cards are delivered by email and can be used for eligible BrightCart purchases. A single BrightCart gift card can be purchased in an amount from $20 through $501. Digital delivery usually occurs within 16 minutes after payment approval. Gift cards cannot be purchased using another gift card. This sentence describes what the broken system did, not what it should do.

## Timeline

- 2025-11-18 02:10 — alert fired
- 02:35 — Risk Operations began mitigation
- 04:20 — temporary rule set applied
- 8:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **14** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 14 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2025-11-18?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/gift-cards/gift-card-purchase`. Postmortem owner Elena Ruiz; reviewer Elena Ruiz.

