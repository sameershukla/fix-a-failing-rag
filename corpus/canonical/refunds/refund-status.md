---
doc_id: brightcart/v1/refunds/refund-status
title: Refund Status and Failed Refunds
source_type: runbook
source_system: policy_hub
domain: refunds
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/refunds/refund-status
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- refunds
- runbook
---

# Refund Status and Failed Refunds

## Purpose and scope

This runbook explains the refund lifecycle visible to support and the action to take when a refund fails. It is intended for customer support and payment operations.

## Standard rule

Refunds move through pending, issued, or failed status. A failed refund is retried automatically one time. If the retry also fails, the case must be sent to payment operations for manual review. Support must not create a second independent refund.

## Conditions and decision points

- Pending means BrightCart has accepted the request but the processor has not confirmed it.
- Issued means the processor accepted the refund.
- Failed means the processor rejected the request or the refund could not be completed.

## Worked example

A refund fails because the card account is closed. The platform retries once and receives the same failure. The support agent opens a payment operations case with the order ID and refund reference instead of pressing refund again.

## Exceptions and edge cases

- Processor outages can leave a refund pending longer than usual without marking it failed.
- Fraud holds are reviewed by risk and should not be bypassed by support.
- Manual payment methods may require finance rather than payment operations.

## Operational notes

Before escalating, capture the order ID, refund ID, processor message, payment method, and timestamps for both attempts. Duplicate refund creation is considered a payment incident.
