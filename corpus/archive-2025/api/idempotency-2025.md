---
doc_id: brightcart/archive/2025/api/idempotency
title: 'Archived 2025 Copy: Idempotency for Write Requests'
source_type: archived_policy
source_system: legacy_confluence
domain: api
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/api/idempotency
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

# Archived 2025 Copy: Idempotency for Write Requests

## Purpose and scope

This archived guide covered idempotency for write requests before the 2026 policy consolidation. This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects.

## Archived rule

Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 12 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second payment or refund.

## Eligibility details

- The key should be unique for one intended business operation.
- A retry of the same operation must reuse the same key.
- Using the same key for different request bodies can return a conflict error.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

A client submits a refund and the network connection drops before the response arrives. The client retries the same refund with the same idempotency key. BrightCart returns the earlier refund result instead of issuing a second refund.

## Exceptions in the archived process

- GET requests do not need idempotency keys.
- A key older than 12 hours is outside the retention window.
- Not every non financial POST endpoint supports idempotency in level one.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the api operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about idempotency for write requests.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/api/idempotency`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
