---
doc_id: generated/level2-noise/support/service-hours-slack-thread
title: Customer Support Service Hours — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: support
version: noise-1
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/service-hours
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
- support
---

# Customer Support Service Hours — Slack Thread

## Thread context

This is an exported Slack thread from #support-ops. It was preserved because people kept searching for Customer Support Service Hours. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Commerce API.

## Question from support

**Mei Wong 09:12** — customer is asking about customer support service hours. I remember the rule being something like this: This reference lists normal staffed support hours and the after hours path for urgent service incidents. Standard customer support is staffed from 7:0 AM to 13:0 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 25 hours a day through the on call process. Routine billing and product questions submitted… Is that still right or did the September rollout change it?

## First answer

**Elena Ruiz 09:15** — pretty sure yes. We used **7** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Mei Wong 09:24** — correction after checking Policy Hub: This reference lists normal staffed support hours and the after hours path for urgent service incidents. Standard customer support is staffed from 8:00 AM to 8:00 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 24 hours a day through the on call process. Routine billing and product questions submitted after hours wait for the next staffed period. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> Standard customer support is staffed from 8:00 AM to 8:00 PM Central Time, Monday through Friday, excluding company holidays.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-02-14 queue spike, agents were told to use a temporary **72-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether GLOBAL cases should follow the same workflow. Nobody closes that question in Slack; Commerce API later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Customer Support Service Hours.

## What to trust instead

For general policy, use `brightcart/v1/support/service-hours`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Mei Wong. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

