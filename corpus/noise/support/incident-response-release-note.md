---
doc_id: generated/level2-noise/support/incident-response-release-note
title: Incident Response Process — Release Note
source_type: release_note
source_system: release_portal
domain: support
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/incident-response
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

# Incident Response Process — Release Note

## Release overview

Release notes for the support service mention changes around Incident Response Process. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 20 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 10 business… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 15 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 5 business days after a SEV 1 or qualifying SEV 2 incident is resolved.

## Feature flag

The new behavior initially ran behind `bc_support_42` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **4 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **45 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Fulfillment compared production behavior with `brightcart/v1/support/incident-response` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-08-22. Owner Dana Whitfield. Canonical reference `brightcart/v1/support/incident-response`. This page is active because engineers still use it for debugging historical client behavior.

