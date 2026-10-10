---
doc_id: generated/level2-noise/api/idempotency-release-note
title: Idempotency for Write Requests — Release Note
source_type: release_note
source_system: release_portal
domain: api
version: noise-6
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/idempotency
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

# Idempotency for Write Requests — Release Note

## Release overview

Release notes for the api service mention changes around Idempotency for Write Requests. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 13 hours. Repeating the same request with the same key during that period returns the… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 24 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second…

## Feature flag

The new behavior initially ran behind `bc_api_71` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **12 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **45 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Trust and Safety compared production behavior with `brightcart/v1/api/idempotency` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Dana Whitfield. Canonical reference `brightcart/v1/api/idempotency`. This page is active because engineers still use it for debugging historical client behavior.

