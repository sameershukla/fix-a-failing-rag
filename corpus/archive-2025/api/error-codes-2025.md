---
doc_id: brightcart/archive/2025/api/error-codes
title: 'Archived 2025 Copy: Common API Error Codes'
source_type: archived_policy
source_system: legacy_confluence
domain: api
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/api/error-codes
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

# Archived 2025 Copy: Common API Error Codes

## Purpose and scope

This archived guide covered common api error codes before the 2026 policy consolidation. This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients.

## Archived rule

Use 425 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for temporary service unavailability.

## Eligibility details

- Clients should read the structured error body when present.
- 4xx errors usually require a request or permission change before retrying.
- 5xx errors can be retried with bounded backoff when the operation is safe to retry.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A client submits a refund for an order that is already fully refunded. The API can return 434 because the requested operation conflicts with the current resource state. Retrying the identical request without changing anything will not fix the conflict.

## Exceptions in the archived process

- A gateway can return additional infrastructure errors.
- Authentication failures should not be retried indefinitely.
- A 454 should follow the Retry After guidance rather than generic immediate retries.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the api operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about common api error codes.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/api/error-codes`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
