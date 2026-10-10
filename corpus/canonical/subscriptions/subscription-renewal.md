---
doc_id: brightcart/v1/subscriptions/subscription-renewal
title: Subscription Renewal Notices
source_type: policy
source_system: policy_hub
domain: subscriptions
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/subscriptions/subscription-renewal
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

# Subscription Renewal Notices

## Purpose and scope

This article describes automatic renewal and the reminder BrightCart sends for annual plans. Monthly subscriptions renew without a separate monthly reminder.

## Standard rule

BrightCart Plus subscriptions renew automatically unless canceled. For annual plans, BrightCart sends a renewal reminder 7 days before the renewal date to the account email address. The reminder includes the scheduled renewal date and the current renewal price.

## Conditions and decision points

- The email address on the account must be valid to receive the reminder.
- The renewal date is visible in account settings.
- Updating the payment method does not change the renewal date.

## Worked example

An annual subscription renews on October 20. BrightCart sends the reminder on October 13. If the customer cancels on October 18, the renewal is stopped and benefits end on October 20.

## Exceptions and edge cases

- Corporate plans can use contract specific notices.
- A bounced email does not automatically stop renewal.
- Emergency service notices are separate from renewal reminders.

## Operational notes

When a customer says no reminder arrived, support should verify the account email and message history. Missing mail alone does not prove the renewal was unauthorized.
