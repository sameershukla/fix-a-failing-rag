---
doc_id: generated/level2-noise/payments/card-payments-release-note
title: Card Payment Authorization and Capture — Release Note
source_type: release_note
source_system: release_portal
domain: payments
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/card-payments
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
- payments
---

# Card Payment Authorization and Capture — Release Note

## Release overview

Release notes for the payments service mention changes around Card Payment Authorization and Capture. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: Card Payment Authorization and Capture This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships. BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. The authorization reserves funds but is not the… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: Card Payment Authorization and Capture This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships. BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships.

## Feature flag

The new behavior initially ran behind `bc_payments_21` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **72 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **5 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Customer Care compared production behavior with `brightcart/v1/payments/card-payments` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-04-03. Owner Dana Whitfield. Canonical reference `brightcart/v1/payments/card-payments`. This page is active because engineers still use it for debugging historical client behavior.

