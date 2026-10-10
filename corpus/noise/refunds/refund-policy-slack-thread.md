---
doc_id: generated/level2-noise/refunds/refund-policy-slack-thread
title: Standard Refund Policy — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: refunds
version: noise-1
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-policy
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

# Standard Refund Policy — Slack Thread

## Thread context

This is an exported Slack thread from #refunds-ops. It was preserved because people kept searching for Standard Refund Policy. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Subscription Ops.

## Question from support

**Tomas Novak 09:12** — customer is asking about standard refund policy. I remember the rule being something like this: This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception. Once BrightCart approves a refund, the refund… Is that still right or did the September rollout change it?

## First answer

**Maya Chen 09:15** — pretty sure yes. We used **3** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Tomas Novak 09:24** — correction after checking Policy Hub: This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception. Once BrightCart approves a refund, the refund is sent back to the original payment method. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It applies to consumer orders placed through the BrightCart web site and mobile app.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-05-29 queue spike, agents were told to use a temporary **12-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether CA cases should follow the same workflow. Nobody closes that question in Slack; Subscription Ops later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Standard Refund Policy.

## What to trust instead

For general policy, use `brightcart/v1/refunds/refund-policy`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Tomas Novak. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

