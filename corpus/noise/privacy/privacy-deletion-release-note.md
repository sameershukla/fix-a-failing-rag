---
doc_id: generated/level2-noise/privacy/privacy-deletion-release-note
title: Privacy Deletion Requests — Release Note
source_type: release_note
source_system: release_portal
domain: privacy
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/privacy/privacy-deletion
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

# Privacy Deletion Requests — Release Note

## Release overview

Release notes for the privacy service mention changes around Privacy Deletion Requests. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy covers privacy requests asking BrightCart to delete eligible personal data. It complements, but is broader than, normal account closure. BrightCart verifies the requester before processing a privacy deletion request and targets completion within 31 days. Data required for tax, fraud prevention, legal claims, or other mandatory retention can be… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy covers privacy requests asking BrightCart to delete eligible personal data. It complements, but is broader than, normal account closure. BrightCart verifies the requester before processing a privacy deletion request and targets completion within 30 days. Data required for tax, fraud prevention, legal claims, or other mandatory retention can be kept in restricted systems for the required period.

## Feature flag

The new behavior initially ran behind `bc_privacy_26` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **24 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **60 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Commerce API compared production behavior with `brightcart/v1/privacy/privacy-deletion` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-04-03. Owner Mei Wong. Canonical reference `brightcart/v1/privacy/privacy-deletion`. This page is active because engineers still use it for debugging historical client behavior.

