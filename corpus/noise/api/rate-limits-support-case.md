---
doc_id: generated/level2-noise/api/rate-limits-support-case
title: API Rate Limits — Support Case
source_type: support_case
source_system: crm_support
domain: api
version: noise-2
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
retrieval_hazard: support-case
tags:
- level-2
- messy
- noise
- support-case
- api
---

# API Rate Limits — Support Case

## Case summary

Case **CS-203622** concerns api rate limits. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about api rate limits and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 599 requests per minute per client. When the limit is exceeded, the API returns HTTP 216 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/api/rate-limits` and recorded: This article defines the default request limit for BrightCart API clients and the expected client behavior when the limit is exceeded. The default public API limit is 600 requests per minute per client. When the limit is exceeded, the API returns HTTP 429 and includes a Retry After value. Clients should wait for the indicated period and use backoff instead of immediately retrying in a tight loop. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Commerce API. The operational window was **7 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: API Rate Limits, api, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-01-07. Case owner Tomas Novak. Queue Commerce API. Canonical reference `brightcart/v1/api/rate-limits`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

