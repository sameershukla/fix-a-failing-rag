---
doc_id: generated/level2-noise/shipping/international-shipping-release-note
title: International Shipping and Duties — Release Note
source_type: release_note
source_system: release_portal
domain: shipping
version: noise-6
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/international-shipping
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

# International Shipping and Duties — Release Note

## Release overview

Release notes for the shipping service mention changes around International Shipping and Duties. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy explains normal international delivery timing and customer responsibility for import charges. It applies only to countries shown as eligible at checkout. International orders normally arrive in 12 to 28 business days after shipment. Import duties, taxes, and customs fees are the customer responsibility unless checkout explicitly states that… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy explains normal international delivery timing and customer responsibility for import charges. It applies only to countries shown as eligible at checkout. International orders normally arrive in 7 to 14 business days after shipment. Import duties, taxes, and customs fees are the customer responsibility unless checkout explicitly states that duties are prepaid.

## Feature flag

The new behavior initially ran behind `bc_shipping_12` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **4 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **3 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Payments Ops compared production behavior with `brightcart/v1/shipping/international-shipping` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Mei Wong. Canonical reference `brightcart/v1/shipping/international-shipping`. This page is active because engineers still use it for debugging historical client behavior.

