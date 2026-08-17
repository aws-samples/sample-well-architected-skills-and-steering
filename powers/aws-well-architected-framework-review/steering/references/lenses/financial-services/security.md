# Security

**Pillar**: Security  
**Questions**: 16

---

# FSISEC01: How does your governance enable secure cloud adoption at scale?

Cloud infrastructure provides more agility and responsiveness
than traditional IT environments. This requires organizations
to think differently about how they design, build, and manage
applications. Cloud resources can be disposable. Because it is
a pay-per-use model, it often requires a strong integration
between IT governance and organizational governance. Financial
services companies need to operate in a cloud environment
that's agile and safe at the same time. With the adoption of
generative AI capabilities, organizations need to implement
comprehensive security controls across AI components while
maintaining agility and innovation.

## FSISEC01-BP01 Consider and leverage a Cloud Center of Excellence (CCoE)

When it comes to cloud adoption and governance, CCoEs (also
referred as Cloud Enablement Engine (CEE)) are known drivers
of change across the enterprise and the focal point for its
transformation. CCoEs should have a functional model that is
more aligned to provisioning and operating cloud resources,
or they should act as the advisory group for cloud
migrations and security baseline definitions. CCoEs help
create and manage governance and security policies in
collaboration with a cross-functional team and select
governance tools to provide financial and risk management.

When implementing generative AI workloads, CCoEs should
establish comprehensive governance frameworks that
encompass:

- AI model lifecycle management and approval processes
- Data governance for training datasets and model inputs
- Model performance monitoring and drift detection
- Compliance tracking for AI regulatory requirements
- Risk assessment frameworks for AI model deployment
- Guardrails to control system behaviors
- Standardized resource management for prompts and models

The following tenets are key guiding principles for
[creating
a CCoE](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/):

- The CCoE structure evolves as the organization changes.
- Treat the cloud as your product and application team
leaders as the customers you are serving.
- Build company culture into everything you do.
- Organizational change management is central to business
transformation. Use intentional and targeted
organizational change management to change company culture
and norms.
- Embrace a change-as-normal mindset. Security policies and
procedures must be flexible enough to keep up with the
changes in applications, IT systems, and business
direction over the time and should be aligned with the
financial services industry regulations and best practices.
- Operating model decisions determine how people fill roles
that achieve business outcomes.

Traditionally, companies in the financial sector have
distributed internal teams with distinct roles, as part of
their division of duties policies. Even so, you can still
get the benefits described here if the duties of a CCoE are
distributed among multidisciplinary teams.

## FSISEC01-BP02 Use cloud-native services for management and governance

Financial sector organizations focus on achieving security and
compliance objectives in balance with faster innovation and
agility.
[AWS Management and Governance native services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/management-governance.html)
takes advantage of both innovation and control as you can
provision resources and applications to help meet your
policies and operate your environment for business agility and
governance control. These services are designed to make it
easier to manage your AWS environment at scale, facilitating
the secure adoption of cloud services without losing control
of the environment growth.

The following articles and blogs provide advice for improving
the overall security of your workloads and to hone the
security posture of your internal IT resources.

