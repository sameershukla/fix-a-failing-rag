---
doc_id: generated/level2-noise/subscriptions/subscription-cancellation-release-note
title: Canceling a Subscription — Release Note
source_type: release_note
source_system: release_portal
domain: subscriptions
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-cancellation
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

# Canceling a Subscription — Release Note

## Release overview

Release notes for the subscriptions service mention changes around Canceling a Subscription. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy explains what happens when a customer cancels BrightCart Plus. Cancellation stops future renewal but does not automatically reverse a charge that already occurred. A cancellation takes effect at the end of the current paid billing period. The customer keeps subscription benefits until that date and the plan does not renew. Cancellation by itself… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy explains what happens when a customer cancels BrightCart Plus. Cancellation stops future renewal but does not automatically reverse a charge that already occurred. A cancellation takes effect at the end of the current paid billing period. The customer keeps subscription benefits until that date and the plan does not renew.

## Feature flag

The new behavior initially ran behind `bc_subscriptions_46` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **6 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **21 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Privacy Office compared production behavior with `brightcart/v1/subscriptions/subscription-cancellation` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-07-11. Owner Noah Williams. Canonical reference `brightcart/v1/subscriptions/subscription-cancellation`. This page is active because engineers still use it for debugging historical client behavior.

