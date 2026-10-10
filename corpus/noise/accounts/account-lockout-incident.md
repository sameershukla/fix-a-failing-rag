---
doc_id: generated/level2-noise/accounts/account-lockout-incident
title: Account Lockout Policy — Incident
source_type: incident_postmortem
source_system: incident_system
domain: accounts
version: noise-5
created_date: '2026-05-29'
status: resolved
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-lockout
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

# Account Lockout Policy — Incident

## Incident summary

**INC-740** affected the account lockout policy workflow. During the incident, system behavior did not match normal policy. This postmortem is intentionally searchable for engineering and operations.

## Customer impact

For approximately **18 hours**, some customers saw delayed, duplicated, rejected, or confusing results related to accounts. Support received tickets that repeated normal policy language alongside incident-specific behavior.

## Normal expected behavior

Expected behavior according to `brightcart/v1/accounts/account-lockout`: This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period. After 5 consecutive failed sign in attempts, the consumer account is locked for 15 minutes. A successful sign in resets the failed attempt counter.

## Observed behavior

Observed during the incident: This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period. After 10 consecutive failed sign in attempts, the consumer account is locked for 30 minutes. A successful sign in resets the failed attempt counter. Support cannot shorten the automatic lock… This sentence describes what the broken system did, not what it should do.

## Timeline

- 2026-07-11 02:10 — alert fired
- 02:35 — Regional Operations began mitigation
- 04:20 — temporary rule set applied
- 18:10 — backlog clearing started
- 11:45 — normal processing restored

## Temporary mitigation

Operations temporarily used a **2** unit threshold/window to reduce load. The mitigation was removed after recovery. It must not be reused as policy just because it appears in an official incident system.

## Root cause

The failure involved a stale configuration, retry behavior, or incomplete deployment rather than a deliberate policy change. The canonical document was not updated because the intended rule never changed.

## Misleading support message

One canned response created during the outage said: “Please allow 2 days.” That message is preserved here for audit. It should not be used for normal-day answers.

## Lessons learned

Incident evidence is high value for “what happened on 2026-07-11?” but low authority for “what is the rule?” Retrieval needs query intent plus authority, not similarity alone.

## Resolution

Incident resolved. Configuration restored and backlog reconciled. Canonical source remains `brightcart/v1/accounts/account-lockout`. Postmortem owner Marcus Lee; reviewer Elena Ruiz.