The section
[Building
a CCOE to transform the entire enterprise](https://docs.aws.amazon.com/whitepapers/latest/public-sector-cloud-transformation/building-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise.html),
from AWS documentation describes the benefits of creating a
Cloud Center of Excellence (CCOE) within your organization.
This allows you to adopt a number of policies that helps you
evolve your security measures across several dimensions over
time and scope.

The whitepaper
[Cloud
Enablement Engine: A Practical Guide](https://d1.awsstatic.com/whitepapers/cloud-enablement-engine-practical-guide.pdf)
describes the step-by-step process for the initial setup
activities for a CCOE, and the top ten best practices gleaned
by AWS while working across a large number of customers.

By using a Service Catalog, your organization can create
and manage catalogs of IT services that are approved for AWS.
These IT services can include everything from virtual machine
images, servers, software, databases, to complete multi-tier application
architectures. For more information, see
[Manage pre-approved services for secure adoption at scale with Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).

[AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) can offer a straightforward way
to set up and govern an AWS multi-account environment,
following prescriptive best practices. AWS Control Tower
orchestrates the capabilities of several other
[AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html), including AWS Organizations, Service Catalog, and AWS IAM Identity Center. It allows you to
build a landing zone in less than an hour.

## Resources

**Related documents:**

- [Using a Cloud Center of Excellence (CCOE) to Transform the Entire Enterprise](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/)
- [7
Pitfalls to Avoid When Building a CCOE](https://aws.amazon.com/blogs/enterprise-strategy/7-pitfalls-to-avoid-when-building-a-ccoe/)
- [AWS Control Tower and AWS Security Hub CSPM – Powerful Enterprise Twins](https://aws.amazon.com/blogs/enterprise-strategy/aws-control-tower-and-aws-security-hub-powerful-enterprise-twins/)

**Related videos:**

- [Transform your organization's culture with a Cloud Center of Excellence](https://www.youtube.com/watch?v=VN1vj0d3Z1Y&ab_channel=AWSEvents)
- [How to Build Your Cloud Enablement Engine with the People You Already Have](https://pages.awscloud.com/How-to-Build-Your-Cloud-Enablement-Engine-with-the-People-You-Already-Have_2019_0617-ENT_OD.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec01.html*

---

# FSISEC02: How do you achieve, maintain, and monitor ongoing compliance with regulatory guidelines and mandates?

Companies in the financial sector have more demanding compliance
monitoring and implementation requirements than most other
sectors of the economy. Traditional methods of compliance
assessment do not keep pace with the dynamics of the agile cloud
environment. For this reason, the best practices and tools
required are specific to this type of environment. Regulations
ensure that consumers' personal and financial data are
protected. Compliance with these regulations helps prevent
identity theft, fraud, and unauthorized disclosure of personal
information. Compliance also helps maintain the integrity and
stability of the financial markets by ensuring that institutions
engage in responsible lending and investment practices and avoid
excessive risk-taking. The following best practices help
facilitate compliance in the cloud.

## FSISEC02-BP01 Automate your compliance management

AWS has services to help you identify, optimize and remediate
resource configurations for continuous compliance and
operational efficiency. AWS services help customers achieve
immutable resource configuration and offer configurable
logging for the auditing of user and API activity. Using
[AWS Config](https://aws.amazon.com/config/) and its

[proactive mode](https://aws.amazon.com/blogs/aws/new-aws-config-rules-now-support-proactive-compliance/)
helps you save time and remove the risk of human error when
you automate and scale compliance management. It helps FIs
(mainly the first line of defense) effectively manage risk for
their cloud resources.

## FSISEC02-BP02 Use ready-to-deploy templates for standards and best practices

Ready-to-deploy templates are a quick and assertive way to
measure what level of security is present in cloud
environments. These templates are available both for best
practices in technology such as database, serverless, and
networking, and are aligned to frameworks that are widely

accepted and recognized. Among the most suitable templates
are
[managed
rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html), AWS Config
[Conformance
Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) in AWS Config, and
[AWS Security Hub CSPM standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-available.html). FIs can benefit
from Conformance Packs that are available and ready to be
used for alignment to the financial services industry's
standards and regulatory requirements, such as PCI-DSS,
NYDFS, and FFIEC.

### Prescriptive guidance

- Use Amazon Bedrock Guardrails for automated response
validation and content filtering.
- Use pre-configured security controls for AI service
endpoints and model access.
- Use compliance templates for AI model governance
including model cards and documentation.
- Deploy standard configurations for secure prompt
management and version control.
- Use automated monitoring for AI system outputs and
potential security issues.

- A Conformance Pack can be deployed as is or it can be
edited to include your specific resources and use cases.
For more information, see
[Deploying
a Conformance Pack Using the AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-console.html)
[Console](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-console.html).
- When adding a new rule, choose how it evaluates your
resources, as well as how it is initiated. For more
information, see
[Evaluation
Mode and Trigger Types for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html).
- To determine if requirements in a standard are being
met, enable the controls from AWS Security Hub CSPM
standards. For more information, see
[Security
standards and controls in AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html).
- Leverage Amazon Bedrock's Prompt Management catalog for
secure prompt storage and version control.

## Resources

**Related documents:**

- [AWS Config Rules Now Support Proactive Compliance](https://aws.amazon.com/blogs/aws/new-aws-config-rules-now-support-proactive-compliance/)

**Related videos:**

- [Cloud compliance, assurance, and auditing](https://www.youtube.com/watch?v=xREhfrUqpd4&ab_channel=AWSEvents)
- [Setting up controls at scale in your AWS environment](https://www.youtube.com/watch?v=NkE9_okfPG8&t=1697s&ab_channel=AWSEvents)
- [Proactive governance and compliance for AWS
workloads](https://www.youtube.com/watch?v=PpUnH9Y52X0&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec02.html*

---

# FSISEC03: How do you monitor the use of elevated credentials, such as administrative accounts, and guard against privilege escalation?

IAM policies are powerful and complex, so it's important to
study and understand the permissions that are granted by each
policy. Mitigate privilege escalation and monitor unauthorized
activity in your AWS accounts. With the introduction of
generative AI systems, monitoring elevated credentials extends
to model access, prompt engineering, and AI service
management.

## FSISEC03-BP01 Review IAM policies and permissions

[IAM
policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) are powerful and complex, so it's
important to study and understand the permissions that are
granted by each policy.

As part of the tight controls FIs implement around identity
management and broader identity management policies, it is
important to perform periodic reviews of your IAM roles
using
[last accessed
information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html)
to get a report about the last time that an IAM entity (user
or role) attempted to access a service, and
[delete
roles that are not in use](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html). Before you
delete a role, review its recent service-level activity by
viewing service last accessed data report. Use that
information to refine your policies to allow access to only
the services that are in use. Repeat this process to
generate a report for each type of resource in IAM.

For generative AI services, implement comprehensive IAM
policies that grant least privilege access to foundation
model endpoints while establishing private network
communication, monitoring elevated credential usage in AI
workflows, and implementing permissions boundaries for AI
service roles including attribute-based access controls for
dynamic AI resource management.

## FSISEC03-BP02 Mitigate privilege escalation

Privilege escalation refers to the ability of unauthorized
users gaining access to elevated permissions, often by way of
improperly written code or misconfigurations. Privilege
escalation can result from misusing a number of
non-administrator or non-full access permissions. To help
avoid scenarios like this, pay attention to permissions that
would allow the creation, change and deletion of users, roles,
and policies.

As a way to help prevent privilege escalation, you should use
service control policies (SCPs) to
[block
users in](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-restricts-with-exception)

[your accounts, except for IAM administrators](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-restricts-with-exception) or
delegated admins, from performing administrative IAM actions.
Delegation is a common practice for FIs. If you want to safely
delegate permissions management to trusted employees, use
[IAM permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html). IAM permissions
boundaries allow for safe delegation of IAM permissions
management while minimizing escalation of privileges. For
example, developers can safely create IAM roles for Lambda
functions and Amazon EC2 instances without exceeding certain
permissions boundaries defined by your IAM administrators.

## FSISEC03-BP03 Monitor unauthorized activity in your AWS accounts

Use the following guidelines to monitor your AWS account
activity:

- Turn on AWS CloudTrail in each account, and use it in each
supported Region.
- Store AWS CloudTrail log in a centralized logging account
with very restricted access.
- Periodically examine CloudTrail log files. Use Amazon GuardDuty, which provides threat detection by continually
analyzing AWS CloudTrail events, VPC Flow Logs and DNS
logs.
- Enable Amazon GuardDuty in each account, and use it in
each supported Region to automatically detect CloudTrail
management events that can lead to
[IAM privilege escalation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#privilegeescalation-iam-anomalousbehavior) and other IAM

[finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html).
- Enable Amazon S3 bucket logging to monitor requests made
to each bucket.
- If you believe there has been unauthorized use of your
account, pay attention to temporary credentials that have
been issued. If temporary credentials have been issued
that you don't recognize,
[disable their permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html).
- [View the last accessed information for IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html)
through the Management Console, CLI or AWS API.

Administrators can configure roles to require identities to
pass a custom string that identifies the person or application
that is performing actions in AWS when the role is assumed.
This identity information is stored as the
[source
identity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html#STS-API-source-identity) in AWS CloudTrail. Administrators
can review this activity in CloudTrail, and they can view the
source identity information to determine who or what performed
actions with assumed role sessions.

It is also a good practice to periodically
[review
IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-audit-guide.html#aws-security-audit-review-policy-tips) as well as setting restrictive
user access on a need to know basis. You can
[prevent IAM user and roles from making specified changes](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-restricts-with-exception), through Service Control Policies
(SCPs) and set

[Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html).

## Resources

**Related documents:**

- [How
to use trust policies with IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/)
- [Monitor and Notify on AWS Account Root User
Activity](https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/)

**Related videos:**

- [AWS re:Inforce 2022 - Security best practices with AWS IAM](https://www.youtube.com/watch?v=SMjvtxXOXdU)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec03.html*

---

# FSISEC04: How do you accommodate separation of duties as part of your identity and access management design?

## FSISEC04-BP01 Implement the principle of separation of duties

Separation of duties, as it relates to security, has two
primary objectives. The first objective is the prevention of
conflict of interest, abuse, and errors. The second objective
is the detection of control failures that include security
breaches, information theft, and circumvention of security
controls.

While robust automation of infrastructure and application
deployments helps reduce the need for human access, there
can be instances where individuals need to complete key
functions. For users with increased privileges, it is
important to distribute system administration activities, so
no one administrator can hide their activities or control an
entire system. Separation of duties can help mitigate risk
on critical tasks by ensuring different people are required
to perform a task where the requestor and the approver can't
be the same person. A common example is the use of an
approver during the
[running
of an automation on AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-require-approvals.html).
This principle can be used to implement numerous tasks
including controlling access to your cloud resources.

For generative AI workloads, implement clear separation of
duties by creating distinct roles for prompt engineering,
security administration, and model governance, while
maintaining separate permissions for model access,
management and deployment as well as establishing dedicated
approval workflows for AI system changes, and enforcing
strict boundaries between development and production AI
environments.

## FSISEC04-BP02 Use AWS Config to view historical IAM configuration and changes over time

Use
[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource.html) to view the IAM policy that was
assigned to an IAM user, group, or role at any time in which
AWS Config was recording. This information can help you
determine the permissions that belonged to a user at a specific time. For example, it allows
you to view whether a user had permission to modify settings
on a specific date in the past.

## FSISEC04-BP03 Set up alerts for IAM configuration changes and perform audits

[Set
up alerts](https://aws.amazon.com/blogs/security/how-to-receive-alerts-when-your-iam-configuration-changes/)

to notify on IAM configuration
changes including when an
[IAM user is created](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html) or when conflicting
permissions are added to a user or role, such as being able to
approve its own requests on a given workflow. This is helpful
for monitoring activities by users with increased privileges.
The added notification can be set up using a combination of
[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html),

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html),

and
[Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

### Prescriptive guidance

- To manage changes for an entire organization or for a
single AWS account, you can use Change Manager, a
capability of AWS Systems Manager. For more details see,
[Setting up Change Manager at](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-setting-up.html)

[AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-setting-up.html).
- AWS Config is a service that helps you manage compliance
state changes for resources. For more details, see
[Viewing AWS Resource Configurations and History](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource.html).
- An approval process for changes can be deployed using
AWS Step Functions. To review the step-by- step
tutorial, see
[Deploying an Example Human Approval Project](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html).

## Resources

**Related documents:**

- [Apply the principle of separation of duties to shell access to your EC2 instances](https://aws.amazon.com/blogs/security/apply-the-principle-of-separation-of-duties-to-shell-access-to-your-ec2-instances/)
- [How to Record and Govern Your IAM Resource Configurations Using AWS Config](https://aws.amazon.com/blogs/security/how-to-record-and-govern-your-iam-resource-configurations-using-aws-config/)

**Related videos:**

- [Least Privilege & Separation of Duties for AWS ACM Private CA](https://www.youtube.com/watch?v=ifImMYHQbp0&ab_channel=AmazonWebServices)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec04.html*

---

# FSISEC05: How are you monitoring your ongoing cloud environment for potential threats?

Financial services organizations require in-depth visibility
into the security of their infrastructure and applications.
Achieving this high level of visibility requires the
collection of logs and audit trails and the reservation of
these logs for analytics and reporting. AWS services and
partners' cloud-based solutions help you implement real-time
monitoring in your environment for security threats and
alerting on threats once detected. With generative AI systems,
monitoring extends to model behaviors, response validation,
and potential misuse of AI capabilities.

## FSISEC05-BP01 Track configuration changes

As part of monitoring the environment against threats, it is
critical to identify changes in the security settings that
keep the environment protected. One of the benefits of the
cloud is being able to maintain full visibility of what is
changing in the environment. Establishing a security
baseline of the deployed resources is key for a FIs first
line of defense to manage the risk of its infrastructure, as
well as to track changes over time.

Use
[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) to audit and evaluate the
configuration settings of your AWS resources. AWS Config
continually tracks the configuration changes that occur in
your resources, and by using
[AWS Config Managed
Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html), it checks to see if these changes
comply with the your defined desired state. This allows you
to identify and correct configuration deviations as soon as
they happen, and also helps the second and third lines of
defense respond quickly.

For generative AI systems, establish comprehensive
monitoring of model endpoint configurations, prompt catalog
changes, and AI service policy modifications while
implementing guardrails for response validation and tracking
data access patterns across AI workflows.

## FSISEC05-BP02 Detect unusual and unauthorized activity early

Cloud processing of large event data helps detect unauthorized
activity early, which is crucial in a financial institution's
incident response strategy.

Threat detection services like
[Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) can continually monitor for
unauthorized behavior to protect your AWS accounts and
workloads by focusing on indication of compromise of
credentials, resources, accounts or buckets.
[Enable Amazon GuardDuty on all of the](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html)

[accounts](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html)
in your AWS Organization and for all of the AWS Regions, as it
can detect unintended activities in unused Regions as well.

AWS Security Hub CSPM provides you with a comprehensive view of the
security state in AWS and helps you check your environment
against
[security
industry standards and best practices](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html). The
activities surrounding Amazon GuardDuty and AWS Security Hub CSPM
must also be tracked and analyzed using AWS CloudTrail, and
they can feed a normalized central data-lake of your
security-related information on
[Amazon Security Lake](https://aws.amazon.com/security-lake/).

Detecting malware in your environment is essential. Consider
enabling
[malware protection](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html) in Amazon GuardDuty to identify
your resources that are at risk or have already been
compromised by malware. Whenever Amazon GuardDuty detects
suspicious behavior on an EC2 instance or a container
workload, malware protection automatically initiates an
agentless scan on the EBS volume attached to the resource to
detect the presence of malware.

Additionally, you should also consider scanning data coming in
through third party sources and often landing in your S3
buckets, as they may expose you to potentially malicious files,
objects that may be infected with malware, ransomware, or
viruses. To do this, leverage AWS Partner solutions found in
the
[AWS Marketplace](https://aws.amazon.com/marketplace/solutions/security).

[AWS CloudTrail insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-insights-events.html) helps AWS users identify
and respond to unusual activity associated with API calls by
continually analyzing CloudTrail management events, and should
[be enabled in your trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html).

You can
[track configuration changes at the edge with AWS Config](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/TrackingChanges.html), by recording and tracking CloudFront distribution settings changes.

## Resources

**Related documents:**

- [Cloud security software - AWS Marketplace](https://aws.amazon.com/marketplace/solutions/security)
- [GuardDuty Malware Protection FAQ](https://aws.amazon.com/guardduty/faqs/#GuardDuty_Malware_Protection)

**Related videos:**

- [The top 7 ways to operationalize AWS Security Hub CSPM](https://www.youtube.com/watch?v=ZEgCsKHPpFI&ab_channel=AWSOnlineTechTalks)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec05.html*

---

# FSISEC06: How do you address emerging threats?

Security-focused enterprises are improving threat
identification and remediation with DevSecOps. This approach
accelerates application development and identifies threats
early, and security testing is performed at each step of the
software development lifecycle. Applying a DevSecOps framework
is critical for an FI's software development, meeting the
needs of a rapidly-changing product and a highly regulated
environment.

Emerging threats now include AI-specific concerns such as
prompt injection, model manipulation, harmful model responses,
and excessive agency risks from autonomous AI systems.
Integrate AI-specific vulnerability scanning into CI/CD
pipelines.

## FSISEC06-BP01 Automate remediation of common vulnerabilities and exposures (CVEs)

Scanning servers for common vulnerabilities is a
long-standing best practice. However, in the cloud, you
should not only automate the evaluation of operating
environments and applications, but also remediate known and
emerging security vulnerabilities automatically. For
example, you can use
[Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) service to automatically scan
servers in production, publish security findings to an Amazon Simple Notification Service (SNS) topic, run an AWS Lambda
function from those notifications to examine the findings, and
implement the appropriate remediation based on the type of
issue.

For generative AI systems, implement automated response
validation through multiple complementary patterns with
custom code validation using AWS Lambda with input and
output validation logic and AWS Step Functions for
orchestrated validation workflows. Consider LLM-as-a-judge
where a specialized model (like Amazon Nova Premier)
evaluates primary responses for safety and accuracy. Use
Amazon Bedrock Guardrails with built-in content filters,
prompt injection detection, and contextual grounding checks
that can be applied at both input and output stages.

## FSISEC06-BP02 Perform static analysis on all code deploys

As part of a DevSecOps strategy, you can secure your
application deployments by integrating preventive and
detective security controls within the pipeline. One of the
key benefits of static code analysis is that you can learn
about security vulnerabilities prior to provisioning AWS
resources, which can help reduce costs and risk.

## FSISEC06-BP03 Conduct regular penetration testing

Simulating security incidents inside the AWS environment helps
you have a better understanding of your security posture.
Financial services organizations perform penetration testing
of web applications most often when a new application is
launched or when it's first migrated to the cloud. Some may
even conduct penetration testing periodically every year. Run
penetration testing regularly after every major release that
involves significant re-architecture changes. Major releases
might introduce vulnerabilities that didn't exist earlier.

## FSISEC06-BP04 Deploy web application firewalls

[AWS WAF](https://aws.amazon.com/waf/) is an application firewall service for
HTTP applications that applies a set of rules to an HTTP
conversation. You can buy managed rule sets from the AWS Marketplace that protect against application vulnerabilities,
such as the Open Worldwide Application Security Project
([OWASP
Top 10](https://aws.amazon.com/marketplace/pp/prodview-p77unujkxrg7g)), bots, or emerging CVEs. Managed rules are
automatically updated by AWS Marketplace security sellers.

### Prescriptive guidance

- Automation is key to maintain continuous vulnerability
management and a remediation posture. For details, see
[Automate vulnerability management and remediation in
AWS](https://aws.amazon.com/blogs/mt/automate-vulnerability-management-and-remediation-in-aws-using-amazon-inspector-and-aws-systems-manager-part-1/).
- Application modernization leads to containerized
applications. You can deploy vulnerability management
into your CI/CD pipeline and scan container images. For
more details, see
[Use Amazon Inspector to manage your build and deploy pipelines for containerized applications](https://aws.amazon.com/blogs/security/use-amazon-inspector-to-manage-your-build-and-deploy-pipelines-for-containerized-applications/).
- From a shift left approach, apply vulnerability
management in your CI/CD pipeline. For more details, see
[Detect security vulnerabilities and automate code reviews](https://aws.amazon.com/blogs/devops/automating-detection-of-security-vulnerabilities-and-bugs-in-ci-cd-pipelines-using-amazon-codeguru-reviewer-cli/).

## Resources

**Related documents:**

- [Penetration
Testing at AWS](https://aws.amazon.com/security/penetration-testing/)
- [Detect Python and Java code security vulnerabilities with Amazon CodeGuru Reviewer](https://aws.amazon.com/blogs/devops/detect-python-and-java-code-security-vulnerabilities-with-codeguru-reviewer/)
- [Amazon Inspector FAQs](https://aws.amazon.com/inspector/faqs/)

**Related videos:**

- [AWS re:Invent 2022 - Detect vulnerabilities in AWS Lambda functions using Amazon Inspector](https://www.youtube.com/watch?v=gWoJqnRB3MA&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec06.html*

---

# FSISEC07: How are you inspecting your financial services infrastructure and network for unauthorized traffic?

Monitor network traffic for expected and unexpected traffic to
identify irregularities and gain key insights into the
security of the system. For example, a poorly-performing
network can indicate that the network is under threat, and
irregular attempts to contact unexpected external systems can
indicate that an internal host has been compromised. With
generative AI services, inspection includes monitoring AI
endpoint access and authentication attempts, model
invocations, and data flow patterns.

## FSISEC07-BP01 Monitor instance traffic

Amazon EC2 instances automatically track aggregate network
inbound and outbound traffic with Amazon CloudWatch.
[Use
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) and push log files to Amazon CloudWatch for storage, aggregation, reporting, and alert
notification.
[Create
profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) for the expected network behavior
for each EC2 instance and
[generate
alarms when deviations are detected](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html). For
example, system or web logs sent to Amazon CloudWatch Logs
could generate alarms based on the number of login failures
or web request latencies. Similarly, TCP connection or
outstanding connection request counts could be stored in
Amazon CloudWatch and used to detect security threats like
SYN flood threats.

For AI workloads, implement comprehensive monitoring of
model endpoint access and API usage patterns while
establishing private network communication and tracking data
access across AI systems.

## FSISEC07-BP02 Use VPC Traffic Mirroring

Use
[VPC
Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html) to copy network traffic from
an elastic network interface of Amazon EC2 instances and
forward that traffic to security and monitoring appliances for
use cases such as content inspection, threat monitoring, and
troubleshooting. These security and monitoring appliances can
be deployed on a fleet of instances behind a Network Load
Balancer (NLB) with a User Datagram Protocol (UDP) listener.
Amazon VPC traffic mirroring supports traffic
[filtering](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html)
and packet truncation, allowing you to extract traffic that you
are interested in monitoring. It also addresses challenges
around having to install and run packet-forwarding agents on
EC2 instances. Packets are captured at the Elastic Network
Interface level, which cannot be tampered with from the user
space, thus offering better security posture.

## FSISEC07-BP03 Use immutable infrastructure with no human access

Immutable infrastructure is a model in which no updates,
security patches, or configuration changes happen in place on
production systems. If changes are needed, a new version of
the architecture is built and deployed. Because changes aren't
allowed in immutable infrastructure, you can be confident in
the deployed system. Immutable infrastructures are more
consistent, reliable, and predictable, and they simplify many
aspects of software development and operations by minimizing
common issues related to mutability.

Adopt
[immutable
infrastructure](https://aws.amazon.com/blogs/mt/leveraging-immutable-infrastructure-nubank/) practices with no human
access to better adhere to your audit and compliance needs.
You can version control your infrastructure, and handling
failure becomes a routine and continual way of doing business.

## FSISEC07-BP04 Allow interactive access for emergencies only

Tightly control and monitor interactive access to EC2
instances. Interactive access should typically be provided for
emergency-only,
[break-glass](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/break-glass-access.html)
scenarios.

Test and review these pre-staged emergency user accounts,
which normally are highly privileged and could be limited to
read only. Limit the time duration of break-glass procedure
and the password time duration. Have a ticketing system with
procedures requiring that an acceptable form of authentication
be provided by the requester and recorded before the accounts
are made available. This helps control and reduce the account's misuse, having only pre-approved
personnel who complete a certain emergency task. The
break-glass accounts and distribution procedures must be
documented and tested as part of implementation and carefully
managed to provide timely access when needed. A special audit
trail needs to be in place to monitor such emergency access
for later audit and review.

Use
[AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) to provide
an interactive, one-click browser-based shell to your Amazon EC2 instances, on-premises instances, and virtual machines
(VMs). Session Manager provides secure and auditable instance management without the
need to open inbound ports, maintain bastion hosts, or manage
SSH keys.

### Prescriptive guidance

- Publish and view statistical graphs of your own metrics
with Amazon CloudWatch. For more details, see
[Publishing
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html).
- You can use the CloudWatch feature of Anomaly Detection,
which analyzes past metric data to create a model of
expected values. The steps for that implementation is
described in the following documentation:
[Implement CloudWatch alarms based on anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html).
- Enable traffic mirroring to analyze the selected traffic
from a mirror source sent to a mirror target. For more
information, see
[Get
started with Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-getting-started.html).
- To adopt a strategy of immutable servers, see the
following blog post:
[Create immutable servers using EC2 Image Builder and AWS CodePipeline](https://aws.amazon.com/blogs/mt/create-immutable-servers-using-ec2-image-builder-aws-codepipeline/).

## Resources

**Related documents:**

- [Leveraging AWS CloudFormation to create an immutable infrastructure](https://aws.amazon.com/blogs/mt/leveraging-immutable-infrastructure-nubank/)
- [Managing temporary elevated access to your AWS environment](https://aws.amazon.com/blogs/security/managing-temporary-elevated-access-to-your-aws-environment/)

**Related videos:**

- [AWS re:Invent 2022 - A deep dive on the current security threat landscape with AWS](https://www.youtube.com/watch?v=h7WvCyygb8U)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec07.html*

---

# FSISEC08: How do you isolate your software development lifecycle (SDLC) environments (like development, test, and production)?

We recommend that you separate production workloads from
non-production workloads. Maintaining resource isolation
between software development lifecycle (SDLC) environments
reduces the chance of misuse and accidents in production
environments. This is an important guidance for all financial
institutions, including those that are subject to Payment Card
Industry Data Security Standard (PCI DSS). For generative AI
workloads, environment isolation extends to model artifacts,
prompt catalogs, AI service endpoints, and data isolation for
training datasets and inference data.

## FSISEC08-BP01 Implement a multi-account strategy

Using multiple AWS accounts to help isolate and manage your
business applications and data can help you optimize across
most of the
[AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) pillars,
including operational excellence, security, reliability, and
cost optimization. We recommend organizing your overall AWS
environment with a
[multi-account
strategy](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html). The extent to which you use
these best practices depends on your stage of the cloud
adoption journey and specific business needs.

We recommend that you isolate production workload
environments and data in production accounts housed within
production OUs, under your top-level workload-oriented OUs.
Apart from production OUs, we recommend that you define one
or more non-production OUs that contain accounts and
workload environments that are used to develop and test
workloads.

For AI systems, establish clear separation between
development and production environments while isolating
model training and inference environments, maintaining
separate prompt catalogs for each environment, and
implementing strict controls for cross-environment AI
service access.

Having different accounts dedicated to different SDLC
environments provides a natural isolation in managing
privileges in IAM. AWS Organizations facilitates the
management of account hierarchy. Define service control
policies (SCPs) to limit the actions a user can perform
inside these accounts. For example, you could minimize
changes in production to CloudTrail logging, help prevent
internet gateways set up in a VPC, or help prevent modifying
AWS Config tracking.

To offer a straightforward way to set up and govern an AWS
multi-account environment that follows prescriptive best
practices, AWS has created
[AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), which extends the
capabilities of AWS Organizations. To help keep your
organizations and accounts from *drift*,
or divergence from best practices, AWS Control Tower applies
[comprehensive
controls](https://aws.amazon.com/blogs/aws/new-for-aws-control-tower-comprehensive-controls-management-preview/) (sometimes called
*guardrails*). For more detail, see
[Limitations
and quotas in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/limits.html).

## FSISEC08-BP02 Enforce network isolation

Some financial industry regulators require the implementation
of techniques such as
[Zero
Trust](https://aws.amazon.com/security/zero-trust/) or microsegmentation in their
regulated entities. In addition to IAM isolation, enforce
clear separation of resources between production and
non-production environments. Using different accounts helps create the highest form of isolation possible on AWS. However,
you may need to reach resources across accounts, especially
when accessing shared services such as logging and security
services.

[VPC
Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) connects resources in two VPCs (in
the same account or between different accounts) without the
need of additional gateways or VPN connections, and it makes
the peered network visible to each other. This requires complete network trust between
the two VPCs, and better alternatives exist depending on your
use case. If the objective is to access only a few services in
the other VPC, use
[AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), which provides connectivity
over an internal network without VPN and limits network exposure. Service publishers also have to specify which IAM
principals can consume these endpoints and attach an IAM
resources policy specifying what actions are allowed. If more
extensive cross-VPC access is needed, separation and private
connectivity can be also established with
[AWS Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

## Resources

**Related documents:**

- [Best Practices for Organizational Units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/)
- [Supporting Data Residency Requirements by Extending AWS Control Tower Governance to Non-supported
Regions](https://aws.amazon.com/blogs/mt/supporting-data-residency-requirements-by-extending-aws-control-tower-governance-to-non-supported-regions/)
- [The
AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html)
- [Zero
Trust architectures: An AWS perspective](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/)

**Related videos:**

- [AWS Summit DC 2022 - Integrating AWS services and Zero Trust networks](https://www.youtube.com/watch?v=4sWFKtoAMsI&ab_channel=AWSEvents)
- [AWS re:Invent 2020: Zero Trust: An AWS perspective](https://www.youtube.com/watch?v=O33LPy4M4vA&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec08.html*

---

# FSISEC09: How are you managing your encryption keys?

In addition to implementing the
[data
protection recommendations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html) applicable to any
company seen in the AWS Well-Architected Framework Security
Pillar, financial institutions often have additional
industry-specific requirements that can influence the management
of cryptographic keys. With generative AI systems, key
management extends to protecting model artifacts, training
data, knowledge bases, sensitive prompts and prompt catalogs.

## FSISEC09-BP01 Consider compliance obligations regarding location of cryptographic keys

AWS Key Management Service (AWS KMS) uses an
[envelope
encryption strategy](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), which
consists of encrypting plaintext data with a data key, and
then encrypting the data key with another key. AWS KMS keys
are created in AWS KMS and never leave AWS KMS unencrypted.

AWS KMS supports three types of keys: customer-managed keys,
AWS managed keys, and AWS owned keys (for more information,
see the
[AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)). For many FSI customers,
customer- managed keys are the preferred option, because
they allow for control of the permissions to use keys from
their applications or AWS services. It also provides added
flexibility for key generation and storage.

Although it's less common, AWS customers who have a
compliance or regulatory need to store and use their
encryption keys on-premises or outside of the AWS Cloud can
do so by using
[external
key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html).

### Prescriptive guidance

- Work backwards from your company's compliance objectives
and security standards in order to determine the right
encryption method for your use case.

Leverage AWS audit reports, available for download
at
[AWS Artifact](https://aws.amazon.com/artifact/), to understand the
controls implemented by AWS, and tested for
operating effectiveness by third-party auditors on
AWS KMS.
- Review the list of services that you are using for
your workload to understand
[how
AWS KMS integrates
with the service](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html).
- Review
[AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) with AWS KMS
integration if your application needs to encrypt
data client-side.

- Evaluate the differences between
[different
key types in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt).
- When using customer managed keys, consider the default
key store to provide the best balance between agility,
security, data sovereignty, and availability.
- Consider using custom key stores with
[AWS CloudHSM](https://aws.amazon.com/cloudhsm/) or the
[external
key store](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) to adhere to specific
compliance obligations.
- For AI workloads, implement comprehensive encryption for
model artifacts and sensitive training data while
protecting prompt catalogs and verifying compliant key
management across all AI data flows.

## Resources

**Related documents:**

- [How Financial Institutions can Select the Appropriate Controls to Protect Sensitive Data](https://aws.amazon.com/blogs/industries/how-financial-institutions-can-select-the-appropriate-controls-to-protect-sensitive-data/)
- [Announcing
AWS KMS External Key Store (XKS)](https://aws.amazon.com/blogs/aws/announcing-aws-kms-external-key-store-xks/)

**Related videos:**

- [AWS re:Invent 2022 – Protecting secrets, keys, and data: Cryptography for the long term](https://www.youtube.com/watch?v=9vr3oMODIUE&t=2535s&ab_channel=AWSEvents)
- [AWS re:Invent 2022 – AWS data protection: Using locks, keys, signatures, and certificates](https://www.youtube.com/watch?v=lD34wbc7KNA&ab_channel=AWSEvents)
- [AWS re:Invent 2022 – Introducing AWS KMS external keys](https://www.youtube.com/watch?v=prj6xgpHFTo&t=672s&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec09.html*

---

# FSISEC10: How are you handling data loss prevention in the cloud environment?

Data loss as part of a security event, accident or business
process can affect both your operation and state of compliance.
The following recommendations can help with the protection
from theft and inadvertent or malicious loss. Generative AI
systems introduce new considerations for data loss prevention,
including model outputs, prompt security, training data, model
artifacts, and AI-generated content.

## FSISEC10-BP01 Prevent modifications and deletions of logs and data

Financial services agencies around the world, including the
Securities and Exchange Commission (SEC) and the Financial
Industry Regulatory Authority (FINRA) in the US, have
created rules

that require a broker-dealer to maintain and preserve
electronic records exclusively in a non- rewriteable,
non-erasable format, also known as a write once, read many
(WORM) format.

For object data, Amazon
[S3
Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) allows you to store objects
using a WORM model. You can use WORM protection for
scenarios where it is imperative that data is not changed or
deleted after it has been written. With S3 Object lock, you
can securely deliver logs to a designated S3 bucket, and use
the S3 Object Lock feature to make the logs immutable. It
blocks object version deletion during a customer- defined
retention period so that you can enforce retention policies.
In

conjunction with
[S3
versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), which protects objects from
being overwritten, you're able to keep objects immutable for
as long as S3 Object Lock protection is applied.

For file data, use
[SnapLock](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock.html),
a feature on
[Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html) that allows you to
store files using a WORM model, helping prevent accidental or
malicious attempts at modification and deletion for a
customizable retention period. You can also back up data on
FSx for ONTAP using AWS Backup and WORM-protect your backups
using
[AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html).

For AI systems, implement secure prompt catalogs and
validate model responses for potential data leakage while
protecting training data integrity and maintaining
continuous monitoring of AI system outputs and establishing
audit trails for all AI data interactions.

## FSISEC10-BP02 Limit and monitor key deletes

Once encrypted, the data is protected by cryptographic keys
that must be kept as long as the data is to be accessed. Only
[key
administrators](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-adding-permission.html) should perform key deletion.
Review all destruction requests within the safety window, as a
key cannot be destroyed immediately. Instead, it is disabled,
which prevents use, and is deleted at the expiry of the
window.

To help validate that the key deletion won't impact your
company,
[set
up an alarm](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html) that detects use of an AWS KMS
key pending deletion.

### Prescriptive guidance

- Make sure that the Amazon S3 buckets are configured to
use the
[Object
Lock feature](https://aws.amazon.com/blogs/storage/protecting-data-with-amazon-s3-object-lock/) to help prevent the
objects they store from being deleted, and help meet
regulatory compliance needs.
- Make sure that
[Amazon S3 object versioning is enabled](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) for
your Amazon S3 buckets in order to preserve and recover
overwritten and deleted Amazon S3 objects as an extra
layer of data protection or data retention.
- Set up
[AWS Config managed rule](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-versioning-enabled.html) to identify Amazon S3 buckets that do not have versioning enabled, and

[implement
automatic remediation](https://aws.amazon.com/blogs/storage/automate-amazon-s3-versioning-using-aws-config-rules/) to configure
versioning on non-compliant Amazon S3 buckets.
- Implement backup and restore processes to help you
restore data to a point in time before data corruption,
modification or destruction. AWS
[provides
several solutions](https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/) for backups to
integrate with your operational and security incident
recovery procedures.

Use
[AWS Backup](https://aws.amazon.com/backup/) with AWS Organizations to
centrally deploy data protection policies to
configure, manage, and govern your backup activities
across your AWS accounts and resources.
- Beyond creating and storing your backups,
[AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) can
continuously evaluate backup activity and generate
audit reports that can help you demonstrate
compliance with regulatory requirements. These
reports also provide you with more visibility into
your backup activities, helping you monitor your
operational posture and identify failures that may
need further action.

- Deleting an AWS KMS key is destructive and potentially
dangerous. After an AWS KMS key is deleted, you can no
longer decrypt the data that was encrypted under that
AWS KMS key, which means that data becomes
unrecoverable.

Delete an AWS KMS key only when you are sure that
you don't need to use it anymore.
- If you are not sure, consider
[disabling
the AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) instead of
deleting it.
- [Control
access to key deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-adding-permission.html) by creating
fine-grained access control policies and allow only
authorized principals with the ability to
[schedule
key deletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html).

- Create an alarm to detect and notify on AWS KMS key
deletion events.
- [Create an alarm to detect usage of an AWS KMS key that is scheduled for deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html).

## Resources

**Related documents:**

- [How to manage retention periods in bulk using Amazon S3 Batch Operations](https://aws.amazon.com/blogs/storage/how-to-manage-retention-periods-in-bulk-using-amazon-s3-batch-operations/)

**Related videos:**

[Data protection strategies for the cloud - AWS Online Tech Talks](https://www.youtube.com/watch?v=4PgoBjqpm8U&ab_channel=AWSOnlineTechTalks)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec10.html*

---

# FSISEC11: How are you protecting against ransomware?

Ransomware refers to a business model and a wide range of
associated technologies that bad actors use to extort money.
The bad actors use a range of tactics to gain unauthorized
access to their victims data and systems, including exploiting
unpatched vulnerabilities, taking advantage of weak or stolen
credentials, and using social engineering. Access to the data
and systems is restricted by the bad actors, and a ransom
demand is made for the safe return of these digital assets.
Protection against ransomware now includes securing AI models,
model registries, prompts, prompt catalogs and training data
from manipulation or compromise.

## FSISEC11-BP01 Prevent malware infiltration by securing compute resources

To detect malware that may be the source of a ransomware
incident, enable
[malware
protection in](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html)
[Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html). This feature automatically
initiates an agentless scan on the Amazon Elastic Block Store (EBS) volumes attached to the impacted EC2 instance or
container workload to detect the presence of malware. For AI
workloads, implement secure prompts, prompt catalogs and
validate user inputs while monitoring for potential model
manipulation and enforcing response filtering mechanisms.

### Prescriptive guidance

- Use
[Amazon S3 Object Lock](https://aws.amazon.com/s3/features/object-lock/) for object storage
immutability and ransomware protection within cloud
storage.
- Implement backup and restore processes to help you
restore data to a point in time before data corruption,
modification or destruction. AWS
[provides
several solutions](https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/) for backups to
integrate with your operational and security incident
recovery procedures.

Use
[AWS Backup](https://aws.amazon.com/backup/) with AWS Organizations to
centrally deploy data protection policies to
configure, manage, and govern your backup activities
across your AWS accounts and resources.
- Enable
[AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html), which enforces
WORM (write-once-read-many) setting for the backups
you store and create in a backup vault.

- Because many ransomware events arise from unintended
disclosure of static IAM access keys, AWS recommends
that you use IAM roles that provide short-term
credentials, rather than using long-term IAM access
keys. This includes using
[identity
federation](https://aws.amazon.com/identity/federation/) for your developers who are
accessing AWS, using IAM roles for system-to-system
access, and using
[IAM
Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) for hybrid access.
- Enable
[Amazon S3 protection in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html).
With Amazon S3 protection, GuardDuty monitors
object-level API operations to identify potential
security risks for data in your Amazon S3 buckets. This
includes findings related to anomalous API activity and
unusual behavior related to your data in Amazon S3, and
can help you identify a security event early on.
- Enable
[Amazon GuardDuty Malware Protection](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html) across
all AWS accounts in your organization, to help you
detect the potential presence of malware by scanning the
Amazon EBS volumes that are attached to the Amazon EC2
instances and container workloads.

## FSISEC11-BP02 Prevent threats from accessing your data stores

Scoping access to data based on the principal of minimum
privileges helps prevent as well as limit the blast radius of
an exploit. An effective data classification scheme, along with
enforcement and monitoring based on that scheme can help
prevent an bad actor from having accessing and encrypting your
data.

Network isolation and segregation is another effective
protection as compromised systems cannot reach deep into your
network. Leverage the best practices recommended in the
Infrastructure protection section to funnel access to data
stores over a private network, from a limited number of hosts.

## FSISEC11-BP03 Use frequent backups to recover from a threat

Because ransomware makes itself known quickly, incorporate
short-lived anti-ransomware backups into your backup cycle.
AWS take snapshots of data stores, so back up often and keep
these around for only a few days to limit costs.

For more information on how to protect from Ransomware at AWS,
see
[Ransomware Risk Management on AWS Using the NIST Cyber Security Framework (CSF)](https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/ransomware-risk-management-on-aws-using-nist-csf.html).

### Prescriptive guidance

- Use
[Amazon S3 Object Lock](https://aws.amazon.com/s3/features/object-lock/) for object storage
immutability and ransomware protection within cloud
storage.
- Implement backup and restore processes to help you
restore data to a point in time before data corruption,
modification or destruction. AWS
[provides
several solutions](https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/) for backups to
integrate with your operational and security incident
recovery procedures.

Use
[AWS Backup](https://aws.amazon.com/backup/) with AWS Organizations to
centrally deploy data protection policies to
configure, manage, and govern your backup activities
across your AWS accounts and resources.
- Enable
[AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html), which enforces
WORM (write-once-read-many) setting for the backups
you store and create in a backup vault.

- Because many ransomware events arise from unintended
disclosure of static IAM access keys, AWS recommends
that you use IAM roles that provide short-term
credentials, rather than using long-term IAM access
keys. This includes using
[identity
federation](https://aws.amazon.com/identity/federation/) for your developers who are
accessing AWS, using IAM roles for system-to-system
access, and using
[IAM
Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) for hybrid access.
- Enable
[Amazon S3 protection in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html).
With Amazon S3 protection, GuardDuty monitors
object-level API operations to identify potential
security risks for data in your Amazon S3 buckets.

This includes findings related to anomalous API activity
and unusual behavior related to your data in Amazon S3,
and can help you identify a security event early on.

- Enable
[Amazon GuardDuty Malware Protection](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html) across
all AWS accounts in your organization, to help you
detect the potential presence of malware by scanning the
Amazon EBS volumes that are attached to the Amazon EC2
instances and container workloads.

## Resources

**Related documents:**

- [Protecting
against ransomware](https://aws.amazon.com/security/protecting-against-ransomware/)
- [GuardDuty findings that initiate Malware Protection scans](https://docs.aws.amazon.com/guardduty/latest/ug/gd-findings-initiate-malware-protection-scan.html)
- [Ransomware Risk Management on AWS Using the NIST Cyber Security Framework (CSF)](https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/ransomware-risk-management-on-aws-using-nist-csf.html)
- [Ransomware mitigation: Top 5 protections and recovery preparation actions](https://aws.amazon.com/blogs/security/ransomware-mitigation-top-5-protections-and-recovery-preparation-actions/)
- [Workshop: Ransomware on S3 - Simulation and Detection](https://catalog.workshops.aws/aws-cirt-ransomware-simulation-and-detection/en-US)

**Related videos:**

- [What is Amazon GuardDuty Malware Protection? | Amazon Web Services](https://www.youtube.com/watch?v=xKAp5lx1Sb0&ab_channel=AmazonWebServices)
- [AWS re:Invent 2021 - Backup, disaster recovery, and ransomware protection with AWS](https://www.youtube.com/watch?v=Ru4jxh9qazc&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec11.html*

---

# FSISEC12: How are you meeting your obligations for incident reporting to regulators?

Various regulations require that the banking organizations and
managed service providers notify the regulators as soon as a
cyber security incident has been discovered, such as the
[Final
Issuances](https://www.occ.treas.gov/topics/laws-and-regulations/occ-regulations/final-issuances/index-final-issuances.html) published by the Office of the
Comptroller of the Currency (OCC), Security and Exchanges
Commision (SEC)
[Cybersecurity
Disclosure](https://www.sec.gov/news/statement/gerding-cybersecurity-disclosure-20231214) or the Network and Information
Systems (NIS) regulation. Incident reporting now includes
AI-specific events such as harmful model responses or
unauthorized model access, model manipulation and poisoning
attacks.

## FSISEC12-BP01 Regularly review your incident response plan for regulatory compliance

Organizations that are operating in multiple Regions need to
be aware the
[regulatory
requirements](https://aws.amazon.com/financial-services/security-compliance/compliance-center/) of the regions they are
operating in and any local data residency requirements (such
as
[GDPR](https://aws.amazon.com/compliance/gdpr-center/)).
With local data residency requirements, you cannot copy the
data to a different Region for analysis purposes. In this
case, you may need to consider the latency aspects if you
have a global team that needs to access and analyze data
from a different Region. Consider setting up a local incident
response team that can act on the incident in a timely
manner and report to local regulators as necessary.

As mentioned before, as part of your incident response plan,
you should
[develop
playbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) to standardize response process
for cybersecurity incidents. With the ever-changing
regulatory requirements of the financial industry and the
dynamic nature of cloud environments, it is important to
establish a process that reviews the playbooks in use to
perform incident or recovery communications as required.

### Prescriptive guidance

- Create your own playbooks to facilitate responses during
cybersecurity incidents. Refer to
[building
incident response playbooks for AWS](https://github.com/aws-samples/aws-incident-response-playbooks-workshop)
for sample playbooks.
- Use
[AWS Compliance Center](https://aws.amazon.com/financial-services/security-compliance/compliance-center/?country-compliance-center-cards.sort-by=item.additionalFields.headline&country-compliance-center-cards.sort-order=asc&awsf.country-compliance-center-master-filter=%2Aall) for information on
regulatory responsibilities that can be related to
incident responses.
- For AI systems:

Include AI-specific incidents in response
procedures.
- Develop playbooks for model misuse.
- Establish reporting procedures for AI incidents.
- Include AI events in regulatory reporting
requirements.

## Resources

**Related documents:**

- [General
Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/)

**Related videos:**

- [Introduction
to AWS Compliance Center](https://www.youtube.com/watch?v=lp-Yn-xkhM8&ab_channel=AmazonWebServices)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec12.html*

---

# FSISEC13: How do you secure AI/ML models and protect training data?

Financial institutions implementing generative AI must
establish comprehensive security controls throughout the AI
lifecycle, from data preparation to model deployment and
monitoring. This includes protecting training data integrity,
securing model development environments, and implementing
robust controls for inference to prevent unauthorized access,
model manipulation, and data poisoning attacks.

## FSISEC13-BP01 Implement comprehensive model security controls

Securing AI/ML models requires implementing multiple layers
of protection to maintain model integrity and prevent
unauthorized access. Establish least privilege access to
foundation model endpoints and implement private network
communication between AI components using VPC endpoints or
AWS PrivateLink. Use customer-managed encryption keys for
model artifacts and training data, implement model
versioning with integrity checking mechanisms, and establish
secure model storage with strict access controls and audit
logging.

## FSISEC13-BP02 Protect training data integrity

The integrity of training data directly impacts the security
and compliance of AI models. Implement data purification
filters to detect harmful inputs, establish data lineage
tracking for regulatory compliance, and apply classification
schemes for sensitive financial data. Deploy continuous
monitoring to detect data poisoning attempts and implement
backup and recovery procedures aligned with your
organization's data protection strategy.

## FSISEC13-BP03 Secure model deployment and inference

Securing deployment and inference stages is critical for
preventing unauthorized access and protecting against
AI-specific attacks. Implement version-controlled prompt
catalogs with security review processes, establish model
access controls using IAM policies, and deploy monitoring
for anomalous invocation patterns. Implement response
filtering mechanisms like Amazon Bedrock Guardrails and
secure API gateways with appropriate authentication,
authorization, and comprehensive logging.

## Resources

### Documents

- [AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/wellarchitected-generative-ai-lens.html)
- [Securing
Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html)
- [AI/ML
for Security](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/ai-ml.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec13.html*

---

# FSISEC14: How do you monitor AI system outputs for security issues?

Continuous monitoring of AI system outputs is critical for
financial institutions to detect harmful responses, potential
data leakage, and security violations. Without proper
monitoring, AI systems may generate responses that expose
sensitive information, violate compliance requirements, or
create security vulnerabilities. Implementing comprehensive
monitoring across all AI interactions enables organizations to
identify and address security issues before they impact
customers or operations.

## FSISEC14-BP01 Implement automated response validation

Automated response validation is essential for ensuring AI
systems operate within defined security parameters. Deploy
guardrails for content filtering to detect and prevent
harmful, biased, or non-compliant responses from reaching
users. Monitor for prompt injection attempts where malicious
inputs might manipulate model behavior and implement
automated detection systems that flag potentially harmful
responses for review.

Establish clear response quality and safety metrics that
align with your organization's security and compliance
requirements. Create alert mechanisms that notify security
teams when suspicious AI system behavior is detected,
enabling rapid investigation and remediation of potential
security issues.

## FSISEC14-BP02 Monitor AI system interactions

Comprehensive monitoring of AI system interactions provides
visibility into potential security issues and enables
proactive threat detection. Track all model invocations and
user interactions to establish usage patterns and identify
anomalies that may indicate security incidents. Monitor for
unauthorized access patterns to AI services that could
signal credential compromise or insider threats.

Implement comprehensive logging of AI system events
including user inputs, model responses, and system actions.
Establish baseline behavior patterns for AI systems to
enable anomaly detection and monitor for potential data
leakage in model responses that could expose sensitive
financial information or intellectual property.

## FSISEC14-BP03 Establish AI incident response procedures

Financial institutions must develop specialized incident
response procedures for AI-specific security events. Develop
playbooks that address unique AI security incidents such as
prompt injection attacks, harmful model responses, or model
manipulation attempts. Include harmful model responses in
your incident classification system to ensure appropriate
escalation and response.

Establish clear procedures for handling model response
validation failures, including containment, investigation,
and remediation steps. Create escalation procedures for AI
security events that define roles, responsibilities, and
communication channels. Where appropriate, implement
automated response mechanisms that can take immediate action
when AI security issues are detected, such as blocking
suspicious requests or disabling compromised endpoints.

## Resources

### Documents

- [AWS Well-Architected Generative AI Lens - Governance](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/governance.html)
- [IAM
Best Practices for AI Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Amazon SageMaker AI Model Governance](https://docs.aws.amazon.com/sagemaker/latest/dg/model-governance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec14.html*

---

# FSISEC15: How do you implement AI model governance and access controls?

Effective AI governance requires comprehensive access
controls, model lifecycle management, and continuous oversight
to adhere to regulatory requirements and organizational
policies. Financial institutions must establish structured
governance frameworks that define roles, responsibilities, and
processes for managing AI systems throughout their lifecycle.
Without proper governance and access controls, organizations
risk unauthorized model changes, compliance violations, and
security breaches.

## FSISEC15-BP01 Establish an AI model governance framework

A comprehensive AI model governance framework provides
structure and oversight for all AI activities within the
organization. Implement model approval workflows and change
management processes that ensure proper review and
authorization before models are deployed or modified. These
workflows should include security reviews, compliance
assessments, and performance validation.

Establish model performance monitoring and drift detection
capabilities to identify when models deviate from expected
behavior, which could indicate security issues or degraded
performance. Create standardized model documentation
requirements including model cards that capture key
information about model purpose, limitations, training data,
and security considerations.

Implement model retirement and lifecycle management
procedures that ensure secure decommissioning of outdated
models and proper transition to new versions. Establish AI
ethics and responsible AI guidelines that align with your
organization's values and regulatory requirements, providing
clear direction for AI development and deployment.

## FSISEC15-BP02 Implement comprehensive access controls

Granular access controls are essential for maintaining the
security and integrity of AI systems. Create distinct roles
for prompt engineering and security administration to
enforce separation of duties and prevent unauthorized
modifications. Maintain separate permissions for model
access and management using IAM policies, resource-based
policies, and permission boundaries.

Establish dedicated approval workflows for AI system changes
that ensure proper review and authorization before
modifications are implemented. Enforce strict boundaries
between development and production AI environments to
prevent unauthorized changes from affecting production
systems. Implement permissions boundaries for agentic
workflows to control how AI agents can interact with other
systems and data.

## FSISEC15-BP03 Monitor and audit AI system governance

Continuous monitoring and auditing of AI governance
activities improves ongoing regulatory adherence and
effectiveness. Track adherence to AI governance policies
through automated checks and regular assessments. Monitor
model performance against established baselines to detect
anomalies that could indicate security issues.

Audit AI system access patterns and permissions to identify
potential security risks or unauthorized activities.
Establish regular governance reviews and assessments that
evaluate the effectiveness of your AI governance framework
and identify areas for improvement. Implement automated
compliance checking for AI systems that can verify adherence
to security policies, regulatory requirements, and
organizational standards.

## Resources

### Documents

- [AWS Well-Architected Generative AI Lens - Governance](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/governance.html)
- [IAM
Best Practices for AI Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Amazon SageMaker AI Model Governance](https://docs.aws.amazon.com/sagemaker/latest/dg/model-governance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec15.html*

---

# FSISEC16: How do you use AI for threat detection and security automation?

Financial institutions can use AI capabilities to enhance
their security posture through automated threat detection,
incident response, and security monitoring. AI-powered
security solutions can process vast amounts of data to
identify patterns and anomalies that might indicate security
threats, enabling faster and more effective responses. While
implementing these AI security systems, organizations must
verify that the AI components themselves remain secure and
operate within appropriate governance frameworks.

## FSISEC16-BP01 Implement AI-powered threat detection

AI technologies can significantly enhance threat detection
capabilities by identifying subtle patterns and anomalies
that traditional rule-based systems might miss. Use AI for
anomaly detection in network traffic and user behavior to
identify potential security incidents based on deviations
from normal patterns. Use these systems to establish
baselines of normal behavior and flag activities that fall
outside expected parameters.

Implement AI-enhanced malware detection and analysis to
identify novel threats and variants not captured by
signature-based detection. Deploy AI for automated security
event correlation and analysis to identify relationships
between seemingly unrelated events that might indicate
coordinated attacks. Use AI for predictive threat
intelligence and risk assessment to anticipate potential
threats based on historical data and current trends,
allowing proactive security measures. For financial
institutions, implement AI-powered fraud detection and
prevention systems that can identify unusual transaction
patterns and potential fraud attempts in real-time.

## FSISEC16-BP02 Automate security responses with AI

AI can enhance security operations by automating responses
to detected threats, reducing response times and minimizing
human error. Implement AI-driven incident response and
remediation that can automatically contain threats and
initiate remediation actions based on predefined playbooks.
Use AI for automated security policy enforcement to
consistently apply security controls across your
environment.

Deploy AI for real-time security decision making that can
analyze threats and recommend or implement appropriate
responses without human intervention for lower-risk
scenarios. Implement AI-powered security orchestration and
automation to coordinate responses across multiple security
tools and systems. Use AI for continuous security posture
assessment to identify vulnerabilities and configuration
issues before they can be exploited.

## Resources

### Documents

- [AWS Security Hub CSPM Machine Learning Models](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-ml-models.html)
- [Amazon GuardDuty Machine Learning](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_ml.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec16.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
