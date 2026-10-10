---
doc_id: brightcart/v1/orders/order-modification
title: Changing an Order Before Fulfillment
source_type: policy
source_system: policy_hub
domain: orders
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/orders/order-modification
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

# Changing an Order Before Fulfillment

## Purpose and scope

This policy explains which changes can be made after checkout but before warehouse fulfillment begins. It avoids edits that would create inventory or payment mismatches after packing starts.

## Standard rule

A shipping address or item quantity can be changed only while the order is in received status and before fulfillment starts. Once the order moves to picking or packed status, item and address changes are not allowed. The customer can then use cancellation or return options if eligible.

## Conditions and decision points

- The replacement address must pass normal validation.
- Increasing quantity requires available inventory and payment authorization.
- Changing to a different product creates a new order rather than editing the original line.

## Worked example

A customer places an order at 9:00 AM and contacts support at 9:10 AM while the order still shows received. The apartment number can be corrected. If the warehouse already started picking, the address cannot be edited.

## Exceptions and edge cases

- A carrier delivery instruction after shipment is controlled by the carrier, not an order edit.
- Fraud holds may prevent all changes.
- Business purchase orders can have separate change procedures.

## Operational notes

Check the live fulfillment status before making any promise. If the order crosses into picking while the case is open, stop the edit and explain the available next action.
