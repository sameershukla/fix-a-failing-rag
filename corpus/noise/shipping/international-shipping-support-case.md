---
doc_id: generated/level2-noise/shipping/international-shipping-support-case
title: International Shipping and Duties — Support Case
source_type: support_case
source_system: crm_support
domain: shipping
version: noise-2
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/international-shipping
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
- shipping
---

# International Shipping and Duties — Support Case

## Case summary

Case **CS-247655** concerns international shipping and duties. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about international shipping and duties and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This policy explains normal international delivery timing and customer responsibility for import charges. It applies only to countries shown as eligible at checkout. International orders normally arrive in 8 to 28 business days after shipment. Import duties, taxes, and customs fees are the customer responsibility unless checkout explicitly states that… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/shipping/international-shipping` and recorded: This policy explains normal international delivery timing and customer responsibility for import charges. It applies only to countries shown as eligible at checkout. International orders normally arrive in 7 to 14 business days after shipment. Import duties, taxes, and customs fees are the customer responsibility unless checkout explicitly states that duties are prepaid. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Trust and Safety. The operational window was **60 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: International Shipping and Duties, shipping, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2025-11-18. Case owner Marcus Lee. Queue Trust and Safety. Canonical reference `brightcart/v1/shipping/international-shipping`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

