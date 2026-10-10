---
doc_id: generated/level2-noise/gift-cards/gift-card-redemption-release-note
title: Redeeming Gift Cards — Release Note
source_type: release_note
source_system: release_portal
domain: gift-cards
version: noise-6
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-redemption
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

# Redeeming Gift Cards — Release Note

## Release overview

Release notes for the gift-cards service mention changes around Redeeming Gift Cards. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 4 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 3 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with another supported payment method.

## Feature flag

The new behavior initially ran behind `bc_gift-cards_97` for **25%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **48 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **7 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Privacy Office compared production behavior with `brightcart/v1/gift-cards/gift-card-redemption` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-05-29. Owner Ifeoma Okafor. Canonical reference `brightcart/v1/gift-cards/gift-card-redemption`. This page is active because engineers still use it for debugging historical client behavior.

