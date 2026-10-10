---
doc_id: generated/level2-noise/refunds/refund-policy-release-note
title: Standard Refund Policy — Release Note
source_type: release_note
source_system: release_portal
domain: refunds
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-policy
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

# Standard Refund Policy — Release Note

## Release overview

Release notes for the refunds service mention changes around Standard Refund Policy. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception. Once BrightCart approves a refund, the refund… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception. Once BrightCart approves a refund, the refund is sent back to the original payment method.

## Feature flag

The new behavior initially ran behind `bc_refunds_57` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **4 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Trust and Safety compared production behavior with `brightcart/v1/refunds/refund-policy` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-01-07. Owner Elena Ruiz. Canonical reference `brightcart/v1/refunds/refund-policy`. This page is active because engineers still use it for debugging historical client behavior.

