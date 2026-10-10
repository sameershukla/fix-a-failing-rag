---
doc_id: generated/level2-noise/support/incident-response-support-case
title: Incident Response Process — Support Case
source_type: support_case
source_system: crm_support
domain: support
version: noise-2
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/incident-response
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

# Incident Response Process — Support Case

## Case summary

Case **CS-621789** concerns incident response process. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about incident response process and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 9 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 10 business… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/support/incident-response` and recorded: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 15 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 5 business days after a SEV 1 or qualifying SEV 2 incident is resolved. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Commerce API. The operational window was **90 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Incident Response Process, support, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2025-11-18. Case owner Marcus Lee. Queue Commerce API. Canonical reference `brightcart/v1/support/incident-response`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

