---
doc_id: brightcart/v1/orders/order-cancellation
title: Canceling an Order
source_type: policy
source_system: policy_hub
domain: orders
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/orders/order-cancellation
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

# Canceling an Order

## Purpose and scope

This policy defines when a customer order can be canceled before shipment. Cancellation is separate from returning an item after it has already entered the shipping process.

## Standard rule

A customer can cancel an order while it is in received or picking status if the warehouse can still stop fulfillment. Once the order reaches packed status, cancellation is no longer available. After packed status, the customer should wait for delivery and use the applicable return process.

## Conditions and decision points

- The cancellation request is not complete until the order status changes to canceled.
- A payment authorization can remain visible temporarily after a successful cancellation.
- Partial cancellation is allowed only for order lines not already packed.

## Worked example

An order is in picking when the customer requests cancellation. The warehouse successfully stops the pick and the order changes to canceled, so no shipment occurs. If the order had already changed to packed, support would not promise cancellation.

## Exceptions and edge cases

- Safety recalls can stop a shipment outside the normal customer cancellation path.
- Digital goods can have separate fulfillment rules.
- Fraud teams can cancel orders as a risk action.

## Operational notes

Always verify the final order status. Telling a customer that a request was submitted is not the same as confirming the order was canceled.
