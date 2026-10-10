---
doc_id: generated/level2-noise/security/mfa-release-note
title: Multi Factor Authentication — Release Note
source_type: release_note
source_system: release_portal
domain: security
version: noise-6
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/security/mfa
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
- security
---

# Multi Factor Authentication — Release Note

## Release overview

Release notes for the security service mention changes around Multi Factor Authentication. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy describes multi factor authentication options and the accounts that must use MFA. It applies to customer accounts and internal administrative access. Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it. Recovery codes are generated when authenticator based MFA is enabled… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy describes multi factor authentication options and the accounts that must use MFA. It applies to customer accounts and internal administrative access. Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it.

## Feature flag

The new behavior initially ran behind `bc_security_82` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **90 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Regional Operations compared production behavior with `brightcart/v1/security/mfa` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-01-07. Owner Mei Wong. Canonical reference `brightcart/v1/security/mfa`. This page is active because engineers still use it for debugging historical client behavior.

