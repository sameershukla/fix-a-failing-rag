---
doc_id: brightcart/v1/api/idempotency
title: Idempotency for Write Requests
source_type: reference
source_system: policy_hub
domain: api
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/api/idempotency
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- api
- reference
---

# Idempotency for Write Requests

## Purpose and scope

This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects.

## Standard rule

Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 24 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second payment or refund.

## Conditions and decision points

- The key should be unique for one intended business operation.
- A retry of the same operation must reuse the same key.
- Using the same key for different request bodies can return a conflict error.

## Worked example

A client submits a refund and the network connection drops before the response arrives. The client retries the same refund with the same idempotency key. BrightCart returns the earlier refund result instead of issuing a second refund.

## Exceptions and edge cases

- GET requests do not need idempotency keys.
- A key older than 24 hours is outside the retention window.
- Not every non financial POST endpoint supports idempotency in level one.

## Operational notes

Log the idempotency key alongside the client operation ID, but do not use secrets or customer payment data as the key value.
