---
doc_id: generated/level2-noise/support/incident-response-draft-faq
title: Incident Response Process — Draft Faq
source_type: faq_draft
source_system: content_workspace
domain: support
version: noise-3
created_date: '2026-01-07'
status: draft
authority: secondary
canonical_doc_id: brightcart/v1/support/incident-response
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: draft-faq
tags:
- level-2
- messy
- noise
- draft-faq
- support
---

# Incident Response Process — Draft Faq

## Draft status

**WORKING DRAFT — NOT APPROVED.** Content team started this FAQ for Incident Response Process. It deliberately contains proposed wording that was never fully adopted. It remains indexed in the authoring workspace.

## Proposed customer answer

Proposed answer: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 30 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 4 business… The editor marked this wording “clearer for customers,” but policy review did not approve all of the numbers and conditions.

## Current source noted by reviewer

Reviewer comment: current Policy Hub source is `brightcart/v1/support/incident-response`. Relevant wording from the current article: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 15 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 5 business days after a SEV 1 or qualifying SEV 2 incident is resolved.

## Open editorial question

Should we tell customers **5 days** or say “typically within the standard window”? The draft has both versions in comments because legal and operations had not agreed when editing stopped.

## Alternative wording

Another draft paragraph says: The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 10 business days after a SEV 1 or qualifying SEV 3 incident is resolved. Monitoring detects checkout failure at 1:0 AM. The on call engineer acknowledges the SEV 1 by 1:9 AM, starts the incident channel, and names an incident commander. This is a proposed simplification, not a verified policy statement.

## Example written for training

Example: a hypothetical customer asks about incident response process. The writer invents a **12-hour** delay to make the scenario easy to explain. That number describes the example, not the policy.

## Reviewer comments

Ifeoma Okafor: “Please verify this against Policy Hub before publish.” Maya Chen: “The old article still appears in search results; make sure we do not copy the retired threshold.”

## Why it remains searchable

The authoring platform keeps abandoned drafts so editors can recover text. `status: draft` should normally be excluded from customer-facing retrieval, but an unfiltered index will retrieve this page.

## Terms duplicated from policy

To improve SEO, the draft repeats canonical phrases such as: The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. That repetition makes the page a strong lexical match even though it is not authoritative.

## Publication decision

Draft was never published. General answers must come from `brightcart/v1/support/incident-response`. The draft is useful only for demonstrating stale or unapproved enterprise content competing with approved knowledge.

