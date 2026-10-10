---
doc_id: generated/level2-noise/payments/bank-transfer-release-note
title: Business ACH Payments — Release Note
source_type: release_note
source_system: release_portal
domain: payments
version: noise-6
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/bank-transfer
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

# Business ACH Payments — Release Note

## Release overview

Release notes for the payments service mention changes around Business ACH Payments. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 7 to 2 business days to clear. Orders that require cleared funds are not released until the payment reaches cleared status. That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 2 to 3 business days to clear.

## Feature flag

The new behavior initially ran behind `bc_payments_83` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **10 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Payments Ops compared production behavior with `brightcart/v1/payments/bank-transfer` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-04-03. Owner Maya Chen. Canonical reference `brightcart/v1/payments/bank-transfer`. This page is active because engineers still use it for debugging historical client behavior.

