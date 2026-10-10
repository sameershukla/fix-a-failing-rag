---
doc_id: brightcart/v1/payments/payment-declines
title: Handling Card Payment Declines
source_type: runbook
source_system: policy_hub
domain: payments
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/payments/payment-declines
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

# Handling Card Payment Declines

## Purpose and scope

This runbook helps support respond to card declines without creating repeated authorization attempts or exposing bank information.

## Standard rule

After a card decline, the customer may retry once after checking the billing address, expiration date, and available funds. Repeated rapid retries should be avoided because they can trigger issuer fraud controls. BrightCart cannot see the issuer's private decline reason beyond the processor code returned to us.

## Conditions and decision points

- Do not ask the customer to send a full card number in chat or email.
- A corrected billing address can justify one new attempt.
- A hard processor code such as stolen card should not be retried.

## Worked example

A customer mistypes the postal code and receives a decline. After correcting the billing address, one retry is reasonable. If that retry also fails, the customer should contact the card issuer or use another payment method.

## Exceptions and edge cases

- Temporary processor outages can return a system error rather than a true issuer decline.
- Fraud blocked orders require risk review.
- Gift card balance failures follow the gift card rules.

## Operational notes

Record the processor code and whether a retry occurred. Never copy sensitive card data into case notes.
