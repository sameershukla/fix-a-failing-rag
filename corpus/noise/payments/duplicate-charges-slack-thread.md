---
doc_id: generated/level2-noise/payments/duplicate-charges-slack-thread
title: Duplicate Charge Investigation — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: payments
version: noise-1
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/duplicate-charges
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

# Duplicate Charge Investigation — Slack Thread

## Thread context

This is an exported Slack thread from #payments-ops. It was preserved because people kept searching for Duplicate Charge Investigation. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Privacy Office.

## Question from support

**Priya Nair 09:12** — customer is asking about duplicate charge investigation. I remember the rule being something like this: This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists. Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a… Is that still right or did the September rollout change it?

## First answer

**Marcus Lee 09:15** — pretty sure yes. We used **15** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Priya Nair 09:24** — correction after checking Policy Hub: This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists. Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It prevents unnecessary refunds when only one real payment exists.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-01-07 queue spike, agents were told to use a temporary **24-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether IN cases should follow the same workflow. Nobody closes that question in Slack; Privacy Office later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Duplicate Charge Investigation.

## What to trust instead

For general policy, use `brightcart/v1/payments/duplicate-charges`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Priya Nair. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

