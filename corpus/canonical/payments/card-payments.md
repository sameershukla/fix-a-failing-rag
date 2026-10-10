---
doc_id: brightcart/v1/payments/card-payments
title: Card Payment Authorization and Capture
source_type: reference
source_system: policy_hub
domain: payments
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/payments/card-payments
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
- reference
---

# Card Payment Authorization and Capture

## Purpose and scope

This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships.

## Standard rule

BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. The authorization reserves funds but is not the final settled charge. If the order is canceled before capture, BrightCart releases the authorization request.

## Conditions and decision points

- Visa, Mastercard, American Express, and Discover are supported for standard consumer checkout.
- A bank can continue showing a released authorization as pending for several days.
- Split shipments may create more than one capture up to the authorized total.

## Worked example

A customer places a $90 order on Monday and sees a pending $90 amount. The order ships Tuesday, so BrightCart captures the $90 charge on Tuesday. If the order had been canceled Monday before shipment, no final capture should occur.

## Exceptions and edge cases

- Preorders use the preorder payment rule.
- Some digital goods can capture immediately.
- A manual finance adjustment is not a normal card capture.

## Operational notes

When a customer reports two card entries, determine whether one is an authorization and one is a capture before labeling the situation a duplicate charge.
