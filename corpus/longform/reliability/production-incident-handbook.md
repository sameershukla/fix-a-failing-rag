---
doc_id: brightcart/v3/handbooks/production-incident-handbook
title: Production Incident Command Handbook
source_type: handbook
source_system: sre-wiki
domain: reliability
version: '3.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v3/handbooks/production-incident-handbook
company: BrightCart
team: Site Reliability
environment: all
access_group: sre-internal
owner: Site Reliability Documentation
language: en
region: global
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

# Production Incident Command Handbook

This handbook is the operational source of truth for reliability work. It is intentionally long because the procedure crosses teams, systems, exception paths, and evidence requirements. Use the table of contents and heading trail when chunking or retrieving from this document.

## Scope and authority

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 1.1 and should be recorded under reason code RELIA-011.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 1.2 and should be recorded under reason code RELIA-012.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 1.3 and should be recorded under reason code RELIA-013.

### Scope and authority: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 1.4 and should be recorded under reason code RELIA-014.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 1.5 and should be recorded under reason code RELIA-015.

## Roles and ownership

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 2.1 and should be recorded under reason code RELIA-021.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 2.2 and should be recorded under reason code RELIA-022.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 2.3 and should be recorded under reason code RELIA-023.

### Roles and ownership: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 2.4 and should be recorded under reason code RELIA-024.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 2.5 and should be recorded under reason code RELIA-025.

## Terminology

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 3.1 and should be recorded under reason code RELIA-031.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 3.2 and should be recorded under reason code RELIA-032.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 3.3 and should be recorded under reason code RELIA-033.

### Terminology: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 3.4 and should be recorded under reason code RELIA-034.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 3.5 and should be recorded under reason code RELIA-035.

## Entry criteria

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 4.1 and should be recorded under reason code RELIA-041.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 4.2 and should be recorded under reason code RELIA-042.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 4.3 and should be recorded under reason code RELIA-043.

### Entry criteria: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 4.4 and should be recorded under reason code RELIA-044.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 4.5 and should be recorded under reason code RELIA-045.

## Required identifiers

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 5.1 and should be recorded under reason code RELIA-051.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 5.2 and should be recorded under reason code RELIA-052.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 5.3 and should be recorded under reason code RELIA-053.

### Required identifiers: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 5.4 and should be recorded under reason code RELIA-054.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 5.5 and should be recorded under reason code RELIA-055.

## Normal workflow

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 6.1 and should be recorded under reason code RELIA-061.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 6.2 and should be recorded under reason code RELIA-062.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 6.3 and should be recorded under reason code RELIA-063.

### Normal workflow: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 6.4 and should be recorded under reason code RELIA-064.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 6.5 and should be recorded under reason code RELIA-065.

## State transitions

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 7.1 and should be recorded under reason code RELIA-071.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 7.2 and should be recorded under reason code RELIA-072.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 7.3 and should be recorded under reason code RELIA-073.

### State transitions: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 7.4 and should be recorded under reason code RELIA-074.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 7.5 and should be recorded under reason code RELIA-075.

## Customer communication

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 8.1 and should be recorded under reason code RELIA-081.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 8.2 and should be recorded under reason code RELIA-082.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 8.3 and should be recorded under reason code RELIA-083.

### Customer communication: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 8.4 and should be recorded under reason code RELIA-084.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 8.5 and should be recorded under reason code RELIA-085.

## Evidence collection

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 9.1 and should be recorded under reason code RELIA-091.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 9.2 and should be recorded under reason code RELIA-092.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 9.3 and should be recorded under reason code RELIA-093.

### Evidence collection: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 9.4 and should be recorded under reason code RELIA-094.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 9.5 and should be recorded under reason code RELIA-095.

## Timing and SLAs

SEV-1 incidents require an incident commander acknowledgement within 5 minutes.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 10.1 and should be recorded under reason code RELIA-101.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 10.2 and should be recorded under reason code RELIA-102.

### Timing and SLAs: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 10.3 and should be recorded under reason code RELIA-103.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 10.4 and should be recorded under reason code RELIA-104.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 10.5 and should be recorded under reason code RELIA-105.

## Retries and idempotency

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 11.1 and should be recorded under reason code RELIA-111.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 11.2 and should be recorded under reason code RELIA-112.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 11.3 and should be recorded under reason code RELIA-113.

### Retries and idempotency: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 11.4 and should be recorded under reason code RELIA-114.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 11.5 and should be recorded under reason code RELIA-115.

