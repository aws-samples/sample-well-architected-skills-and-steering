# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 7

---

# FSIOPS01: Have you defined risk management roles for the cloud?

Financial institutions typically adopt a Three Lines of Defense model to improve
effectiveness of risk management. The second and third lines of defense must have the
appropriate skills and training necessary to understand the risks involved in the delivery
of business services using cloud - services owned and managed by the first line. Establish
clear roles and responsibilities both within and across the three lines of defense's
functions to verify the effectiveness and auditability of the cloud operating model.
Reassess these roles and responsibilities at regular intervals to keep the governance model
efficient and effective.

Financial institutions deploying generative AI workloads must extend their traditional Three Lines of Defense model to address unique risks associated with large language models (LLMs) and foundation models. Establish specialized governance for model selection and validation, implement robust output validation and bias monitoring processes, verify algorithmic explainability and accountability, and develop specialized oversight capabilities for AI/ML risks across model development, deployment, and ongoing operations.

## FSIOPS01-BP01 Define roles and responsibilities across risk functions

As explained in the preceding general design principles section, financial
institutions typically adopt a Three Lines of Defense model to improve effectiveness of
risk management. The second and third lines of defense must have the appropriate skills
and training necessary to understand the risks involved in the delivery of business
services using the cloud (services owned and managed by the first line). Clear roles and
responsibilities need to be established both within and across the three lines of
defense's functions to verify the effectiveness and auditability of the cloud operating
model. These roles and responsibilities must be reassessed at regular intervals to keep
the governance model efficient and effective.

### Prescriptive guidance

The roles and responsibilities of each of the three lines of defense should be
clearly communicated and understood. Publishing a RACI (Responsible, Accountable,
Consulted, Informed) matrix on an intranet or wiki page is a good way to reduce
misunderstandings about which role owns each activity. Periodic review of these roles
and responsibilities should occur more frequently immediately after they are defined or
dramatically changed, and can be less frequent otherwise. The people who fill roles
within the three lines of defense should be documented as well, and membership in these
roles should require a standard level of training in order to consistently handle risk
management.

## FSIOPS01-BP02 Engage with your risk management and internal audit functions to implement a process for the approval of cloud risk controls

Significant changes in technology necessitate a refreshed assessment of new potential
risks and their validations. Technology changes include migrating to the cloud, use of
newer database tools, extensive mobile application usage, and AI/ML technologies. These
changes may present risks to the existing control environment such that it may be unable
to mitigate the original identiﬁed risks, but also may not be eﬀective across a much
broader spectrum of changes. Engagement with the risk and internal audit functions helps
align with required governance obligations as cloud usage increases. This engagement needs
to include documentation and demonstration by the first line, to the second and third
lines, of the controls, technology, and processes that have been implemented to secure and
operate the cloud environment. This process can contain a regular review cadence for new
controls, so the first line can evolve their implementations as needed to quickly and
safely adopt best practices for new threats.

### Prescriptive guidance

All stakeholders from the three lines of defense should be invited to participate
in suggesting, evaluating, and approving changes to risk controls. A periodic review of
risk controls, as well as an out-of-cycle mechanism to suggest updates, should be
clearly documented and understood by all stakeholders. The lifecycle of a risk control
(suggestion, review, approval, training, implementation, and retirement) should also be
documented and understood. Prior to implementation of a specific risk control, metrics
should be identified to indicate the effectiveness of the control. These metrics should
be generated and compiled automatically and should be reviewed periodically throughout
the risk control's lifecycle. Thresholds that indicate effectiveness should be
established, and the continued breach of those thresholds should prompt review of the
risk control, with an expectation that it be updated or retired.

## FSIOPS01-BP03 Implement a process for adopting appropriate risk appetites

