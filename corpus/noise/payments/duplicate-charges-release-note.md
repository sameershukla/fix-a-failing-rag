---
doc_id: generated/level2-noise/payments/duplicate-charges-release-note
title: Duplicate Charge Investigation — Release Note
source_type: release_note
source_system: release_portal
domain: payments
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/duplicate-charges
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
- payments
---

# Duplicate Charge Investigation — Release Note

## Release overview

Release notes for the payments service mention changes around Duplicate Charge Investigation. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists. Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists. Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment.

## Feature flag

The new behavior initially ran behind `bc_payments_11` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **48 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **5 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Subscription Ops compared production behavior with `brightcart/v1/payments/duplicate-charges` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-01-07. Owner Ifeoma Okafor. Canonical reference `brightcart/v1/payments/duplicate-charges`. This page is active because engineers still use it for debugging historical client behavior.

