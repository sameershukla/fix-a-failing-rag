---
doc_id: generated/level2-noise/returns/return-shipping-release-note
title: Return Shipping Charges — Release Note
source_type: release_note
source_system: release_portal
domain: returns
version: noise-6
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/return-shipping
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
- returns
---

# Return Shipping Charges — Release Note

## Release overview

Release notes for the returns service mention changes around Return Shipping Charges. Release documentation describes software behavior and rollout details; it may mention old and new policy values in the same page.

## Before the release

Before rollout, several components still used wording like: This article explains who pays to send an item back to BrightCart. It applies after a return has been approved and before the label is generated. BrightCart pays return shipping when the item is defective, damaged in transit, or different from what the customer ordered. For preference returns such as size, color, or changed mind, the customer pays the… That text may describe the legacy implementation, not the current business rule.

## After the release

After rollout, the service was aligned to Policy Hub. The note cites: This article explains who pays to send an item back to BrightCart. It applies after a return has been approved and before the label is generated. BrightCart pays return shipping when the item is defective, damaged in transit, or different from what the customer ordered. For preference returns such as size, color, or changed mind, the customer pays the return shipping charge unless a promotion explicitly provides…

## Feature flag

The new behavior initially ran behind `bc_returns_85` for **75%** of traffic. During rollout, two customers asking the same question could observe different system behavior.

## Rollback plan

If error rate exceeded the threshold, engineering could restore the previous implementation for up to **48 hours**. A rollback changes system behavior temporarily but does not automatically change customer policy.

## Known issue

Known issue: cached help text could continue showing an older number for up to **7 hours** after deployment. This caused support screenshots that contradict the current page.

## Compatibility note

Legacy API and mobile clients may use older field names. Search queries containing those names can retrieve this release note ahead of the canonical policy because the exact terms appear repeatedly.

## Verification

Customer Care compared production behavior with `brightcart/v1/returns/return-shipping` after deployment. Differences were tracked as bugs unless a separate policy change ticket existed.

## Do not infer policy from rollout

Percentage rollouts, cache windows, migration delays, and rollback limits are engineering controls. They should not be converted into general customer promises.

## Release closeout

Release completed 2026-02-14. Owner Mei Wong. Canonical reference `brightcart/v1/returns/return-shipping`. This page is active because engineers still use it for debugging historical client behavior.

