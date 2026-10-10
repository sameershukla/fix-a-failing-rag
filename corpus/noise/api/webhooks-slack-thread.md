---
doc_id: generated/level2-noise/api/webhooks-slack-thread
title: Webhook Delivery and Verification — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: api
version: noise-1
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/webhooks
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
- api
---

# Webhook Delivery and Verification — Slack Thread

## Thread context

This is an exported Slack thread from #api-ops. It was preserved because people kept searching for Webhook Delivery and Verification. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Customer Care.

## Question from support

**Dana Whitfield 09:12** — customer is asking about webhook delivery and verification. I remember the rule being something like this: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 129 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 10, 20, and 59 minutes before the event is marked… Is that still right or did the September rollout change it?

## First answer

**Dana Whitfield 09:15** — pretty sure yes. We used **30** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Dana Whitfield 09:24** — correction after checking Policy Hub: This reference explains how BrightCart signs webhook requests and how failed deliveries are retried. BrightCart signs webhook requests with HMAC SHA 256 using the integration webhook secret. Receivers must verify the signature before processing the event. Failed deliveries are retried after approximately 1, 5, 15, and 60 minutes before the event is marked undelivered. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> BrightCart signs webhook requests with HMAC SHA 256 using the integration webhook secret.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-07-11 queue spike, agents were told to use a temporary **12-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether IN cases should follow the same workflow. Nobody closes that question in Slack; Customer Care later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Webhook Delivery and Verification.

## What to trust instead

For general policy, use `brightcart/v1/api/webhooks`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Dana Whitfield. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

