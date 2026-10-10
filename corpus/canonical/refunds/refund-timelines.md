---
doc_id: brightcart/v1/refunds/refund-timelines
title: Refund Timelines by Payment Method
source_type: reference
source_system: policy_hub
domain: refunds
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/refunds/refund-timelines
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- refunds
- reference
---

# Refund Timelines by Payment Method

## Purpose and scope

This reference separates BrightCart processing time from the time a bank or card issuer may take to display the credit. Use it when a refund is already in issued status and the customer wants to know when the money will appear.

## Standard rule

After a refund is issued, card refunds usually appear within 3 to 5 business days, ACH refunds usually appear within 5 to 7 business days, and gift card refunds are normally available the same day. These are posting estimates after BrightCart has issued the refund.

## Conditions and decision points

- The refund must show issued, not pending.
- Issuer or bank posting time is controlled by the financial institution.
- The estimate is counted in business days.

## Worked example

BrightCart issues a Visa refund on Wednesday. The customer should normally see the credit between the following Monday and Wednesday, depending on bank holidays and the card issuer.

## Exceptions and edge cases

- A failed refund does not follow the normal posting estimate.
- Closed bank accounts may cause a refund to be rejected and returned.
- Chargeback credits follow the issuer dispute process, not this timeline.

## Operational notes

Agents should never create another refund simply because a bank has not posted the first one yet. If the normal window has passed, collect the refund reference number and open a trace with payments.
