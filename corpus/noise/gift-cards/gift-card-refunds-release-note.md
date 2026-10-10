---
doc_id: generated/level2-noise/gift-cards/gift-card-refunds-release-note
title: Refunds for Gift Card and Mixed Payments — Release Note
source_type: release_note
source_system: release_portal
domain: gift-cards
version: noise-6
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-refunds
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
- gift-cards
---

# Refunds for Gift Card and Mixed Payments — Release Note

## Release overview

Release notes for the gift-cards service mention changes around Refunds for Gift Card and Mixed Payments. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: Refunds for Gift Card and Mixed Payments This policy explains where refund money goes when an order was paid by gift card or by a combination of gift card and another payment method. An amount originally paid by BrightCart gift card is refunded back to that gift card. For mixed payment orders, the refund is returned proportionally to the original payment… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: Refunds for Gift Card and Mixed Payments This policy explains where refund money goes when an order was paid by gift card or by a combination of gift card and another payment method. An amount originally paid by BrightCart gift card is refunded back to that gift card. For mixed payment orders, the refund is returned proportionally to the original payment methods until each method has received its share.

## Feature flag

The new behavior initially ran behind `bc_gift-cards_74` for **10%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **20 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **90 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Regional Operations compared production behavior with `brightcart/v1/gift-cards/gift-card-refunds` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-05-29. Owner Priya Nair. Canonical reference `brightcart/v1/gift-cards/gift-card-refunds`. This page is active because engineers still use it for debugging historical client behavior.

