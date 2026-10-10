---
doc_id: brightcart/v1/gift-cards/gift-card-refunds
title: Refunds for Gift Card and Mixed Payments
source_type: policy
source_system: policy_hub
domain: gift-cards
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-refunds
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- gift-cards
- policy
---

# Refunds for Gift Card and Mixed Payments

## Purpose and scope

This policy explains where refund money goes when an order was paid by gift card or by a combination of gift card and another payment method.

## Standard rule

An amount originally paid by BrightCart gift card is refunded back to that gift card. For mixed payment orders, the refund is returned proportionally to the original payment methods until each method has received its share. Support cannot choose to move the entire refund to a credit card for convenience.

## Conditions and decision points

- The original payment allocation is the source of truth.
- A gift card refund is normally available the same day it is issued.
- Card portions follow normal card posting times.

## Worked example

A $100 order was paid with $40 gift card and $60 Visa. A full refund returns $40 to the gift card and $60 to the Visa. A $50 proportional refund returns $20 to the gift card and $30 to the Visa.

## Exceptions and edge cases

- If the original gift card is disabled for confirmed fraud, payment operations determines the replacement path.
- Promotional credits can have separate expiration rules.
- Chargeback settlements do not follow this customer refund allocation.

## Operational notes

When explaining a mixed refund, show the customer each payment destination and amount. This prevents the customer from expecting the whole refund on one statement.
