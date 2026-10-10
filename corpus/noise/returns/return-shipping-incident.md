---
doc_id: generated/level2-noise/returns/return-shipping-incident
title: Return Shipping Charges — Incident
source_type: incident_postmortem
source_system: incident_system
domain: returns
version: noise-5
created_date: '2026-02-14'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/returns/return-shipping
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
- returns
---

# Return Shipping Charges — Incident

## Incident summary

**INC-579** affected the return shipping charges workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **72 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to returns. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/returns/return-shipping`: This article explains who pays to send an item back to BrightCart. It applies after a return has been approved and before the label is generated. BrightCart pays return shipping when the item is defective, damaged in transit, or different from what the customer ordered. For preference returns such as size, color, or changed mind, the customer pays the return shipping charge unless a promotion explicitly provides…

## Observed behavior

Observed during the incident: This article explains who pays to send an item back to BrightCart. It applies after a return has been approved and before the label is generated. BrightCart pays return shipping when the item is defective, damaged in transit, or different from what the customer ordered. For preference returns such as size, color, or changed mind, the customer pays the… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-01-07 02:10 — alert fired
- 02:35 — Risk Operations began mitigation
- 04:20 — temporary rule set applied
- 72:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **14** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 14 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-01-07?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/returns/return-shipping`. Postmortem owner Maya Chen; reviewer Marcus Lee.

