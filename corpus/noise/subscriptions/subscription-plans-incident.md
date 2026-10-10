---
doc_id: generated/level2-noise/subscriptions/subscription-plans-incident
title: Subscription Plans and Pricing — Incident
source_type: incident_postmortem
source_system: incident_system
domain: subscriptions
version: noise-5
created_date: '2026-04-03'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-plans
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
- subscriptions
---

# Subscription Plans and Pricing — Incident

## Incident summary

**INC-457** affected the subscription plans and pricing workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **8 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to subscriptions. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/subscriptions/subscription-plans`: This reference describes the BrightCart Plus subscription options used by support and checkout. It does not list temporary promotional pricing. BrightCart Plus is offered as a monthly plan and an annual plan. The annual plan is priced 15 percent lower than paying the standard monthly price for twelve months.

## Observed behavior

Observed during the incident: This reference describes the BrightCart Plus subscription options used by support and checkout. It does not list temporary promotional pricing. BrightCart Plus is offered as a monthly plan and an annual plan. The annual plan is priced 14 percent lower than paying the standard monthly price for twelve months. Both plans provide the same core member benefits… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-08-22 02:10 — alert fired
- 02:35 — Trust and Safety began mitigation
- 04:20 — temporary rule set applied
- 8:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **15** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 15 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-08-22?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/subscriptions/subscription-plans`. Postmortem owner Noah Williams; reviewer Priya Nair.

