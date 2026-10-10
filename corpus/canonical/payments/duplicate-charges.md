---
doc_id: brightcart/v1/payments/duplicate-charges
title: Duplicate Charge Investigation
source_type: runbook
source_system: policy_hub
domain: payments
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/payments/duplicate-charges
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- payments
- runbook
---

# Duplicate Charge Investigation

## Purpose and scope

This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists.

## Standard rule

Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment. If two captured charges exist for the same order and amount, payments should void or refund the extra capture.

## Conditions and decision points

- Compare transaction IDs, status, amount, and order reference.
- Pending bank entries may disappear after the issuer releases the authorization.
- A split shipment can legitimately create multiple captures with different amounts.

## Worked example

A bank app shows one $75 pending amount and one $75 posted amount for the same order. BrightCart finds one authorization and one capture. Support explains the pending authorization instead of issuing a second refund.

## Exceptions and edge cases

- Two settled charges with distinct transaction IDs require payment operations action.
- A customer may have placed two separate identical orders.
- Chargebacks are not handled as duplicate capture refunds.

## Operational notes

Attach the processor transaction details to the case. If an extra capture is confirmed, link the corrective refund or void to the duplicate transaction ID.
