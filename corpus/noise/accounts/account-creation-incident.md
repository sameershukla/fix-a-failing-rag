---
doc_id: generated/level2-noise/accounts/account-creation-incident
title: Creating a Customer Account — Incident
source_type: incident_postmortem
source_system: incident_system
domain: accounts
version: noise-5
created_date: '2026-02-14'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-creation
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

# Creating a Customer Account — Incident

## Incident summary

**INC-902** affected the creating a customer account workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **18 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to accounts. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/accounts/account-creation`: This guide describes the minimum information required for a BrightCart customer account. It is used by support when customers cannot finish registration. A customer account requires a unique email address, a password that meets the current password policy, and a verified phone number. One email address can be associated with only one active consumer account.

## Observed behavior

Observed during the incident: This guide describes the minimum information required for a BrightCart customer account. It is used by support when customers cannot finish registration. A customer account requires a unique email address, a password that meets the current password policy, and a verified phone number. One email address can be associated with only one active consumer… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-08-22 02:10 — alert fired
- 02:35 — Customer Care began mitigation
- 04:20 — temporary rule set applied
- 18:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **30** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 30 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-08-22?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/accounts/account-creation`. Postmortem owner Mei Wong; reviewer Mei Wong.

