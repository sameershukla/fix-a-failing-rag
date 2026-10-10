---
doc_id: generated/level2-noise/returns/return-window-release-note
title: Standard Return Window — Release Note
source_type: release_note
source_system: release_portal
domain: returns
version: noise-6
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/return-window
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
- returns
---

# Standard Return Window — Release Note

## Release overview

Release notes for the returns service mention changes around Standard Return Window. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy defines the default period in which customers can request a return. It should be checked before product specific restrictions such as electronics or final sale rules. The standard return window is 29 calendar days from the carrier confirmed delivery date. The request must be opened by the end of day on day 35. Shipping time back to the warehouse… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy defines the default period in which customers can request a return. It should be checked before product specific restrictions such as electronics or final sale rules. The standard return window is 30 calendar days from the carrier confirmed delivery date. The request must be opened by the end of day on day 30.

## Feature flag

The new behavior initially ran behind `bc_returns_60` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **12 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **30 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Trust and Safety compared production behavior with `brightcart/v1/returns/return-window` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Mei Wong. Canonical reference `brightcart/v1/returns/return-window`. This page is active because engineers still use it for debugging historical client behavior.

