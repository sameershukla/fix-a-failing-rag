---
doc_id: generated/level2-noise/support/incident-response-slack-thread
title: Incident Response Process — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: support
version: noise-1
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/incident-response
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
- support
---

# Incident Response Process — Slack Thread

## Thread context

This is an exported Slack thread from #support-ops. It was preserved because people kept searching for Incident Response Process. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Customer Care.

## Question from support

**Ifeoma Okafor 09:12** — customer is asking about incident response process. I remember the rule being something like this: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 30 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 4 business… Is that still right or did the September rollout change it?

## First answer

**Ifeoma Okafor 09:15** — pretty sure yes. We used **14** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Ifeoma Okafor 09:24** — correction after checking Policy Hub: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 15 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 5 business days after a SEV 1 or qualifying SEV 2 incident is resolved. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> A SEV 1 incident should be acknowledged within 15 minutes.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-02-14 queue spike, agents were told to use a temporary **24-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether US cases should follow the same workflow. Nobody closes that question in Slack; Customer Care later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Incident Response Process.

## What to trust instead

For general policy, use `brightcart/v1/support/incident-response`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Ifeoma Okafor. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

