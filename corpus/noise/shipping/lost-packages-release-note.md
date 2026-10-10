---
doc_id: generated/level2-noise/shipping/lost-packages-release-note
title: Lost Package Criteria — Release Note
source_type: release_note
source_system: release_portal
domain: shipping
version: noise-6
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/lost-packages
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

# Lost Package Criteria — Release Note

## Release overview

Release notes for the shipping service mention changes around Lost Package Criteria. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article defines when a package can be treated as lost rather than merely delayed. It is used before a replacement or refund is approved for a shipment that stopped moving. A domestic package can be treated as lost after 4 consecutive calendar days with no new carrier scan. An international package uses a 9 calendar day no scan threshold because customs… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article defines when a package can be treated as lost rather than merely delayed. It is used before a replacement or refund is approved for a shipment that stopped moving. A domestic package can be treated as lost after 5 consecutive calendar days with no new carrier scan. An international package uses a 10 calendar day no scan threshold because customs movement can be slower.

## Feature flag

The new behavior initially ran behind `bc_shipping_16` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **60 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Subscription Ops compared production behavior with `brightcart/v1/shipping/lost-packages` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-04-03. Owner Jordan Patel. Canonical reference `brightcart/v1/shipping/lost-packages`. This page is active because engineers still use it for debugging historical client behavior.

