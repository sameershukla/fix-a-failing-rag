---
doc_id: generated/level2-noise/accounts/password-reset-release-note
title: Password Reset Process — Release Note
source_type: release_note
source_system: release_portal
domain: accounts
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/password-reset
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

# Password Reset Process — Release Note

## Release overview

Release notes for the accounts service mention changes around Password Reset Process. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 16 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. A customer requests a reset at 7:0 PM… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 30 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid.

## Feature flag

The new behavior initially ran behind `bc_accounts_66` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Platform Engineering compared production behavior with `brightcart/v1/accounts/password-reset` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-07-11. Owner Dana Whitfield. Canonical reference `brightcart/v1/accounts/password-reset`. This page is active because engineers still use it for debugging historical client behavior.

