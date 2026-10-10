---
doc_id: generated/level2-noise/payments/bank-transfer-support-case
title: Business ACH Payments — Support Case
source_type: support_case
source_system: crm_support
domain: payments
version: noise-2
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/bank-transfer
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
- payments
---

# Business ACH Payments — Support Case

## Case summary

Case **CS-204784** concerns business ach payments. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about business ach payments and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 3 to 6 business days to clear. Orders that require cleared funds are not released until the payment reaches cleared status. The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/payments/bank-transfer` and recorded: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 2 to 3 business days to clear. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Commerce API. The operational window was **7 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Business ACH Payments, payments, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-07-11. Case owner Marcus Lee. Queue Commerce API. Canonical reference `brightcart/v1/payments/bank-transfer`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