Failures can happen at any time. The appropriate risk authority within the firm (for
example, the board of directors, chief risk officers, or business risk officers) needs to
evaluate the criticality of a business process (and the underlying workloads that support
that process) and specify the level of availability that the firm requires for that
process. This must take into consideration the potential impact that a disruption of that
process has on the firm, the market, the customers, and regulatory bodies managing the
financial infrastructure, as well as the cost of operating the workload in a high
availability mode weighed against business agility and innovation. Working backwards from
these risk appetites allows you to drive the operational priorities and the resiliency
design choices of cloud workloads supporting business services in a prioritized manner.
Setting clear risk appetites allows for effective risk management and governance.

### Prescriptive guidance

All workloads should be categorized based on their criticality and associated risk
tolerance. In financial services organizations, this classification has often already
occurred as part of disaster recovery planning, and these risk categorizations can be
reused elsewhere. Once risk categories are established, requirements should be
identified to be applied to workloads within each risk category. Examples of
requirements might be recovery time objective (RTO) or recovery point objective (RPO)
expectations, use of encryption for data in-transit and at rest, and geographies within
which data must be stored. Building upon these requirements, preferred architectural
patterns should be identified that help meet the needs of each risk category in an
efficient and manageable way. Publishing these reference architectures is a good way to
encourage their adoption, as it simplifies the use of a consistent and preferred
architecture, and also provides a foundation for automation.

## FSIOPS01-BP04 Define a generative AI model risk management framework

Establish a comprehensive framework for evaluating, approving, and monitoring generative AI models used in production. This framework should include model inventory management, risk tiering based on use case criticality, and clear approval processes for model deployment and updates. Document acceptable use policies for generative AI, prohibited use cases, and escalation procedures for model-related incidents, and address governance for both internally developed and third-party foundation models.

### Prescriptive guidance

Create a generative AI model registry documenting all models in use, their versions, approved use cases, and risk classifications, training data sources, and model dependencies.

Implement a formal model validation process as well as comprehensive model evaluation capabilities including automated quality and safety assessments with guardrails for hallucination detection, bias and continuous drift detection, model explainability, fairness, and ongoing compliance monitoring.

Establish clear ownership and accountability for each generative AI model across the three lines of defense.

Use Amazon SageMaker AI Model Registry and AWS Service Catalog to manage approved model versions and deployment patterns. Verify that the registry supports comprehensive audit trails and regulatory reporting requirements.

Establish model retirement and rollback procedures for underperforming or problematic models with clear triggers and processes.

Implement governance processes for third-party foundation models and API services, including vendor risk assessment and ongoing monitoring.

## FSIOPS01-BP05 Implement human-in-the-loop validation for critical processes

Implement human-in-the-loop for critical processes by establishing systematic review workflows where subject matter experts validate AI-generated outputs, especially low-confidence predictions and high-stakes decisions, using tools to create feedback loops that enable continuous model improvement, improve regulatory adherence, and maintain appropriate human oversight for decisions impacting critical business processes or customer experiences.

### Prescriptive guidance

For high-risk use cases customer-facing decisions, regulatory reporting, or financial calculations, implement mandatory human review processes. Design workflows that require human validation before generative AI outputs are used in critical business processes.

Establish clear escalation procedures and conflict resolution processes when human reviewers disagree with AI recommendations.

Implement comprehensive audit trail requirements that log all human interventions, rationales, timestamps, and reviewer identities.

Ensure human reviewers receive appropriate AI training and maintain current domain expertise for their review areas.

Create feedback loops to capture human reviewer insights for continuous model improvement.

Implement monitoring and reporting on human override rates and patterns to identify potential model performance issues.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops01.html*

---

# FSIOPS2: Have you completed an operational risk assessment?

Financial services workloads should be continually reviewed and prioritized with regard
to their risk impact to the overall business (for example, based on their reputational,
financial, or regulatory impact).

## FSIOPS02-BP01 Understand the Shared Responsibility Model and how it applies to services and workloads you run in the cloud

