---
doc_id: brightcart/v1/support/severity
title: Incident Severity Levels
source_type: reference
source_system: policy_hub
domain: support
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/support/severity
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
- reference
---

# Incident Severity Levels

## Purpose and scope

This reference defines BrightCart incident severity so teams use the same language when deciding response urgency.

## Standard rule

SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 3 covers moderate issues, and SEV 4 covers low impact defects or questions.

## Conditions and decision points

- Severity is based on customer and business impact, not the job title of the reporter.
- Security can raise severity based on data risk even when few customers are affected.
- Severity can change as new evidence appears.

## Worked example

Checkout fails for most customers in all regions with no workaround. That is SEV 1. If one payment method fails but customers can use another method, the incident may begin as SEV 2 depending on scale.

## Exceptions and edge cases

- Planned maintenance is not automatically an incident.
- A single high value customer does not automatically make an issue SEV 1.
- A confirmed sensitive data exposure can be SEV 1 despite limited traffic impact.

## Operational notes

The incident commander owns severity during an active incident. Changes to severity should include a short reason in the incident timeline.
