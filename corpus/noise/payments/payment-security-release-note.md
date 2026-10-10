---
doc_id: generated/level2-noise/payments/payment-security-release-note
title: Payment Data Security Rules — Release Note
source_type: release_note
source_system: release_portal
domain: payments
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/payment-security
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

# Payment Data Security Rules — Release Note

## Release overview

Release notes for the payments service mention changes around Payment Data Security Rules. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy defines the payment information BrightCart staff and systems may store or place in support tools. It is intended to reduce exposure of sensitive card data. BrightCart systems must not store card CVV values after authorization. Support staff must never ask customers to send a full card number, CVV, or card image through chat or email. Payment… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy defines the payment information BrightCart staff and systems may store or place in support tools. It is intended to reduce exposure of sensitive card data. BrightCart systems must not store card CVV values after authorization. Support staff must never ask customers to send a full card number, CVV, or card image through chat or email.

## Feature flag

The new behavior initially ran behind `bc_payments_68` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **72 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **5 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Fulfillment compared production behavior with `brightcart/v1/payments/payment-security` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-02-14. Owner Mei Wong. Canonical reference `brightcart/v1/payments/payment-security`. This page is active because engineers still use it for debugging historical client behavior.