In connection with your use of the cloud, you must understand how the [AWS Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) affects your control environment. For example, certain
controls may be the responsibility of AWS, but certain controls remain the
responsibility of the financial services institution. Review the AWS Shared
Responsibility Model and map AWS responsibilities and customer responsibilities
according to each AWS service you use and your control environment. For those controls
that are the responsibility of AWS, you can use [AWS Artifact](https://aws.amazon.com/artifact/) to access audit reports and review the implementation and
operating effectiveness of AWS security controls.

### Prescriptive guidance

Review and understand the [AWS Shared Responsibility
Model](https://aws.amazon.com/compliance/shared-responsibility-model/), and the different demarcation points that apply to AWS infrastructure
services (such as EC2), container services (such as RDS), and abstracted services (such
as S3). If your organization has central functions (like a Cloud Center of Excellence or
governance team), publish a shared responsibility model for your organization, which
clearly defines the roles of AWS, the central team, and distributed teams.

## FSIOPS02-BP02 Develop an enterprise cloud risk plan

Map the interactions between business consumers of cloud services and the internal
stakeholders that shape this consumption, including risk and control considerations.
Integrate across the three lines of defense functions, and provide necessary resources and
training to satisfy their mandates for operating and protecting your business in the cloud
while you strive to achieve your strategic goals.

This integration can be achieved by carrying out a risk-based assessment of your
operating model, and is especially effective when complemented with a review of
decision-making processes and authority to determine if they are cloud-appropriate. As
requirements are translated into controls, pay attention to the strength of the controls
to mitigate the identified risks. Another key risk factor includes the ability to control
design and performance to facilitate independent assessment by internal risk management
and audit functions. Focus on control design helps you incorporate key control
requirements into the design from the start.

### Prescriptive guidance

Evaluate existing risk models in use, and related policies, for relevance in a
cloud environment. Many risk models are focused on on-premises architectures and do not
account for advantages of cloud-based workloads. Reach out to your AWS account team to
leverage AWS expertise in risk and compliance.

## FSIOPS02-BP03 Evaluate data privacy and security requirements for generative AI

Generative AI models require careful consideration of data handling, especially when processing sensitive financial information. Implement data classification, tokenization, and privacy-preserving techniques when using foundation models. Adhere to data residency requirements and understand the data processing practices of third-party model providers. Establish data retention policies and ensure generative AI systems support regulatory requirements including data subject rights.

### Prescriptive guidance

Use Amazon Bedrock with AWS PrivateLink to implement network isolation for generative AI inference. Implement data masking and tokenization before sending sensitive data to foundation models. Configure Amazon Bedrock Guardrails to prevent unauthorized data exposure in model outputs. Use AWS KMS for encryption of prompts and responses containing sensitive information. Document data flow diagrams showing how sensitive data moves through generative AI pipelines including retention periods and deletion schedules.

Implement AWS CloudTrail and Amazon CloudWatch for comprehensive audit logging of data access and model interactions.

Define specific data retention periods for prompts, responses, and model training data in accordance with regulatory requirements.

## FSIOPS02-BP04 Establish prompt engineering standards and version control

Prompts are critical operational assets in generative AI systems requiring comprehensive governance frameworks. Implement version control, testing, and approval processes for prompt templates used in production. Establish prompt engineering best practices and security guidelines to prevent prompt injection attacks.

### Prescriptive guidance

Store production prompts in AWS CodeCommit or similar version control systems with change tracking and approval workflows.

Implement automated testing for prompt templates using representative test cases. Use AWS Lambda and AWS Step Functions to create controlled prompt execution pipelines with automated rollback capabilities.

Establish prompt security guidelines including input validation, sanitization and protection against prompt injection attacks.

Establish prompt performance monitoring to track effectiveness and model response quality over time with automated alerting.

Define escalation procedures for prompt-related security incidents and integrate with existing incident response frameworks.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops2.html*

---

# FSIOPS3: Have you assessed your specific workload against regulatory needs?

Financial services institutions must be aware of all applicable regulatory and
compliance obligations for their use of cloud services, and they should take appropriate
steps to meet those obligations.

## FSIOPS03-BP01 Implement a process for the review of applicable compliance and regulatory requirements for your workload

Financial services institutions must be aware of all applicable regulatory and
compliance obligations for their use of the cloud, and they should take appropriate steps
to meet those obligations. As part of your strategy, review your migration plan and
control frameworks with the relevant internal stakeholders responsible for compliance to
identify any compliance requirements, including legal and regulatory requirements that
apply to your use of the cloud. Note that designing a workload to meet specific technical
requirements may only be one aspect of compliance, so it's important to conduct a
comprehensive regulatory and compliance review. This process must include both initial
design and planning, as well as pre-production readiness activities.

### Prescriptive guidance

Use the [AWS Compliance Center](https://www.atlas.aws/) to
learn about key cloud-related regulatory requirements that impact your use of the cloud,
and the regulations that apply within your geography. Design a process to monitor
evolving changes to compliance and regulatory obligations. Use [AWS Config Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) and AWS Audit Manager to continually evaluate
your compliance to applicable regulatory frameworks. If appropriate, review the [AWS Sub-Processors](https://aws.amazon.com/compliance/sub-processors/) list
and [sign up](https://pages.awscloud.com/sub-processors/) to be
notified of changes. Use [AWS Artifact](https://aws.amazon.com/artifact/)
to gather compliance reports that apply to your workload and geography.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops3.html*

---

# FSIOPS4: How do you assess your ability to operate a workload in the cloud?

Financial services institutions often have a robust set of operating policies that
govern behaviors and decision-making for activities such as disaster recovery planning,
capacity management, security and compliance guardrails, and data backup and recovery. Cloud
services support new technologies, architectural patterns, and automations which are not
possible or practical for on-premises environments. Policies which were originally created
for on-premise environments should be revisited from a cloud perspective, rather than
assumed to be necessary and relevant.

## FSIOPS04-BP01 Implement a change management process for cloud resources

Cloud IT change management processes facilitate changes to IT systems in order to
minimize risks to production environments while adhering to policies, audit, and risk
controls. It is not uncommon, especially within financial services institutions, to see a
gated change management process often requiring a review by external change advisory
boards, which can take days or even weeks. As organizations take advantage of
configuration management, infrastructure as code (IaC), automated testing and validation,
and continuous integration and delivery, they can implement lightweight approval processes
that are tightly integrated into CI/CD pipeline tools.

By automating detection and rejection of bad changes, many manual approval steps can
be fully automated with a higher degree of confidence. Even in highly regulated industries
where external reviews are required, such as financial services, reviews should still be
integrated with the overall pipeline, even if they are manual steps initially. Regulatory
requirements such as the Sarbanes-Oxley Act requires all financial reports to include an
internal controls report that documents every change made to your workloads. Performing
operations as code provides the capability to test, model, and simulate scenarios before
rollout, which limits the potential for human error. Additionally, it satisfies regulatory
requirements by providing auditors a complete record of all applied changes, including the
environment in which tests and validations were run and the identity and timestamp of each
change approval. This speeds up deployment cycles and innovation, while preserving
security controls and guardrails.

A good change management process delivers business value while balancing risk against
business value. It should do so in a way that maximizes productivity and minimizes wasted
effort or cost for all participants in the process. Automation, integration, and
deployment tools in the cloud allow businesses to make small, frequent changes that reduce
risk and deliver business value at an increased rate. For additional guidance, see [Change Management in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/change-management-in-the-cloud/change-management-in-the-cloud.html).

### Prescriptive guidance

Financial services institutions must develop cloud capabilities in layers,
producing approved, reusable artifacts at each layer, such as:

- [golden Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-update-patch-golden-ami.html),
- [CloudFormation
Templates](https://aws.amazon.com/cloudformation/),
- [Service Catalog](https://aws.amazon.com/servicecatalog/) Products,
- [container base
images](https://aws.amazon.com/blogs/containers/designing-a-secure-container-image-registry/),
- software packages,
- and [Lambda deployment
packages](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html).

Artifacts at foundational layers must go through a change control process so that
they comply with enterprise guidelines, which can then be repurposed as building blocks
by the rest of the organization. AWS Systems Manager Change Manager provides tracking and
approval, and allows for the implementation of operational changes to application
configurations and infrastructures. As the organization builds higher-level applications
on a foundation of certified artifacts, you can expedite the change control process, as
it only needs to focus on the higher-level artifacts, accelerating change while
minimizing risk and ensuring compliance. Over time, organizations develop capabilities
to administer most of the changes in automated fashion, with only a subset of changes
that require manual intervention.

## FSIOPS04-BP02 Implement infrastructure as code

The benefit of the cloud and infrastructure as code is the ability to build and tear
down entire environments programmatically and automatically. If architected with
resiliency in mind, a recovery environment can be implemented in minutes using AWS CloudFormation
templates or AWS Systems Manager automation. Automation is critical for maintaining high
availability and fast recovery.

### Prescriptive guidance

AWS offers a wide breadth of automation tools to accomplish resiliency
objectives. AWS Systems Manager helps automate complete runbooks that are used during the
recovery of an application during a disaster. You can sequence a complete set of
operations to automatically initiate on detection of an event. With Systems Manager
automation documents, you can manage these runbooks similar to the way you manage code.
You can version them and update them along with every release. This helps keep your
recovery plan in sync with released code and updates to infrastructure.

## FSIOPS04-BP03 Prevent configuration drift

Drift of infrastructure configuration between primary and secondary sites can lead to
failure in recovery during a disaster event. Implementation of code-based management
practices across your infrastructure, applications, and operational procedures provides a
high degree of version control, testing, validation, and mitigation of human error and
configuration drift, which is necessary to limit the introduction of errors into your
environment and to reduce the mean time to recover (MTTR).

### Prescriptive guidance

Financial services institutions should monitor changes to application
infrastructure by using:

- [AWS CloudFormation
drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html),
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/),
- and [AWS Config](https://aws.amazon.com/config/).

These services monitor activity within your AWS account, including actions taken
through the [AWS Management Console](https://aws.amazon.com/console/), [AWS SDKs](https://aws.amazon.com/developer/tools/), command line tools, and
other AWS services. Once detected, you can automate the reactive action by defining
workflows using [AWS EventBridge](https://aws.amazon.com/eventbridge/)
integration and [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops4.html*

---

# FSIOPS5: How do you understand the health of your workload?

Financial services institutions are required to communicate service disruptions,
operational events, and failures to downstream stakeholders and regulatory bodies. They
should continually monitor their workloads in the cloud and conduct root cause analysis
(RCA) as an exercise in understanding the events and circumstances that led to unexpected
results, as well as mitigation efforts put in place to prevent recurrence.

## FSIOPS05-BP01 Use enhanced monitoring in the cloud

High availability for financial services workloads that support critical functions
requires the ability to detect failures and quickly recover from them. You can understand
the operational state of your workloads by defining, collecting, and analyzing metrics in
the cloud that can be incorporated into your operating model. These metrics are emitted by
your code, workloads, and user activity, and need to be collected in a centralized,
queryable system that can be used to visualize and examine real-world performance data.
This is important for diagnosing issues that are often not clear from looking at just at
application logs, Amazon CloudWatch, or system logs in isolation.

### Prescriptive guidance

Review [Monitoring and Observability](https://aws.amazon.com/cloudops/monitoring-and-observability/) to familiarize yourself with the capabilities of
AWS services. Financial institutions require logs and metrics for two distinct use
cases: operational analysis (such as troubleshooting during an incident) and regulatory
compliance. Application logs can be collected with Amazon CloudWatch Logs and stored in a centralized
AWS account dedicated to logging. Access to the dedicated logging AWS account should
be limited and based on least privilege, and the data can be shared in a read-only
manner to other AWS accounts for analysis.

If immutable log storage is required for regulatory or corporate policy compliance,
use [Amazon S3 Object Lock](https://aws.amazon.com/s3/features/object-lock/)

or [Amazon Glacier Vault
Lock](https://aws.amazon.com/blogs/aws/glacier-vault-lock/) for WORM storage.

Use AWS tools such as [OpenSearch](https://aws.amazon.com/opensearch-service/) or [Amazon Athena](https://aws.amazon.com/athena/), or
third party tools such as Splunk, Datadog, or Sumo Logic, to provide indexing, search,
analysis, and visualization capabilities.

Use [CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) for metrics and [CloudWatch anomaly
detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) to detect changes in trends and send alerts to Operations
teams.

[AWS X-Ray](https://aws.amazon.com/xray/) helps you understand how your
application and its underlying services perform to identify and troubleshoot performance
issues and errors.

You can also experience these capabilities in your own AWS account by running the
[One Observability Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US), where you learn about AWS observability
functionalities on [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html),
[AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html), [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html), and [AWS Distro for
OpenTelemetry](https://aws-otel.github.io/). This workshop deploys a microservice-based application and
guides you in discovering actionable insights through various monitoring tools. Upon
conclusion, the learner is expected to have a clear understanding of logging, metrics,
and traces, as well as techniques for using them across a variety of workload types.

For critical or regulated workloads workloads, Enterprise Support customers should
consider subscribing to [AWS Incident Detection and
Response](https://aws.amazon.com/premiumsupport/aws-incident-detection-response/).

AWS Incident Detection and Response offers eligible AWS Enterprise Support
customers proactive engagement and incident management to reduce the potential for
failure and accelerate recovery of critical workloads from disruption. It achieves these
objectives by fostering joint preparation with AWS to develop runbooks and response
plans customized to the context of each workload onboarded to the service. Onboarded
workloads are monitored by a team of Incident Management Engineers (IMEs) to detect and
engage you on a call bridge within five minutes of a critical alarm.

AWS Incident Detection and Response begins with a review of your workloads for
reliability and operational excellence. AWS experts work with you to define critical
metrics and alarms that provide improved visibility into the application and
infrastructure layers of your workloads, which makes it easier to find and prioritize
issues during an incident. AWS Incident Management Engineers continually monitor your
workloads, detect critical incidents, and engage you on a call bridge with the right
AWS experts to accelerate the recovery of your workloads. All incidents are managed
with the highest level of severity and escalation, and AWS remains engaged until the
incidents are resolved. Lessons learned from previous incidents inform improvements to
response plans and workload architecture, which drives a continuous improvement cycle to
improve the resiliency of your workloads.

## FSIOPS05-BP02 Monitor cloud provider events

Financial institutions should use the AWS Health Dashboard, which provides
information and remediation guidance when AWS is experiencing events that may impact
workloads. The dashboard displays relevant and timely information to help manage events in
progress, and provides proactive notifications to help plan for scheduled activities. With
AWS Health Dashboard, alerts are generated by changes in the health of the AWS
resources used in your applications, giving you event visibility and guidance to help
quickly diagnose and resolve issues. Enterprise support and business support accounts who
have access to the AWS Health API can use this API to integrate the information from
AWS Health Dashboard into the centralized monitoring system and define a consistent
and comprehensive alerting mechanism.

### Prescriptive guidance

[AWS Health](https://docs.aws.amazon.com/health/) provides ongoing
visibility into your resource performance and the availability of your AWS services
and accounts. You can use AWS Health events to learn how service and resource changes
might affect your applications running on AWS. AWS Health provides relevant and
timely information to help you manage events in progress. AWS Health also helps you be
aware of and prepare for planned activities. The service delivers alerts and
notifications initiated by changes in the health of AWS resources, which provides
event visibility and guidance to help accelerate issue resolution. AWS Health provides
information about service operations, such as operational issues, planned maintenance,
and planned software lifecycle events.

For comprehensive visibility into AWS Health event details, such as affected
resource IDs, current status (open or closed), and resource status, use AWS Health
endpoints, such as the AWS Health API, the `aws.health` source in Amazon EventBridge,
and the AWS Health Dashboard. These endpoints provide the most detailed and real-time information
about ongoing events and changes that might affect your workloads.

[AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) notifies you through additional UX channels (email, chat, or push
notifications to the AWS Management Console mobile application). AWS Health event notifications don’t
contain as much detailed data as the endpoints listed previously. However, they provide a
simple and effective way to notify stakeholders of issues and changes. Based on rules that
you create, User Notifications creates and sends a notification when an event matches the values that
you specify in a rule. You can select which UX delivery channels a notification is sent to
and set up aggregation to reduce the number of notifications generated for specific
events. Notifications are also visible in the AWS Management Console Notifications Center. For example,
you can receive chat notifications if you have resources in your AWS account that are
scheduled for updates, such as EC2 instances. For more detail, see [Getting
started with AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html).

You can integrate AWS Health events with Jira and ServiceNow to receive operational
and account information, prepare for scheduled changes, and manage AWS Health events
using the AWS Service Management Connector. The Service Management Connector integration with AWS Health can use AWS Health events
sent through EventBridge to automatically create, map, and update JIRA tickets and ServiceNow
incidents.

You can use organizational view and delegated administrator access to manage
AWS Health events across the organization within Jira and ServiceNow and incorporate
AWS Health information directly into your team’s workflow. For more detail on ServiceNow
integration using the Service Management Connector, see [Integrating AWS Health in ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-aws-health.html).
For more detail on Jira Management Cloud integration using the Service Management Connector, see [AWS Health](https://docs.aws.amazon.com/smc/latest/ag/cloud-sys-health.html).

## FSIOPS05-BP03 Implement comprehensive generative AI observability

Deploy [specialized monitoring](https://aws.amazon.com/cloudwatch/features/generative-ai-observability/) for generative AI workloads that tracks model performance, output quality, token usage, latency, and cost metrics. Monitor for hallucinations, bias, and drift in model outputs. Implement automated alerting for anomalous model behavior and establish prompt performance monitoring to track effectiveness and model response quality over time with automated alerting.

Define escalation procedures for prompt-related security incidents and integrate with existing incident response frameworks.

### Prescriptive guidance

Use Amazon CloudWatch custom metrics to track generative AI-specific KPIs (like tokens per second, prompt success rates, and output validation scores) and customer satisfaction metrics for generative AI-powered interactions. Implement Amazon Bedrock's built-in logging capabilities to capture all model interactions.

Deploy automated quality checks using AWS Lambda to validate model outputs against expected patterns. Use Amazon SageMaker AI Model Monitor for continuous model performance tracking.

Set up cost alerting for token usage to prevent unexpected expenses and optimize resource utilization.

Use Amazon Bedrock's model evaluation capabilities for automated quality assessments and performance benchmarking.

Establish baseline performance metrics and use Amazon CloudWatch anomaly detection for automated drift identification and alerting.

Implement data leakage detection in model outputs and monitor unauthorized access attempts to generative AI endpoints.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops5.html*

---

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

---

# FSIOPS7: Have you developed a continuous improvement model?

Financial institutions should continually assess and optimize their operational
processes.

## FSIOPS07-BP01 Test, model, and simulate scenarios before rollout

One of the best practices to determine if you have addressed your risk with
appropriate controls is to actually run scenarios against your cloud control framework and
operational procedures. Once your risk and control program is established, financial
institutions should continually asses and optimize their operational processes. Regular
[game days](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_run_game_days.html) for workloads deployed on AWS can help build your team's muscle
memory and validate that all operational procedures are effective in supporting your
recovery objectives and compliance with notification requirements to regulatory bodies. We
recommend designing game days to test your risk appetite and include severe, but plausible
scenarios.

### Prescriptive guidance

Identify financial services compliance requirements first, and then structure your
game days to meet those requirements. Align the complexity of game days with the
resources available within your organization. For large organizations, game days are
often scoped to a specific business unit or product team. It's acceptable to presume
certain inputs from other teams during your initial game days, which can make scheduling
more practical. It's more important to complete simple game days regularly, and iterate
on the scope and complexity over time, than to try to run complex game days from the
beginning. The most critical piece of a game day is the retrospective review of lessons
learned and the iterative improvement over time. Sufficient time to accomplish this
should be set aside early in the planning process so that it can occur in the days
immediately following the game day.

## FSIOPS07-BP02 Conduct post-event operational reviews

Post-event operational reviews should be conducted after an incident. After
troubleshooting and performing repair procedures, follow-up documentation and actions
should be assigned. An effective post-event review results in a list of practical actions
that address each of the issues that allowed the threat actor to succeed. These actions
should minimize the impact of the event and teach the wider enterprise how to prevent,
detect, and respond to a similar event in the future. For significant events, a Correction
of Error (COE) document should be composed to capture the root cause and take preventative
actions for the future. Implementation of the preventative measures should be measured in
future operations meetings.

### Prescriptive guidance

Post-event operational reviews are comprised of two components: identification of
the problem (root cause analysis) and the identification of actions to help prevent a
reoccurrence of the event (corrective actions). Identify a mechanism, such as an ITSM
tool or ticketing system, to track root cause analysis efforts and associated corrective
actions. Ownership for each task should be assigned to an individual, and a periodic
review should be used to track status. In a large and complex environment, competing
priorities and urgent activities can supersede processes such as post-event reviews that
are important for long-term stability. Leaders should establish a culture which
prioritizes these reviews, and should encourage teams to set aside a recurring time to
spend on analysis and corrective actions.

## FSIOPS07-BP03 Implement feedback loops for model improvement

Establish mechanisms to capture user feedback on generative AI
outputs and use this data to improve prompt engineering, model
selection, bias detection, and operational procedures. Create
processes for incorporating lessons learned into model
governance and operational practices.

### Prescriptive guidance

Deploy feedback collection mechanisms using Amazon DynamoDB to
store user ratings and comments. Use Amazon Comprehend to
analyze feedback sentiment and identify improvement areas.
Implement A/B testing frameworks using AWS Lambda to compare
different models or prompts. Create monthly operational
reviews focused on generative AI metrics and improvement
opportunities. Use Amazon SageMaker AI Clarify for automated bias
detection and fairness analysis based on feedback patterns.
Implement Amazon Athena for advanced analytics on feedback
trends and correlation analysis.

## FSIOPS07-BP04 Conduct generative AI-specific chaos engineering

Test the
[resilience
of generative AI workloads](https://catalog.us-east-1.prod.workshops.aws/workshops/d56fd754-5e56-43c5-addc-d69ac130a099/en-US) through controlled experiments
including model API failures, rate limiting scenarios, quality
degradation simulations, and bias amplification scenarios.
Validate that fallback mechanisms and human oversight processes
function correctly under stress.

### Prescriptive guidance

Use
[AWS Fault Injection Service](https://builder.aws.com/content/2uSMnBJb3h7JxB9SkryFvXfQWk8/chaos-engineering-scenarios-for-genai-workloads) to test generative AI workload
resilience.

Simulate model API throttling, timeout scenarios, and complete
service or model unavailability to test failover mechanisms
and business continuity procedures.

Test fallback mechanisms when primary models are unavailable
including automated switching to backup models.

Validate that human review processes can handle increased load
during model failures.

Test system behavior when input data quality deteriorates to
ensure graceful degradation and appropriate human intervention
triggers.

Simulate bias amplification scenarios to test detection
mechanisms and response procedures for maintaining fair and
compliant AI outputs.

Test cross-system dependencies by simulating failures in
databases, APIs, and other generative AI services' dependent
systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops7.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
