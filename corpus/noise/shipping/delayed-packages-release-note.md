---
doc_id: generated/level2-noise/shipping/delayed-packages-release-note
title: Delayed Package Handling — Release Note
source_type: release_note
source_system: release_portal
domain: shipping
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/delayed-packages
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

# Delayed Package Handling — Release Note

## Release overview

Release notes for the shipping service mention changes around Delayed Package Handling. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This runbook defines when support should treat a shipment as delayed and what checks to perform before replacing or refunding an order. A package is considered delayed when it is more than 3 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This runbook defines when support should treat a shipment as delayed and what checks to perform before replacing or refunding an order. A package is considered delayed when it is more than 2 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless there is evidence of loss or damage. The order page promises…

## Feature flag

The new behavior initially ran behind `bc_shipping_53` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **12 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **90 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Privacy Office compared production behavior with `brightcart/v1/shipping/delayed-packages` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-07-11. Owner Maya Chen. Canonical reference `brightcart/v1/shipping/delayed-packages`. This page is active because engineers still use it for debugging historical client behavior.

