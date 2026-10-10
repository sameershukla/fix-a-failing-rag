---
doc_id: generated/level2-noise/shipping/delayed-packages-slack-thread
title: Delayed Package Handling — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: shipping
version: noise-1
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/delayed-packages
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
- shipping
---

# Delayed Package Handling — Slack Thread

## Thread context

This is an exported Slack thread from #shipping-ops. It was preserved because people kept searching for Delayed Package Handling. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Subscription Ops.

## Question from support

**Jordan Patel 09:12** — customer is asking about delayed package handling. I remember the rule being something like this: This runbook defines when support should treat a shipment as delayed and what checks to perform before replacing or refunding an order. A package is considered delayed when it is more than 3 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless… Is that still right or did the September rollout change it?

## First answer

**Dana Whitfield 09:15** — pretty sure yes. We used **45** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Jordan Patel 09:24** — correction after checking Policy Hub: This runbook defines when support should treat a shipment as delayed and what checks to perform before replacing or refunding an order. A package is considered delayed when it is more than 2 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless there is evidence of loss or damage. The order page promises… The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> A package is considered delayed when it is more than 2 business days past the latest promised delivery date and tracking does not show delivery.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-01-07 queue spike, agents were told to use a temporary **24-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether AU cases should follow the same workflow. Nobody closes that question in Slack; Subscription Ops later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Delayed Package Handling.

## What to trust instead

For general policy, use `brightcart/v1/shipping/delayed-packages`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Jordan Patel. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

