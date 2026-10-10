---
doc_id: generated/level2-noise/api/api-auth-copied-wiki
title: API Authentication — Copied Wiki
source_type: wiki_copy
source_system: team_wiki
domain: api
version: noise-7
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/api-auth
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

# API Authentication — Copied Wiki

## Page background

Team wiki page titled “API Authentication quick notes.” It was copied from several sources over time. Ownership is unclear and the page has no formal approval workflow.

## Copied policy text

This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 2.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes. The paragraph was copied from an older or current Policy Hub page, but the copy does not record which version.

## Hand edited shortcut

Below the copied text someone added a shortcut: “just use **5** for most cases.” That sentence has no citation and conflicts with some examples elsewhere on the page.

## Old checklist

- search customer record
- verify basic conditions
- use the team shortcut if queue is busy
- escalate unusual cases
- check Policy Hub if the customer challenges the answer

The checklist predates the current retrieval guidance.

## Conflicting example

Example from an old training session: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 4.0 client credentials to obtain an access token. Access tokens are valid for 120 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to… No date was attached to the example, so readers cannot tell whether it describes a retired rule or a special case.

## Pinned comment

Priya Nair wrote: “I think Policy Hub changed this recently; can someone clean up the wiki?” Ifeoma Okafor replied with a link but did not rewrite the page.

## Search aliases

Aliases: api authentication, api policy, customer issue, exception, timing, limit, eligibility, status. The alias list makes this low quality wiki page rank well for many queries.

## What is probably current

The latest copied fragment says: Server integrations use OAuth 2.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to application logs. An order integration requests a token at 9:00 AM and receives a token that expires at 10:00 AM. However, because the page is manually maintained, “latest” here means latest edit, not necessarily latest approved policy.

## Cleanup request

Cleanup task opened 2026-07-11. Status still open. Until cleanup is complete, the wiki page should be treated as secondary context and not as the primary source of truth.

## Source of truth

For a general customer answer, prefer `brightcart/v1/api/api-auth`. Use this page only to understand team vocabulary and historical confusion. `status: active` reflects page availability, not authority.

