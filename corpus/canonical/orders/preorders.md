---
doc_id: brightcart/v1/orders/preorders
title: Preorder Fulfillment and Payment
source_type: policy
source_system: policy_hub
domain: orders
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/orders/preorders
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- orders
- policy
---

# Preorder Fulfillment and Payment

## Purpose and scope

This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled.

## Standard rule

For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier schedule changes.

## Conditions and decision points

- The customer must keep a valid payment method on the order.
- An authorization check can expire before the ship date without being a final charge.
- BrightCart sends an update when the expected ship date changes materially.

## Worked example

A customer preorders a console in May for an expected July shipment. The card is verified in May, but the final capture occurs when the console ships in July. If the supplier moves the date, BrightCart sends an updated estimate.

## Exceptions and edge cases

- Gift cards can reserve value immediately because they do not use card authorization holds.
- Limited release items can have quantity limits.
- Business purchase orders can follow contract terms.

## Operational notes

Support should not describe a temporary authorization as a settled preorder charge. Check transaction status before advising the customer.
