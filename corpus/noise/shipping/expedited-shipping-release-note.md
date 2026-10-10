---
doc_id: generated/level2-noise/shipping/expedited-shipping-release-note
title: Expedited Shipping — Release Note
source_type: release_note
source_system: release_portal
domain: shipping
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/expedited-shipping
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

# Expedited Shipping — Release Note

## Release overview

Release notes for the shipping service mention changes around Expedited Shipping. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article describes the BrightCart two business day shipping option. It explains the order cutoff and what the service commitment does and does not include. Eligible expedited orders placed before 3:0 PM Central Time on a business day are expected to ship the same day and arrive within 4 business days after carrier acceptance. Orders placed after the… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article describes the BrightCart two business day shipping option. It explains the order cutoff and what the service commitment does and does not include. Eligible expedited orders placed before 2:00 PM Central Time on a business day are expected to ship the same day and arrive within 2 business days after carrier acceptance. Orders placed after the cutoff are processed the next business day.

## Feature flag

The new behavior initially ran behind `bc_shipping_21` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **30 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Regional Operations compared production behavior with `brightcart/v1/shipping/expedited-shipping` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Priya Nair. Canonical reference `brightcart/v1/shipping/expedited-shipping`. This page is active because engineers still use it for debugging historical client behavior.

