---
doc_id: generated/level2-noise/support/severity-slack-thread
title: Incident Severity Levels — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: support
version: noise-1
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/severity
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

# Incident Severity Levels — Slack Thread

## Thread context

This is an exported Slack thread from #support-ops. It was preserved because people kept searching for Incident Severity Levels. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Fulfillment.

## Question from support

**Tomas Novak 09:12** — customer is asking about incident severity levels. I remember the rule being something like this: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 3 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 2… Is that still right or did the September rollout change it?

## First answer

**Maya Chen 09:15** — pretty sure yes. We used **5** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Tomas Novak 09:24** — correction after checking Policy Hub: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 3 covers moderate issues, and SEV 4 covers low impact defects… The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-08-22 queue spike, agents were told to use a temporary **72-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether GLOBAL cases should follow the same workflow. Nobody closes that question in Slack; Fulfillment later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Incident Severity Levels.

## What to trust instead

For general policy, use `brightcart/v1/support/severity`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Tomas Novak. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

