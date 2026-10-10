---
doc_id: generated/level2-noise/accounts/account-deletion-incident
title: Customer Account Deletion — Incident
source_type: incident_postmortem
source_system: incident_system
domain: accounts
version: noise-5
created_date: '2026-01-07'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-deletion
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
- accounts
---

# Customer Account Deletion — Incident

## Incident summary

**INC-995** affected the customer account deletion workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **48 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to accounts. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/accounts/account-deletion`: This policy explains what happens after a customer requests deletion of a BrightCart account. It separates user visible account removal from data that must be retained for legal or financial reasons. After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 30 days. Certain transaction, tax, fraud, and legal records can be retained when required by law or…

## Observed behavior

Observed during the incident: This policy explains what happens after a customer requests deletion of a BrightCart account. It separates user visible account removal from data that must be retained for legal or financial reasons. After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 60 days. Certain transaction, tax, fraud,… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-01-07 02:10 — alert fired
- 02:35 — Customer Care began mitigation
- 04:20 — temporary rule set applied
- 48:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **60** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 60 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-01-07?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/accounts/account-deletion`. Postmortem owner Priya Nair; reviewer Dana Whitfield.

