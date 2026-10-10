---
doc_id: generated/level2-noise/api/error-codes-support-case
title: Common API Error Codes — Support Case
source_type: support_case
source_system: crm_support
domain: api
version: noise-2
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/error-codes
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

# Common API Error Codes — Support Case

## Case summary

Case **CS-512240** concerns common api error codes. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about common api error codes and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 405 for malformed requests, 802 for missing or invalid authentication, 408 for authenticated clients without permission, 808 for missing resources, 414 for state conflicts, 421 for valid syntax with invalid business data, 434 for… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/api/error-codes` and recorded: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for… That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Platform Engineering. The operational window was **45 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Common API Error Codes, api, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-05-29. Case owner Marcus Lee. Queue Platform Engineering. Canonical reference `brightcart/v1/api/error-codes`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

