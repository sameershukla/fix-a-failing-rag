---
doc_id: brightcart/v1/accounts/password-reset
title: Password Reset Process
source_type: runbook
source_system: policy_hub
domain: accounts
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/accounts/password-reset
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
- runbook
---

# Password Reset Process

## Purpose and scope

This runbook explains the self service password reset flow and how support should handle expired or already used links.

## Standard rule

A password reset link is valid for 30 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid.

## Conditions and decision points

- The reset request is sent to the verified account email.
- The new password must meet the active password policy.
- Support never asks the customer to reveal the new password.

## Worked example

A customer requests a reset at 2:00 PM and again at 2:10 PM. The first link becomes invalid when the second request is created. The second link remains valid until 2:40 PM unless it is used earlier.

## Exceptions and edge cases

- Security can force an immediate password reset after suspicious activity.
- Accounts under legal hold can still reset passwords.
- A locked account may require the lockout timer or security review in addition to a password reset.

## Operational notes

If a reset email does not arrive, verify the email address, spam folder, and account status. Do not manually set a password on behalf of the customer.
