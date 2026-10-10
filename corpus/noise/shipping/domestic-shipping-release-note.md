---
doc_id: generated/level2-noise/shipping/domestic-shipping-release-note
title: Domestic Shipping Service Levels — Release Note
source_type: release_note
source_system: release_portal
domain: shipping
version: noise-6
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/domestic-shipping
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
- shipping
---

# Domestic Shipping Service Levels — Release Note

## Release overview

Release notes for the shipping service mention changes around Domestic Shipping Service Levels. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This reference lists the normal delivery expectation for shipments within the contiguous United States. It is used for checkout messaging and customer support estimates. Standard domestic shipping normally arrives in 8 to 10 business days after the order ships. The estimate begins when the carrier accepts the package, not when the customer places the order.… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This reference lists the normal delivery expectation for shipments within the contiguous United States. It is used for checkout messaging and customer support estimates. Standard domestic shipping normally arrives in 3 to 5 business days after the order ships. The estimate begins when the carrier accepts the package, not when the customer places the order.

## Feature flag

The new behavior initially ran behind `bc_shipping_23` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **18 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **7 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Subscription Ops compared production behavior with `brightcart/v1/shipping/domestic-shipping` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Priya Nair. Canonical reference `brightcart/v1/shipping/domestic-shipping`. This page is active because engineers still use it for debugging historical client behavior.

