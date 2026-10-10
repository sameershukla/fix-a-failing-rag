---
doc_id: brightcart/v1/subscriptions/subscription-refunds
title: Subscription Refund Eligibility
source_type: policy
source_system: policy_hub
domain: subscriptions
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/subscriptions/subscription-refunds
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- subscriptions
- policy
---

# Subscription Refund Eligibility

## Purpose and scope

This policy defines the narrow cases in which a recently renewed BrightCart Plus subscription can be refunded. It should be used separately from the cancellation process.

## Standard rule

An accidental subscription renewal can be refunded when the customer requests the refund within 48 hours of the renewal charge and has not used a paid membership benefit after that renewal. When approved, the subscription is canceled and the latest renewal charge is refunded.

## Conditions and decision points

- The request must be within 48 hours of the renewal timestamp.
- No paid membership benefit can have been used after renewal.
- The refund applies to the most recent renewal, not earlier billing periods.

## Worked example

An annual plan renews at 9:00 AM Monday. The customer contacts support Tuesday morning and has not used any member benefit since renewal. The renewal meets the standard refund conditions.

## Exceptions and edge cases

- Charges older than 48 hours require supervisor review and are normally not refundable.
- Fraud claims use the payment dispute process.
- Promotional credits are not refunded as cash.

## Operational notes

Support should verify the renewal timestamp and recent benefit usage before approving. If eligible, process cancellation and refund as linked actions so the plan does not renew again.
