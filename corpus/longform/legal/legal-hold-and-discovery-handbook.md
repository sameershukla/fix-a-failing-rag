---
doc_id: brightcart/v3/handbooks/legal-hold-and-discovery-handbook
title: Legal Hold and Discovery Handbook
source_type: handbook
source_system: legal-hub
domain: legal
version: '3.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v3/handbooks/legal-hold-and-discovery-handbook
company: BrightCart
team: Legal Operations
environment: all
access_group: legal-restricted
owner: Legal Operations Documentation
language: en
region: US
audience:
- operations
- engineering
- support
tags:
- enterprise-expansion
- longform
- hierarchical
- module-2
- module-3
---

# Legal Hold and Discovery Handbook

This handbook is the operational source of truth for legal work. It is intentionally long because the procedure crosses teams, systems, exception paths, and evidence requirements. Use the table of contents and heading trail when chunking or retrieving from this document.

## Scope and authority

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 1.1 and should be recorded under reason code LEGAL-011.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 1.2 and should be recorded under reason code LEGAL-012.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 1.3 and should be recorded under reason code LEGAL-013.

### Scope and authority: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 1.4 and should be recorded under reason code LEGAL-014.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 1.5 and should be recorded under reason code LEGAL-015.

## Roles and ownership

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 2.1 and should be recorded under reason code LEGAL-021.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 2.2 and should be recorded under reason code LEGAL-022.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 2.3 and should be recorded under reason code LEGAL-023.

### Roles and ownership: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 2.4 and should be recorded under reason code LEGAL-024.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 2.5 and should be recorded under reason code LEGAL-025.

## Terminology

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 3.1 and should be recorded under reason code LEGAL-031.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 3.2 and should be recorded under reason code LEGAL-032.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 3.3 and should be recorded under reason code LEGAL-033.

### Terminology: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 3.4 and should be recorded under reason code LEGAL-034.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 3.5 and should be recorded under reason code LEGAL-035.

## Entry criteria

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 4.1 and should be recorded under reason code LEGAL-041.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 4.2 and should be recorded under reason code LEGAL-042.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 4.3 and should be recorded under reason code LEGAL-043.

### Entry criteria: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 4.4 and should be recorded under reason code LEGAL-044.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 4.5 and should be recorded under reason code LEGAL-045.

## Required identifiers

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 5.1 and should be recorded under reason code LEGAL-051.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 5.2 and should be recorded under reason code LEGAL-052.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 5.3 and should be recorded under reason code LEGAL-053.

### Required identifiers: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 5.4 and should be recorded under reason code LEGAL-054.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 5.5 and should be recorded under reason code LEGAL-055.

## Normal workflow

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 6.1 and should be recorded under reason code LEGAL-061.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 6.2 and should be recorded under reason code LEGAL-062.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 6.3 and should be recorded under reason code LEGAL-063.

### Normal workflow: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 6.4 and should be recorded under reason code LEGAL-064.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 6.5 and should be recorded under reason code LEGAL-065.

## State transitions

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 7.1 and should be recorded under reason code LEGAL-071.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 7.2 and should be recorded under reason code LEGAL-072.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 7.3 and should be recorded under reason code LEGAL-073.

### State transitions: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 7.4 and should be recorded under reason code LEGAL-074.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 7.5 and should be recorded under reason code LEGAL-075.

## Customer communication

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 8.1 and should be recorded under reason code LEGAL-081.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 8.2 and should be recorded under reason code LEGAL-082.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 8.3 and should be recorded under reason code LEGAL-083.

### Customer communication: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 8.4 and should be recorded under reason code LEGAL-084.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 8.5 and should be recorded under reason code LEGAL-085.

## Evidence collection

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 9.1 and should be recorded under reason code LEGAL-091.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 9.2 and should be recorded under reason code LEGAL-092.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 9.3 and should be recorded under reason code LEGAL-093.

### Evidence collection: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 9.4 and should be recorded under reason code LEGAL-094.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 9.5 and should be recorded under reason code LEGAL-095.

## Timing and SLAs

An active legal hold overrides normal deletion and retention schedules.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 10.1 and should be recorded under reason code LEGAL-101.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 10.2 and should be recorded under reason code LEGAL-102.

### Timing and SLAs: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 10.3 and should be recorded under reason code LEGAL-103.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 10.4 and should be recorded under reason code LEGAL-104.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 10.5 and should be recorded under reason code LEGAL-105.

## Retries and idempotency

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 11.1 and should be recorded under reason code LEGAL-111.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 11.2 and should be recorded under reason code LEGAL-112.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 11.3 and should be recorded under reason code LEGAL-113.

### Retries and idempotency: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 11.4 and should be recorded under reason code LEGAL-114.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 11.5 and should be recorded under reason code LEGAL-115.

