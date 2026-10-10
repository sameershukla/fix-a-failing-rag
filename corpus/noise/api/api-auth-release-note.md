---
doc_id: generated/level2-noise/api/api-auth-release-note
title: API Authentication — Release Note
source_type: release_note
source_system: release_portal
domain: api
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/api-auth
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

# API Authentication — Release Note

## Release overview

Release notes for the api service mention changes around API Authentication. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 3.0 client credentials to obtain an access token. Access tokens are valid for 61 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 2.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes.

## Feature flag

The new behavior initially ran behind `bc_api_21` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **18 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **21 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Fulfillment compared production behavior with `brightcart/v1/api/api-auth` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-02-14. Owner Noah Williams. Canonical reference `brightcart/v1/api/api-auth`. This page is active because engineers still use it for debugging historical client behavior.

