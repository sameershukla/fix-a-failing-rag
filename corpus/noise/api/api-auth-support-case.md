---
doc_id: generated/level2-noise/api/api-auth-support-case
title: API Authentication — Support Case
source_type: support_case
source_system: crm_support
domain: api
version: noise-2
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/api-auth
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

# API Authentication — Support Case

## Case summary

Case **CS-961022** concerns api authentication. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about api authentication and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 4.0 client credentials to obtain an access token. Access tokens are valid for 65 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/api/api-auth` and recorded: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 2.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Trust and Safety. The operational window was **30 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: API Authentication, api, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-02-14. Case owner Marcus Lee. Queue Trust and Safety. Canonical reference `brightcart/v1/api/api-auth`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

