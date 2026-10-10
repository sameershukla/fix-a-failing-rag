---
doc_id: generated/level2-noise/returns/damaged-items-release-note
title: Damaged Item Claims — Release Note
source_type: release_note
source_system: release_portal
domain: returns
version: noise-6
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/damaged-items
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

# Damaged Item Claims — Release Note

## Release overview

Release notes for the returns service mention changes around Damaged Item Claims. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This runbook covers merchandise that arrives physically damaged. It helps support distinguish delivery damage from customer caused damage and collect enough information for a replacement or refund decision. Customers should report visible delivery damage within 5 calendar days of delivery. Support should request clear photos of the item and shipping package… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This runbook covers merchandise that arrives physically damaged. It helps support distinguish delivery damage from customer caused damage and collect enough information for a replacement or refund decision. Customers should report visible delivery damage within 7 calendar days of delivery. Support should request clear photos of the item and shipping package when practical.

## Feature flag

The new behavior initially ran behind `bc_returns_33` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **60 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Trust and Safety compared production behavior with `brightcart/v1/returns/damaged-items` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Ifeoma Okafor. Canonical reference `brightcart/v1/returns/damaged-items`. This page is active because engineers still use it for debugging historical client behavior.

