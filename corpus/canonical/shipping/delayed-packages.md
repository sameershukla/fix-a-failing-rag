---
doc_id: brightcart/v1/shipping/delayed-packages
title: Delayed Package Handling
source_type: runbook
source_system: policy_hub
domain: shipping
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/shipping/delayed-packages
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
- runbook
---

# Delayed Package Handling

## Purpose and scope

This runbook defines when support should treat a shipment as delayed and what checks to perform before replacing or refunding an order.

## Standard rule

A package is considered delayed when it is more than 2 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless there is evidence of loss or damage.

## Conditions and decision points

- Use the latest promised date shown on the order.
- Check for carrier exception scans and address problems.
- Confirm that the package was not delivered to a mailroom, parcel locker, or household member.

## Worked example

The order page promises delivery by Wednesday. On Thursday the package is one business day late, so support provides the latest tracking update. If it is still undelivered after Friday, it meets the delayed package threshold.

## Exceptions and edge cases

- A carrier scan that explicitly says lost can move directly to the lost package process.
- Temperature sensitive items may require earlier action.
- A customer reported theft after confirmed delivery follows the delivered not received process, which is outside this corpus.

## Operational notes

Open a carrier trace when required and record the promised date, last scan, and customer confirmation. Do not issue duplicate replacements while an earlier replacement is already in transit.
