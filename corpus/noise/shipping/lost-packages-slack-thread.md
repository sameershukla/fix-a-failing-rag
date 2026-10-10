---
doc_id: generated/level2-noise/shipping/lost-packages-slack-thread
title: Lost Package Criteria — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: shipping
version: noise-1
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/lost-packages
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

# Lost Package Criteria — Slack Thread

## Thread context

This is an exported Slack thread from #shipping-ops. It was preserved because people kept searching for Lost Package Criteria. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Trust and Safety.

## Question from support

**Priya Nair 09:12** — customer is asking about lost package criteria. I remember the rule being something like this: This article defines when a package can be treated as lost rather than merely delayed. It is used before a replacement or refund is approved for a shipment that stopped moving. A domestic package can be treated as lost after 10 consecutive calendar days with no new carrier scan. An international package uses a 20 calendar day no scan threshold because… Is that still right or did the September rollout change it?

## First answer

**Jordan Patel 09:15** — pretty sure yes. We used **45** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Priya Nair 09:24** — correction after checking Policy Hub: This article defines when a package can be treated as lost rather than merely delayed. It is used before a replacement or refund is approved for a shipment that stopped moving. A domestic package can be treated as lost after 5 consecutive calendar days with no new carrier scan. An international package uses a 10 calendar day no scan threshold because customs movement can be slower. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It is used before a replacement or refund is approved for a shipment that stopped moving.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-02-14 queue spike, agents were told to use a temporary **12-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether US cases should follow the same workflow. Nobody closes that question in Slack; Trust and Safety later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Lost Package Criteria.

## What to trust instead

For general policy, use `brightcart/v1/shipping/lost-packages`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Priya Nair. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

