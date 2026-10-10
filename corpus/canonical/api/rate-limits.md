---
doc_id: brightcart/v1/api/rate-limits
title: API Rate Limits
source_type: reference
source_system: policy_hub
domain: api
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/api/rate-limits
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

# API Rate Limits

## Purpose and scope

This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded.

## Standard rule

The default public API limit is 600 requests per minute per client. When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop.

## Conditions and decision points

- The limit is measured per registered client.
- Short traffic bursts can consume the available window quickly.
- Repeated 429 responses can indicate a design problem in polling or retry logic.

## Worked example

An integration sends more than 600 requests within the active minute and receives 429 responses with Retry After: 20. The client waits at least 20 seconds and resumes gradually rather than sending the failed requests all at once.

## Exceptions and edge cases

- Some contracted integrations can have a different approved limit.
- Webhook delivery does not consume the client's inbound API quota.
- A 503 service unavailable response is not a rate limit response.

## Operational notes

Record rate limit headers in client telemetry. If normal traffic consistently needs more capacity, request a limit review instead of ignoring 429 responses.
