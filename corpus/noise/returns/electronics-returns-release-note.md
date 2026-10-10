---
doc_id: generated/level2-noise/returns/electronics-returns-release-note
title: Electronics Return Rules — Release Note
source_type: release_note
source_system: release_portal
domain: returns
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/electronics-returns
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

# Electronics Return Rules — Release Note

## Release overview

Release notes for the returns service mention changes around Electronics Return Rules. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: Electronics have a shorter return window because activated or opened devices can lose resale value. This article applies to headphones, tablets, smart home devices, cameras, and similar products listed as electronics. Electronics may be returned within 8 calendar days of delivery. Opened electronics are not returnable for preference changes, but defective… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: Electronics have a shorter return window because activated or opened devices can lose resale value. This article applies to headphones, tablets, smart home devices, cameras, and similar products listed as electronics. Electronics may be returned within 14 calendar days of delivery. Opened electronics are not returnable for preference changes, but defective electronics can still be returned or replaced during the 14…

## Feature flag

The new behavior initially ran behind `bc_returns_17` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **48 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **3 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Customer Care compared production behavior with `brightcart/v1/returns/electronics-returns` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Ifeoma Okafor. Canonical reference `brightcart/v1/returns/electronics-returns`. This page is active because engineers still use it for debugging historical client behavior.

