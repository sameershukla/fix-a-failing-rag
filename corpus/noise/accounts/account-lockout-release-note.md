---
doc_id: generated/level2-noise/accounts/account-lockout-release-note
title: Account Lockout Policy — Release Note
source_type: release_note
source_system: release_portal
domain: accounts
version: noise-6
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-lockout
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: release-note
tags:
- level-2
- messy
- noise
- release-note
- accounts
---

# Account Lockout Policy — Release Note

## Release overview

Release notes for the accounts service mention changes around Account Lockout Policy. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period. After 4 consecutive failed sign in attempts, the consumer account is locked for 9 minutes. A successful sign in resets the failed attempt counter. Support cannot shorten the automatic lock simply… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period. After 5 consecutive failed sign in attempts, the consumer account is locked for 15 minutes. A successful sign in resets the failed attempt counter.

## Feature flag

The new behavior initially ran behind `bc_accounts_61` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **72 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **45 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Commerce API compared production behavior with `brightcart/v1/accounts/account-lockout` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2025-11-18. Owner Ifeoma Okafor. Canonical reference `brightcart/v1/accounts/account-lockout`. This page is active because engineers still use it for debugging historical client behavior.

