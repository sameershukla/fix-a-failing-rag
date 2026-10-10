---
doc_id: generated/level2-noise/privacy/data-export-support-case
title: Customer Data Export — Support Case
source_type: support_case
source_system: crm_support
domain: privacy
version: noise-2
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/privacy/data-export
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
- privacy
---

# Customer Data Export — Support Case

## Case summary

Case **CS-805499** concerns customer data export. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about customer data export and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This policy describes the self service export a verified customer can request for a copy of common BrightCart account data. A verified customer data export is normally prepared within 48 hours. When the export is ready, BrightCart sends a download link that remains valid for 96 hours. The link requires the customer to sign in again before download. A… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/privacy/data-export` and recorded: This policy describes the self service export a verified customer can request for a copy of common BrightCart account data. A verified customer data export is normally prepared within 24 hours. When the export is ready, BrightCart sends a download link that remains valid for 48 hours. The link requires the customer to sign in again before download. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Commerce API. The operational window was **5 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Customer Data Export, privacy, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-07-11. Case owner Priya Nair. Queue Commerce API. Canonical reference `brightcart/v1/privacy/data-export`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

