---
doc_id: brightcart/v1/accounts/account-creation
title: Creating a Customer Account
source_type: guide
source_system: policy_hub
domain: accounts
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/accounts/account-creation
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
- guide
---

# Creating a Customer Account

## Purpose and scope

This guide describes the minimum information required for a BrightCart customer account. It is used by support when customers cannot finish registration.

## Standard rule

A customer account requires a unique email address, a password that meets the current password policy, and a verified phone number. One email address can be associated with only one active consumer account.

## Conditions and decision points

- The email verification link must be completed.
- The phone verification code expires after 10 minutes.
- Disposable email domains can be blocked by risk controls.

## Worked example

A customer enters an email already tied to an existing account. Registration stops and directs the customer to sign in or reset the existing account rather than creating a duplicate identity.

## Exceptions and edge cases

- Business organizations can have multiple users under one company profile while each user still has a unique email.
- Guest checkout does not automatically create a full account.
- Support cannot bypass phone verification for convenience.

## Operational notes

When registration fails, identify whether the problem is email duplication, password validation, phone verification, or a risk block before recommending a fix.
