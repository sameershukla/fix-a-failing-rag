---
doc_id: brightcart/v1/orders/backorders
title: Backordered Items
source_type: policy
source_system: policy_hub
domain: orders
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/orders/backorders
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

# Backordered Items

## Purpose and scope

This article explains how BrightCart handles items that were orderable but are temporarily unavailable at the warehouse.

## Standard rule

A backordered item is not captured on a standard card until it ships. The order page shows an estimated availability date. If the estimate changes, BrightCart updates the order and sends a notice when the change is significant.

## Conditions and decision points

- In stock items on the same order can ship separately.
- The card must remain valid when the backordered item becomes ready.
- Customers can cancel an unshipped backordered line.

## Worked example

A customer orders two items, one in stock and one backordered. The in stock item ships and is charged first. The backordered item remains open and is captured only when it later ships.

## Exceptions and edge cases

- Gift card value can be reserved differently from a credit card capture.
- Supplier cancellation can cause BrightCart to cancel and refund the line.
- Made to order products follow their own lead time terms.

## Operational notes

Support should quote the latest availability estimate and avoid promising a supplier date as guaranteed. If the customer no longer wants the item, cancel the unshipped line when allowed.
