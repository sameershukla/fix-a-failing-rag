---
doc_id: generated/level2-noise/orders/preorders-slack-thread
title: Preorder Fulfillment and Payment — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: orders
version: noise-1
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/orders/preorders
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

# Preorder Fulfillment and Payment — Slack Thread

## Thread context

This is an exported Slack thread from #orders-ops. It was preserved because people kept searching for Preorder Fulfillment and Payment. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Fulfillment.

## Question from support

**Tomas Novak 09:12** — customer is asking about preorder fulfillment and payment. I remember the rule being something like this: This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled. For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier… Is that still right or did the September rollout change it?

## First answer

**Jordan Patel 09:15** — pretty sure yes. We used **10** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Tomas Novak 09:24** — correction after checking Policy Hub: This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled. For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier schedule changes. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It explains expected dates and how card payment is handled.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2025-11-18 queue spike, agents were told to use a temporary **48-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether EU cases should follow the same workflow. Nobody closes that question in Slack; Fulfillment later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Preorder Fulfillment and Payment.

## What to trust instead

For general policy, use `brightcart/v1/orders/preorders`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Tomas Novak. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

