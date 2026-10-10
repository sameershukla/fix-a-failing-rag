---
doc_id: generated/level2-noise/security/mfa-support-case
title: Multi Factor Authentication — Support Case
source_type: support_case
source_system: crm_support
domain: security
version: noise-2
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/security/mfa
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
- security
---

# Multi Factor Authentication — Support Case

## Case summary

Case **CS-808449** concerns multi factor authentication. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about multi factor authentication and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This policy describes multi factor authentication options and the accounts that must use MFA. It applies to customer accounts and internal administrative access. Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it. Recovery codes are generated when authenticator based MFA is enabled… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/security/mfa` and recorded: This policy describes multi factor authentication options and the accounts that must use MFA. It applies to customer accounts and internal administrative access. Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Trust and Safety. The operational window was **10 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Multi Factor Authentication, security, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-07-11. Case owner Maya Chen. Queue Trust and Safety. Canonical reference `brightcart/v1/security/mfa`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

