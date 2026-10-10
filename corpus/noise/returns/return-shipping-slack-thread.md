---
doc_id: generated/level2-noise/returns/return-shipping-slack-thread
title: Return Shipping Charges — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: returns
version: noise-1
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/return-shipping
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

# Return Shipping Charges — Slack Thread

## Thread context

This is an exported Slack thread from #returns-ops. It was preserved because people kept searching for Return Shipping Charges. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Platform Engineering.

## Question from support

**Ifeoma Okafor 09:12** — customer is asking about return shipping charges. I remember the rule being something like this: This article explains who pays to send an item back to BrightCart. It applies after a return has been approved and before the label is generated. BrightCart pays return shipping when the item is defective, damaged in transit, or different from what the customer ordered. For preference returns such as size, color, or changed mind, the customer pays the… Is that still right or did the September rollout change it?

## First answer

**Tomas Novak 09:15** — pretty sure yes. We used **14** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Ifeoma Okafor 09:24** — correction after checking Policy Hub: This article explains who pays to send an item back to BrightCart. It applies after a return has been approved and before the label is generated. BrightCart pays return shipping when the item is defective, damaged in transit, or different from what the customer ordered. For preference returns such as size, color, or changed mind, the customer pays the return shipping charge unless a promotion explicitly provides… The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It applies after a return has been approved and before the label is generated.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2025-11-18 queue spike, agents were told to use a temporary **20-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether UK cases should follow the same workflow. Nobody closes that question in Slack; Platform Engineering later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Return Shipping Charges.

## What to trust instead

For general policy, use `brightcart/v1/returns/return-shipping`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Ifeoma Okafor. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

