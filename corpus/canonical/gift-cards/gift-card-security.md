---
doc_id: brightcart/v1/gift-cards/gift-card-security
title: Lost and Stolen Gift Cards
source_type: runbook
source_system: policy_hub
domain: gift-cards
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-security
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
- runbook
---

# Lost and Stolen Gift Cards

## Purpose and scope

This runbook covers claims that a gift card code was lost, deleted, or stolen. Gift cards are cash like instruments, so replacement requires evidence of ownership.

## Standard rule

BrightCart may replace a lost digital gift card only when the claimant can verify the original purchase or recipient information and the remaining balance has not been spent. Gift cards are not redeemable for cash and spent balances are not restored merely because the code was shared with another person.

## Conditions and decision points

- Verify order number or purchaser account when possible.
- Check redemption history before replacement.
- Freeze the remaining balance when fraud is reasonably suspected.

## Worked example

A buyer deleted the original email but can verify the gift card order and recipient address. The card still has its full balance. Support can resend or replace the code after verification.

## Exceptions and edge cases

- A fully redeemed card normally has no balance to replace.
- Confirmed account takeover cases are handled with security.
- Corporate bulk cards follow the business contract.

## Operational notes

Never paste complete gift card codes into general support notes. Record masked identifiers and the replacement decision.
