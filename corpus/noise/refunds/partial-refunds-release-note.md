---
doc_id: generated/level2-noise/refunds/partial-refunds-release-note
title: Partial Refunds and Deductions — Release Note
source_type: release_note
source_system: release_portal
domain: refunds
version: noise-6
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/partial-refunds
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

# Partial Refunds and Deductions — Release Note

## Release overview

Release notes for the refunds service mention changes around Partial Refunds and Deductions. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: Partial refunds are used when the customer is owed money but not the full original item price. This guide explains the allowed reasons for deductions and the information that must be shown to the customer. A partial refund may be issued when returned merchandise is missing customer removable parts, shows customer caused damage, or only part of a multi item… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: Partial refunds are used when the customer is owed money but not the full original item price. This guide explains the allowed reasons for deductions and the information that must be shown to the customer. A partial refund may be issued when returned merchandise is missing customer removable parts, shows customer caused damage, or only part of a multi item order is being refunded. The deduction must be tied to a…

## Feature flag

The new behavior initially ran behind `bc_refunds_12` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **6 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **60 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Subscription Ops compared production behavior with `brightcart/v1/refunds/partial-refunds` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-04-03. Owner Dana Whitfield. Canonical reference `brightcart/v1/refunds/partial-refunds`. This page is active because engineers still use it for debugging historical client behavior.

