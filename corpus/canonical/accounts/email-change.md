---
doc_id: brightcart/v1/accounts/email-change
title: Changing the Account Email Address
source_type: runbook
source_system: policy_hub
domain: accounts
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/accounts/email-change
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

# Changing the Account Email Address

## Purpose and scope

This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account.

## Standard rule

To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change. The new email becomes the sign in identifier only after verification succeeds.

## Conditions and decision points

- The new email cannot already belong to another active consumer account.
- The verification code expires after 15 minutes.
- A recently recovered account can be temporarily blocked from email changes.

## Worked example

A signed in customer enters a new email but does not complete verification. The account continues using the old email. Once the verification code is completed, the new address becomes active and the old address receives a change notice.

## Exceptions and edge cases

- Customers who no longer control the old account credentials must use account recovery rather than a normal email change.
- Security can freeze profile changes during an active takeover investigation.
- Business administrator changes follow organization controls.

## Operational notes

If a customer reports an email change they did not make, treat it as suspicious account activity and follow the session revocation process.
