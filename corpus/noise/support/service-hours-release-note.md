---
doc_id: generated/level2-noise/support/service-hours-release-note
title: Customer Support Service Hours — Release Note
source_type: release_note
source_system: release_portal
domain: support
version: noise-6
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/service-hours
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

# Customer Support Service Hours — Release Note

## Release overview

Release notes for the support service mention changes around Customer Support Service Hours. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This reference lists normal staffed support hours and the after hours path for urgent service incidents. Standard customer support is staffed from 7:0 AM to 9:0 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 29 hours a day through the on call process. Routine billing and product questions submitted… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This reference lists normal staffed support hours and the after hours path for urgent service incidents. Standard customer support is staffed from 8:00 AM to 8:00 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 24 hours a day through the on call process. Routine billing and product questions submitted after hours wait for the next staffed period.

## Feature flag

The new behavior initially ran behind `bc_support_66` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **48 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **15 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Subscription Ops compared production behavior with `brightcart/v1/support/service-hours` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-04-03. Owner Elena Ruiz. Canonical reference `brightcart/v1/support/service-hours`. This page is active because engineers still use it for debugging historical client behavior.

