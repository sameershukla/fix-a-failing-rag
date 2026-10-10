---
doc_id: brightcart/v1/support/escalation
title: Support Escalation Path
source_type: runbook
source_system: policy_hub
domain: support
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/support/escalation
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- support
- runbook
---

# Support Escalation Path

## Purpose and scope

This runbook defines when a support case should move beyond the front line queue. It gives agents a consistent escalation path for complex or high risk situations.

## Standard rule

Routine product and order questions stay with Level 1 support. Cases needing deeper product or payment investigation move to Level 2. Suspected security events, material financial loss, broad service impact, or repeated system failure should be escalated immediately to the incident or specialist team rather than waiting for normal queue aging.

## Conditions and decision points

- Include the customer impact and what has already been checked.
- Use the payment queue for processor issues and the security queue for takeover or data exposure.
- A broad outage should not be handled as dozens of unrelated tickets.

## Worked example

Three customers report the same checkout error within minutes and monitoring also shows failures. Instead of sending each case separately to Level 2, support links the reports and starts the incident path.

## Exceptions and edge cases

- A known incident with an active status page update does not need a new incident for every customer.
- Executive visibility alone does not change technical severity.
- Immediate safety threats should follow emergency procedures.

## Operational notes

Every escalation should contain the reason, impact, evidence, timestamps, and owner. A vague note such as please investigate is not sufficient handoff context.
