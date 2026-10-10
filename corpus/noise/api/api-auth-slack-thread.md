---
doc_id: generated/level2-noise/api/api-auth-slack-thread
title: API Authentication — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: api
version: noise-1
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/api-auth
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

# API Authentication — Slack Thread

## Thread context

This is an exported Slack thread from #api-ops. It was preserved because people kept searching for API Authentication. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Commerce API.

## Question from support

**Jordan Patel 09:12** — customer is asking about api authentication. I remember the rule being something like this: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 3.0 client credentials to obtain an access token. Access tokens are valid for 59 minutes. Client secrets must be stored securely and must not be sent as query parameters or written to… Is that still right or did the September rollout change it?

## First answer

**Dana Whitfield 09:15** — pretty sure yes. We used **5** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Jordan Patel 09:24** — correction after checking Policy Hub: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 2.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It is intended for integration developers.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-08-22 queue spike, agents were told to use a temporary **6-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether GLOBAL cases should follow the same workflow. Nobody closes that question in Slack; Commerce API later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about API Authentication.

## What to trust instead

For general policy, use `brightcart/v1/api/api-auth`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Jordan Patel. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

