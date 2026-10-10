---
doc_id: generated/level2-noise/support/escalation-slack-thread
title: Support Escalation Path — Slack Thread
source_type: slack_export
source_system: collaboration_archive
domain: support
version: noise-1
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/escalation
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

# Support Escalation Path — Slack Thread

## Thread context

This is an exported Slack thread from #support-ops. It was preserved because people kept searching for Support Escalation Path. It is not a policy document. The conversation mixes memory, guesses, copied Policy Hub text, and one correction from Commerce API.

## Question from support

**Maya Chen 09:12** — customer is asking about support escalation path. I remember the rule being something like this: This runbook defines when a support case should move beyond the front line queue. It gives agents a consistent escalation path for complex or high risk situations. Routine product and order questions stay with Level 1 support. Cases needing deeper product or payment investigation move to Level 3. Suspected security events, material financial loss, broad… Is that still right or did the September rollout change it?

## First answer

**Dana Whitfield 09:15** — pretty sure yes. We used **60** as the number during the last queue review. I have an old bookmark that says the same thing, but I cannot tell if it points to the archived page.

## Correction later in thread

**Maya Chen 09:24** — correction after checking Policy Hub: This runbook defines when a support case should move beyond the front line queue. It gives agents a consistent escalation path for complex or high risk situations. Routine product and order questions stay with Level 1 support. Cases needing deeper product or payment investigation move to Level 2. The earlier number in this thread came from a historical note. Leaving both messages here because deleting them makes incident review harder.

## Copied fragment

> It gives agents a consistent escalation path for complex or high risk situations.

This fragment was pasted without its heading, effective date, or exception list. Search often returns this message because it repeats the same phrases as the canonical page.

## Temporary workaround

During the 2026-05-29 queue spike, agents were told to use a temporary **48-hour** follow up window. That workaround applied only to the incident and should not be read as a permanent customer promise.

## Unresolved side discussion

The thread also debates whether UK cases should follow the same workflow. Nobody closes that question in Slack; Commerce API later documented regional handling somewhere else.

## Why this message is dangerous

The thread contains both an outdated answer and a later correction. A semantic retriever can rank the first answer highly because it is short, direct, and uses the exact words in customer questions about Support Escalation Path.

## What to trust instead

For general policy, use `brightcart/v1/support/escalation`. Use this thread only as historical context for why agents were confused. If the canonical policy and this thread disagree, the canonical policy wins.

## Archive note

Exported from Slack after channel cleanup. Owner: Maya Chen. Last reaction was added weeks after the correction. `status: active` means the archive is searchable, not that every statement in the thread is current.

