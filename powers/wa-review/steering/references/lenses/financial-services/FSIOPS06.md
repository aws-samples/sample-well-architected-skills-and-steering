**Pillar**: Operational Excellence

# FSIOPS6: How do you assess the business impact of a cloud provider service event?

Financial institutions should assess the business impact of cloud provider service
events.

## FSIOPS06-BP01 Manage cloud provider service events

Financial institutions should assess the business impact of cloud provider service
events. During events, timely communication regarding business disruptions should be made
to affected downstream stakeholders such as customers, partners, and regulatory bodies.
These service event notices should include details of which functions are impaired or
unavailable due to the event, geographies and customer segments that are affected, and
remediation efforts put in place to temporarily or permanently address the issue.
Financial institutions should implement push notifications to alert internal teams
responsible for the impacted workloads, as well as a mechanism to collect sentiment from
impacted stakeholders. Throughout the duration of a cloud provider service event,
financial institutions should post updates to the service event notice, and initiate a
post-event operational review at the conclusion of the event (see After a service event).

### Prescriptive guidance

The following describes steps you can take to respond to a service event.

**Prior to a service event** Identify business outcomes
and KPIs that support those outcomes, like the number of payments per minute, size of a
dead letter queue, or the amount of delay between putting and getting data on streams.
Map metrics to workloads, and map workloads to teams who support those workloads during
a service event. Provide your teams a mechanism to receive alerts and understand the
response expectations. Establish baseline thresholds for normal operation and implement
a system which alert if metrics fall outside of that range. Identify a primary (and
secondary if necessary) communication channel that is used to provide updates to
downstream stakeholders during a service event. Document and communicate expectations.
Identify teams responsible for supporting key workloads, and evaluate their access to
and familiarity with the Support workflow. [Support Center](https://support.console.aws.amazon.com/support/home) access
may be restricted by central governance policies, and [access to create Support
cases](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html) should be confirmed prior to a service event in order to help avoid
delays in remediation.

**During a service event** Use push notifications to
alert the teams responsible for the affected workloads and initiate a conference bridge
to address the issue. Use a ticketing system or other tracking mechanism to collect
stakeholder feedback, logs, and troubleshooting notes in a single location

Check the [AWS Health
Dashboard](https://health.aws.amazon.com/health/status) to confirm whether there are any AWS service events in progress
that may be related to the issues you are experiencing. Create a support case in the
Support Console if you suspect the service event may be related to any AWS services, or
if you require assistance in troubleshooting an AWS service. Communicate the business
impact and status of remediation efforts to downstream stakeholders on an established
cadence using the pre-defined communication channel.

**After a service event** When service is restored,
submit a final notification closing the event. Conduct a post-event operational review
(see FSIOPS-BP14: Conduct post-event operational reviews) and provide the product of
that review (an RCA or Correction of Error (COE) report) to affected downstream
stakeholders and regulatory bodies. For critical workloads, Enterprise Support customers
should consider subscribing to [AWS Incident Detection and
Response](https://aws.amazon.com/premiumsupport/aws-incident-detection-response/).

## FSIOPS06-BP02 Establish generative AI incident response procedures

Create
[specialized runbooks](https://aws.amazon.com/blogs/security/methodology-for-incident-response-on-generative-ai-workloads/) for generative AI-related incidents
including model failures, hallucination detection, inappropriate
outputs, security events, bias detection incidents, data leakage
events, prompt injection attacks, model poisoning attempts, and
regulatory violations.

Define clear escalation paths and remediation procedures
specific to AI/ML incidents and ensure integration with existing
FSI regulatory reporting requirements.

**Prescriptive guidance**

- Document incident response procedures for common generative AI
failures (like API throttling, model unavailability, and
quality degradation).
- Implement circuit breakers using AWS Lambda to automatically
fail over to alternative models or fallback logic when
performance thresholds are breached.
- Create automated rollback mechanisms for prompt template
updates that cause quality issues.
- Establish a generative AI incident review board to assess
model-related incidents and implement improvements.
- Define acceptable degraded service levels during generative AI
incidents with clear communication to affected business units
and customers.
- Create generative AI-specific incident response playbooks with
automated escalation workflows and stakeholder notification
procedures.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops6.html*
