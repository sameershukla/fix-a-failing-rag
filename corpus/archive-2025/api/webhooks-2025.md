---
doc_id: brightcart/archive/2025/api/webhooks
title: 'Archived 2025 Copy: Webhook Delivery and Verification'
source_type: archived_policy
source_system: legacy_confluence
domain: api
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/api/webhooks
company: BrightCart
audience:
- support
- operations
tags:
- level-2
- stale
- near-duplicate
- api
- archived
---

# Archived 2025 Copy: Webhook Delivery and Verification

## Purpose and scope

This archived guide covered webhook delivery and verification before the 2026 policy consolidation. This reference explains how BrightCart signs webhook requests and how failed deliveries are retried.

## Archived rule

BrightCart signs webhook requests with HMAC SHA 256 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 2, 10, 30, and 90 minutes before the event is marked undelivered.

## Eligibility details

- Verification should use the raw request body.
- The endpoint should return a successful 2xx response only after accepting the event.
- Consumers should handle duplicate delivery safely.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A webhook endpoint times out on the first delivery. BrightCart retries about one minute later. The receiver verifies the HMAC signature and uses the event ID to avoid processing the same business event twice.

## Exceptions in the archived process

- A permanently disabled endpoint stops receiving new events after it is disabled.
- Manual replay can be available for recent events.
- Network delays can shift retry timing slightly.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the api operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about webhook delivery and verification.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/api/webhooks`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
