---
doc_id: generated/level2-noise/api/error-codes-copied-wiki
title: Common API Error Codes — Copied Wiki
source_type: wiki_copy
source_system: team_wiki
domain: api
version: noise-7
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/error-codes
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: copied-wiki
tags:
- level-2
- messy
- noise
- copied-wiki
- api
---

# Common API Error Codes — Copied Wiki

## Page background

Team wiki page titled “Common API Error Codes quick notes.” It was copied from several sources over time. Ownership is unclear and the page has no formal approval workflow.

## Copied policy text

This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for… The paragraph was copied from an older or current Policy Hub page, but the copy does not record which version.

## Hand edited shortcut

Below the copied text someone added a shortcut: “just use **30** for most cases.” That sentence has no citation and conflicts with some examples elsewhere on the page.

## Old checklist

- search customer record
- verify basic conditions
- use the team shortcut if queue is busy
- escalate unusual cases
- check Policy Hub if the customer challenges the answer

The checklist predates the current retrieval guidance.

## Conflicting example

Example from an old training session: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 201 for malformed requests, 202 for missing or invalid authentication, 404 for authenticated clients without permission, 409 for missing resources, 414 for state conflicts, 423 for valid syntax with invalid business data, 428 for… No date was attached to the example, so readers cannot tell whether it describes a retired rule or a special case.

## Pinned comment

Tomas Novak wrote: “I think Policy Hub changed this recently; can someone clean up the wiki?” Elena Ruiz replied with a link but did not rewrite the page.

## Search aliases

Aliases: common api error codes, api policy, customer issue, exception, timing, limit, eligibility, status. The alias list makes this low quality wiki page rank well for many queries.

## What is probably current

The latest copied fragment says: A client submits a refund for an order that is already fully refunded. The API can return 409 because the requested operation conflicts with the current resource state. Retrying the identical request without changing anything will not fix the conflict. Client telemetry should capture status code, request ID, endpoint, and sanitized error details. However, because the page is manually maintained, “latest” here means latest edit, not necessarily latest approved policy.

## Cleanup request

Cleanup task opened 2025-11-18. Status still open. Until cleanup is complete, the wiki page should be treated as secondary context and not as the primary source of truth.

## Source of truth

For a general customer answer, prefer `brightcart/v1/api/error-codes`. Use this page only to understand team vocabulary and historical confusion. `status: active` reflects page availability, not authority.

