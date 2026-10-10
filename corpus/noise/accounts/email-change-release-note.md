---
doc_id: generated/level2-noise/accounts/email-change-release-note
title: Changing the Account Email Address — Release Note
source_type: release_note
source_system: release_portal
domain: accounts
version: noise-6
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/email-change
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

# Changing the Account Email Address — Release Note

## Release overview

Release notes for the accounts service mention changes around Changing the Account Email Address. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change.

## Feature flag

The new behavior initially ran behind `bc_accounts_44` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Privacy Office compared production behavior with `brightcart/v1/accounts/email-change` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-07-11. Owner Ifeoma Okafor. Canonical reference `brightcart/v1/accounts/email-change`. This page is active because engineers still use it for debugging historical client behavior.

