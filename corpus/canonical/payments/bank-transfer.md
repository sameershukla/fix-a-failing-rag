---
doc_id: brightcart/v1/payments/bank-transfer
title: Business ACH Payments
source_type: policy
source_system: policy_hub
domain: payments
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/payments/bank-transfer
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
- policy
---

# Business ACH Payments

## Purpose and scope

This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout.

## Standard rule

Approved business customers can pay by ACH. ACH payments normally take 2 to 3 business days to clear. Orders that require cleared funds are not released until the payment reaches cleared status.

## Conditions and decision points

- The business account must be approved for ACH.
- The bank account must pass verification.
- Returned ACH payments place the account on payment review.

## Worked example

A business submits an ACH payment on Monday. With no bank holiday, the payment will normally clear between Wednesday and Thursday. An order configured to wait for funds will remain on hold until the clear event arrives.

## Exceptions and edge cases

- Same day wire transfers are handled manually by finance and are not ACH.
- Weekends and bank holidays can extend clearing time.
- Very large transfers may require additional finance approval.

## Operational notes

Support can report pending or cleared status but should not promise a precise bank settlement hour. Returned payments should be escalated to finance.
