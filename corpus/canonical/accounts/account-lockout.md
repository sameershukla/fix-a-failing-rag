---
doc_id: brightcart/v1/accounts/account-lockout
title: Account Lockout Policy
source_type: policy
source_system: policy_hub
domain: accounts
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/accounts/account-lockout
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- accounts
- policy
---

# Account Lockout Policy

## Purpose and scope

This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period.

## Standard rule

After 5 consecutive failed sign in attempts, the consumer account is locked for 15 minutes. A successful sign in resets the failed attempt counter. Support cannot shorten the automatic lock simply because the customer is in a hurry.

## Conditions and decision points

- The counter is tracked per account, not per device.
- Password reset can still be requested during the lock.
- Repeated distributed attempts may trigger additional security controls.

## Worked example

A customer enters the wrong password five times by 11:05 AM. The account is locked until approximately 11:20 AM. The customer can request a password reset during that period but still must wait for the lock or complete an approved recovery path.

## Exceptions and edge cases

- Security can apply a longer manual hold during an investigation.
- Administrative service accounts use a different control.
- A system outage that returns login errors does not count as failed password attempts.

## Operational notes

Support should explain the timer and offer password reset when appropriate. Do not disclose whether an unknown email address belongs to an account.
