---
doc_id: brightcart/v1/shipping/domestic-shipping
title: Domestic Shipping Service Levels
source_type: reference
source_system: policy_hub
domain: shipping
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/shipping/domestic-shipping
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- shipping
- reference
---

# Domestic Shipping Service Levels

## Purpose and scope

This reference lists the normal delivery expectation for shipments within the contiguous United States. It is used for checkout messaging and customer support estimates.

## Standard rule

Standard domestic shipping normally arrives in 3 to 5 business days after the order ships. The estimate begins when the carrier accepts the package, not when the customer places the order. Processing time before shipment is separate.

## Conditions and decision points

- Business days exclude weekends and federal holidays.
- The delivery estimate can vary for Alaska, Hawaii, and remote postal codes.
- A tracking number is created before the carrier may show the first scan.

## Worked example

An order ships on Monday using standard service. With no holiday, the expected delivery range is Thursday through the following Monday. A Tuesday label creation without a carrier acceptance scan does not start the delivery clock.

## Exceptions and edge cases

- Weather and carrier disruptions can extend the estimate.
- Backordered and preorder items have separate ship dates.
- Expedited service follows the expedited shipping article.

## Operational notes

Support should quote the tracking based estimate when available. If the shipment is more than two business days beyond the promised date, use the delayed package runbook.