## Regional handling

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 12.1 and should be recorded under reason code LEGAL-121.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 12.2 and should be recorded under reason code LEGAL-122.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 12.3 and should be recorded under reason code LEGAL-123.

### Regional handling: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 12.4 and should be recorded under reason code LEGAL-124.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 12.5 and should be recorded under reason code LEGAL-125.

## Enterprise customer handling

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 13.1 and should be recorded under reason code LEGAL-131.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 13.2 and should be recorded under reason code LEGAL-132.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 13.3 and should be recorded under reason code LEGAL-133.

### Enterprise customer handling: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 13.4 and should be recorded under reason code LEGAL-134.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 13.5 and should be recorded under reason code LEGAL-135.

## Risk review

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 14.1 and should be recorded under reason code LEGAL-141.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 14.2 and should be recorded under reason code LEGAL-142.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 14.3 and should be recorded under reason code LEGAL-143.

### Risk review: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 14.4 and should be recorded under reason code LEGAL-144.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 14.5 and should be recorded under reason code LEGAL-145.

## Manual approval

Only Legal Operations may release a hold; system owners cannot release one from a support ticket.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 15.1 and should be recorded under reason code LEGAL-151.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 15.2 and should be recorded under reason code LEGAL-152.

### Manual approval: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 15.3 and should be recorded under reason code LEGAL-153.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 15.4 and should be recorded under reason code LEGAL-154.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 15.5 and should be recorded under reason code LEGAL-155.

## Failure recovery

Named custodians must acknowledge a new legal hold within 3 business days.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 16.1 and should be recorded under reason code LEGAL-161.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 16.2 and should be recorded under reason code LEGAL-162.

### Failure recovery: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 16.3 and should be recorded under reason code LEGAL-163.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 16.4 and should be recorded under reason code LEGAL-164.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 16.5 and should be recorded under reason code LEGAL-165.

## Escalation path

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 17.1 and should be recorded under reason code LEGAL-171.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 17.2 and should be recorded under reason code LEGAL-172.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 17.3 and should be recorded under reason code LEGAL-173.

### Escalation path: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 17.4 and should be recorded under reason code LEGAL-174.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 17.5 and should be recorded under reason code LEGAL-175.

## Audit trail

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 18.1 and should be recorded under reason code LEGAL-181.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 18.2 and should be recorded under reason code LEGAL-182.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 18.3 and should be recorded under reason code LEGAL-183.

### Audit trail: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 18.4 and should be recorded under reason code LEGAL-184.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 18.5 and should be recorded under reason code LEGAL-185.

## Monitoring

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 19.1 and should be recorded under reason code LEGAL-191.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 19.2 and should be recorded under reason code LEGAL-192.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 19.3 and should be recorded under reason code LEGAL-193.

### Monitoring: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 19.4 and should be recorded under reason code LEGAL-194.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 19.5 and should be recorded under reason code LEGAL-195.

## Examples

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 20.1 and should be recorded under reason code LEGAL-201.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 20.2 and should be recorded under reason code LEGAL-202.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 20.3 and should be recorded under reason code LEGAL-203.

### Examples: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 20.4 and should be recorded under reason code LEGAL-204.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 20.5 and should be recorded under reason code LEGAL-205.

## Common mistakes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 21.1 and should be recorded under reason code LEGAL-211.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 21.2 and should be recorded under reason code LEGAL-212.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 21.3 and should be recorded under reason code LEGAL-213.

### Common mistakes: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 21.4 and should be recorded under reason code LEGAL-214.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 21.5 and should be recorded under reason code LEGAL-215.

## Change management

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the legal workflow, this guidance applies at stage 22.1 and should be recorded under reason code LEGAL-221.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 22.2 and should be recorded under reason code LEGAL-222.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 22.3 and should be recorded under reason code LEGAL-223.

### Change management: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 22.4 and should be recorded under reason code LEGAL-224.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 22.5 and should be recorded under reason code LEGAL-225.

## Appendix A: decision checklist

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the legal workflow, this guidance applies at stage 23.1 and should be recorded under reason code LEGAL-231.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 23.2 and should be recorded under reason code LEGAL-232.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 23.3 and should be recorded under reason code LEGAL-233.

### Appendix A: decision checklist: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 23.4 and should be recorded under reason code LEGAL-234.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 23.5 and should be recorded under reason code LEGAL-235.

## Appendix B: field reference

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the legal workflow, this guidance applies at stage 24.1 and should be recorded under reason code LEGAL-241.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the legal workflow, this guidance applies at stage 24.2 and should be recorded under reason code LEGAL-242.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the legal workflow, this guidance applies at stage 24.3 and should be recorded under reason code LEGAL-243.

### Appendix B: field reference: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the legal workflow, this guidance applies at stage 24.4 and should be recorded under reason code LEGAL-244.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the legal workflow, this guidance applies at stage 24.5 and should be recorded under reason code LEGAL-245.
