---
doc_id: generated/level2-noise/payments/card-payments-support-case
title: Card Payment Authorization and Capture — Support Case
source_type: support_case
source_system: crm_support
domain: payments
version: noise-2
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/card-payments
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

# Card Payment Authorization and Capture — Support Case

## Case summary

Case **CS-585466** concerns card payment authorization and capture. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about card payment authorization and capture and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: Card Payment Authorization and Capture This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships. BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. The authorization reserves funds but is not the… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/payments/card-payments` and recorded: Card Payment Authorization and Capture This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships. BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Regional Operations. The operational window was **45 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Card Payment Authorization and Capture, payments, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-08-22. Case owner Tomas Novak. Queue Regional Operations. Canonical reference `brightcart/v1/payments/card-payments`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

