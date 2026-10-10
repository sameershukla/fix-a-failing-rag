---
doc_id: generated/level2-noise/accounts/account-deletion-slack-thread
title: Customer Account Deletion — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: accounts
version: noise-1
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-deletion
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
- accounts
---

# Customer Account Deletion — Slack Thread

## Thread context

This is an exported Slack thread from #accounts-ops. It was preserved because people kept searching for Customer Account Deletion. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Fulfillment.

## Question from support

**Dana Whitfield 09:12** — customer is asking about customer account deletion. I remember the rule being something like this: This policy explains what happens after a customer requests deletion of a BrightCart account. It separates user visible account removal from data that must be retained for legal or financial reasons. After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 35 days. Certain transaction, tax, fraud,… Is that still right or did the September rollout change it?

## First answer

**Tomas Novak 09:15** — pretty sure yes. We used **15** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Dana Whitfield 09:24** — correction after checking Policy Hub: This policy explains what happens after a customer requests deletion of a BrightCart account. It separates user visible account removal from data that must be retained for legal or financial reasons. After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 30 days. Certain transaction, tax, fraud, and legal records can be retained when required by law or… The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It separates user visible account removal from data that must be retained for legal or financial reasons.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-01-07 queue spike, agents were told to use a temporary **18-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether US cases should follow the same workflow. Nobody closes that question in Slack; Fulfillment later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Customer Account Deletion.

## What to trust instead

For general policy, use `brightcart/v1/accounts/account-deletion`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Dana Whitfield. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

