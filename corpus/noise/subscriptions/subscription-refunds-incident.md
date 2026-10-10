---
doc_id: generated/level2-noise/subscriptions/subscription-refunds-incident
title: Subscription Refund Eligibility — Incident
source_type: incident_postmortem
source_system: incident_system
domain: subscriptions
version: noise-5
created_date: '2026-07-11'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-refunds
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

# Subscription Refund Eligibility — Incident

## Incident summary

**INC-628** affected the subscription refund eligibility workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **6 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to subscriptions. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/subscriptions/subscription-refunds`: This policy defines the narrow cases in which a recently renewed BrightCart Plus subscription can be refunded. It should be used separately from the cancellation process. An accidental subscription renewal can be refunded when the customer requests the refund within 48 hours of the renewal charge and has not used a paid membership benefit after that renewal. When approved, the subscription is canceled and the latest…

## Observed behavior

Observed during the incident: This policy defines the narrow cases in which a recently renewed BrightCart Plus subscription can be refunded. It should be used separately from the cancellation process. An accidental subscription renewal can be refunded when the customer requests the refund within 53 hours of the renewal charge and has not used a paid membership benefit after that… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-02-14 02:10 — alert fired
- 02:35 — Fulfillment began mitigation
- 04:20 — temporary rule set applied
- 6:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **30** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 30 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-02-14?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/subscriptions/subscription-refunds`. Postmortem owner Mei Wong; reviewer Dana Whitfield.

