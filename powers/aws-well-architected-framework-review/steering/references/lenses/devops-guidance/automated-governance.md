# Automated governance

**Saga**: Automated governance  
**Best Practices**: 39

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.1] Adopt a risk-based compliance framework

**Category:** FOUNDATIONAL

Managing compliance in a DevOps model can initially feel even
more challenging than traditional models due to the
fast-paced, iterative, and distributed ways of workings.
Risk-based compliance framework such as NIST Cybersecurity
Framework, ISO 27001, or CIS Controls help to align your
DevOps processes and tools with industry best practices and
compliance requirements. These frameworks offer a structured
methodology for managing cybersecurity risk in compliance with
the organization's business needs.

Select a relevant framework that fits your business and security needs and assess
your current practices against this framework, identifying any gaps in compliance. Work
towards addressing these gaps and continually monitor and reassess your practices to help
ensure ongoing compliance. Leverage this well-architected guidance to improve your DevOps
capabilities to more efficiently meet these compliance requirements. Use cloud-native
services and tools to track compliance against your chosen framework.

**Related information:**

- [Security Hub CSPM standards reference](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html)
- [Conformance
Packs - AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)
- [Automate
Cloud Audits - AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.1-adopt-a-risk-based-compliance-framework.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.2] Implement controlled procedures for introducing new services and features

**Category:** FOUNDATIONAL

To maintain the balance between encouraging innovation and
upholding compliance and governance requirements, platform
teams need a scalable, controlled procedure for introducing
new cloud vendor or third-party services to be used.

DevOps culture encourages continuous learning and exploration
of new technologies, tools, and services. Provide teams with
the ability to explore and experiment with new features and
services while maintaining organizational security and
compliance standards. Structure these exploration
opportunities in a controlled, secure manner, to promote
agility without compromising integrity.

Establish well-defined guardrails that uphold security and
compliance when introducing new features and services. This
includes access restrictions, acceptable use cases, and
alignment with security policies. Create sandbox environments
where teams can safely explore and test these features without
compromising production environments or violating governance
policies. Develop a systematic, scalable onboarding process
which allows platform teams to enable guardrails and policies
for governing usage of the service, which leads to enabling
the feature or service in other environments, including
production.

Follow the principle of least privilege by granting teams access to use only specific
actions or API calls for approved services. As services update and add new features, this
will help ensure that the platform team reserves the ability to perform onboarding
procedures with these new features as well.

**Related information:**

- [Example
service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.2-implement-controlled-procedures-for-introducing-new-services-and-features.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.3] Automate deployment of detective controls

**Category:** FOUNDATIONAL

Perform rapid and consistent detection of potential security
issues or misconfigurations by deploying automated,
centralized detective controls. Automated detective controls
are guardrails which continuously monitor the environment,
quickly identifying potential risks, and potentially
mitigating them.

Use a *compliance as code* approach to integrate compliance rules
into deployment pipelines. Additionally, implement detective rules in the environment for
real-time checks. Leveraging artificial intelligence (AI) and machine learning (ML) can
further enhance the capability to monitor and detect non-compliant configurations or complex
security threats.

**Related information:**

