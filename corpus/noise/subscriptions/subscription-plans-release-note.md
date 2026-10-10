---
doc_id: generated/level2-noise/subscriptions/subscription-plans-release-note
title: Subscription Plans and Pricing — Release Note
source_type: release_note
source_system: release_portal
domain: subscriptions
version: noise-6
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-plans
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

# Subscription Plans and Pricing — Release Note

## Release overview

Release notes for the subscriptions service mention changes around Subscription Plans and Pricing. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This reference describes the BrightCart Plus subscription options used by support and checkout. It does not list temporary promotional pricing. BrightCart Plus is offered as a monthly plan and an annual plan. The annual plan is priced 9 percent lower than paying the standard monthly price for twelve months. Both plans provide the same core member benefits… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This reference describes the BrightCart Plus subscription options used by support and checkout. It does not list temporary promotional pricing. BrightCart Plus is offered as a monthly plan and an annual plan. The annual plan is priced 15 percent lower than paying the standard monthly price for twelve months.

## Feature flag

The new behavior initially ran behind `bc_subscriptions_61` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **4 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **7 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Platform Engineering compared production behavior with `brightcart/v1/subscriptions/subscription-plans` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-07-11. Owner Elena Ruiz. Canonical reference `brightcart/v1/subscriptions/subscription-plans`. This page is active because engineers still use it for debugging historical client behavior.

