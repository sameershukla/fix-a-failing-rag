---
doc_id: brightcart/v1/shipping/lost-packages
title: Lost Package Criteria
source_type: runbook
source_system: policy_hub
domain: shipping
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/shipping/lost-packages
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- shipping
- runbook
---

# Lost Package Criteria

## Purpose and scope

This article defines when a package can be treated as lost rather than merely delayed. It is used before a replacement or refund is approved for a shipment that stopped moving.

## Standard rule

A domestic package can be treated as lost after 5 consecutive calendar days with no new carrier scan. An international package uses a 10 calendar day no scan threshold because customs movement can be slower. An explicit carrier lost status overrides these waiting periods.

## Conditions and decision points

- Count from the timestamp of the last meaningful carrier scan.
- A label created event without carrier possession is handled as a fulfillment issue.
- A customs hold message is a scan and resets the international no movement clock.

## Worked example

A domestic package has its last carrier movement scan on June 1 and there are no later scans. On June 6 it reaches the five day no scan threshold and support can start the lost package resolution process.

## Exceptions and edge cases

- High value items may require a carrier investigation before replacement.
- Fraud flagged orders require risk review.
- An explicit carrier confirmation of loss allows immediate resolution.

## Operational notes

When resolving a lost package, record the last scan time, destination, item value, and whether the customer wants replacement or refund. A replacement shipment should have a new tracking number.
