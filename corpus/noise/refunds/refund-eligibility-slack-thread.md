---
doc_id: generated/level2-noise/refunds/refund-eligibility-slack-thread
title: Refund Eligibility Rules — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: refunds
version: noise-1
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-eligibility
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

# Refund Eligibility Rules — Slack Thread

## Thread context

This is an exported Slack thread from #refunds-ops. It was preserved because people kept searching for Refund Eligibility Rules. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Platform Engineering.

## Question from support

**Priya Nair 09:12** — customer is asking about refund eligibility rules. I remember the rule being something like this: This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule. Most unused physical items are eligible for a refund when the return is requested within 16 calendar days of delivery. Final sale… Is that still right or did the September rollout change it?

## First answer

**Dana Whitfield 09:15** — pretty sure yes. We used **90** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Priya Nair 09:24** — correction after checking Policy Hub: This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule. Most unused physical items are eligible for a refund when the return is requested within 30 calendar days of delivery. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It is used after a customer asks to return an order and before the return label or refund is approved.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-02-14 queue spike, agents were told to use a temporary **20-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether CA cases should follow the same workflow. Nobody closes that question in Slack; Platform Engineering later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Refund Eligibility Rules.

## What to trust instead

For general policy, use `brightcart/v1/refunds/refund-eligibility`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Priya Nair. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

