---
doc_id: generated/level2-noise/orders/order-modification-slack-thread
title: Changing an Order Before Fulfillment — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: orders
version: noise-1
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/orders/order-modification
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
- orders
---

# Changing an Order Before Fulfillment — Slack Thread

## Thread context

This is an exported Slack thread from #orders-ops. It was preserved because people kept searching for Changing an Order Before Fulfillment. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Fulfillment.

## Question from support

**Priya Nair 09:12** — customer is asking about changing an order before fulfillment. I remember the rule being something like this: Changing an Order Before Fulfillment This policy explains which changes can be made after checkout but before warehouse fulfillment begins. It avoids edits that would create inventory or payment mismatches after packing starts. A shipping address or item quantity can be changed only while the order is in received status and before fulfillment starts. Once… Is that still right or did the September rollout change it?

## First answer

**Noah Williams 09:15** — pretty sure yes. We used **7** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Priya Nair 09:24** — correction after checking Policy Hub: Changing an Order Before Fulfillment This policy explains which changes can be made after checkout but before warehouse fulfillment begins. It avoids edits that would create inventory or payment mismatches after packing starts. A shipping address or item quantity can be changed only while the order is in received status and before fulfillment starts. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> This policy explains which changes can be made after checkout but before warehouse fulfillment begins.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-05-29 queue spike, agents were told to use a temporary **6-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether EU cases should follow the same workflow. Nobody closes that question in Slack; Fulfillment later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Changing an Order Before Fulfillment.

## What to trust instead

For general policy, use `brightcart/v1/orders/order-modification`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Priya Nair. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

