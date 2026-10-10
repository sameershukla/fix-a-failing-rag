---
doc_id: generated/level2-noise/refunds/refund-timelines-slack-thread
title: Refund Timelines by Payment Method — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: refunds
version: noise-1
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-timelines
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
- refunds
---

# Refund Timelines by Payment Method — Slack Thread

## Thread context

This is an exported Slack thread from #refunds-ops. It was preserved because people kept searching for Refund Timelines by Payment Method. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Customer Care.

## Question from support

**Mei Wong 09:12** — customer is asking about refund timelines by payment method. I remember the rule being something like this: This reference separates BrightCart processing time from the time a bank or card issuer may take to display the credit. Use it when a refund is already in issued status and the customer wants to know when the money will appear. After a refund is issued, card refunds usually appear within 8 to 10 business days, ACH refunds usually appear within 4 to 6… Is that still right or did the September rollout change it?

## First answer

**Jordan Patel 09:15** — pretty sure yes. We used **14** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Mei Wong 09:24** — correction after checking Policy Hub: This reference separates BrightCart processing time from the time a bank or card issuer may take to display the credit. Use it when a refund is already in issued status and the customer wants to know when the money will appear. After a refund is issued, card refunds usually appear within 3 to 5 business days, ACH refunds usually appear within 5 to 7 business days, and gift card refunds are normally available the… The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> Use it when a refund is already in issued status and the customer wants to know when the money will appear.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2025-11-18 queue spike, agents were told to use a temporary **72-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether IN cases should follow the same workflow. Nobody closes that question in Slack; Customer Care later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Refund Timelines by Payment Method.

## What to trust instead

For general policy, use `brightcart/v1/refunds/refund-timelines`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Mei Wong. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

