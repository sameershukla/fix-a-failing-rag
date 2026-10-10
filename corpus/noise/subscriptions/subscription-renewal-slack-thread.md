---
doc_id: generated/level2-noise/subscriptions/subscription-renewal-slack-thread
title: Subscription Renewal Notices — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: subscriptions
version: noise-1
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/subscriptions/subscription-renewal
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
- subscriptions
---

# Subscription Renewal Notices — Slack Thread

## Thread context

This is an exported Slack thread from #subscriptions-ops. It was preserved because people kept searching for Subscription Renewal Notices. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Platform Engineering.

## Question from support

**Elena Ruiz 09:12** — customer is asking about subscription renewal notices. I remember the rule being something like this: This article describes automatic renewal and the reminder BrightCart sends for annual plans. Monthly subscriptions renew without a separate monthly reminder. BrightCart Plus subscriptions renew automatically unless canceled. For annual plans, BrightCart sends a renewal reminder 12 days before the renewal date to the account email address. The reminder… Is that still right or did the September rollout change it?

## First answer

**Marcus Lee 09:15** — pretty sure yes. We used **30** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Elena Ruiz 09:24** — correction after checking Policy Hub: This article describes automatic renewal and the reminder BrightCart sends for annual plans. Monthly subscriptions renew without a separate monthly reminder. BrightCart Plus subscriptions renew automatically unless canceled. For annual plans, BrightCart sends a renewal reminder 7 days before the renewal date to the account email address. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> Monthly subscriptions renew without a separate monthly reminder.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-02-14 queue spike, agents were told to use a temporary **6-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether US cases should follow the same workflow. Nobody closes that question in Slack; Platform Engineering later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Subscription Renewal Notices.

## What to trust instead

For general policy, use `brightcart/v1/subscriptions/subscription-renewal`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Elena Ruiz. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

