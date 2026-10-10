---
doc_id: generated/level2-noise/refunds/refund-status-release-note
title: Refund Status and Failed Refunds — Release Note
source_type: release_note
source_system: release_portal
domain: refunds
version: noise-6
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-status
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

# Refund Status and Failed Refunds — Release Note

## Release overview

Release notes for the refunds service mention changes around Refund Status and Failed Refunds. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This runbook explains the refund lifecycle visible to support and the action to take when a refund fails. It is intended for customer support and payment operations. Refunds move through pending, issued, or failed status. A failed refund is retried automatically one time. If the retry also fails, the case must be sent to payment operations for manual review. That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This runbook explains the refund lifecycle visible to support and the action to take when a refund fails. It is intended for customer support and payment operations. Refunds move through pending, issued, or failed status. A failed refund is retried automatically one time.

## Feature flag

The new behavior initially ran behind `bc_refunds_35` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **3 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Risk Operations compared production behavior with `brightcart/v1/refunds/refund-status` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-05-29. Owner Noah Williams. Canonical reference `brightcart/v1/refunds/refund-status`. This page is active because engineers still use it for debugging historical client behavior.

