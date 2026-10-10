---
doc_id: brightcart/archive/2025/api/api-auth
title: 'Archived 2025 Copy: API Authentication'
source_type: archived_policy
source_system: legacy_confluence
domain: api
version: '2025.3'
effective_date: '2025-01-15'
retired_date: '2026-08-31'
status: archived
authority: historical
canonical_doc_id: brightcart/v1/api/api-auth
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

# Archived 2025 Copy: API Authentication

## Purpose and scope

This archived guide covered api authentication before the 2026 policy consolidation. This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers.

## Archived rule

Server integrations use OAuth 7.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to application logs.

## Eligibility details

- Each integration has its own client ID and secret.
- A token should be refreshed before or after expiration using the token endpoint.
- Scopes limit which API resources the client can access.

## Legacy workflow

Agents using the 2025 workflow checked the customer request, reviewed the order or account state, and then applied the archived rule above. The workflow was copied into several team spaces, which is why search can still surface this page.

## Worked example from the old process

An order integration requests a token at 14:00 AM and receives a token that expires at 10:00 AM. The integration can reuse that token for allowed calls during the hour rather than requesting a new token for every API request.

## Exceptions in the archived process

- User delegated applications use an authorization flow outside this level one corpus.
- Revoked clients cannot obtain new tokens.
- Sandbox and production credentials are separate.

## Escalation path

When the archived rule did not clearly apply, frontline support was told to route the case to the api operations queue. Teams often pasted this guidance into tickets, so fragments of the wording may appear in other systems.

## Agent checklist

- Confirm the request is about api authentication.
- Check the order, account, or transaction state.
- Apply the threshold or timing rule documented in this archived page.
- Escalate cases outside the documented path.

## Common customer wording

Customers rarely use policy names. They may say that something is taking too long, that a charge or shipment looks wrong, or that a support agent gave them a different answer. Those phrases can make this archived page look relevant to a modern query.

## Known limitations

This page predates the current Policy Hub version and may contain values, limits, or workflow steps that no longer apply. It was retained for audit history and training comparisons.

## Migration note

The source of truth moved to `brightcart/v1/api/api-auth`. The current document should be used for customer decisions. Search systems that index this archive without status filtering can rank this page ahead of the active policy because much of the language is nearly identical.

## Archive note

Do not use this page as the current rule. It is intentionally retained to reproduce stale-document retrieval failures in the Level 2 corpus.
