---
doc_id: generated/level2-noise/gift-cards/gift-card-purchase-release-note
title: Gift Card Purchase Rules — Release Note
source_type: release_note
source_system: release_portal
domain: gift-cards
version: noise-6
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-purchase
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

# Gift Card Purchase Rules — Release Note

## Release overview

Release notes for the gift-cards service mention changes around Gift Card Purchase Rules. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This policy covers digital BrightCart gift card purchases. Gift cards are delivered by email and can be used for eligible BrightCart purchases. A single BrightCart gift card can be purchased in an amount from $15 through $1000. Digital delivery usually occurs within 20 minutes after payment approval. Gift cards cannot be purchased using another gift card. That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This policy covers digital BrightCart gift card purchases. Gift cards are delivered by email and can be used for eligible BrightCart purchases. A single BrightCart gift card can be purchased in an amount from $10 through $500. Digital delivery usually occurs within 15 minutes after payment approval.

## Feature flag

The new behavior initially ran behind `bc_gift-cards_35` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **72 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **15 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Risk Operations compared production behavior with `brightcart/v1/gift-cards/gift-card-purchase` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-05-29. Owner Dana Whitfield. Canonical reference `brightcart/v1/gift-cards/gift-card-purchase`. This page is active because engineers still use it for debugging historical client behavior.

