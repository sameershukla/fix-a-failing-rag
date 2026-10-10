---
doc_id: brightcart/v1/returns/return-window
title: Standard Return Window
source_type: policy
source_system: policy_hub
domain: returns
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/returns/return-window
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

# Standard Return Window

## Purpose and scope

This policy defines the default period in which customers can request a return. It should be checked before product specific restrictions such as electronics or final sale rules.

## Standard rule

The standard return window is 30 calendar days from the carrier confirmed delivery date. The request must be opened by the end of day on day 30. Shipping time back to the warehouse does not need to fit inside the 30 day window.

## Conditions and decision points

- Use the actual delivery date when available.
- If a package was never delivered, handle it as a delivery problem rather than a late return.
- A return request is considered opened when a case or self service return authorization is created.

## Worked example

An order delivered on April 2 can have a standard return request opened through May 2. If the customer ships the package on May 4 using the approved label, the request is still timely because it was opened within the window.

## Exceptions and edge cases

- Electronics have a separate 14 day rule.
- Holiday extensions may be announced in a dated seasonal notice.
- Warranty claims are not limited by the normal return window.

## Operational notes

Agents should record the delivery date and the date the return was requested. If the dates are uncertain, use the carrier record rather than a customer estimate.
