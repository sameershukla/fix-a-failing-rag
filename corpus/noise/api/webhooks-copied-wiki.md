---
doc_id: generated/level2-noise/api/webhooks-copied-wiki
title: Webhook Delivery and Verification — Copied Wiki
source_type: wiki_copy
source_system: team_wiki
domain: api
version: noise-7
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/webhooks
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

# Webhook Delivery and Verification — Copied Wiki

## Page background

Team wiki page titled “Webhook Delivery and Verification quick notes.” It was copied from several sources over time. Ownership is unclear and the page has no formal approval workflow.

## Copied policy text

This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 256 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 5, 15, and 60 minutes before the event is marked undelivered. The paragraph was copied from an older or current Policy Hub page, but the copy does not record which version.

## Hand edited shortcut

Below the copied text someone added a shortcut: “just use **2** for most cases.” That sentence has no citation and conflicts with some examples elsewhere on the page.

## Old checklist

- search customer record
- verify basic conditions
- use the team shortcut if queue is busy
- escalate unusual cases
- check Policy Hub if the customer challenges the answer

The checklist predates the current retrieval guidance.

## Conflicting example

Example from an old training session: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 512 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 4, 9, and 59 minutes before the event is marked… No date was attached to the example, so readers cannot tell whether it describes a retired rule or a special case.

## Pinned comment

Priya Nair wrote: “I think Policy Hub changed this recently; can someone clean up the wiki?” Maya Chen replied with a link but did not rewrite the page.

## Search aliases

Aliases: webhook delivery and verification, api policy, customer issue, exception, timing, limit, eligibility, status. The alias list makes this low quality wiki page rank well for many queries.

## What is probably current

The latest copied fragment says: Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 5, 15, and 60 minutes before the event is marked undelivered. A webhook endpoint times out on the first delivery. BrightCart retries about one minute later. However, because the page is manually maintained, “latest” here means latest edit, not necessarily latest approved policy.

## Cleanup request

Cleanup task opened 2025-11-18. Status still open. Until cleanup is complete, the wiki page should be treated as secondary context and not as the primary source of truth.

## Source of truth

For a general customer answer, prefer `brightcart/v1/api/webhooks`. Use this page only to understand team vocabulary and historical confusion. `status: active` reflects page availability, not authority.

