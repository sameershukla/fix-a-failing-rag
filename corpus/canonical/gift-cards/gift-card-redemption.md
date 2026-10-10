---
doc_id: brightcart/v1/gift-cards/gift-card-redemption
title: Redeeming Gift Cards
source_type: reference
source_system: policy_hub
domain: gift-cards
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-redemption
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
- reference
---

# Redeeming Gift Cards

## Purpose and scope

This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total.

## Standard rule

Customers can apply up to 3 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with another supported payment method.

## Conditions and decision points

- The gift card must be active and have a positive balance.
- The checkout displays the amount taken from each card.
- Gift cards cannot be redeemed for cash through normal checkout.

## Worked example

A customer has gift cards with $25 and $40 balances and buys a $50 item. Checkout can use $25 from the first card and $25 from the second, leaving $15 on the second card.

## Exceptions and edge cases

- Fraud locked gift cards cannot be redeemed until reviewed.
- Some restricted products may not accept promotional credits, but normal gift cards remain valid.
- More than three gift cards requires customer care assistance and is not guaranteed.

## Operational notes

If redemption fails, verify the card status and balance before replacing anything. Do not create a new gift card simply because a customer entered the code incorrectly.
