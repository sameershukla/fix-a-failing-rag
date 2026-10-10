---
doc_id: generated/level2-noise/orders/backorders-release-note
title: Backordered Items — Release Note
source_type: release_note
source_system: release_portal
domain: orders
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/orders/backorders
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
- orders
---

# Backordered Items — Release Note

## Release overview

Release notes for the orders service mention changes around Backordered Items. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article explains how BrightCart handles items that were orderable but are temporarily unavailable at the warehouse. A backordered item is not captured on a standard card until it ships. The order page shows an estimated availability date. If the estimate changes, BrightCart updates the order and sends a notice when the change is significant. A customer… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article explains how BrightCart handles items that were orderable but are temporarily unavailable at the warehouse. A backordered item is not captured on a standard card until it ships. The order page shows an estimated availability date. If the estimate changes, BrightCart updates the order and sends a notice when the change is significant.

## Feature flag

The new behavior initially ran behind `bc_orders_97` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **18 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Risk Operations compared production behavior with `brightcart/v1/orders/backorders` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2025-11-18. Owner Priya Nair. Canonical reference `brightcart/v1/orders/backorders`. This page is active because engineers still use it for debugging historical client behavior.

