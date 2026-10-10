---
doc_id: brightcart/v3/restricted/restricted-large-credit
title: Large Credit Approval Standard
source_type: restricted_policy
source_system: restricted_wiki
domain: finance
version: '3.0'
effective_date: '2026-10-01'
status: active
authority: primary
company: BrightCart
team: Finance Risk
environment: prod
access_group: finance-restricted
owner: Finance Risk
language: en
region: US
retrieval_hazard: ACL enforcement
tags:
- enterprise-expansion
- restricted
- access-control
- module-5
---

# Large Credit Approval Standard

## Rule

A credit above $10,000 requires an approval from finance-approvers and expires after 60 minutes if nobody approves it.

## Access

This page is restricted to `finance-restricted`. Retrieval systems must filter by the caller's allowed access groups before generation.
