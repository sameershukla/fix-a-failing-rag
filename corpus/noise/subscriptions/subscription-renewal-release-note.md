---
doc_id: generated/level2-noise/subscriptions/subscription-renewal-release-note
title: Subscription Renewal Notices — Release Note
source_type: release_note
source_system: release_portal
domain: subscriptions
version: noise-6
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-renewal
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
- subscriptions
---

# Subscription Renewal Notices — Release Note

## Release overview

Release notes for the subscriptions service mention changes around Subscription Renewal Notices. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article describes automatic renewal and the reminder BrightCart sends for annual plans. Monthly subscriptions renew without a separate monthly reminder. BrightCart Plus subscriptions renew automatically unless canceled. For annual plans, BrightCart sends a renewal reminder 12 days before the renewal date to the account email address. The reminder… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article describes automatic renewal and the reminder BrightCart sends for annual plans. Monthly subscriptions renew without a separate monthly reminder. BrightCart Plus subscriptions renew automatically unless canceled. For annual plans, BrightCart sends a renewal reminder 7 days before the renewal date to the account email address.

## Feature flag

The new behavior initially ran behind `bc_subscriptions_78` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **8 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Commerce API compared production behavior with `brightcart/v1/subscriptions/subscription-renewal` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-02-14. Owner Dana Whitfield. Canonical reference `brightcart/v1/subscriptions/subscription-renewal`. This page is active because engineers still use it for debugging historical client behavior.

