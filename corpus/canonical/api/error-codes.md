---
doc_id: brightcart/v1/api/error-codes
title: Common API Error Codes
source_type: reference
source_system: policy_hub
domain: api
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/api/error-codes
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

# Common API Error Codes

## Purpose and scope

This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients.

## Standard rule

Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for temporary service unavailability.

## Conditions and decision points

- Clients should read the structured error body when present.
- 4xx errors usually require a request or permission change before retrying.
- 5xx errors can be retried with bounded backoff when the operation is safe to retry.

## Worked example

A client submits a refund for an order that is already fully refunded. The API can return 409 because the requested operation conflicts with the current resource state. Retrying the identical request without changing anything will not fix the conflict.

## Exceptions and edge cases

- A gateway can return additional infrastructure errors.
- Authentication failures should not be retried indefinitely.
- A 429 should follow the Retry After guidance rather than generic immediate retries.

## Operational notes

Client telemetry should capture status code, request ID, endpoint, and sanitized error details. Use idempotency for retryable write operations.
