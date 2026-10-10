---
doc_id: brightcart/v1/accounts/account-deletion
title: Customer Account Deletion
source_type: policy
source_system: policy_hub
domain: accounts
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/accounts/account-deletion
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

# Customer Account Deletion

## Purpose and scope

This policy explains what happens after a customer requests deletion of a BrightCart account. It separates user visible account removal from data that must be retained for legal or financial reasons.

## Standard rule

After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 30 days. Certain transaction, tax, fraud, and legal records can be retained when required by law or legitimate business obligations even after the account is no longer active.

## Conditions and decision points

- Identity verification is required before deletion starts.
- Active subscription renewal should be canceled before the account is closed.
- Open refunds or disputes may need to finish before some data is archived.

## Worked example

A verified customer requests deletion on August 1. BrightCart disables normal account use and completes the deletion process by August 31, while retaining required invoice records in restricted systems for the legally required period.

## Exceptions and edge cases

- A legal hold can delay deletion of specific records.
- Fraud investigation evidence may be retained under security policy.
- Deleting an account does not erase data held by an independent bank or carrier.

## Operational notes

Support should confirm the request date and explain that deletion is not the same as erasing every record immediately. Privacy questions beyond the standard process should be escalated to the privacy team.
