---
doc_id: brightcart/v1/security/mfa
title: Multi Factor Authentication
source_type: policy
source_system: policy_hub
domain: security
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/security/mfa
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- security
- policy
---

# Multi Factor Authentication

## Purpose and scope

This policy describes multi factor authentication options and the accounts that must use MFA. It applies to customer accounts and internal administrative access.

## Standard rule

Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it. Recovery codes are generated when authenticator based MFA is enabled and should be stored by the user in a safe place.

## Conditions and decision points

- A verification challenge is required on new or high risk sign ins when MFA is active.
- Recovery codes are single use.
- Changing MFA settings requires a recently verified session.

## Worked example

An administrator signs in with the correct password but cannot access the admin console until the second factor succeeds. There is no option to bypass MFA because the administrator finds it inconvenient.

## Exceptions and edge cases

- Break glass administrator access is handled by a separate emergency process with security approval.
- SMS availability depends on supported phone regions.
- Support cannot read or recover an authenticator secret.

## Operational notes

If a customer loses all second factor methods, use the account recovery process. Do not disable MFA solely based on information available to an unverified chat user.
