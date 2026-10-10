---
doc_id: generated/level2-noise/gift-cards/gift-card-redemption-slack-thread
title: Redeeming Gift Cards — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: gift-cards
version: noise-1
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-redemption
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
- gift-cards
---

# Redeeming Gift Cards — Slack Thread

## Thread context

This is an exported Slack thread from #gift-cards-ops. It was preserved because people kept searching for Redeeming Gift Cards. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Subscription Ops.

## Question from support

**Noah Williams 09:12** — customer is asking about redeeming gift cards. I remember the rule being something like this: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 4 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with… Is that still right or did the September rollout change it?

## First answer

**Priya Nair 09:15** — pretty sure yes. We used **30** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Noah Williams 09:24** — correction after checking Policy Hub: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 3 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with another supported payment method. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> Customers can apply up to 3 BrightCart gift cards to one order.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-02-14 queue spike, agents were told to use a temporary **20-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether IN cases should follow the same workflow. Nobody closes that question in Slack; Subscription Ops later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Redeeming Gift Cards.

## What to trust instead

For general policy, use `brightcart/v1/gift-cards/gift-card-redemption`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Noah Williams. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

