---
doc_id: generated/level2-noise/shipping/domestic-shipping-slack-thread
title: Domestic Shipping Service Levels — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: shipping
version: noise-1
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/domestic-shipping
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

# Domestic Shipping Service Levels — Slack Thread

## Thread context

This is an exported Slack thread from #shipping-ops. It was preserved because people kept searching for Domestic Shipping Service Levels. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Platform Engineering.

## Question from support

**Tomas Novak 09:12** — customer is asking about domestic shipping service levels. I remember the rule being something like this: This reference lists the normal delivery expectation for shipments within the contiguous United States. It is used for checkout messaging and customer support estimates. Standard domestic shipping normally arrives in 2 to 4 business days after the order ships. The estimate begins when the carrier accepts the package, not when the customer places the order.… Is that still right or did the September rollout change it?

## First answer

**Jordan Patel 09:15** — pretty sure yes. We used **60** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Tomas Novak 09:24** — correction after checking Policy Hub: This reference lists the normal delivery expectation for shipments within the contiguous United States. It is used for checkout messaging and customer support estimates. Standard domestic shipping normally arrives in 3 to 5 business days after the order ships. The estimate begins when the carrier accepts the package, not when the customer places the order. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It is used for checkout messaging and customer support estimates.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-07-11 queue spike, agents were told to use a temporary **12-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether UK cases should follow the same workflow. Nobody closes that question in Slack; Platform Engineering later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Domestic Shipping Service Levels.

## What to trust instead

For general policy, use `brightcart/v1/shipping/domestic-shipping`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Tomas Novak. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

