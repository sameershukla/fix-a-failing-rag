---
doc_id: generated/level2-noise/refunds/refund-eligibility-release-note
title: Refund Eligibility Rules — Release Note
source_type: release_note
source_system: release_portal
domain: refunds
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-eligibility
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
- refunds
---

# Refund Eligibility Rules — Release Note

## Release overview

Release notes for the refunds service mention changes around Refund Eligibility Rules. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule. Most unused physical items are eligible for a refund when the return is requested within 35 calendar days of delivery. Final sale… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule. Most unused physical items are eligible for a refund when the return is requested within 30 calendar days of delivery.

## Feature flag

The new behavior initially ran behind `bc_refunds_51` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **4 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Payments Ops compared production behavior with `brightcart/v1/refunds/refund-eligibility` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-01-07. Owner Mei Wong. Canonical reference `brightcart/v1/refunds/refund-eligibility`. This page is active because engineers still use it for debugging historical client behavior.

