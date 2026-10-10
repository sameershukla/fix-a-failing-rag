---
doc_id: brightcart/v1/api/api-auth
title: API Authentication
source_type: reference
source_system: policy_hub
domain: api
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/api/api-auth
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

# API Authentication

## Purpose and scope

This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers.

## Standard rule

Server integrations use OAuth 2.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to application logs.

## Conditions and decision points

- Each integration has its own client ID and secret.
- A token should be refreshed before or after expiration using the token endpoint.
- Scopes limit which API resources the client can access.

## Worked example

An order integration requests a token at 9:00 AM and receives a token that expires at 10:00 AM. The integration can reuse that token for allowed calls during the hour rather than requesting a new token for every API request.

## Exceptions and edge cases

- User delegated applications use an authorization flow outside this level one corpus.
- Revoked clients cannot obtain new tokens.
- Sandbox and production credentials are separate.

## Operational notes

If a secret is exposed, rotate it immediately and review logs for unauthorized use. Do not solve authentication errors by placing secrets in URLs.
