---
doc_id: generated/level2-noise/privacy/data-export-release-note
title: Customer Data Export — Release Note
source_type: release_note
source_system: release_portal
domain: privacy
version: noise-6
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/privacy/data-export
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
- privacy
---

# Customer Data Export — Release Note

## Release overview

Release notes for the privacy service mention changes around Customer Data Export. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy describes the self service export a verified customer can request for a copy of common BrightCart account data. A verified customer data export is normally prepared within 13 hours. When the export is ready, BrightCart sends a download link that remains valid for 96 hours. The link requires the customer to sign in again before download. A… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy describes the self service export a verified customer can request for a copy of common BrightCart account data. A verified customer data export is normally prepared within 24 hours. When the export is ready, BrightCart sends a download link that remains valid for 48 hours. The link requires the customer to sign in again before download.

## Feature flag

The new behavior initially ran behind `bc_privacy_48` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **4 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Fulfillment compared production behavior with `brightcart/v1/privacy/data-export` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Marcus Lee. Canonical reference `brightcart/v1/privacy/data-export`. This page is active because engineers still use it for debugging historical client behavior.

