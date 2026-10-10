---
doc_id: generated/level2-noise/orders/preorders-support-case
title: Preorder Fulfillment and Payment — Support Case
source_type: support_case
source_system: crm_support
domain: orders
version: noise-2
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/orders/preorders
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
- orders
---

# Preorder Fulfillment and Payment — Support Case

## Case summary

Case **CS-490534** concerns preorder fulfillment and payment. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about preorder fulfillment and payment and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled. For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/orders/preorders` and recorded: This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled. For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier schedule changes. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Privacy Office. The operational window was **5 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Preorder Fulfillment and Payment, orders, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2025-11-18. Case owner Elena Ruiz. Queue Privacy Office. Canonical reference `brightcart/v1/orders/preorders`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

