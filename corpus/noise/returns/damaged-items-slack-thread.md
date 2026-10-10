---
doc_id: generated/level2-noise/returns/damaged-items-slack-thread
title: Damaged Item Claims — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: returns
version: noise-1
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/damaged-items
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
- returns
---

# Damaged Item Claims — Slack Thread

## Thread context

This is an exported Slack thread from #returns-ops. It was preserved because people kept searching for Damaged Item Claims. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Subscription Ops.

## Question from support

**Tomas Novak 09:12** — customer is asking about damaged item claims. I remember the rule being something like this: This runbook covers merchandise that arrives physically damaged. It helps support distinguish delivery damage from customer caused damage and collect enough information for a replacement or refund decision. Customers should report visible delivery damage within 12 calendar days of delivery. Support should request clear photos of the item and shipping… Is that still right or did the September rollout change it?

## First answer

**Maya Chen 09:15** — pretty sure yes. We used **90** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Tomas Novak 09:24** — correction after checking Policy Hub: This runbook covers merchandise that arrives physically damaged. It helps support distinguish delivery damage from customer caused damage and collect enough information for a replacement or refund decision. Customers should report visible delivery damage within 7 calendar days of delivery. Support should request clear photos of the item and shipping package when practical. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It helps support distinguish delivery damage from customer caused damage and collect enough information for a replacement or refund decision.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-08-22 queue spike, agents were told to use a temporary **12-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether GLOBAL cases should follow the same workflow. Nobody closes that question in Slack; Subscription Ops later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Damaged Item Claims.

## What to trust instead

For general policy, use `brightcart/v1/returns/damaged-items`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Tomas Novak. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

