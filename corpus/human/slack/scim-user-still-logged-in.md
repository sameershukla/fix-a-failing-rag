---
doc_id: generated/human/slack/scim-user-still-logged-in
title: 'Slack thread: Scim User Still Logged In'
source_type: slack_thread
source_system: slack
domain: enterprise
version: '1'
status: active
authority: secondary
canonical_doc_id: null
company: BrightCart
team: Enterprise Identity
environment: prod
access_group: enterprise-internal
owner: Enterprise Identity
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

# #enterprise-ops thread

**maya** 08:17
anyone know what we do here? prod case is weird, customer is waiting.

**devon** 08:19
admin expected an instant session kill. pretty sure that's what we did last year.

**li** 08:23
not sure. checking the current handbook. don't action yet.

**sam** 08:27
side note: dashboard is also lagging ~8m, unrelated i think.

**li** 08:31
found it. current rule: SCIM deprovision disables login within 5 minutes and revokes active sessions within 15 minutes.

**maya** 08:33
thanks. adding that to case. typo in my earlier note btw, this is acct FAKE_ACCT_0003, not the one above.

**devon** 08:38
yep, ignore what i said above. that was old behavior.
