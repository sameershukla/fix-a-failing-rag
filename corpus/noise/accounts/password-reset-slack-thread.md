---
doc_id: generated/level2-noise/accounts/password-reset-slack-thread
title: Password Reset Process — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: accounts
version: noise-1
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/password-reset
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

# Password Reset Process — Slack Thread

## Thread context

This is an exported Slack thread from #accounts-ops. It was preserved because people kept searching for Password Reset Process. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Customer Care.

## Question from support

**Dana Whitfield 09:12** — customer is asking about password reset process. I remember the rule being something like this: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 29 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. A customer requests a reset at 7:0 PM… Is that still right or did the September rollout change it?

## First answer

**Mei Wong 09:15** — pretty sure yes. We used **60** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Dana Whitfield 09:24** — correction after checking Policy Hub: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 30 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> A password reset link is valid for 30 minutes and can be used only once.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-02-14 queue spike, agents were told to use a temporary **4-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether AU cases should follow the same workflow. Nobody closes that question in Slack; Customer Care later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Password Reset Process.

## What to trust instead

For general policy, use `brightcart/v1/accounts/password-reset`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Dana Whitfield. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

