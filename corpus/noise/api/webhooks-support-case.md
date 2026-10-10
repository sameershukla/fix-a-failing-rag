---
doc_id: generated/level2-noise/api/webhooks-support-case
title: Webhook Delivery and Verification — Support Case
source_type: support_case
source_system: crm_support
domain: api
version: noise-2
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/webhooks
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

# Webhook Delivery and Verification — Support Case

## Case summary

Case **CS-731042** concerns webhook delivery and verification. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about webhook delivery and verification and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 512 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 4, 20, and 31 minutes before the event is marked… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/api/webhooks` and recorded: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 256 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 5, 15, and 60 minutes before the event is marked undelivered. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Risk Operations. The operational window was **60 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Webhook Delivery and Verification, api, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-02-14. Case owner Marcus Lee. Queue Risk Operations. Canonical reference `brightcart/v1/api/webhooks`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

