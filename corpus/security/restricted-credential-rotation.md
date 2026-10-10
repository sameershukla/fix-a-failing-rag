---
doc_id: brightcart/v3/restricted/restricted-credential-rotation
title: Credential Rotation Incident
source_type: restricted_policy
source_system: restricted_wiki
domain: security
version: '3.0'
effective_date: '2026-10-01'
status: active
authority: primary
company: BrightCart
team: Security Engineering
environment: prod
access_group: security-restricted
owner: Security Engineering
language: en
region: US
retrieval_hazard: ACL enforcement
tags:
- enterprise-expansion
- restricted
- access-control
- module-5
---

# Credential Rotation Incident

## Rule

A leaked production token must be revoked within 15 minutes of confirmation and rotated in every dependent service before the incident is closed.

## Access

This page is restricted to `security-restricted`. Retrieval systems must filter by the caller's allowed access groups before generation.
