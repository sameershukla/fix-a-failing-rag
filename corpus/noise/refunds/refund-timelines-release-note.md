---
doc_id: generated/level2-noise/refunds/refund-timelines-release-note
title: Refund Timelines by Payment Method — Release Note
source_type: release_note
source_system: release_portal
domain: refunds
version: noise-6
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-timelines
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

# Refund Timelines by Payment Method — Release Note

## Release overview

Release notes for the refunds service mention changes around Refund Timelines by Payment Method. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This reference separates BrightCart processing time from the time a bank or card issuer may take to display the credit. Use it when a refund is already in issued status and the customer wants to know when the money will appear. After a refund is issued, card refunds usually appear within 8 to 10 business days, ACH refunds usually appear within 10 to 14… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This reference separates BrightCart processing time from the time a bank or card issuer may take to display the credit. Use it when a refund is already in issued status and the customer wants to know when the money will appear. After a refund is issued, card refunds usually appear within 3 to 5 business days, ACH refunds usually appear within 5 to 7 business days, and gift card refunds are normally available the…

## Feature flag

The new behavior initially ran behind `bc_refunds_51` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **12 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Regional Operations compared production behavior with `brightcart/v1/refunds/refund-timelines` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-01-07. Owner Priya Nair. Canonical reference `brightcart/v1/refunds/refund-timelines`. This page is active because engineers still use it for debugging historical client behavior.

