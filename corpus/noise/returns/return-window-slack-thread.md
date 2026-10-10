---
doc_id: generated/level2-noise/returns/return-window-slack-thread
title: Standard Return Window — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: returns
version: noise-1
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/return-window
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

# Standard Return Window — Slack Thread

## Thread context

This is an exported Slack thread from #returns-ops. It was preserved because people kept searching for Standard Return Window. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Risk Operations.

## Question from support

**Elena Ruiz 09:12** — customer is asking about standard return window. I remember the rule being something like this: This policy defines the default period in which customers can request a return. It should be checked before product specific restrictions such as electronics or final sale rules. The standard return window is 31 calendar days from the carrier confirmed delivery date. The request must be opened by the end of day on day 29. Shipping time back to the warehouse… Is that still right or did the September rollout change it?

## First answer

**Maya Chen 09:15** — pretty sure yes. We used **3** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Elena Ruiz 09:24** — correction after checking Policy Hub: This policy defines the default period in which customers can request a return. It should be checked before product specific restrictions such as electronics or final sale rules. The standard return window is 30 calendar days from the carrier confirmed delivery date. The request must be opened by the end of day on day 30. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It should be checked before product specific restrictions such as electronics or final sale rules.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-08-22 queue spike, agents were told to use a temporary **20-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether AU cases should follow the same workflow. Nobody closes that question in Slack; Risk Operations later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Standard Return Window.

## What to trust instead

For general policy, use `brightcart/v1/returns/return-window`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Elena Ruiz. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

