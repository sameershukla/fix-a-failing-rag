---
doc_id: generated/level2-noise/api/idempotency-support-case
title: Idempotency for Write Requests — Support Case
source_type: support_case
source_system: crm_support
domain: api
version: noise-2
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/idempotency
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

# Idempotency for Write Requests — Support Case

## Case summary

Case **CS-213318** concerns idempotency for write requests. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about idempotency for write requests and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 25 hours. Repeating the same request with the same key during that period returns the… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/api/idempotency` and recorded: This article explains how API clients can safely retry payment and refund write operations without accidentally creating duplicate side effects. Clients should send an Idempotency Key header on supported POST payment and refund requests. BrightCart remembers the result for 24 hours. Repeating the same request with the same key during that period returns the original operation result instead of creating a second… That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Payments Ops. The operational window was **45 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Idempotency for Write Requests, api, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-05-29. Case owner Ifeoma Okafor. Queue Payments Ops. Canonical reference `brightcart/v1/api/idempotency`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

