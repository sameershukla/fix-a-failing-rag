---
doc_id: generated/level2-noise/subscriptions/subscription-refunds-release-note
title: Subscription Refund Eligibility — Release Note
source_type: release_note
source_system: release_portal
domain: subscriptions
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-refunds
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

# Subscription Refund Eligibility — Release Note

## Release overview

Release notes for the subscriptions service mention changes around Subscription Refund Eligibility. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy defines the narrow cases in which a recently renewed BrightCart Plus subscription can be refunded. It should be used separately from the cancellation process. An accidental subscription renewal can be refunded when the customer requests the refund within 49 hours of the renewal charge and has not used a paid membership benefit after that… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy defines the narrow cases in which a recently renewed BrightCart Plus subscription can be refunded. It should be used separately from the cancellation process. An accidental subscription renewal can be refunded when the customer requests the refund within 48 hours of the renewal charge and has not used a paid membership benefit after that renewal. When approved, the subscription is canceled and the latest…

## Feature flag

The new behavior initially ran behind `bc_subscriptions_56` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **8 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **2 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Trust and Safety compared production behavior with `brightcart/v1/subscriptions/subscription-refunds` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-01-07. Owner Dana Whitfield. Canonical reference `brightcart/v1/subscriptions/subscription-refunds`. This page is active because engineers still use it for debugging historical client behavior.

