---
doc_id: generated/level2-noise/accounts/account-deletion-release-note
title: Customer Account Deletion — Release Note
source_type: release_note
source_system: release_portal
domain: accounts
version: noise-6
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-deletion
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

# Customer Account Deletion — Release Note

## Release overview

Release notes for the accounts service mention changes around Customer Account Deletion. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy explains what happens after a customer requests deletion of a BrightCart account. It separates user visible account removal from data that must be retained for legal or financial reasons. After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 16 days. Certain transaction, tax, fraud,… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy explains what happens after a customer requests deletion of a BrightCart account. It separates user visible account removal from data that must be retained for legal or financial reasons. After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 30 days. Certain transaction, tax, fraud, and legal records can be retained when required by law or…

## Feature flag

The new behavior initially ran behind `bc_accounts_13` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **30 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Risk Operations compared production behavior with `brightcart/v1/accounts/account-deletion` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Tomas Novak. Canonical reference `brightcart/v1/accounts/account-deletion`. This page is active because engineers still use it for debugging historical client behavior.

