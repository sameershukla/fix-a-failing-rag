---
doc_id: brightcart/v1/returns/return-shipping
title: Return Shipping Charges
source_type: policy
source_system: policy_hub
domain: returns
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/returns/return-shipping
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- returns
- policy
---

# Return Shipping Charges

## Purpose and scope

This article explains who pays to send an item back to BrightCart. It applies after a return has been approved and before the label is generated.

## Standard rule

BrightCart pays return shipping when the item is defective, damaged in transit, or different from what the customer ordered. For preference returns such as size, color, or changed mind, the customer pays the return shipping charge unless a promotion explicitly provides free returns.

## Conditions and decision points

- The selected return reason must match the case notes.
- A prepaid label can be issued when BrightCart is responsible.
- Customer paid return costs are shown before the customer confirms the return.

## Worked example

A customer orders a blue backpack and receives a red backpack. BrightCart provides a prepaid label because the wrong item was shipped. If the customer received the blue backpack but later prefers black, the normal customer paid return shipping rule applies.

## Exceptions and edge cases

- VIP free return promotions can override the preference rule during their valid dates.
- Do not charge return shipping for an order canceled before shipment.
- Oversize freight returns require logistics review instead of a standard label.

## Operational notes

If the return reason changes after inspection, support should correct the case and any shipping charge. Do not use a free label reason merely to satisfy a customer complaint.
