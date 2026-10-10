---
doc_id: generated/level2-noise/support/escalation-release-note
title: Support Escalation Path — Release Note
source_type: release_note
source_system: release_portal
domain: support
version: noise-6
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/escalation
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
- support
---

# Support Escalation Path — Release Note

## Release overview

Release notes for the support service mention changes around Support Escalation Path. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This runbook defines when a support case should move beyond the front line queue. It gives agents a consistent escalation path for complex or high risk situations. Routine product and order questions stay with Level 1 support. Cases needing deeper product or payment investigation move to Level 4. Suspected security events, material financial loss, broad… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This runbook defines when a support case should move beyond the front line queue. It gives agents a consistent escalation path for complex or high risk situations. Routine product and order questions stay with Level 1 support. Cases needing deeper product or payment investigation move to Level 2.

## Feature flag

The new behavior initially ran behind `bc_support_92` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **12 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **7 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Subscription Ops compared production behavior with `brightcart/v1/support/escalation` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Marcus Lee. Canonical reference `brightcart/v1/support/escalation`. This page is active because engineers still use it for debugging historical client behavior.

