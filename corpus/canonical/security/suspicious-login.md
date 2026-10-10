---
doc_id: brightcart/v1/security/suspicious-login
title: Suspicious Login Response
source_type: runbook
source_system: policy_hub
domain: security
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/security/suspicious-login
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
- runbook
---

# Suspicious Login Response

## Purpose and scope

This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly.

## Standard rule

For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified channel. High confidence account takeover cases are escalated to security.

## Conditions and decision points

- Confirm the customer identity before discussing account details.
- Review recent email, phone, shipping address, and saved payment changes.
- Check whether MFA was added, removed, or challenged.

## Worked example

A customer receives a new device alert from a city they did not visit. After identity verification, support revokes sessions and starts a password reset. The account shows an unauthorized shipping address change, so the case is escalated to security.

## Exceptions and edge cases

- Travel or VPN use can create a false positive alert.
- A failed login attempt alone is not proof of takeover.
- Active fraud or payment theft can require immediate order cancellation.

## Operational notes

Document the alert time, suspicious session, customer confirmation, session revocation, and any profile changes. Do not leave the account active while waiting for a routine queue if takeover is likely.
