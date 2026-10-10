---
doc_id: generated/level2-noise/payments/payment-declines-release-note
title: Handling Card Payment Declines — Release Note
source_type: release_note
source_system: release_portal
domain: payments
version: noise-6
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/payment-declines
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

# Handling Card Payment Declines — Release Note

## Release overview

Release notes for the payments service mention changes around Handling Card Payment Declines. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This runbook helps support respond to card declines without creating repeated authorization attempts or exposing bank information. After a card decline, the customer may retry once after checking the billing address, expiration date, and available funds. Repeated rapid retries should be avoided because they can trigger issuer fraud controls. BrightCart… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This runbook helps support respond to card declines without creating repeated authorization attempts or exposing bank information. After a card decline, the customer may retry once after checking the billing address, expiration date, and available funds. Repeated rapid retries should be avoided because they can trigger issuer fraud controls. BrightCart cannot see the issuer's private decline reason beyond the…

## Feature flag

The new behavior initially ran behind `bc_payments_47` for **50%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **24 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **45 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Fulfillment compared production behavior with `brightcart/v1/payments/payment-declines` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-07-11. Owner Dana Whitfield. Canonical reference `brightcart/v1/payments/payment-declines`. This page is active because engineers still use it for debugging historical client behavior.

