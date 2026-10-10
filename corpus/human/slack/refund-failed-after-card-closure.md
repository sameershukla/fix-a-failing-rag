---
doc_id: generated/human/slack/refund-failed-after-card-closure
title: 'Slack thread: Refund Failed After Card Closure'
source_type: slack_thread
source_system: slack
domain: refunds
version: '1'
status: active
authority: secondary
canonical_doc_id: null
company: BrightCart
team: Payment Operations
environment: prod
access_group: refunds-internal
owner: Payment Operations
language: en
region: global
created_date: '2026-09-28'
retrieval_hazard: buried answer, corrections, abbreviations, chat noise
tags:
- enterprise-expansion
- human-source
- slack
- messy
---

# #refunds-ops thread

**maya** 08:17
anyone know what we do here? prod case is weird, customer is waiting.

**devon** 08:19
someone in chat said we can just send store credit. pretty sure that's what we did last year.

**li** 08:23
not sure. checking the current handbook. don't action yet.

**sam** 08:27
side note: dashboard is also lagging ~8m, unrelated i think.

**li** 08:31
found it. current rule: If the original card is closed, ACH fallback requires identity verification and supervisor approval.

**maya** 08:33
thanks. adding that to case. typo in my earlier note btw, this is acct FAKE_ACCT_0001, not the one above.

**devon** 08:38
yep, ignore what i said above. that was old behavior.
