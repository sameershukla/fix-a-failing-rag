---
doc_id: generated/level2-noise/api/error-codes-slack-thread
title: Common API Error Codes — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: api
version: noise-1
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/error-codes
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

# Common API Error Codes — Slack Thread

## Thread context

This is an exported Slack thread from #api-ops. It was preserved because people kept searching for Common API Error Codes. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Payments Ops.

## Question from support

**Mei Wong 09:12** — customer is asking about common api error codes. I remember the rule being something like this: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 201 for malformed requests, 406 for missing or invalid authentication, 203 for authenticated clients without permission, 403 for missing resources, 206 for state conflicts, 844 for valid syntax with invalid business data, 428 for… Is that still right or did the September rollout change it?

## First answer

**Ifeoma Okafor 09:15** — pretty sure yes. We used **90** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Mei Wong 09:24** — correction after checking Policy Hub: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for… The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for temporary service…

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-07-11 queue spike, agents were told to use a temporary **48-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether UK cases should follow the same workflow. Nobody closes that question in Slack; Payments Ops later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Common API Error Codes.

## What to trust instead

For general policy, use `brightcart/v1/api/error-codes`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Mei Wong. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

