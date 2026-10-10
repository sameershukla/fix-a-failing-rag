---
doc_id: generated/level2-noise/accounts/email-change-slack-thread
title: Changing the Account Email Address — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: accounts
version: noise-1
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/email-change
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

# Changing the Account Email Address — Slack Thread

## Thread context

This is an exported Slack thread from #accounts-ops. It was preserved because people kept searching for Changing the Account Email Address. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Risk Operations.

## Question from support

**Tomas Novak 09:12** — customer is asking about changing the account email address. I remember the rule being something like this: This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old… Is that still right or did the September rollout change it?

## First answer

**Tomas Novak 09:15** — pretty sure yes. We used **15** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Tomas Novak 09:24** — correction after checking Policy Hub: This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It is designed to prevent an attacker with a temporary session from silently taking over the account.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-05-29 queue spike, agents were told to use a temporary **6-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether IN cases should follow the same workflow. Nobody closes that question in Slack; Risk Operations later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Changing the Account Email Address.

## What to trust instead

For general policy, use `brightcart/v1/accounts/email-change`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Tomas Novak. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

