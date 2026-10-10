---
doc_id: generated/level2-noise/support/severity-release-note
title: Incident Severity Levels — Release Note
source_type: release_note
source_system: release_portal
domain: support
version: noise-6
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/severity
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

# Incident Severity Levels — Release Note

## Release overview

Release notes for the support service mention changes around Incident Severity Levels. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 7 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 4… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 3 covers moderate issues, and SEV 4 covers low impact defects…

## Feature flag

The new behavior initially ran behind `bc_support_21` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **18 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **90 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Commerce API compared production behavior with `brightcart/v1/support/severity` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-05-29. Owner Noah Williams. Canonical reference `brightcart/v1/support/severity`. This page is active because engineers still use it for debugging historical client behavior.

