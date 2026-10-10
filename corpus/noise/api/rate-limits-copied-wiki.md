---
doc_id: generated/level2-noise/api/rate-limits-copied-wiki
title: API Rate Limits — Copied Wiki
source_type: wiki_copy
source_system: team_wiki
domain: api
version: noise-7
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/rate-limits
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

# API Rate Limits — Copied Wiki

## Page background

Team wiki page titled “API Rate Limits quick notes.” It was copied from several sources over time. Ownership is unclear and the page has no formal approval workflow.

## Copied policy text

This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 600 requests per minute per client. When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop. The paragraph was copied from an older or current Policy Hub page, but the copy does not record which version.

## Hand edited shortcut

Below the copied text someone added a shortcut: “just use **60** for most cases.” That sentence has no citation and conflicts with some examples elsewhere on the page.

## Old checklist

- search customer record
- verify basic conditions
- use the team shortcut if queue is busy
- escalate unusual cases
- check Policy Hub if the customer challenges the answer

The checklist predates the current retrieval guidance.

## Conflicting example

Example from an old training session: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 601 requests per minute per client. When the limit is exceeded, the API returns HTTP 216 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead… No date was attached to the example, so readers cannot tell whether it describes a retired rule or a special case.

## Pinned comment

Elena Ruiz wrote: “I think Policy Hub changed this recently; can someone clean up the wiki?” Ifeoma Okafor replied with a link but did not rewrite the page.

## Search aliases

Aliases: api rate limits, api policy, customer issue, exception, timing, limit, eligibility, status. The alias list makes this low quality wiki page rank well for many queries.

## What is probably current

The latest copied fragment says: When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop. An integration sends more than 600 requests within the active minute and receives 429 responses with Retry After: 20. The client waits at least 20 seconds and resumes gradually rather than sending the failed requests all… However, because the page is manually maintained, “latest” here means latest edit, not necessarily latest approved policy.

## Cleanup request

Cleanup task opened 2026-05-29. Status still open. Until cleanup is complete, the wiki page should be treated as secondary context and not as the primary source of truth.

## Source of truth

For a general customer answer, prefer `brightcart/v1/api/rate-limits`. Use this page only to understand team vocabulary and historical confusion. `status: active` reflects page availability, not authority.

