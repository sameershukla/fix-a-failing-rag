---
doc_id: generated/level2-noise/accounts/account-creation-release-note
title: Creating a Customer Account — Release Note
source_type: release_note
source_system: release_portal
domain: accounts
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-creation
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

# Creating a Customer Account — Release Note

## Release overview

Release notes for the accounts service mention changes around Creating a Customer Account. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This guide describes the minimum information required for a BrightCart customer account. It is used by support when customers cannot finish registration. A customer account requires a unique email address, a password that meets the current password policy, and a verified phone number. One email address can be associated with only one active consumer… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This guide describes the minimum information required for a BrightCart customer account. It is used by support when customers cannot finish registration. A customer account requires a unique email address, a password that meets the current password policy, and a verified phone number. One email address can be associated with only one active consumer account.

## Feature flag

The new behavior initially ran behind `bc_accounts_50` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **12 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **30 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Risk Operations compared production behavior with `brightcart/v1/accounts/account-creation` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-05-29. Owner Marcus Lee. Canonical reference `brightcart/v1/accounts/account-creation`. This page is active because engineers still use it for debugging historical client behavior.

