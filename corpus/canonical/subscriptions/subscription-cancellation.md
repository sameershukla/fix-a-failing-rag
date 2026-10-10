---
doc_id: brightcart/v1/subscriptions/subscription-cancellation
title: Canceling a Subscription
source_type: policy
source_system: policy_hub
domain: subscriptions
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/subscriptions/subscription-cancellation
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- subscriptions
- policy
---

# Canceling a Subscription

## Purpose and scope

This policy explains what happens when a customer cancels BrightCart Plus. Cancellation stops future renewal but does not automatically reverse a charge that already occurred.

## Standard rule

A cancellation takes effect at the end of the current paid billing period. The customer keeps subscription benefits until that date and the plan does not renew. Cancellation by itself does not create a refund for the current period.

## Conditions and decision points

- The account must have an active subscription.
- The cancellation confirmation shows the benefit end date.
- Future renewal is disabled immediately after cancellation.

## Worked example

A monthly plan renews on the 10th. The customer cancels on the 18th. Benefits continue until the next 10th, and there is no new charge on that date. The charge from the current period is not automatically refunded.

## Exceptions and edge cases

- A qualifying accidental renewal can be refunded under the subscription refund policy.
- A fraud related subscription charge follows the payment dispute process.
- Account deletion does not replace the need to cancel a subscription before deletion.

## Operational notes

Support should distinguish cancel from refund. If the customer asks for both, complete the cancellation and separately evaluate whether the latest charge meets refund rules.
