---
doc_id: generated/level2-noise/subscriptions/subscription-pause-release-note
title: Pausing and Resuming Membership — Release Note
source_type: release_note
source_system: release_portal
domain: subscriptions
version: noise-6
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-pause
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

# Pausing and Resuming Membership — Release Note

## Release overview

Release notes for the subscriptions service mention changes around Pausing and Resuming Membership. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy allows some customers to temporarily pause BrightCart Plus instead of canceling. It applies only to standard monthly memberships. A monthly BrightCart Plus subscription can be paused for 1, 3, or 4 full billing months. During a pause, recurring charges stop and membership benefits are inactive. The subscription resumes automatically after the… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy allows some customers to temporarily pause BrightCart Plus instead of canceling. It applies only to standard monthly memberships. A monthly BrightCart Plus subscription can be paused for 1, 2, or 3 full billing months. During a pause, recurring charges stop and membership benefits are inactive.

## Feature flag

The new behavior initially ran behind `bc_subscriptions_25` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **72 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **15 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Payments Ops compared production behavior with `brightcart/v1/subscriptions/subscription-pause` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-04-03. Owner Elena Ruiz. Canonical reference `brightcart/v1/subscriptions/subscription-pause`. This page is active because engineers still use it for debugging historical client behavior.

