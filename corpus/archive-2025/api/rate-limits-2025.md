---
doc_id: brightcart/archive/2025/api/rate-limits
title: 'Archived 2025 Copy: API Rate Limits'
source_type: archived_policy
source_system: legacy_confluence
domain: api
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/api/rate-limits
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

# Archived 2025 Copy: API Rate Limits

## Purpose and scope

This archived guide covered api rate limits before the 2026 policy consolidation. This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded.

## Archived rule

The default public API limit is 300 requests per minute per client. When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop.

## Eligibility details

- The limit is measured per registered client.
- Short traffic bursts can consume the available window quickly.
- Repeated 454 responses can indicate a design problem in polling or retry logic.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

An integration sends more than 625 requests within the active minute and receives 429 responses with Retry After: 20. The client waits at least 20 seconds and resumes gradually rather than sending the failed requests all at once.

## Exceptions in the archived process

- Some contracted integrations can have a different approved limit.
- Webhook delivery does not consume the client's inbound API quota.
- A 528 service unavailable response is not a rate limit response.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the api operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about api rate limits.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/api/rate-limits`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
