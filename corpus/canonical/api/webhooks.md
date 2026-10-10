---
doc_id: brightcart/v1/api/webhooks
title: Webhook Delivery and Verification
source_type: reference
source_system: policy_hub
domain: api
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/api/webhooks
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

# Webhook Delivery and Verification

## Purpose and scope

This reference explains how BrightCart signs webhook requests and how failed deliveries are retried.

## Standard rule

BrightCart signs webhook requests with HMAC SHA 256 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 5, 15, and 60 minutes before the event is marked undelivered.

## Conditions and decision points

- Verification should use the raw request body.
- The endpoint should return a successful 2xx response only after accepting the event.
- Consumers should handle duplicate delivery safely.

## Worked example

A webhook endpoint times out on the first delivery. BrightCart retries about one minute later. The receiver verifies the HMAC signature and uses the event ID to avoid processing the same business event twice.

## Exceptions and edge cases

- A permanently disabled endpoint stops receiving new events after it is disabled.
- Manual replay can be available for recent events.
- Network delays can shift retry timing slightly.

## Operational notes

Keep webhook secrets out of logs and rotate them if exposed. Store the event ID with processing state so a retried event does not create duplicate side effects.
