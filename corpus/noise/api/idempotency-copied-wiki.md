---
doc_id: generated/level2-noise/api/idempotency-copied-wiki
title: Idempotency for Write Requests — Copied Wiki
source_type: wiki_copy
source_system: team_wiki
domain: api
version: noise-7
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/idempotency
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

# Idempotency for Write Requests — Copied Wiki

## Page background

Team wiki page titled “Idempotency for Write Requests quick notes.” It was copied from several sources over time. Ownership is unclear and the page has no formal approval workflow.

## Copied policy text

This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 24 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second… The paragraph was copied from an older or current Policy Hub page, but the copy does not record which version.

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

Example from an old training session: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 29 hours. Repeating the same request with the same key during that period returns the… No date was attached to the example, so readers cannot tell whether it describes a retired rule or a special case.

## Pinned comment

Mei Wong wrote: “I think Policy Hub changed this recently; can someone clean up the wiki?” Dana Whitfield replied with a link but did not rewrite the page.

## Search aliases

Aliases: idempotency for write requests, api policy, customer issue, exception, timing, limit, eligibility, status. The alias list makes this low quality wiki page rank well for many queries.

## What is probably current

The latest copied fragment says: BrightCart remembers the result for 24 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second payment or refund. A client submits a refund and the network connection drops before the response arrives. The client retries the same refund with the same idempotency key. However, because the page is manually maintained, “latest” here means latest edit, not necessarily latest approved policy.

## Cleanup request

Cleanup task opened 2026-04-03. Status still open. Until cleanup is complete, the wiki page should be treated as secondary context and not as the primary source of truth.

## Source of truth

For a general customer answer, prefer `brightcart/v1/api/idempotency`. Use this page only to understand team vocabulary and historical confusion. `status: active` reflects page availability, not authority.