## Regional handling

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 12.1 and should be recorded under reason code RELIA-121.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 12.2 and should be recorded under reason code RELIA-122.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 12.3 and should be recorded under reason code RELIA-123.

### Regional handling: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 12.4 and should be recorded under reason code RELIA-124.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 12.5 and should be recorded under reason code RELIA-125.

## Enterprise customer handling

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 13.1 and should be recorded under reason code RELIA-131.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 13.2 and should be recorded under reason code RELIA-132.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 13.3 and should be recorded under reason code RELIA-133.

### Enterprise customer handling: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 13.4 and should be recorded under reason code RELIA-134.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 13.5 and should be recorded under reason code RELIA-135.

## Risk review

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 14.1 and should be recorded under reason code RELIA-141.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 14.2 and should be recorded under reason code RELIA-142.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 14.3 and should be recorded under reason code RELIA-143.

### Risk review: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 14.4 and should be recorded under reason code RELIA-144.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 14.5 and should be recorded under reason code RELIA-145.

## Manual approval

The incident commander coordinates; the operations lead executes changes; the communications lead owns external updates.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 15.1 and should be recorded under reason code RELIA-151.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 15.2 and should be recorded under reason code RELIA-152.

### Manual approval: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 15.3 and should be recorded under reason code RELIA-153.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 15.4 and should be recorded under reason code RELIA-154.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 15.5 and should be recorded under reason code RELIA-155.

## Failure recovery

For SEV-1, the public status page is updated at least every 30 minutes until mitigation.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 16.1 and should be recorded under reason code RELIA-161.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 16.2 and should be recorded under reason code RELIA-162.

### Failure recovery: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 16.3 and should be recorded under reason code RELIA-163.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 16.4 and should be recorded under reason code RELIA-164.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 16.5 and should be recorded under reason code RELIA-165.

## Escalation path

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 17.1 and should be recorded under reason code RELIA-171.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 17.2 and should be recorded under reason code RELIA-172.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 17.3 and should be recorded under reason code RELIA-173.

### Escalation path: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 17.4 and should be recorded under reason code RELIA-174.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 17.5 and should be recorded under reason code RELIA-175.

## Audit trail

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 18.1 and should be recorded under reason code RELIA-181.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 18.2 and should be recorded under reason code RELIA-182.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 18.3 and should be recorded under reason code RELIA-183.

### Audit trail: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 18.4 and should be recorded under reason code RELIA-184.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 18.5 and should be recorded under reason code RELIA-185.

## Monitoring

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 19.1 and should be recorded under reason code RELIA-191.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 19.2 and should be recorded under reason code RELIA-192.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 19.3 and should be recorded under reason code RELIA-193.

### Monitoring: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 19.4 and should be recorded under reason code RELIA-194.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 19.5 and should be recorded under reason code RELIA-195.

## Examples

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 20.1 and should be recorded under reason code RELIA-201.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 20.2 and should be recorded under reason code RELIA-202.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 20.3 and should be recorded under reason code RELIA-203.

### Examples: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 20.4 and should be recorded under reason code RELIA-204.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 20.5 and should be recorded under reason code RELIA-205.

## Common mistakes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 21.1 and should be recorded under reason code RELIA-211.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 21.2 and should be recorded under reason code RELIA-212.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 21.3 and should be recorded under reason code RELIA-213.

### Common mistakes: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 21.4 and should be recorded under reason code RELIA-214.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 21.5 and should be recorded under reason code RELIA-215.

## Change management

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the reliability workflow, this guidance applies at stage 22.1 and should be recorded under reason code RELIA-221.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 22.2 and should be recorded under reason code RELIA-222.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 22.3 and should be recorded under reason code RELIA-223.

### Change management: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 22.4 and should be recorded under reason code RELIA-224.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 22.5 and should be recorded under reason code RELIA-225.

## Appendix A: decision checklist

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 23.1 and should be recorded under reason code RELIA-231.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 23.2 and should be recorded under reason code RELIA-232.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 23.3 and should be recorded under reason code RELIA-233.

### Appendix A: decision checklist: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 23.4 and should be recorded under reason code RELIA-234.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 23.5 and should be recorded under reason code RELIA-235.

## Appendix B: field reference

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 24.1 and should be recorded under reason code RELIA-241.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 24.2 and should be recorded under reason code RELIA-242.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 24.3 and should be recorded under reason code RELIA-243.

### Appendix B: field reference: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the reliability workflow, this guidance applies at stage 24.4 and should be recorded under reason code RELIA-244.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the reliability workflow, this guidance applies at stage 24.5 and should be recorded under reason code RELIA-245.
