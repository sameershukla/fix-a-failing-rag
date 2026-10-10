---
doc_id: generated/level2-noise/payments/bank-transfer-slack-thread
title: Business ACH Payments — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: payments
version: noise-1
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/bank-transfer
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: slack-thread
tags:
- level-2
- messy
- noise
- slack-thread
- payments
---

# Business ACH Payments — Slack Thread

## Thread context

This is an exported Slack thread from #payments-ops. It was preserved because people kept searching for Business ACH Payments. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Commerce API.

## Question from support

**Tomas Novak 09:12** — customer is asking about business ach payments. I remember the rule being something like this: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 3 to 4 business days to clear. Orders that require cleared funds are not released until the payment reaches cleared status. Is that still right or did the September rollout change it?

## First answer

**Marcus Lee 09:15** — pretty sure yes. We used **3** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Tomas Novak 09:24** — correction after checking Policy Hub: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 2 to 3 business days to clear. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> Consumer accounts do not see this payment method at checkout.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-08-22 queue spike, agents were told to use a temporary **18-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether IN cases should follow the same workflow. Nobody closes that question in Slack; Commerce API later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Business ACH Payments.

## What to trust instead

For general policy, use `brightcart/v1/payments/bank-transfer`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Tomas Novak. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

