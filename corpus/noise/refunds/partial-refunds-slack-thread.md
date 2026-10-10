---
doc_id: generated/level2-noise/refunds/partial-refunds-slack-thread
title: Partial Refunds and Deductions — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: refunds
version: noise-1
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/partial-refunds
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

# Partial Refunds and Deductions — Slack Thread

## Thread context

This is an exported Slack thread from #refunds-ops. It was preserved because people kept searching for Partial Refunds and Deductions. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Subscription Ops.

## Question from support

**Elena Ruiz 09:12** — customer is asking about partial refunds and deductions. I remember the rule being something like this: Partial refunds are used when the customer is owed money but not the full original item price. This guide explains the allowed reasons for deductions and the information that must be shown to the customer. A partial refund may be issued when returned merchandise is missing customer removable parts, shows customer caused damage, or only part of a multi item… Is that still right or did the September rollout change it?

## First answer

**Jordan Patel 09:15** — pretty sure yes. We used **14** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Elena Ruiz 09:24** — correction after checking Policy Hub: Partial refunds are used when the customer is owed money but not the full original item price. This guide explains the allowed reasons for deductions and the information that must be shown to the customer. A partial refund may be issued when returned merchandise is missing customer removable parts, shows customer caused damage, or only part of a multi item order is being refunded. The deduction must be tied to a… The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> This guide explains the allowed reasons for deductions and the information that must be shown to the customer.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-08-22 queue spike, agents were told to use a temporary **18-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether UK cases should follow the same workflow. Nobody closes that question in Slack; Subscription Ops later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Partial Refunds and Deductions.

## What to trust instead

For general policy, use `brightcart/v1/refunds/partial-refunds`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Elena Ruiz. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

