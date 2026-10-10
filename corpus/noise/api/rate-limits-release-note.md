---
doc_id: generated/level2-noise/api/rate-limits-release-note
title: API Rate Limits — Release Note
source_type: release_note
source_system: release_portal
domain: api
version: noise-6
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/rate-limits
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
- api
---

# API Rate Limits — Release Note

## Release overview

Release notes for the api service mention changes around API Rate Limits. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 1200 requests per minute per client. When the limit is exceeded, the API returns HTTP 430 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 600 requests per minute per client. When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop.

## Feature flag

The new behavior initially ran behind `bc_api_13` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **8 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **7 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Customer Care compared production behavior with `brightcart/v1/api/rate-limits` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-02-14. Owner Elena Ruiz. Canonical reference `brightcart/v1/api/rate-limits`. This page is active because engineers still use it for debugging historical client behavior.