- [Cloud
Security Posture Management (CSPM) - AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS Config and AWS Organizations - AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-config.html)
- [Intelligent
Threat Detection - Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Building
Prowler into a QuickSight powered AWS Security
Dashboard](https://catalog.us-east-1.prod.workshops.aws/workshops/b1cdc52b-eb11-44ed-8dc8-9dfe5fb254f5/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.3-automate-deployment-of-detective-controls.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.4] Strengthen security posture with ubiquitous preventative guardrails

**Category:** FOUNDATIONAL

Perform rapid and consistent detection of potential security issues or
misconfigurations by deploying automated, centralized detective controls. Automated
detective controls are guardrails that continuously monitor the environment, quickly
identifying potential risks, and potentially mitigating them.

Guardrails can be placed at various stages of the development lifecycle, including
being directly enforceable within the environment itself—providing the most control and
security assurance. To provide a balance between agility and governance, use multiple layers
of guardrails. Use environmental guardrails, such as access control limitations or API
conditions, which enforce security measures and compliance ubiquitously across an
environment. Embed similar detective and preventative checks within the deployment pipeline,
which will provide faster feedback to development teams.

The actual implementation of environmental guardrails can vary
based on the specific tools and technologies used within the
environment. An example of preventative guardrails in AWS are
Service Control Policies (SCPs) and IAM conditions.

**Related information:**

- [Example
service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.4-strengthen-security-posture-with-ubiquitous-preventative-guardrails.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.5] Automate compliance for data regulations and policies

**Category:** RECOMMENDED

The rapid pace of development and decentralized nature of
operating under in a DevOps environment can pose challenges
for maintaining data privacy compliance. Automation and
guardrails can greatly ease this process by integrating
compliance checks and remediation actions throughout the
development lifecycle. This extends to automated enforcement
of data access and handling protocols, continuous monitoring
of resource configurations for data sovereignty and residency
requirements, and automated auditing and risk assessment.

Implement automated tools that can enforce data access and
handling policies. Set up continuous monitoring systems to
assess compliance with data sovereignty and residency
requirements. These tools should also be capable of automated
auditing, risk assessment, and triggering incident response
mechanisms when anomalies or threats are detected. By doing
so, your organization can adapt swiftly to changing data
privacy laws and regulations, bolster your data security
governance, and reduce the risk of data breaches or
non-compliance.

Automating this process is categorized as recommended because
not all organization practicing DevOps handle applicable
personal data.

**Related information:**

- [Data
Protection & Privacy at AWS](https://aws.amazon.com/compliance/data-protection)
- [Amazon
Information Request Report](https://d1.awsstatic.com/Security/pdfs/Amazon_Information_Request_Report.pdf)
- [AWS Security Blog: Data Privacy](https://aws.amazon.com/blogs/security/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.5-automate-compliance-for-data-regulations-and-policies.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.6] Implement auto-remediation for non-compliant findings

**Category:** RECOMMENDED

Manual identification and remediation of non-compliance issues
can be time-consuming and prone to errors. Automated systems
can rapidly respond to non-compliant resources,
misconfigurations, and insecure defaults as soon as they are
detected.

In the event of a non-compliance issue, an auto-remediation
process should be triggered, which not only resolves the
immediate issue but also initiates an alert to the developers.
This is important because, while the auto-remediation resolves
the problem at the system level, the developers need to be
made aware of the problem so that they can correct the source
of the error and prevent its recurrence. This dual approach of
auto-remediation and developer notification promotes a
learning environment and reduces the likelihood of recurring
non-compliance issues. It allows developers to address the
root cause of the configuration drift or non-compliance to
prevent the continual reintroduction of the same error.

While recommended for its efficiency and rapid response,
auto-remediation is not universally applicable to all
compliance issues. Certain issues might require manual
intervention or a more nuanced approach. Use preventative
guardrails and implementing detective and preventative
controls directly within the development lifecycle where
possible, with auto-remediation being a third best option.
These measures, when used together, yield a more compliant
environment.

The goal of auto-remediation should not just be the swift
resolution of issues, but also the continued education of
developers while reducing the overall incidence of
non-compliance.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP06 Monitor
and alarm proactively](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_monitor_instances_post_launch_proactive.html)
- [AWS Well-Architected Reliability Pillar: REL06-BP04 Automate
responses (Real-time processing and alarming)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_automate_response_monitor.html)
- [Remediating
Noncompliant Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [Automated
Security Response on AWS](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/)
- [Automating
ongoing OS patching - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/automating-os-patching.html)
- [Decommission
resources - Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/decommission-resources.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.6-implement-auto-remediation-for-non-compliant-findings.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.7] Use automated tools for scalable cost management

**Category:** RECOMMENDED

Automated cost management tools enable teams to remain agile
and innovative while maintaining budgetary control. As
deployment frequency increases due to DevOps improvements, it
becomes important to put in place guardrails to control
costs.

Use automated cost tracking mechanisms, such as cost budgets
and alerts, and tag resources for cost allocation. Use cloud
native cost management tools to monitor and report cloud
expenditure continuously. Ensure these tools can alert teams
when costs are approaching or exceeding budgeted amounts, and
where possible, consider implementing auto-remediation methods
to optimize resource usage, apply savings plans or reserved
instances, and decommission unused resources.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST02-BP05
Implement cost controls](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_controls.html)
- [Cloud
Financial Management](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/cloudfinancialmanagement.html)
- [AWS Billing and Cost Management Conductor](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/)
- [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.7-use-automated-tools-for-scalable-cost-management.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.8] Conduct regular scans to identify and remove unused resources

**Category:** RECOMMENDED

Over time, unused resources can often be a byproduct of
experimentation and more frequent deployments, including
dormant servers, unused deployment resources, idle containers,
redundant environments, and unused serverless functions. These
resources can pile up to create a less than ideal operating
environment if not managed effectively, leading to
inefficiencies, inflated costs, system unreliability, and
heightened security risks.

Perform automated scans scoped to all deployed resources in
your environment and pinpoint unused or outdated resources.
This can be accomplished by using health check endpoints,
reviewing logs, using metadata elements such as tags, or
checking billing dashboards for utilization.

Verify the status and compatibility of software running on these resources,
especially if they have been disconnected or powered off for extended periods of time.
These checks are especially useful for preventing *zombie servers*,
which have the potential to be rebooted after long periods of disconnection and might be
running outdated or incompatible software.

Based on the verification results and the organization's
policies, take action to remediate these resources, such as
updating the software, decommissioning the resources, or
integrating them back into the environment. Frequently
performing these scans can prevent potential service
disruptions, maintain up-to-date software across all
resources, and ensure the overall integrity of the DevOps
environment.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST02-BP06
Track project lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_track_lifecycle.html)
- [Implementing
health checks](https://aws.amazon.com/builders-library/implementing-health-checks/)
- [Decommission
resources - Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/decommission-resources.html)
- [Identifying
your unused resources - DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_UnusedResources.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.8-conduct-regular-scans-to-identify-and-remove-unused-resources.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.9] Integrate software provenance tracking throughout the development lifecycle

**Category:** RECOMMENDED

Software provenance tracking inspects the origin and evolution
of software components throughout their lifecycle to
understand where a piece of software originated, its
development and update history, and its distribution.
Provenance tracking ensures the integrity of software,
maintains compliance, and enhances the security of the
software supply chain throughout the development
lifecycle. Effective provenance tracking can prevent the
introduction of insecure components, offer early detection of
potential vulnerabilities, and provide insights for timely
remediation.

Developers are encouraged to use the best tools for the task
at hand, often including third-party software components.
These third-party elements can introduce an additional layer
of complexity and potential risk. Implementing software
provenance tracking mitigates these risks by promoting better
visibility into the lifecycle of software components, thereby
increasing accountability, transparency, and trust.

Provenance tracking should be integrated into all stages of
the development lifecycle. For instance, source code
provenance should be tracked at the time of code check-in or
commit into Version Control Systems like Git, while the
provenance of third-party components should be verified at the
time of component acquisition and usage using tools like
Software Composition Analysis (SCA). A
[Software
Bill of Materials (SBOM)](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html) can be used as a detailed list
of all components within your software, including the exact
version, digital signatures, and origin of each one.

Verify provenance at build and deploy time. Use digital signatures and hashing
algorithms to verify the integrity and provenance of software artifacts as part of the
deployment pipeline, validating the signature of an artifact against a trusted source
before it is used. It can also be useful to check running software continuously to
identify compromised or outdated software components post-deployment.

**Related information:**

- [SLSA
specification](https://slsa.dev/spec/v1.0/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.9-integrate-software-provenance-tracking-throughout-the-development-lifecycle.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.10] Automate resolution of findings in tracking systems

**Category:** RECOMMENDED

Automating the resolution of findings in tracking systems can
accelerate the security incident response process, prevent
untracked mitigation activities, and ensure accuracy in
reporting processes. It also allows teams to focus more on
development, resolving issues, and innovation, while
automation handles the routine tracking and resolution tasks.

Use tools that support automated tracking and resolution capabilities. When an issue
is detected, a ticket should be created automatically in the tracking system. Once the
issue is resolved, the system should be able to automatically validate the resolution and
close the corresponding ticket. This approach reduces the chances of human error, ensures
a faster response to issues, and is capable of providing comprehensive reporting and
analytics capabilities to support continuous improvement of the security posture.

**Related information:**

- [Automation
rules - AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.10-automate-resolution-of-findings-in-tracking-systems.html*

---

**Capability**: AG.ACG — Automated compliance and guardrails

# [AG.ACG.11] Digital attestation verification for zero trust deployments

**Category:** RECOMMENDED

Digital attestations are recommended to be created for each action that occurs during the development lifecycle. Attestations serve as evidence of compliance, which can be verified either during or post-deployment. Authorizing deployments by verifying attestations extends a zero trust security model to the development lifecycle. If attestations for the required quality assurance tests, pipeline stages, or manual approvals are missing or invalid, meaning that compliance and change management requirements were not met during the development lifecycle, the deployment can be either prevented or subjected to an exception mechanism for risk acceptance.

Incorporate the creation of digital attestations into the development lifecycle. Before deployment, verify that the required attestations have been digitally signed by trusted cryptographic keys and that they meet the change management and compliance policies. If a deployment is found to be non-compliant, you can choose to respond in several ways depending on your security and governance requirements. It can be used as a detective control which allows the deployment to proceed while keeping an audit log of the non-compliance for future investigation. It can also be used as a preventive control, stopping the deployment from proceeding entirely. Pairing this with an exception mechanism you could enforce directive controls to accept the identified risks for a period of time.

This approach to automated governance and change management continuously assesses the integrity of the software throughout the development lifecycle. It provides a method of authorizing deployment based on adherence to governance and compliance requirements, extending zero trust security model principles to the deployment process.

**Related information:**

- [Software attestations](https://slsa.dev/attestation-model)
- [in-toto Attestation Framework Spec](https://github.com/in-toto/attestation/blob/main/spec/README.md#in-toto-attestation-framework-spec)
- [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/)
- [Zero Trust Maturity Model](https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.11-digital-attestation-verification-for-zero-trust-deployments.html*

---

**Capability**: AG.CA — Continuous auditing

# [AG.CA.1] Establish comprehensive audit trails

**Category:** FOUNDATIONAL

Comprehensive audit trails involve capturing, recording, and
storing every action taken across your environment. This
provides a log of evidence that can offer insights for
security and audit teams, aiding in identifying suspicious
activities, evidencing non-compliance, and uncovering the root
cause of issues.

Effective DevOps processes are able to streamline both
software delivery and the audit process. Automated governance,
quality assurance, development lifecycle, and observability
capabilities provide a significant amount of data about the
processes that are being followed by your organization, and
the absence of data indicates those that are not. This data
can form a comprehensive audit trail, as steps such as
committing code and doing peer reviews can be traced back to
specific actors, actions, and timestamps.

Use tools for logging and tracking events should be enforced,
along with access controls to maintain the integrity and
confidentiality of audit data. Centralize evidence from these
tools in a secure, accessible location for easy retrieval
during audits. Consider using tools capable of automatically
pulling data from resource APIs to collect and organize
evidence rather than waiting for data to be pushed to it. It's
important that this data remains secure and accessible only to
auditors. There must be controls in place to prevent deletion,
overwriting, or tampering with the evidence in any way.
Regular audits of your audit systems and processes should also
be undertaken to ensure their effectiveness.

Recognize that while developers aren't auditors, they play a
significant role in the compliance process. Provide training
and resources to ensure that everyone on the team understands
the concept of compliance as it relates to each systems
specific industry.

**Related information:**

- [What
Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Automate
Cloud Audits - AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [Cloud
Audit Academy](https://aws.amazon.com/compliance/auditor-learning-path/)
- [Compliance
and Auditing with AWS](https://aws.amazon.com/cloudops/compliance-and-auditing/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc)
- [Verifiable
Controls Evidence Store](https://aws.amazon.com/solutions/implementations/verifiable-controls-evidence-store/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.ca.1-establish-comprehensive-audit-trails.html*

---

**Capability**: AG.CA — Continuous auditing

# [AG.CA.2] Optimize configuration item management

**Category:** FOUNDATIONAL

Configuration item management involves tracking and recording all resources used
across workloads and environments. It enhances visibility, operational efficiency, and helps
to ensure adherence to governance and compliance requirements. It aids in reviewing the
frequent changes and updates to infrastructure and application configurations, providing a
clear understanding of the system's state at any point in time.

In a DevOps environment, where changes are frequent and continual, use a tool that
maintains a resource inventory and continuous configuration log automatically with every
change. Establish a consistent tagging strategy to streamline organizing this inventory and
to assist in managing resources.

In cloud-based environments, with its high degree of dynamism, scalability,
auto-scaling, and elasticity, verify that your tools can keep up with automated, on-demand
changes. Understand the [AWS shared
responsibility model](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/shared-responsibility.html) and which teams within your organization are responsible for
managing each aspect of the configuration. In all cases, maintain an up-to-date and accurate
record of the configuration status of every item, tracking changes over time to provide a
comprehensive audit trail.

**Related information:**

- [What
Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- [Tagging
your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)
- [What
are resource groups?](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.ca.2-optimize-configuration-item-management.html*

---

**Capability**: AG.CA — Continuous auditing

# [AG.CA.3] Implement systematic exception tracking and review processes

**Category:** FOUNDATIONAL

DevOps environments are dynamic, characterized by rapid changes and updates. During
this rapid development cycle, temporary exceptions might need to be made, for instance,
granting greater permissions to a user for a specific task, or turning off a governance
control for a system update. While necessary, these exceptions can lead to unexpected issues
if not properly managed, and therefore, need to be tracked and revisited.

Implement a process for tracking exceptions, documenting each exception made and help
ensure these exceptions are revisited over time. This documentation should take place in a
centralized, searchable, and secure location. Critical details such as the reasoning behind
the exception, when it was made, who approved it, the business use case, and the anticipated
duration should be included. Clear roles and responsibilities should be assigned for the
creation, review, and retirement of exceptions to help ensure accountability.

To prevent exceptions from being lingering for vast amounts of time, implement
automated alerts for active exceptions that exceed their expected time frame. These alerts
serve as reminders to revisit and address these exceptions.

A regular review process of all exceptions should also be
scheduled. Depending on the associated risk, these reviews
could be conducted on a weekly, monthly, or quarterly basis.
These reviews will derive the continued necessity of each
exception, which could be investigated to become an approved
feature, and investigate any unexpected behavior that may have
arisen as a result of the exception. Once an exception is no
longer necessary, it should be retired and documentation
should be updated.

**Related information:**

- [Amazon's
approach to high-availability deployment: Dealing with the
real world](https://youtu.be/bCgD2bX1LI4?t=1349)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.ca.3-implement-systematic-exception-tracking-and-review-processes.html*

---

**Capability**: AG.CA — Continuous auditing

# [AG.CA.4] Enable iterative internal auditing practices

**Category:** RECOMMENDED

The continuous nature of DevOps supports the idea of frequent
audits, providing real-time insights, and practicing proactive
risk management. Consider taking an event-driven auditing
approach which allows for immediate detection and response to
compliance issues, increasing overall agility and efficiency
with automated evidence gathering and report generation
occurring constantly within the environment.

Automated alerts and notifications should be implemented to
identify potential issues rapidly and notify teams of
non-compliance. By running internal audits continuously and
integrating the process into the development lifecycle,
developers can address compliance issues early on, often
before they become a significant problem.

**Related information:**

- [Supported
control data sources for automated evidence - AWS Audit
Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.ca.4-enable-iterative-internal-auditing-practices.html*

---

**Capability**: AG.DEP — Dynamic environment provisioning

# [AG.DEP.1] Establish a controlled, multi-environment landing zone

**Category:** FOUNDATIONAL

Establish a multi-environment landing zone as a controlled foundation which
encompasses all of the environments that workloads run in. A landing zone acts as a
centralized base from which you can deploy workloads and applications across multiple
environments. In AWS, it is common to run each environment in a separate AWS account,
leading to hundreds or thousands of accounts being provisioned. Landing zones allow you to
scale and securely manage those accounts, services, and resources within.

Operate the landing zone using platform teams and the *X as a
Service* (XaaS) interaction mode, as detailed in the [Team Topologies](https://teamtopologies.com/) book by Matthew Skelton and
Manuel Pais. This enables teams to request or create resources within the landing zone using
infrastructure as code (IaC), API calls, and other developer tooling.

The landing zone has the benefit of maintaining consistency across multiple
environments through centrally-applied policies and service-level configurations. This
approach allows the governing platform teams to provision and manage resources, apply common
overarching policies, monitor and helps ensure compliance with governance and compliance
standards, manage permissions, and implement guardrails to enforce access control
guidelines, across all of the environments with minimal overhead.

It's a best practice within the landing zone to separate environments, such as
non-production and production, to allow for safer testing and deployments of systems. The
landing zone often includes processes for managing network connectivity and security,
application security, service onboarding, financial management, change management
capabilities, and developer experience and tools.

For most organizations, a single landing zone that includes
all environments for all workloads should suffice. Only under
special circumstances, such as acquisitions, divestments,
management of exceptionally large environments, specific
billing requirements, or varying classification levels for
government applications, might an organization need to manage
multiple landing zones.

Manage the landing zone and all changes to it as code. This
approach simplifies management, makes auditing easier, and
facilitates rollback of changes when necessary.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST02-BP03
Implement an account structure](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_account_structure.html)
- [Cloud
Security Governance - AWS Control Tower](https://aws.amazon.com/controltower/)
- [Landing
zone - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/aws-landing-zone.html)
- [Benefits
of using multiple AWS accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html)
- [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html)
- [AWS Control Tower and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-CTower.html)
- [Establishing
Your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html)
- [Provision
and manage accounts with Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)
- [AWS Account Factory Email: Many AWS Accounts, one email
address](https://github.com/aws-samples/aws-account-factory-email)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.1-establish-a-controlled-multi-environment-landing-zone.html*

---

**Capability**: AG.DEP — Dynamic environment provisioning

# [AG.DEP.2] Continuously baseline environments to manage drift

**Category:** FOUNDATIONAL

Baselining environments is a structured process for routinely updating and
standardizing individual environments within the landing zone to match a specified
configured state or *baseline*. Drift management, a part of this process,
involves the identification and resolution of differences between the environment's current
configuration and its desired baseline state.

Regular baselining helps to ensure consistency across
environments at scale, minimizing errors and enhancing
operational efficiency and governance capabilities. The
centralized platform team that manages the landing zone and
environments within require the ability to consistently add
new features, security configuration, performance
improvements, or resolving detected drift issues.

The team must be able to baseline all targeted environments
every time a change is made to the overall landing zone
desired state definition or when a misconfiguration is
detected within the environment.

It is the shared responsibility of the platform team and teams operating workloads to
verify that the correct policies, alerts, and resources are configured properly and
securely. As these teams are both making changes to the same environment, it is important
that all controls and resources managed by the platform team are secured against
unauthorized modifications by other teams operating within the environment. Changes being
made by the platform team to the environment should be communicated to the other teams
to promote a culture of transparency and collaboration.

All deployment, updates, or new features made to the
environments should be made through an infrastructure as code
(IaC) approach, which allows for version control, testing, and
reproducibility of environments. It is also recommended to
have a separate staging environment to test these changes
before they are deployed to the production environments,
further reducing the risk of disruptions or errors.

**Related information:**

- [Customize
your AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/customize-landing-zone.html)
- [Types
of Landing Zone Governance Drift](https://docs.aws.amazon.com/controltower/latest/userguide/governance-drift.html)
- [Customize
accounts with Account Factory Customization (AFC)](https://docs.aws.amazon.com/controltower/latest/userguide/af-customization-page.html)
- [Overview
of AWS Control Tower Account Factory for Terraform
(AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html)
- [Implementing
automatic drift detection in CDK Pipelines using Amazon EventBridge](https://aws.amazon.com/blogs/devops/implementing-automatic-drift-detection-in-cdk-pipelines-using-amazon-eventbridge)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.2-continuously-baseline-environments-to-manage-drift.html*

---

**Capability**: AG.DEP — Dynamic environment provisioning

# [AG.DEP.3] Enable deployment to the landing zone

**Category:** FOUNDATIONAL

Dedicate an environment for each system to host the resources
and tools required to perform controlled and uniform
application deployments to related non-production and
production environments. These deployment environments can
include infrastructure or services such as pipelines and build
agents.

At a minimum, each system should have a set of deployment, test, and production
environments to support the development lifecycle. Having these environments at the system
level, as opposed to sharing environments across multiple systems or at the team level,
provides multiple benefits:

- **Isolation of systems:** Each system's resources are
isolated, reducing the risk of cross-system interference, reaching quotas, and security
breaches.
- **Tailored environments:** The environments can be
customized according to the specific needs of each system, improving efficiency and
reducing unnecessary resource usage.
- **Separation of concerns:** Each environment handles a
specific aspect of the application lifecycle (deployment, testing, production), ensuring
a clean and organized workflow.

The deployment environment should include resources and tools to support building,
validation, promotion, and deployment of the system. A deployment environment may not be
necessary for all organizations and scenarios, such as if your development lifecycle tools
are hosted on-premises or outside of your landing zone. For these use cases, you will need
to verify network connectivity between your external tools and your landing zone
environments.

**Related information:**

- [Spaces
in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces.html)
- [Deployments
OU](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/deployments-ou.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.3-enable-deployment-to-the-landing-zone.html*

---

**Capability**: AG.DEP — Dynamic environment provisioning

# [AG.DEP.4] Codify environment vending

**Category:** RECOMMENDED

A core benefit of the DevOps model is team autonomy and reducing cross-team
dependencies. Through infrastructure as code (IaC), teams can establish and manage their
environments autonomously in a self-service manner, shifting from traditional methods
where operations teams would oversee these responsibilities.

By provisioning environments, and the accounts operating them,
as IaC or API calls, teams are empowered with the flexibility
to create environments according to their specific
requirements and ways of working. Codifying the environment
provisioning process provides teams with the flexibility to
create both persistent and ephemeral environments based on
their specific needs and workflows. In particular, this
code-based approach enables the easy creation of ephemeral
environments that can be automatically setup and torn down
when not in use, optimizing resource utilization and cost.

Use shared libraries or services that allow teams to request
and manage environments using IaC. These libraries should
encapsulate best practices for environment configuration and
should be designed to be used directly in deployment
pipelines, enabling individual teams to manage their
environments autonomously. This reduces the need for manual
requests or interactions with a developer portal, as well as
reduces the reliance on platform teams for provisioning and
managing environments on their behalf. This approach promotes
consistency and reduces overhead from cross-team
collaboration.

**Related information:**

- [What
is the AWS CDK?](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- [Create
an AWS Proton environment](https://docs.aws.amazon.com/proton/latest/userguide/ag-create-env.html)
- [Provision
and manage accounts with Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)
- [Provision
Accounts Through Service Catalog](https://docs.aws.amazon.com/controltower/latest/userguide/service-catalog.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.4-codify-environment-vending.html*

---

**Capability**: AG.DEP — Dynamic environment provisioning

# [AG.DEP.5] Standardize and manage shared resources across environments

**Category:** RECOMMENDED

Cross-environment resource sharing is the practice of deploying, managing, and
providing access to common resources across various environments from a centrally managed
account. This approach enables teams to efficiently use and manage shared resources, such
as networking or security services, without the need to replicate their setup in each
environment. By unifying the management of these foundational resources, individual teams
can focus more on the functionality of their workloads, rather than spending time and
effort managing common infrastructure components.

Platform teams should deploy and manage shared resources into
accounts they manage, then provide APIs or libraries that
individual teams can use to consume the shared resources as
needed. This approach reduces redundancy and promotes
standardization across the organization, allowing development
teams to concentrate on their unique workloads rather than
complex infrastructure management.

**Related information:**

- [Infrastructure
OU and accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/infrastructure-ou-and-accounts.html)
- [Sourcing
and distribution](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/sourcinganddistribution.html)
- [Sharing
your AWS resources - AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.5-standardize-and-manage-shared-resources-across-environments.html*

---

**Capability**: AG.DEP — Dynamic environment provisioning

# [AG.DEP.6] Test landing zone changes in a mirrored non-production landing zone

**Category:** RECOMMENDED

Changes to landing zones can have significant impacts across
teams and processes because it is consumed by many teams in an
organization. To minimize the risk of potential failures when
making changes to the landing zone, platform teams should
follow similar practices seen in the development lifecycle,
including thorough testing and validation in a dedicated
environment before rolling out to production.

When making changes to a landing zone, establish mirrored landing zones for testing
changes before deploying to the production landing zone. This allows for changes to be
validated without affecting the production environment. Use deployment pipelines to
promote, validate, and deploy changes between the mirrored and production landing zones,
performing extensive testing and validation at each stage.

Overall, this practice promotes safer changes to the
production landing zone which has the potential to impact many
teams in the organization. Clearly communicate with those
teams before rolling out changes to the production landing
zone so that they are informed of imminent changes, potential
impacts to their environments and systems, and the projected
timeline.

**Related information:**

- [Multiple
organizations: Test changes to your overall AWS
environment](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/multiple-organizations.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.6-test-landing-zone-changes-in-a-mirrored-non-production-landing-zone.html*

---

**Capability**: AG.DEP — Dynamic environment provisioning

# [AG.DEP.7] Utilize metadata for scalable environment management

**Category:** OPTIONAL

Effective environment management at scale requires the
collection and maintenance of key information about each
environment, such as ownership, purpose, criticality,
lifespan, and more. These details can offer visibility and
clarity which reduces potential confusion and misuse of
environments and assists with setting up proper controls based
on specific details associated with the environment.

Adopt techniques like resource tagging to track and maintain this metadata. Not only
does this allow platform teams to track and optimize costs by accurately attributing
resource usage to specific environments, but it also supports the management of access
controls and security measures, aligning governance and compliance needs with individual
environments.

For implementation, use available tagging features and APIs for resource management
and metadata tracking. Where additional metadata capture is required, consider creating or
integrating with a custom tracking system tailored to your specific needs, such as
existing configuration management database (CMDB) or IT service management (ITSM) tools,
providing a holistic view of all environments, thus empowering platform teams to better
govern and manage environments based on their metadata.

Although this practice is marked as optional, it is strongly
recommended for organizations operating in complex and
large-scale environments, where managing resources and
configurations based on metadata can significantly improve
efficiency, governance, and compliance. This indicator focuses
on leveraging metadata for active environment management,
distinguishing it from the broader scope of configuration item
management.

**Related information:**

- [Choosing
tags for your environment](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html)
- [Tag
policies - AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.7-utilize-metadata-for-scalable-environment-management.html*

---

**Capability**: AG.DEP — Dynamic environment provisioning

# [AG.DEP.8] Implement a unified developer portal for self-service environment management

**Category:** OPTIONAL

Consider implementing a self-service portal that empowers
developers to create, manage, and decommission their own
isolated development or sandbox environments, within the
established boundaries set by the platform team. While
fostering autonomy for development teams, this approach
accelerates the development process and reduces the
operational load on the supporting platform team. To ensure
adherence to the organization's standards and ensure
consistency, the portal could include predefined environment
templates and resource bundles.

While beneficial, the implementation of a developer portal is optional, particularly
if the organization is leveraging codified environment vending as recommended.
Infrastructure as code (IaC) presents an alternative approach that reduces human
intervention.

The self-service portal, if implemented, can adopt the *X as a
Service* (XaaS) interaction model as outlined in the [Team Topologies](https://teamtopologies.com/) book by Matthew Skelton and
Manuel Pais. The portal can evolve over time into a central resource for common, reusable
tools and capabilities preconfigured to comply with organizational standards, facilitating
streamlined automated governance activities. This might include centralized access to
common tools into a unified developer portal, including observability, security, quality,
cost, and organizational use cases. If adopted by many teams, this platform can become an
excellent method for communicating changes within the organization.

**Related information:**

- [The
Amazon Software Development Process: Self-Service
Tools](https://youtu.be/52SC80SFPOw?t=579)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.8-implement-a-unified-developer-portal-for-self-service-environment-management.html*

---

**Capability**: AG.DLM — Data lifecycle management

# [AG.DLM.1] Define recovery objectives to maintain business continuity

**Category:** FOUNDATIONAL

Clear recovery objectives help to ensure that teams can
maintain business continuity and recover with minimal data
loss, keeping the delivery pipeline flowing and maintaining
service reliability.

Set recovery point objectives (RPO) indicating how much data
loss is acceptable, and recovery time objectives (RTO)
specifying how quickly services need to be restored following
an incident. Develop and document your disaster recovery (DR)
strategy, make it available to teams, and conduct exercises
and trainings to maintain the ability to perform the
strategy. Implement policies and automated governance
capabilities that align with your RPO and RTO objectives.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL09-BP01 Identify
and back up all data that needs to be backed up, or reproduce the data from sources](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_identified_backups_data.html)
- [AWS Well-Architected Reliability Pillar: REL13-BP01 Define
recovery objectives for downtime and data loss](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html)
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)
- [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html)
- [Blog: Establishing
RPO and RTO Targets for Cloud Applications](https://aws.amazon.com/blogs/mt/establishing-rpo-and-rto-targets-for-cloud-applications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.1-define-recovery-objectives-to-maintain-business-continuity.html*

---

**Capability**: AG.DLM — Data lifecycle management

# [AG.DLM.2] Strengthen security with systematic encryption enforcement

**Category:** FOUNDATIONAL

With continuous delivery, the risk of data breaches that can disrupt the software
delivery process and negatively impact the business increases. To remain agile and rapidly
able to deploy safely, it is necessary to enforce encryption at scale to protect sensitive
data from unauthorized access when it is at rest and in transit.

Infrastructure should be defined as code and expected to change frequently. Resources
being deploy need to be checked for a compliant encryption configuration as part of
deployment process, while continuous scans for unencrypted data and
resource misconfiguration should be automated in the environment. These practices not only
aid in maintaining compliance, but also facilitates seamless and secure data management
across various stages of the development lifecycle.

Automate the process of encryption key creation, distribution,
and rotation to make the use of secure encryption methods
simpler for teams to follow and enable them to focus on their
core tasks without compromising security. Automated governance
guardrails and auto-remediation capabilities should be used to
enforce encryption requirements at scale, ensuring compliance
both during and after deployment.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL09-BP02 Secure and
encrypt backups](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_secured_backups_data.html)
- [AWS Well-Architected Security Pillar: SEC08-BP02 Enforce
encryption at rest](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html)
- [AWS Well-Architected Security Pillar: SEC09-BP02 Enforce
encryption in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html)
- [AWS Well-Architected Security Pillar: SEC09-BP01 Implement
secure key and certificate management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_key_cert_mgmt.html)
- [Encrypting
Data-at-Rest and -in-Transit](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.html)
- [Amazon's
approach to security during development: Encryption](https://youtu.be/NeR7FhHqDGQ?t=1646)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.2-strengthen-security-with-systematic-encryption-enforcement.html*

---

**Capability**: AG.DLM — Data lifecycle management

# [AG.DLM.3] Automate data processes for reliable collection, transformation, and storage using pipelines

**Category:** FOUNDATIONAL

A data pipeline is a series of steps to systematically
collect, transform, and store data from various sources. Data
pipelines can follow different sequences, such as extract,
transform, and load (ETL), or extract and load unstructured
data directly into a data lake without transformations.

Consistent data collection and transformation fuels informed
decision-making, proactive responses, and feedback loops. Data
pipelines play a key role in enhancing data quality by
performing operations like sorting, reformatting,
deduplication, verification, and validation, making data more
useful for analysis.

Just as DevOps principles are applied to software delivery,
the same can be done with data management through pipelines
using a methodology commonly referred to as DataOps. DataOps
incorporates DevOps principles into data management, including
the automation of testing and deployment processes for data
pipelines. This approach improves monitoring, accelerates
issue troubleshooting, and fosters collaboration between
development and data operations teams.

**Related information:**

- [What
Is A Data Pipeline?](https://aws.amazon.com/what-is/data-pipeline/)
- [AWS DataOps Development Kit](https://awslabs.github.io/aws-ddk/)
- [AWS Glue DataBrew](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/databrew.html)
- [AWS Glue ETL](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-etl.html)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Data
Matching Service – AWS Entity Resolution](https://aws.amazon.com/entity-resolution)
- [Blog:
Build a DataOps platform to break silos between engineers
and analysts](https://aws.amazon.com/blogs/big-data/build-a-dataops-platform-to-break-silos-between-engineers-and-analysts/)
- [DataOps](https://en.wikipedia.org/wiki/DataOps)
- [Using
Amazon RDS Blue/Green Deployments for database
updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html)
- [AWS Well-Architected Cost Optimization Pillar: COST11-BP01
Perform automations for operations](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_cost_effort_automations_operations.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.3-automate-data-processes-for-reliable-collection-transformation-and-storage-using-pipelines.html*

---

**Capability**: AG.DLM — Data lifecycle management

# [AG.DLM.4] Maintain data compliance with scalable classification strategies

**Category:** FOUNDATIONAL

Automated data classification includes using tools and
strategies to identify, tag, and categorize data based on
sensitivity levels, type, and more. Data classification aids
in enforcing data security, privacy, and compliance
requirements. Misclassification or lack of data classification
can lead to data breaches or non-compliance with data
protection regulations. Scaling this practice through
automation enables organizations to catalog, secure, and
maintain the vast amounts of data they process.

Use tagging strategies to catalog data effectively and help
maintain visibility of data across different services and
stages of the software development lifecycle. Put guardrails
in place to enforce compliance with data classification and
handling requirements, such as those related to data privacy
and residency. Continuously monitor data at different stages -
collection, processing, classification, and sharing - to
ensure the right handling strategies are in place and are
being followed.

For advanced use cases, AI/ML tools can provide automatic
recognition and classification of data, especially sensitive
data. This approach can reduce the need for manual, human
intervention.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS04-BP01
Implement a data classification policy](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a2.html)
- [AWS Well-Architected Cost Optimization Pillar: COST03-BP02 Add
organization information to cost and usage](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_org_information.html)
- [Data
Classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html)
- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)
- [Sensitive
Data Discovery and Protection - Amazon Macie](https://aws.amazon.com/macie/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.4-maintain-data-compliance-with-scalable-classification-strategies.html*

---

**Capability**: AG.DLM — Data lifecycle management

# [AG.DLM.5] Reduce risks and costs with systematic data retention strategies

**Category:** FOUNDATIONAL

Data is continuously generated, processed, and stored
throughout the development lifecycle, increasing the
complexity and importance of automated data management
capabilities. Automated data retention and disposal is the
process of implementing strategies and tools that
systematically store data for pre-established periods and
securely delete it afterward. The goal of data retention and
disposal is not just about compliance, but also about reducing
risks, sustainability, minimizing costs, and improving
operational efficiency. Automation reduces the manual
workload, decreases the risk of human error, and improves data
governance and compliance.

To effectively implement automated data retention and
disposal, start by defining the data lifecycle policies for
your organization. This includes understanding the regulatory
and business requirements for each type of data your
organization processes, how long it needs to be retained, and
the conditions under which it should be disposed. The policies
should also include procedures for data archiving, backups,
and restoration.

Once these policies are in place, automate the enforcement of
these policies with data lifecycle management tools. These
tools can automatically handle tasks like deletion, archival,
or movement of data based on the predefined rules. As part of
the automation process, develop mechanisms to log and audit
data disposal actions. This not only provides accountability
and traceability but also is essential for demonstrating
compliance during audits.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST04-BP05
Enforce data retention policies](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_data_retention.html)
- [AWS Well-Architected Sustainability Pillar: SUS04-BP03 Use
policies to manage the lifecycle of your datasets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a4.html)
- [AWS Well-Architected Sustainability Pillar: SUS04-BP05 Remove
unneeded or redundant data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a6.html)
- [Managing
your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.5-reduce-risks-and-costs-with-systematic-data-retention-strategies.html*

---

**Capability**: AG.DLM — Data lifecycle management

# [AG.DLM.6] Centralize shared data to enhance governance

**Category:** FOUNDATIONAL

Practicing DevOps puts an emphasis on teams working
collaboratively and continuously exchanging data. Governing
this shared data requires proper control, management, and
distribution of data to prevent unauthorized access, data
breaches, and other security incidents, fostering trust and
enhancing the quality and reliability of software delivery.

Use centralized data lakes to provide a single source of truth
of data and management within your organization, helping to
reduce data silos and inconsistencies. It enables secure and
efficient data sharing across teams, enhancing collaboration
and overall productivity. Use Role-Based Access Control (RBAC)
or Attribute-Based Access Control (ABAC) to limit access to
data based on the user context. Implement automated metadata
management to better understand the context, source, and
lineage of the data, and deploy continuous, automated data
quality checks to ensure the accuracy and usability of the
data.

When collaboration extends beyond the organization's boundaries, *clean
rooms* can be used to maintain data privacy and security. Clean rooms create
isolated data processing environments that let multiple parties collaborate and share data
in a controlled, privacy-safe manner. With predefined rules that automatically govern the
flow and accessibility of data, these clean rooms help ensure data privacy while still
allowing for the extraction of valuable insights. This isolation facilitates decision-making
and strategic planning, enabling stakeholders to collaborate and share information while
protecting user privacy and maintaining compliance with various regulations.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS04-BP06 Use
shared file systems or storage to access common data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a7.html)
- [Data
Collaboration Service - AWS Clean Rooms](https://aws.amazon.com/clean-rooms/)
- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [AWS Data Exchange](https://aws.amazon.com/data-exchange)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.6-centralize-shared-data-to-enhance-governance.html*

---

**Capability**: AG.DLM — Data lifecycle management

# [AG.DLM.7] Ensure data safety with automated backup processes

**Category:** RECOMMENDED

Data loss can be catastrophic for any organization. Automated backup mechanisms help
to ensure that your data is not only routinely backed up, but also that these backups are
maintained and readily available when needed.  As data is constantly being created and
modified, these processes minimize the risk for data loss and reduce the manual,
error-prone manual approach of backing up data.

Define a backup policy that outlines the types of data to be
backed up, the frequency of backups, and the duration for
which backups should be retained. This policy should also
cover data restoration processes and timelines. Create backup
policies that best fit the classification of the data to avoid
backing up unnecessary data.

Choose backup tools that support automation and can be
integrated into your DevOps pipelines and environments. These
tools should have capabilities to schedule backups, maintain
and prune older backups, and ensure the integrity of the
backed-up data. For instance, during the development
lifecycle, trigger backups before altering environments with
business-critical data and in the case of rollbacks ensure
that the data was not impacted.

Regularly test the data restoration process to ensure that the
backed-up data can be effectively restored when required.
Regular audits and reviews of the backup policy and the
effectiveness of the backup process can help identify any gaps
or potential improvements. Alerts and reports should be
configured to provide visibility into the backup process and
notify teams about any issues.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS04-BP08 Back up
data only when difficult to recreate](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a9.html)
- [AWS Well-Architected Reliability Pillar: REL09-BP03 Perform
data backup automatically](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_automated_backups_data.html)
- [Centrally
manage and automate data protection - AWS Backup](https://aws.amazon.com/backup/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.7-ensure-data-safety-with-automated-backup-processes.html*

---

**Capability**: AG.DLM — Data lifecycle management

# [AG.DLM.8] Improve traceability with data provenance tracking

**Category:** RECOMMENDED

Data provenance tracking records the history of data throughout its lifecycle—its
origins, how and when it was processed, and who was responsible for those processes. This
practice forms a vital part of ensuring data integrity, reliability, and traceability,
providing a clear record of the data's journey from its source to its final form.

The process involves capturing, logging, and storing metadata
that provides valuable insights into the lineage of the data.
Key aspects of metadata include the data's source, any
transformations it underwent (such as aggregation, filtering,
or enrichment), the flow of data across systems and services
(movements), and actors (the systems or individuals
interacting with the data).

Use automated tools and processes to manage data provenance by
automatically capturing and logging metadata, and make it
easily accessible and queryable for review and auditing
purposes. For instance, data cataloging tools can manage data
assets and their provenance information effectively, providing
a systematic way to handle large volumes of data and their
metadata across different stages of the development lifecycle.

In more complex use cases, machine learning (ML) algorithms can be used to uncover
hidden patterns and dependencies among data entities and operations. This technique can
reveal insights that might not be easily detectable with traditional methods.

Regularly review and update the data provenance tracking
process to keep it aligned with evolving data practices,
business requirements, and to maintain regulatory compliance.
Provide training and resources to teams, helping them
understand the importance and practical use of data provenance
information.

Data provenance tracking is particularly recommended for
datasets dealing with sensitive, regulated data or complex
data processing workflows. It also adds significant value in
environments where reproducibility and traceability of data
operations are required, such as in data-driven
decision-making, machine learning model development, and
debugging data issues.

Data provenance tracking is particularly recommended for
datasets dealing with sensitive or regulated data, machine
learning workflows, and complex data processing which may
require debugging.

**Related information:**

- [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html)
- [Well-Architected
Data Analytics Lens: Best practice 7.3 – Trace data
lineage](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-7.3---trace-data-lineage..html)
- [Amazon SageMaker AI ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html)
- [Blog: Build
data lineage for data lakes using AWS Glue, Amazon Neptune, and Spline](https://aws.amazon.com/blogs/big-data/build-data-lineage-for-data-lakes-using-aws-glue-amazon-neptune-and-spline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.8-improve-traceability-with-data-provenance-tracking.html*

---

**Capability**: AG.SAD — Secure access and delegation

# [AG.SAD.1] Centralize and federate access with temporary credential vending

**Category:** FOUNDATIONAL

Implement a centralized subsystem for federated access and temporary credential
vending to maintain secure and controlled access to your environments, workloads, and
resources. By implementing a federated access solution, you can leverage your existing
identity systems, provide single sign-on (SSO) capabilities, and avoid the need to maintain
separate user identities across multiple systems which makes scaling in a DevOps model more
tenable. Centralizing identity onboarding and permission management eliminate the
inefficiencies of manual processes, reduce human error, and enable scalability as your
organization grows.

Grant users and services fine-grained access to help ensure secure, granular control
as they interact with resources and systems. By applying the least privilege principle, you
can minimize the risk of unauthorized access and reduce the potential damage from
compromised keys while retaining full control over access to resources and environments. To
reduce the likelihood of keys being compromised, always vend short-lived, temporary
credentials that are scoped for specific tasks to help ensure that privileges are granted
only for the duration needed.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST02-BP04
Implement groups and roles](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_groups_roles.html)
- [Security
best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Well-Architected Security Pillar: SEC02-BP04 Rely on a
centralized identity provider](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_identity_provider.html)
- [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [What
is SSO (Single-Sign-On)?](https://aws.amazon.com/what-is/sso/)
- [Identity
providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.1-centralize-and-federate-access-with-temporary-credential-vending.html*

---

**Capability**: AG.SAD — Secure access and delegation

# [AG.SAD.2] Delegate identity and access management responsibilities

**Category:** FOUNDATIONAL

Create a decentralized Identity and Access Management (IAM) responsibility model
that enables individual teams to handle their own IAM tasks, such as creating roles and
assigning permissions, as long as those teams operate within applied guardrails. This
approach grants teams the autonomy to manage their roles and permissions essential for the
applications they develop, encourages a culture of ownership and accountability, and enables
your organization to scale its permission management effectively as it grows and embraces
more DevOps practices.

Establish a set of well-defined guardrails which limit the
maximum permissions a user or role can safely have. These
guardrails reduce potential security risk while creating
balance between allowing teams to manage their own IAM tasks
and ensuring that they do not exceed the maximum permissions
set.

**Related information:**

- [Security
best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Use
permissions boundaries to delegate permissions management
within an account](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-permissions-boundaries)
- [Establish
permissions guardrails across multiple accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-permissions-guardrails)
- [Blog: Delegate
permission management to developers by using IAM
permissions boundaries](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.2-delegate-identity-and-access-management-responsibilities.html*

---

**Capability**: AG.SAD — Secure access and delegation

# [AG.SAD.3] Treat pipelines as production resources

**Category:** FOUNDATIONAL

Pipelines become pivotal in every aspect of the software
development lifecycle when practicing DevOps, as they become
the sole method of moving code from development to production.
During the process of building, testing, and deploying
software, pipelines require access to all software components
involved, including libraries, frameworks, repositories,
modules, artifacts, and third-party dependencies. Due to this
level of access and their role in deploying to potentially
sensitive environments, pipelines should be recognized as
integral components of your overall system and must be secured
and managed to the same degree as the environments and data
they interact with.

The [application of least-privilege principles](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), commonly applied
to human users, should be extended to pipelines. To reduce the potential for pipelines to
become a security threat, their roles and permissions should be confined to align with their
precise responsibilities. Emphasizing pipeline governance and treating pipelines as
first-class citizens within your security infrastructure can substantially decrease your
potential attack surface and reinforce the security of your overall DevOps environment.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC11-BP07 Regularly
assess security properties of the pipelines](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_regularly_assess_security_properties_of_pipelines.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.3-treat-pipelines-as-production-resources.html*

---

**Capability**: AG.SAD — Secure access and delegation

# [AG.SAD.4] Limit human access with just-in-time access

**Category:** FOUNDATIONAL

As pipelines take on a more prominent role in the software
development lifecycle in a DevOps model, the necessity for
extensive human access to environments decreases. Human users
should be granted minimal access necessary for their role,
which is usually read-only access that does not allow any
modifications or access to sensitive data. For experimentation
which is typically hands-on and exploratory, teams should be
granted access to sandbox environments which are isolated from
system workloads.

In some cases, where things go wrong or a process cannot yet be automated, elevated
permissions might be required. To accommodate these needs without compromising security,
implement a just-in-time (JIT) access control strategy where permissions are temporarily
escalated for a specific duration and purpose, upon explicit request and approval. This
approach maintains the principle of least privilege, allowing necessary operational
functions to be performed efficiently when needed, while also ensuring that the access is
revoked once the task is complete.

By enforcing limited human permissions and using JIT access, you can improve your
organization's security posture and reduce the risk of accidental or deliberate misuse of
access rights. This restrictive and controlled model supports modern, secure DevOps
practices where pipelines, treating everything as code, and automation should take
precedence over manual actions.

**Related information:**

- [Eliminate
the need for human access](https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/use-immutable-infrastructure-with-no-human-access.html)
- [AWS Samples: AWS IAM Temporary Elevated Access Broker](https://github.com/aws-samples/aws-iam-temporary-elevated-access-broker)
- [Blog: Managing
temporary elevated access to your AWS environment](https://aws.amazon.com/blogs/security/managing-temporary-elevated-access-to-your-aws-environment/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.4-limit-human-access-with-just-in-time-access.html*

---

**Capability**: AG.SAD — Secure access and delegation

# [AG.SAD.5] Implement break-glass procedures

**Category:** FOUNDATIONAL

Emergencies or unforeseen circumstances might necessitate temporary access beyond
regular permissions for day-to-day work. Having break-glass procedures helps ensure that
your organization can respond effectively to crises without compromising long-term
security. During emergency scenarios, like the failure of the organization's identity
provider, security incidents, or unavailability of key personnel, these measures provide
temporary, elevated access beyond regular permissions.

Implement measures that improve the resilience of your DevOps environments through
the ability to respond effectively to emergencies without compromising long-term security.
Create break-glass roles and users you can assume control of during emergencies that are
able to bypass established controls, update guardrails, troubleshoot issues with automation
tooling, or remediate security and operational issues that may occur. These break-glass
roles and users should have adequate security measures, such as configuring them with
hardware-based multi-factor authentication (MFA), to ensure that even in emergencies, access
is tightly controlled and auditable. Establish alerts and alarms triggered by the use of
these break-glass roles and users, and tie their usage closely to incident response and
recovery procedures.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC03-BP03 Establish
emergency access process](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_emergency_process.html)
- [Break
glass access](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/break-glass-access.html)
- [Amazon's
approach to high-availability deployment: Dealing with the
real world](https://youtu.be/bCgD2bX1LI4?t=1300)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.5-implement-break-glass-procedures.html*

---

**Capability**: AG.SAD — Secure access and delegation

# [AG.SAD.6] Conduct periodic identity and access management reviews

**Category:** FOUNDATIONAL

With the distributed nature of DevOps Identity and Access Management (IAM)
responsibilities, it is important to systematically review IAM roles and permissions
periodically. This helps ensure that changes in roles and permissions align with the rapidly
shifting needs of the organization, and that the guardrails set in place for delegation are
working as intended or perhaps need to be fine-tuned. This activity aids in identifying
unused or overly broad permissions, reinforcing the adherence to the principle of least
privilege and reducing potential security risks.

Optionally, automate the right-sizing of permissions as part
of these reviews. This proactive approach not only keeps IAM
policies up-to-date, but also minimizes potential avenues for
unauthorized access, further strengthening your overall
security posture. Automatically right sizing roles and
permissions based on actual activity allows organizations to
scalably enforce that the right resources are accessible to
the right entities, at the right times.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC03-BP04 Reduce
permissions continuously](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_continuous_reduction.html)
- [Regularly
review and remove unused users, roles, permissions,
policies, and credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#remove-credentials)
- [Use
IAM Access Analyzer to generate least-privilege policies
based on access activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-gen-least-privilege-policies)
- [Verify
public and cross-account access to resources with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-preview-access)
- [Using
AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [Blog: IAM Access Analyzer makes it easier to implement least
privilege permissions by generating IAM policies based on access activity](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/)
- [Blog: Continuous
permissions rightsizing to ensure least privileges in AWS
using CloudKnox and AWS Config](https://aws.amazon.com/blogs/mt/continuous-permissions-rightsizing-ensure-least-privileges-aws-using-cloudknox-aws-config/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.6-conduct-periodic-identity-and-access-management-reviews.html*

---

**Capability**: AG.SAD — Secure access and delegation

# [AG.SAD.7] Implement rotation policies for secrets, keys, and certificates

**Category:** RECOMMENDED

Regular rotation of secrets, keys, and certificates is a best
practice in securing access, limiting the potential damage
that can occur should these security resources become
compromised. In a DevOps environment, pipelines often require
access to sensitive environments and workloads, making them
potential targets for attacks. The routine rotation of these
resources that are used by pipelines can help to significantly
mitigate this risk.

Establish a policy that clearly defines the lifecycle of these
resources, including their creation, usage, rotation, and
retirement intervals. Enforce these policies by automatically
rotating secrets and keys to reduce the risk of oversights,
delays, and human error.

Certificates play an important role in service-to-service
authentication and providing encryption for both internal and
external facing workloads and environments. When managing
certificates, consider not only those issued within your
organization but also those imported from external sources
which may not be automatically renewable.

Monitoring systems that track the lifespan of these assets and
alert administrators as they near expiration can contribute to
this process. This approach can help prevent service
disruptions caused by expired certificates and, in some cases,
can trigger automated renewal procedures.

**Related information:**

- [Blog: How
to monitor expirations of imported certificates in AWS Certificate Manager (ACM)](https://aws.amazon.com/blogs/security/how-to-monitor-expirations-of-imported-certificates-in-aws-certificate-manager-acm/)
- [Rotate
AWS Secrets Manager secrets - AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)
- [Managing
access keys for IAM users - AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
- [Rotating
AWS KMS keys - AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.7-implement-rotation-policies-for-secrets-keys-and-certificates.html*

---

**Capability**: AG.SAD — Secure access and delegation

# [AG.SAD.8] Adopt a zero trust security model, shifting towards an identity-centric security perimeter

**Category:** RECOMMENDED

When operating under a zero trust security model, no user or
system is trusted by default. It requires all users and
systems, even those inside an organization's network, to be
authenticated, authorized, and continuously validated to
ensure secure configurations and posture. Only after
validation will they be granted access to applications and
data.

Zero trust is beneficial throughout the entire software
development lifecycle. From the initial stages of code
development as developers interact with source code
repositories, through continuous integration using internal
and external tools to build and test software, to the
deployment and maintenance of the workloads, each user,
pipeline, third-party, and service needs to be authenticated
and authorized with every request. In these scenarios, zero
trust enforces adherence to the principle of least privilege,
ensuring that all of these independent users and systems are
granted access to the right resources only when necessary.

Shifting to a zero trust model is not an all-or-nothing
endeavor, it is a gradual process consistent with the DevOps
principles of continuous improvement. Start small by
pinpointing use cases that align with your organization's
unique needs and the value and sensitivity of your systems and
data. This understanding will guide the selection of zero
trust principles, tools, and patterns that are most beneficial
for your organization. Adopting zero trust often involves
rethinking identity, authentication, and other
context-specific factors like user behavior and device health.
Enhance existing security practices over time, improving both
identity-based and network-based security measures that
complement each other to create a secure perimeter where
identity-centric controls can operate.

AWS provides several use cases that illustrate zero trust
principles:

- **Signing API requests:** Every AWS API request is
authenticated and authorized individually, regardless of the trustworthiness of the
underlying network.
- **Service-to-service interactions:** AWS services
authenticate and authorize calls to each other using the same security mechanisms used
by customers.
- **Zero trust for internet of things (IoT):** AWS IoT
extends the zero trust model to IoT devices, enabling secure communication over open
networks.

**Related information:**

- [Zero
Trust on AWS](https://aws.amazon.com/security/zero-trust/)
- [Zero
Trust Maturity Model](https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf)
- [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/)
- [AWS Verified Access](https://aws.amazon.com/verified-access)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.8-adopt-a-zero-trust-security-model-shifting-towards-an-identity-centric-security-perimeter.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
