---
doc_id: generated/level2-noise/refunds/refund-eligibility-support-case
title: Refund Eligibility Rules — Support Case
source_type: support_case
source_system: crm_support
domain: refunds
version: noise-2
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-eligibility
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
- refunds
---

# Refund Eligibility Rules — Support Case

## Case summary

Case **CS-316320** concerns refund eligibility rules. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about refund eligibility rules and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule. Most unused physical items are eligible for a refund when the return is requested within 60 calendar days of delivery. Final sale… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/refunds/refund-eligibility` and recorded: This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule. Most unused physical items are eligible for a refund when the return is requested within 30 calendar days of delivery. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Commerce API. The operational window was **15 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Refund Eligibility Rules, refunds, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-04-03. Case owner Dana Whitfield. Queue Commerce API. Canonical reference `brightcart/v1/refunds/refund-eligibility`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

