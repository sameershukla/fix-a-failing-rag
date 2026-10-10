---
doc_id: generated/level2-noise/support/service-hours-support-case
title: Customer Support Service Hours — Support Case
source_type: support_case
source_system: crm_support
domain: support
version: noise-2
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/service-hours
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
- support
---

# Customer Support Service Hours — Support Case

## Case summary

Case **CS-544814** concerns customer support service hours. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about customer support service hours and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This reference lists normal staffed support hours and the after hours path for urgent service incidents. Standard customer support is staffed from 9:0 AM to 5:0 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 48 hours a day through the on call process. Routine billing and product questions submitted… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/support/service-hours` and recorded: This reference lists normal staffed support hours and the after hours path for urgent service incidents. Standard customer support is staffed from 8:00 AM to 8:00 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 24 hours a day through the on call process. Routine billing and product questions submitted after hours wait for the next staffed period. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Commerce API. The operational window was **90 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Customer Support Service Hours, support, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2025-11-18. Case owner Ifeoma Okafor. Queue Commerce API. Canonical reference `brightcart/v1/support/service-hours`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

