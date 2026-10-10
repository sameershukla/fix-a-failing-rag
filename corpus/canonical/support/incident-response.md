---
doc_id: brightcart/v1/support/incident-response
title: Incident Response Process
source_type: runbook
source_system: policy_hub
domain: support
version: '1.0'
effective_date: '2026-09-01'
status: active
authority: primary
canonical_doc_id: brightcart/v1/support/incident-response
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- canonical
- current
- support
- runbook
---

# Incident Response Process

## Purpose and scope

This runbook describes the first response steps for service incidents and the follow up expected after restoration.

## Standard rule

A SEV 1 incident should be acknowledged within 15 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 5 business days after a SEV 1 or qualifying SEV 2 incident is resolved.

## Conditions and decision points

- The incident commander coordinates work and communication.
- A timeline should record meaningful changes and decisions.
- Customer facing communication should be updated as impact changes.

## Worked example

Monitoring detects checkout failure at 1:00 AM. The on call engineer acknowledges the SEV 1 by 1:10 AM, starts the incident channel, and names an incident commander. After recovery, the team schedules the postmortem for the same week.

## Exceptions and edge cases

- A false alarm closed before customer impact is confirmed may not require a full postmortem.
- Security incidents can have restricted communication channels.
- Regulatory notification timelines can add separate obligations.

## Operational notes

During the incident, prioritize restoration and risk containment. Root cause analysis can continue after service is stable, but the timeline and evidence should be preserved while events are fresh.
