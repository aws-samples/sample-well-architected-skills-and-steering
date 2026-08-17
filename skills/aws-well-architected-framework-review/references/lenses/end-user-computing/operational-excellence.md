# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 17

---

# EUCOPS01 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS01-BP01 Build a project team which includes executive level sponsors and relevant business and technical communities

When starting your AWS EUC project be sure to convene a project board which has
sponsorship from a significant influencer or senior decision maker and buy in from both
business and technology stakeholders, this will make sure that the views of the business and
technology teams are considered when delivering the new service. Each invested project board
member will have their own view of the governance and organizational challenges likely to
arise throughout the project lifecycle, and their input is likely to reduce risk and enhance
the chances of project success.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Many frameworks exist that define a structured project approach, including advice on
project board formulation. The [Prince II methodology](https://prince2.wiki/roles/project-board/) is a common example that embraces this approach.

Implementing a structured approach or following a proven project management framework
will make sure that project requirements, key timelines and success criteria are well
documented, and that day-to-day tracking of project activities and progress towards key
milestones is in effect.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops01-bp01.html*

---

# EUCOPS02 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# EUCOPS02-BP01 Engage technical stakeholders from all disciplines that affect your EUC services

The deployment of AWS EUC services typically requires integration with many diverse
technology areas. Build a project team which includes experts from multiple technology
disciplines to identify resourcing issues early on, understand key technological blockers
affecting deployment of the AWS EUC project, and accommodate and manage key processes and
procedures used by each team to deliver successful outcomes.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Draw upon experiences from across all of your technical teams to make sure that
relevant insights are considered as you navigate through the design, deployment and
support of a new EUC deployment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops02-bp01.html*

---

# EUCOPS02-BP02 Build a matrix of all internal and external stakeholders who may be affected by changes to the way you deliver EUC services

To provide an initial starting point for building a project team, collate a list of all
the technology areas which are directly or indirectly affected by an AWS EUC migration.
Additionally, create a corresponding list of each service owner. This matrix helps you
oversee a successful implementation or migration.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

EUC services in general, require a good understanding of many technology disciplines
to design and deploy secure, reliable, and scalable solutions. The team that manages the
AWS EUC services must have skills across general cloud principles, compute, storage,
networking, applications, and security at a minimum to implement services that deliver
against business requirements and internal and external SLAs while maintaining a first
class user experience.

While technical skills in the EUC discipline are key, incorporate the teams
responsible for maintaining other key processes, such as problem, incident, and capacity
management and change control, into decision making processes. After a deployment or
migration, these teams will be responsible for ongoing support and user experience.

Encourage participating teams to interact with each other in order to exchange
opinions and ideas. Fostering collaboration and gathering diverse opinions typically
results in a better overall solution, improving service and support.

Provide these teams sufficient resources not only to manage and maintain the planned
infrastructure but also to perform continual service development. Plan to accommodate new
features and functionality that meet evolving business needs. If your technical teams lack
the AWS expertise necessary to deploy or migrate to Amazon WorkSpaces, Amazon WorkSpaces Applications, or
Amazon WorkSpaces Secure Browser, consider engaging with AWS Professional Services or one of our
partners.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops02-bp02.html*

---

# EUCOPS03 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS03-BP01 Identify the business goals and success criteria for your EUC project

Verify that the deployment of the selected AWS EUC services addresses the needs of
both internal and external customers. For example, does the feature set of the selected
AWS EUC technology stack meet the requirements of all user personas identified as part of
the proposed project? Both employees, business partners, and external customers could be
affected.

While adopting AWS EUC services to take advantage of a service oriented, pay as you
go cost model has financial benefits, be sure that you understand the technological impact
of this approach for both internal and external customers.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Most organizations have personas that benefit from a deployment of or migration to a
cloud-hosted EUC service. While the business problems being solved may be clear, such as
cost reduction, increased agility and resilience, or global reach, it is also important to
evaluate whether the AWS EUC services being deployed meet the requirements of each user
persona.

Create a matrix of user personas that captures each unique set of hardware and
software requirements, accessibility options, and access requirements, highlighting where
technology limitations may need to be considered to accommodate other benefits.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops03-bp01.html*

---

# EUCOPS04 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS04-BP01 Identify the key capabilities and features that deliver business value and drive project success

While AWS EUC services may offer feature parity with your incumbent vendor, achieving
this parity may require additional engineering effort to integrate with existing operational
or support systems.

Planning for the proof of concept (PoC) or pilot phase of a migration project is an
opportunity to document acceptance criteria and define a list of the features and
functionality currently being delivered by your existing vendor. When moving into pilot and
production, these documents help you verify that all mandatory functionality has been tested
and can be successfully delivered.

Sacrificing features in order to take advantage of a more flexible cost and delivery
model for some user personas may be an acceptable approach. It may be feasible to deliver a
high percentage of your existing use cases, covering most of your user population using
built-in functionality and leaving just a small amount of engineering or the adoption of
third-party solutions to accommodate the remaining use cases.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

A PoC or pilot may reveal that it is not possible to deliver all of the features and
functionality offered by the incumbent EUC system. It may still be possible to roll out a
significant part of the project and reduce costs or realize many of the other benefits of
cloud delivery while investigating ways to bridge functionality gaps in areas where
feature parity cannot be maintained.

Following are some examples of where it may be possible to dispense with bundled EUC
functionality which is either no longer required or has been deprecated by new and
improved capabilities:

- Many existing EUC or VDI system features, such as those that optimize compute
resources, network bandwidth, or audio and video delivery, may no longer be required,
as compute, network, and media capabilities have vastly improved over time.
- Accessing your desktop or application resources from an HTML5 browser as standard
may be a significant change for the user experience, but standardization may offer
operational and support savings in the medium to longer term.
- Deploying WorkSpaces with Ubuntu for developers may reduce development costs for a
large population of users, moving away gradually from an incumbent, more costly EUC
solution.
- Using a vendor-supplied profile management solution may now be less functional
and performant than using a standard Microsoft solution such as FSLogix.
- It may be possible to dispense with complex legacy remote access solutions that
have evolved over time in favor of the pervasive and secure capabilities available
with the current generation of Amazon WorkSpaces and AppStream remoting protocols.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops04-bp01.html*

---

# EUCOPS05 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# EUCOPS05-BP01 Identify monitoring tools to provide the expected levels of insight into operational performance

While existing, familiar tools can be used to monitor an AWS EUC deployment, there
are many AWS services, such as automatic Amazon CloudWatch dashboards for Amazon WorkSpaces and Amazon
AppStream, AWS CloudTrail for API call monitoring, and Amazon Kinesis for log propagation and
centralized log storage.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Implement proactive monitoring of the health of all aspects of an AWS EUC
deployment to quickly identify and remediate problems that affect the user population,
their productivity, and any impact this may have on the business.

For both Amazon WorkSpaces and Amazon WorkSpaces Applications, it is important to monitor both the
service itself in addition to any external service dependencies. Consider the following
monitoring tools:

**Amazon WorkSpaces**

Amazon CloudWatch provides an automatic dashboard which gives an overview of overall service
health, including:

- Available or unhealthy WorkSpaces
- Session launch times
- Connection success and failure
- Session latency
- Users connected, disconnected, stopped, or in maintenance

Additional metrics, such as instance specific CPU, memory, and disk performance can
also be viewed. Develop custom CloudWatch widgets to fine tune the monitoring of specific groups
of WorkSpaces.

[Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-monitoring-alerting.html)

Amazon CloudWatch provides an automatic dashboard which gives an overview of overall service
health, including fleet capacity and utilization.

CloudWatch alarms can be configured to send alerts when specific thresholds are met.

Each WorkSpaces and Amazon WorkSpaces Applications instance exposes a network interface in the
customers managed VPC which can be addressed by third party monitoring tools for
traditional management.

As AppStream instances are ephemeral, logs required for compliance or historical
monitoring, such as event logs, can be harvested at user logoff or shutdown using session
scripts or in real time using services such as Amazon Kinesis.

**External dependencies**

Monitoring should also be in place for:

- Internet connectivity (user to Amazon WorkSpaces or Amazon WorkSpaces Applications service)
- Amazon networking
- Active directory
- RADIUS (or other MFA provider)
- Microsoft PKI (If certificate-based authentication is in use)
- SAML 2.0 Identity Provider (IdP) availability (If SAML 2.0 authentication is in
use)
- Private certificate authority (if certificate-based authentication is in use)
- User data repositories (like file shares and profile stores)
- Application web tiers
- Application database tiers
- Application licensing servers
- Web proxies
- Anti-virus infrastructure

If these services are hosted on Amazon EC2, Amazon CloudWatch can be used to monitor key health
metrics and alert when service degradation is detected.

For services still hosted on-premises, Amazon CloudWatch agents can be installed which send
key metrics to Amazon CloudWatch.

**Log propagation**

For centralized gathering of log files for troubleshooting and retrospective
analysis, Amazon Kinesis agents can be deployed on WorkSpaces or WorkSpaces Applications to deliver real-time
propagation of OS and application-level logs to a central location.

For Amazon WorkSpaces Applications, propagating instance log files in real time to a
centralized location is essential if you need to store logs for compliance purposes, as
AppStream instances are destroyed at the end of each session. For more detail, see [Using the Kinesis Agent to store WorkSpaces Applications Windows event logs](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-kinesis-agent-for-microsoft-windows-to-store-appstream-2-0-windows-event-logs/).

**AWS Health dashboard**

The [AWS Health
dashboard](https://health.aws.amazon.com/health/status) provides insight into the health and availability of AWS services
running across regions. Individual regional services can be filtered in the web page or
added to an RSS feed reader for additional visibility.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops05-bp01.html*

---

# EUCOPS05-BP02 Store and regularly analyze log files to detect anomalous activity and behaviors

Maintaining a central store of log data and performance metrics is frequently a
mandatory requirement if specific compliance standards need to be maintained. Even in the
absence of compliance requirements, maintaining a central store of data facilitates a better
understanding of service scaling, performance, and security enables analysis, which improves
root cause analysis and drives incremental service improvement.

Review the available data sources that provide key insight into the usage of your EUC
environment.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Extracting performance data and log files from both WorkSpaces and WorkSpaces Applications and
storing it centrally is essential if you need to adhere to specific industry compliance
standards or if you want to perform retrospective analysis of data for troubleshooting
purposes, root cause analysis, or predicting service scalability and requirements.

Amazon CloudWatch can be used to capture specific metrics and store the data longer term in
Amazon S3. Amazon Kinesis agents can also be installed on WorkSpaces or WorkSpaces Applications instances to
propagate system logs in real time to a centralized location. For more detail, see [Using Amazon Kinesis Agents to Store AppStream Event Logs](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-kinesis-agent-for-microsoft-windows-to-store-appstream-2-0-windows-event-logs/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops05-bp02.html*

---

# EUCOPS06 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS06-BP01 Deploy test, development, and pre-production environments to reduce risk to production services

Training and testing should be undertaken in isolated environments, with little or no
connectivity to production services.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Separate the EUC environments used for training, testing, and development from
production services to reduce the risk of non-production activities affecting normal
business operations. Create discrete test environments and use them for activities that
could disrupt production services, cause outages or performance degradation, or compromise
security.

When testing and staging new releases or updates to production systems, these should
be undertaken in a separate environment that matches the current production deployment as
closely as possible. This reduces the likelihood of issues arising from disparities
between test, staging and production.

AWS EUC services are Regional in nature and delivered on an AWS account by
account basis. Multiple Regions and accounts can be deployed to separate training,
testing, and production environments.

Multiple AWS accounts can also be deployed to separate production workloads for
scalability reasons, helping to avoid having all resources in the same place or where
service separation is necessary to align with compliance or security requirements.

AWS Control Tower can be used to streamline the management and governance of multiple
AWS accounts.

Unlike on-premises infrastructure, Amazon WorkSpaces and WorkSpaces Applications environments can be
[deployed using automated processes](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0210-EUC_Slide-Deck.pdf) and only attract costs while in use.

AWS CloudFormation templates can be used to deploy new AWS services such as WorkSpaces and
WorkSpaces Applications to reduce the likelihood of human error and reduce configuration drift.

AWS Systems Manager Runbooks can be used to automate some aspects of WorkSpaces deployment. For
more detail, see [SSM
Runbooks for Amazon WorkSpaces](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-wsp.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops06-bp01.html*

---

# EUCOPS07 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS07-BP01 Formalize the mandatory creation and maintenance of all EUC service-related documentation

Maintain a library of documentation related to the business requirements, architectural
design, service delivery, and support of your EUC deployment.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Create deployment and operations guides and keep them updated over time verify that
all processes used to install, administer, update, and maintain the AWS EUC environment
are captured. This documentation provides an effective method of communicating how the
environment should be managed to new administration or support staff and external
partners, when required.

As iterative operational testing takes place, use lessons learned from failover and
DR testing to evolve the deployment and operations guides and capture relevant changes
that were needed in order to successfully complete testing.

While this documentation does not provide an exhaustive list of all aspects of a
deployment that should be captured, gather as much detail of the end to end service
configuration and the subsequent management processes as possible.

For each of the following topics, if a manual installation was performed, capture the
specifics of how and why you configured each setting. If the deployment was automated,
document the methods used (like AWS CloudFormation or Terraform), and call out the specifics of how
and why each configuration decision was made.

**Infrastructure build**

How were the landing zone and your WorkSpaces or WorkSpaces Applications environments created, which
options were configured for each service, and why? CloudFormation templates can be used to
reliably and repeatably build the baseline infrastructure and the rationale behind the
CloudFormation template creation. Deployment and rollback processes can be captured and
documented.

**Active Directory or RADIUS integration**

Your Active Directory and RADIUS deployment and maintenance should be part of a
separate operations guide chapter. For WorkSpaces and WorkSpaces Applications, capture the specifics of
how you integrated Active Directory and RADIUS for the respective service. For WorkSpaces,
document which directory integration method was used, and capture the manual steps used to
deploy or details of the CloudFormation templates used to automate this process.

**SAML 2.0 or certificate-based authentication**

How was your SAML 2.0 IdP configured with respect to integration with Amazon WorkSpaces or
WorkSpaces Applications? Which SAML attributes were used to drive AppStream application
entitlements?

How will you monitor and manage the certificates used to build a chain of trust
between AWS IAM and your SAML provider?

For certificate-based authentication, capture the installation choices taken and the
integration points with Microsoft Certificate Services.

How will you manage certificates and expiry for integration between CBA and Microsoft
Certificate Services?

**Image management**

Document the process followed to create each of your custom images. Which updates and
hotfixes were applied, which applications were installed, how were they configured, and
which registry or file system changes were required?

How were your applications installed and deployed (for example, did you use local
images, App-V, MSIX, AppVolumes, network share, or third party isolation products?).

For WorkSpaces Applications, did you use session scripts? Document the scripts deployed and
what each script does.

For WorkSpaces BYOL deployments, document the process followed to extract your Windows 10
or 11 images, sanitize them, and import into Amazon WorkSpaces.

How should image updates be managed, which version control and naming conventions
will be applied, and how will you roll back to a known good configuration if required?

**Client deployment**

Which clients are required to access Workspaces or WorkSpaces Applications (for example,
Windows, macOS, or web), which user groups require each client type, and how should it be
installed? How will clients be updated?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops07-bp01.html*

---

# EUCOPS08 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS08-BP01 Adopt a mandatory and formalized process for managing any changes to EUC services and dependent infrastructure

Create a new process or integrate with existing processes that track all changes that
can affect the stability and security of your EUC deployment.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Track all changes which might directly or indirectly affect the performance and
availability of Amazon WorkSpaces or Amazon WorkSpaces Applications services. Implement a change control
process that documents each service update with a robust risk assessment and back-out plan
and involves technology stakeholders from all relevant areas. This process can reduce the
risk of service outages or degradation.

Both WorkSpaces and Amazon WorkSpaces Applications have key dependencies on many external services.
If changes to any of these services is required, a representative from the AWS EUC team
should be part of the change control team to review and quantify the risk of the change.

The service dependencies for Amazon WorkSpaces and Amazon WorkSpaces Applications include, but are not
restricted to:

- AWS networking
- Active Directory and connectors
- RADIUS
- Microsoft PKI (if certificate-based authentication is in use)
- Third Party PKI services that may be used to allocate public certificates for
related services
- AWS KMS if used for encryption of WorkSpaces images
- SAML 2.0 IdP availability (if SAML 2.0 authentication is in use)
- Private certificate authority (if certificate-based authentication is in use)
- User data repositories (like file shares or profile stores)
- Application web tiers
- Application database tiers
- Application licensing servers
- Web proxies
- Firewalls and other related security infrastructure
- Anti-malware infrastructure
- Thin client management infrastructure

Amazon WorkSpaces and Amazon WorkSpaces Applications also use other AWS services, such as Amazon EBS and
Amazon S3 for storage, so you should understand any changes being made to these systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops08-bp01.html*

---

# EUCOPS09 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# EUCOPS09-BP01 Maintain an up to date matrix of all EUC service owners and quick access links to the support plans for each service

Amazon WorkSpaces and Amazon WorkSpaces Applications, although easier to implement and administer than
traditional on-premises alternatives, still require specific knowledge to deploy, manage,
and support. To simplify the process of routing issues to the right owners, you should be
able to quickly identify the teams who are responsible for implementation and support along
with clear support plans for each application being delivered, expediting time to
resolution.

Each application delivered by WorkSpaces or WorkSpaces Applications should have a formalized support
plan with designated business and technical owners who are responsible for and involved in
the deployment, maintenance, and support of each application and its dependent technology
stacks.

Each application set should have its own designated level of criticality, with
associated SLAs that are clearly understood by the support teams involved. For disaster
recovery purposes, the business should be able to identify relevant RTO and RPO parameters
which each service should be engineered to accommodate so that critical business services
can be delivered even under the most challenging circumstances.

If you are delivering WorkSpaces or WorkSpaces Applications across multiple AWS Regions, verify that
a support and escalation mechanism exists that documents the transfer of responsibility
between regions when required. This documentation is important to sustain support efforts
across time zones, maximizing service continuity.

Note: Your business RPO and RTO requirements may be more aggressive than the service
can provide, and discrete groups of users may have different RPO and RTO requirements.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Create a process to quickly identify roles and responsibilities for each application
stack so that support teams can quickly identify the resources that need to be employed
and address any issues in service delivery.

## Resources

- [WorkSpaces Service Level Agreement](https://aws.amazon.com/workspaces/sla/)
- [WorkSpaces Applications Service Level
Agreement](https://aws.amazon.com/appstream2/sla/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops09-bp01.html*

---

# EUCOPS09-BP02 Allocate training time so your teams can build and maintain their skills to deploy and manage your AWS EUC environment

Training and enablement are key to maintaining a reliable, successfully-evolving EUC
deployment.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Provide targeted training on the AWS Cloud, Amazon WorkSpaces, and WorkSpaces Applications to verify
that architects, administrators, and support personnel all have the relevant skills to
design, deploy, and maintain the AWS EUC environment. Give this training through
authorized training courses and professional accreditations and create a training
environment that can be used for evaluation and self-instruction, augmenting official
coursework.

The core tenets are the same for WorkSpaces and WorkSpaces Applications as they are for delivering a
remotely accessed, centralized, and virtualized desktop and application delivery service,
either on-premises or from an alternate cloud vendor. Skills in these areas are
transferrable to deploying and managing AWS EUC services. It is essential for your
deployment teams to have a good understanding of compute, networking, storage,
virtualization, and application delivery, at a minimum.

Technical teams may need to be prepared in different ways depending on the nature of
the adoption of Amazon WorkSpaces and WorkSpaces Applications services:

**Greenfield a net new deployment with no prior cloud or EUC
skills**

Teams need to be trained, and they should iteratively maintain their skills in AWS
core competencies such as cloud delivery, compute, networking, and storage, in addition to
specific training and exposure to Amazon WorkSpaces and WorkSpaces Applications. Focus on understanding the
core tenets of cloud delivery such as reducing costs, increasing scalability and
resilience, and taking advantage of the global reach of AWS Cloud services. This may be
an area where AWS Professional Services or an AWS Partner may be able to add
significant value until your technical teams are familiar with the technologies involved.

**A net new deployment with existing EUC skills, but no prior cloud
infrastructure skills**

Teams need to be trained, and they should iteratively maintain their skills in AWS
core competencies such as cloud delivery, compute, networking, and storage. Focus on
understanding the core tenets of cloud delivery such as reducing costs, increasing
scalability and resilience, and taking advantage of the global reach of AWS Cloud
services.

Teams should still be trained on and exposed to Amazon WorkSpaces and WorkSpaces Applications, but
technical teams with prior experience deploying and managing EUC solutions will find this
relatively straightforward.

**Migration from an on-premises deployment of an existing vendors EUC
solution**

Teams need to be trained, and they should iteratively maintain their skills in AWS
core competencies such as cloud delivery, compute, networking, and storage. Focus on
understanding the core tenets of cloud delivery such as reducing costs, increasing
scalability and resilience, and taking advantage of the global reach of AWS Cloud
services.

Teams should still be trained on and exposed to Amazon WorkSpaces and WorkSpaces Applications, but
technical teams with prior experience deploying and managing EUC solutions will find this
relatively straightforward.

Pay particular attention on the training and preparation needed to accommodate the
differences between the incumbent solution and the way AWS EUC services are deployed and
managed. Differences in image lifecycle management, application delivery, user access and
peripheral support will be key.

**Migration from an existing cloud or hybrid deployment of EUC
services**

Technical teams with existing expertise deploying cloud solutions from other vendors
will have transferrable skills that shortcut training requirements. While AWS Cloud and
EUC service training will still be required, the time to absorb and apply this knowledge
will require less time and effort.

Pay particular attention on the training and preparation needed to accommodate the
differences between the incumbent cloud and EUC solutions and the way AWS Cloud and EUC
services are deployed and managed.

While Amazon WorkSpaces and WorkSpaces Applications deliver standard Windows desktops and applications,
which are created, managed, and maintained in a similar way to many other EUC and VDI
systems, there are a few specific differences that need to be considered:-

**Amazon WorkSpaces and Amazon WorkSpaces Applications service specifics**

Amazon WorkSpaces and Amazon WorkSpaces Applications are fully managed services, meaning that there is
no customer access to the control plane. While this reduces control plane hardware
requirements and simplifies deployment, there are some specific differences that need to
be considered:

- **Connectivity**: User connectivity to each of the
services is typically through an AWS-controlled point of presence on the public
internet. Both streaming authentication and streaming traffic are delivered in this
fashion. For Amazon WorkSpaces Applications, streaming traffic can be routed to a
customer-configured VPC endpoint.

[WorkSpaces Applications Interface VPC Endpoints](https://docs.aws.amazon.com/appstream2/latest/developerguide/interface-vpc-endpoints.html)

- **Compute instances**: Amazon WorkSpaces and Amazon WorkSpaces Applications
instances are a specifically engineered version of equivalent EC2 instances. As a
result, the storage and networking configuration is subtly different.
- **Instance availability**: Customers already familiar
with the AWS Cloud and Amazon EC2 may be accustomed to a large selection of available
instance types. While Amazon WorkSpaces and Amazon WorkSpaces Applications offer a range of compute
instances to deliver most typical EUC use cases, these are only a subset of the
instance types available on EC2.
- **Cost management**: Minimizing cost is a key
consideration for most customers when adopting AWS EUC services. All personnel
involved in deploying, managing, and maintaining the environment need to adopt a
mindset that active resources add to the solution costs. For example, optimizing the
running mode of WorkSpaces (Always-On or AutoStop), and managing the scale up and down
policies and running mode for WorkSpaces Applications (Always-On or On-Demand) verifies that you
are managing costs effectively.

Both WorkSpaces and WorkSpaces Applications have cost optimizers that can be used to reduce costs by
automating the shutdown or running mode of compute resources:

- [Cost Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/)
- [Cost Optimizer for Amazon WorkSpaces Applications](https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2)
- [Cost Optimization for WorkSpaces Applications
Fleets](https://aws.amazon.com/blogs/desktop-and-application-streaming/optimizing-costs-using-amazon-appstream-2-0-fleet-options/)

**Amazon WorkSpaces and WorkSpaces Applications targeted training**

While a basic knowledge of AWS services, such as deploying VPCs, subnets,
networking, and storage, is required to deploy AWS EUC services, the following training,
specific to AWS EUC services, is also available:

- [An Introduction to AWS End User
Computing](https://explore.skillbuilder.aws/learn/course/external/view/elearning/504/introduction-to-aws-end-user-computing-services)
- [Amazon WorkSpaces Primer](https://explore.skillbuilder.aws/learn/course/external/view/elearning/517/amazon-workspaces-primer)
- [Amazon WorkSpaces Deep Dive](https://explore.skillbuilder.aws/learn/course/external/view/elearning/1723/amazon-workspaces-deep-dive)
- [Amazon AppStream Primer](https://www.aws.training/Details/Curriculum?id=67990&redirect=false)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops09-bp02.html*

---

# EUCOPS10 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS10-BP01 Encourage user participation during service development and rollout to maximize engagement and project success

Encourage users to participate in online and in-person training for any new service to
promote trust in the new service, increase employee engagement, and reduce support
overheads.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Following the design and initial implementation of a new AWS EUC service, implement
a structured plan to train and prepare users impacted by the introduction of the new
service prior to production launch.

Provide timely and effective user training to avoid overwhelming support teams during
rollout, identify usability issues, and promote employee engagement. If users are
well-educated in the use of new systems, the chances of project success are enhanced.

Many approaches can be taken to provide users with the knowledge they need to adapt
to a new environment, including:

- **Rollout communication**: As the date for production
rollout becomes imminent, keep users up to date with plans and changes to build trust.
Use collaboration tools such as Microsoft Teams, Cisco Webex, Zoom, or a series of
lunch and learn activities, for example, to communicate planned changes to your user
population.
- **Key users**: After a solution is designed and initially
deployed, initiate a pilot production phase. During this period, provide access
limited key user access to the new systems to test the new services, verify that
desktops and applications are delivering the expected functionality and performance,
and check that peripheral devices and user data access are working as expected.
- You can also use your key users when a full production rollout is underway to
assist with deskside or departmental support, as they will already be well versed in
your new AWS EUC services.
- **Face to face**: If there will be significant changes to
the way desktop and applications are delivered, or if the functionality of familiar
applications will change due to upgrades or replacement, plan formalized face to face
training for groups of users to provide them the opportunity to use the new services
in a controlled environment. Verify that experience trainers or key users are in
attendance and provide space to ask relevant questions.
- **Floor walking**: For office-based employees, provide
floor walkers for the first few days of a deployment who can react and respond to user
questions. This process is a great way to build trust and engagement with the user
population.
- **Online or web-based**: Develop web-based training
materials that allow users to consume training at a more convenient time if your user
working patterns are unpredictable. Online training is also a good way to augment face
to face training, as users can reinforce their skills and return to the courses when
needed. Issuing certificates and small incentives to complete training courses is also
a good way of building employee engagement and confidence in a new desktop and
application deployment.
- **Frequently asked questions (FAQ)**: An FAQ is a
well-established and highly successful way of allowing users to help themselves,
reducing support calls and wait times for users with more complex issues. Gather a
comprehensive list of the most common support questions at the pilot phase as key
users start to use the new systems and add to it as you identify and resolve new
common issues. Deliver the FAQ as a web page to allow the information to evolve
quickly and be immediately available for consumption.
- **Chatbot:** With the evolution of AI/ML and generative
AI, delivering an interactive user support capability may be possible for larger
deployments. There are many services like Slack, Microsoft Teams, or [Amazon Q](https://aws.amazon.com/q/) that can accelerate the delivery of online
assistance.

People consume and retain information in different ways. Offering them varied and
complementary ways to build their knowledge of new and improved desktop and application
delivery services contributes to a more engaged workforce and a successful deployment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops10-bp01.html*

---

# EUCOPS11 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS11-BP01 Create EUC health metrics that allow you to meet your operational goals

Spend time reviewing the available metrics which provide quick and insightful
information into the health of your end-to-end EUC deployment.

**Level of risk exposed if this best practice is not
established:** High

## Implementation Guidance

While the tools and processes required to monitor AWS EUC service health are
discussed earlier, from an operational perspective there are key metrics which, at a
minimum, should be gathered to build a baseline for systems health across the tiers of an
Amazon WorkSpaces or WorkSpaces Applications deployment.

The following guidance discusses both the service specific metrics which should be
gathered in addition to the monitoring other key services which contribute to AWS EUC
service:

**Amazon WorkSpaces and WorkSpaces Applications Service or Instance metrics**

Insight into both service level and instance-based performance metrics are key to
identifying availability problems, performance problems or trends and to provide data for
retrospective problem analysis. Consider gathering the following data, at a minimum, in
order to maximize service efficiency and performance:

**Amazon WorkSpaces:** Amazon CloudWatch provides an automatic dashboard
which gives an overview of overall service health for Amazon WorkSpaces, including:

**Service metrics:**

- Available or unhealthy WorkSpaces
- Session launch times
- Connection success or failure
- Session latency
- Users connected, disconnected, stopped, or in maintenance

**Instance metrics:**

- In-session latency
- Network nealth
- CPU usage
- Memory usage
- Root or user volume space usage

Custom dashboards can also be created which use these metrics to focus on a specific
subset of your WorkSpaces.

- [Monitor WorkSpaces
Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-monitoring.html)
- [Monitor your WorkSpaces using CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html)
- [Creating Custom CloudWatch dashboards for Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-custom-amazon-cloudwatch-dashboards-and-widgets-for-amazon-workspaces/)

CloudWatch Alarms can also be configured to send alerts when specific thresholds are met.
For more information, see [Creating CloudWatch
Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).

**Amazon WorkSpaces Applications:** Amazon CloudWatch provides an automatic
dashboard which gives an overview of overall Amazon WorkSpaces Applications service health,
including:

**Service metrics:**

- Fleet capacity or utilization
- Insufficient capacity errors
- Average actual capacity
- Average available capacity
- Average desired capacity
- Average in use capacity
- Average pending capacity

For multi-session AppStream deployments, additional performance metrics can be viewed
for each instance or session, these metrics will also be available for single session
fleets over time.

**Instance metrics:**

- Instance CPU utilization
- Instance memory utilization
- `PagingFileUtilizationInstance`
- Instance disk utilization

**Session metrics:**

- Session CPU utilization
- Session memory utilization

For more information, see [Viewing Instance and Session Performance Metrics Using the Console](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-instance-session-performance.html).

CloudWatch Alarms can also be configured to send alarms when specific thresholds are met.

- [Using Amazon CloudWatch
alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [Monitoring Amazon WorkSpaces Applications Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html)

**Other key areas to monitor**

The following services, and associated metrics, at a minimum, should be monitored in
order to understand the end to end health and performance of AWS EUC services.

**Networking**

With any cloud hosted desktop and application delivery service such as Amazon WorkSpaces or
Amazon WorkSpaces Applications, users are connecting from a remote location, across a variety of
network types, to a service running in a cloud data center. Once they are connected and
logged in, they are dependent upon a number of backend services which are also connected
to the AWS EUC service using a variety of devices which each have their own performance
characteristics. Each part of the connection process and subsequent interaction with
backend services should ideally, be monitored.

**User endpoint device to AWS EUC service**

The following articles discuss the latency and bandwidth requirements for Amazon WorkSpaces
and Amazon WorkSpaces Applications and tools that can be used to validate service performance:

- [Client
network requirements for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-network-requirements.html)
- [AppStream Latency: Bandwidth Recommendations](https://docs.aws.amazon.com/appstream2/latest/developerguide/bandwidth-recommendations-user-connections.html)
- [Measuring Client to
AWS EUC region latency](https://clients.amazonworkspaces.com/Health.html)
- [Visualizing WorkSpaces Applications session latency metrics using AWS Lambda, Amazon Kinesis Data
Stream and Amazon OpenSearch Service](https://aws.amazon.com/blogs/desktop-and-application-streaming/visualizing-appstream-2-0-session-latency-metrics-using-aws-lambda-amazon-kinesis-data-stream-and-amazon-opensearch-service/)
- [CloudWatch Internet
Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)
- [Utilizing CloudWatch Internet Monitor with Amazon WorkSpaces Personal](https://aws.amazon.com/blogs/desktop-and-application-streaming/utilizing-cloudwatch-internet-monitor-with-amazon-workspaces-personal/)

**AWS EUC compute instance to backend services:**

Consider deploying third party tools which proactively monitor client to server
operations such as network flow between WorkSpaces, WorkSpaces Applications and supporting databases,
data feeds, web servers and file or print services. These data points can be used to
accurately determine service degradation or trends which might identify the need to scale
supporting infrastructure service up or down.

**AWS EUC compute instance to externally hosted services:**

While there are no simple ways to individually gather the performance of compute
instance to external service metrics, many third-party cloud providers provide API's which
can be leveraged to determine service status. Both Microsoft and Google for example,
expose API's that can be used to query individual cloud service availability. It should be
possible to architect a centrally hosted solution which pools key external resources and
uses the metrics gathered to align with internal service availability

**Backend service availability:**

Consider using network analysis tools which can identify the reachability of key
services using ICMP, TCP or application layer health probes. For Amazon WorkSpaces and Amazon
AppStream which are dependent on low latency and available bandwidth, built in client-side
network health tools will identify and notify the end user of performance degradation. In
general, the ability to identify performance baselines for network packet flow is crucial.
This applies to various supporting network infrastructures, including AWS-specific
connections through Direct Connect, as well as connections to and from third-party cloud
infrastructures.

**Storage**:

As discussed previously, both Amazon WorkSpaces and AppStream provide metrics which can
trigger alarms based on certain thresholds such as if disk space is running low, but these
do not include storage performance metrics. As part of your scalability testing during
adoption of AWS EUC services, consider testing disk performance if your application
workload is particularly disk i/o intensive. Some WorkSpaces and AppStream instance types are
'EBS Optimized' offering scalable disk throughput, for both services, GPU enabled
instances offer the highest throughput and additional instance storage. The DISKSPD
utility from Microsoft can be used to create synthetic disk i/o profiles for testing
purposes.

- [Amazon EBS
Optimized Volumes and Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#ebs-optimization-support)
- [Instance store temporary block storage for EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Microsoft: Use DISKSPD to test workload storage performance](https://learn.microsoft.com/en-us/azure-stack/hci/manage/diskspd-overview)

If specific issues arise that require deeper insight into Amazon WorkSpaces or Amazon
WorkSpaces Applications storage performance, consider using Windows Task Manager or Performance
Monitor, or iostat/iotop for Linux instances, to better understand disk i/o performance.

**Active Directory**

Active Directory performance is key to the user experience of Amazon WorkSpaces and AppStream
2.0 users as it directly affects the logon process. A badly performing Active Directory
infrastructure may add significant logon time as Group Policies and Logon Scripts are
processed. If AWS Managed Microsoft AD is being used, CloudWatch can be used to provide insights into
directory performance. For EC2 hosted domain controllers, CloudWatch can also be used to gather
most of the metrics required to identify service degradation. For on-premises AD
controllers, CloudWatch agents can be installed to centralize the collection of appropriate
metrics, such as CPU, Memory, disk I/O and network utilization.

For more information, see [Performance tuning for Active Directory Services](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/).

**SAML 2.0**

SAML integration with AWS EUC services is typically provided by external providers
such as Azure AD, Okta or Ping Identity. These systems usually provide an API which can be
used to extract service level heath metrics for propagation into an existing SIEM system.
Azure Monitor or the Okta System Log API, for example, can be used to understand
availability and performance.

**Certificate-based authentication (CBA)**

If end-to-end single sign-on is required for Amazon WorkSpaces or WorkSpaces Applications deployments
which are integrated with SAML, CBA can be used to emulate a virtual smart card login for
each user. While falling back to a standard AD username and password login is possible if
CBA is unavailable, if you do not elect to use this option it will be essential to
implement monitoring for CBA to avoid login failures. The AWS Private Certificate Authority is a resilient service
by default and presents operational metrics through CloudWatch:

- [Monitor
AWS Private CA with CloudWatch Events](https://docs.aws.amazon.com/privateca/latest/userguide/CloudWatchEvents.html)

As certificate-based authentication relies upon a private certificate authority (PCA)
which in turn requires a Microsoft Certificate Service infrastructure, refer to the
following documentation to understand which key metrics should be monitored:

- [Microsoft: Securing PKI: Appendix A: Events to Monitor](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn786423(v=ws.11))

**Network file services**

Amazon WorkSpaces Applications and WorkSpaces are typically integrated with backend network file
services which provide storage for user data and user profiles. These repositories are
typically critical to employee productivity and should form part of end-to-end service
monitoring. If Amazon FSx for Windows is being used for backend storage, a comprehensive
CloudWatch dashboard is available which exposes system performance. If traditional Windows file
servers are being used in EC2 or on-premises, Microsoft provides direction on how to use
the SMB performance metrics to gather the relevant performance statistics.

- [Monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-cloudwatch.html)
- [Performance tuning for SMB file servers](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/role/file-server/smb-file-server)

**RADIUS**

If RADIUS is being used with Amazon WorkSpaces, the documentation for the RADIUS provider in
use should be consulted as these can be Windows or Linux based and will expose performance
metrics in different ways.

**Application web tiers**

Availability and performance of web tiers that support the applications being
delivered from AWS EUC services is typically controlled by load balancers than can also
execute L2, L4 or L7 health probes to ascertain service health and optionally perform
auto-scaling if required. Refer to your web server vendors documentation for information
on monitoring your specific web tiers.

**Application database tiers**

Availability and performance of database tiers that support the applications being
delivered from AWS EUC services is also key to end-to-end service health. Refer to your
web server vendors documentation for information on monitoring your specific web tiers.

**Application licensing servers**

Monitoring license server availability and performance is critical as failure of
these servers can result in complete denial of service for a specific application tier.
Please refer to your license server or application vendors documentation for information
on monitoring these components.

**Web proxies or app firewalls**

Web proxy and app firewall tiers are typically load balanced and auto scaled for
resilience and scalability, but monitoring these is important as failure of this tier can
result in users being denied Internet access, the impact of which can be significant.
Please refer to your web proxy vendor documentation for information on monitoring these
components.

**Anti-virus infrastructure**

While anti-virus and anti-malware products are unlikely to cause systems outage, from
a security perspective, being sure that Amazon WorkSpaces and WorkSpaces Applications instances are being
effectively protected can avoid wider service outage due to intrusion and malign
interference from external bad actors. Furthermore, understanding and minimizing the
impact of anti-virus and anti-malware scans, is key.

**WorkSpaces and WorkSpaces Applications instance metrics**

Amazon WorkSpaces and WorkSpaces Applications compute instances are standard Windows Client/Server, or
Linux instance types. They each have a network interface exposed to a customer managed VPC
and can be managed and monitored in the same way as traditional desktops.

Amazon CloudWatch can be used to extract instance specific metrics such as CPU, Memory, Disk
or Network utilization, and existing third party tools can be used to extract similar
information.

Be aware that as WorkSpaces Applications is a non-persistent application and desktop delivery
service, instances are terminated and destroyed when the last user session is ended
(consider single session versus multi-session), this needs to be considered when gathering
performance statistics or system logs.

There are a number of utilities created by AWS employees that assist in the
gathering and presentation of AWS EUC instance metrics, the EUC Toolkit for example, can
be used for this purpose, the PowerShell code for this utility can also be downloaded and
used as a reference for building your own PowerShell management utilities.

- [Monitor your WorkSpaces using CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html)
- [Monitoring and Reporting for Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-monitoring-reporting.html)
- [Monitoring Amazon WorkSpaces
Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/monitoring-overview.html)
- [Use
the EUC Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/)

In summary, AWS EUC deployments are dependent on the reliability and performance of
both the Amazon WorkSpaces or WorkSpaces Applications services themselves and also many external systems,
taking a holistic approach to management of each component of the end to end deployment is
key to maintaining end user engagement and productivity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops11-bp01.html*

---

# EUCOPS12 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# EUCOPS12-BP01 Deploy alerting mechanisms that quickly identify anomalous metrics

AWS EUC services provide access to desktops and applications which can be highly
variable in their resource requirements over time. Weekly, monthly, quarterly, and year-end
activities can cause spikes in resource consumption that might result in unnecessary alerts
and a degraded user experience.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

The design and pilot phases of an AWS EUC project should identify resource
requirements for each application set over a typical business cycle. Identify the peak
activity levels to verify that the compute instance types selected for both Amazon WorkSpaces and
WorkSpaces Applications can deliver performance that maintains a good user experience and improves
productivity.

Third party tools from vendors such as ControlUp, Nuvens, LiquidWare, Lakeside
Software, and Aternity can be used to collect resource usage trends and build baselines
for key applications. Some of these can be found on the AWS Marketplace.

AWS and the AWS Partner Network offer many services and automation capabilities you can use
to automatically and elastically scale backend application services or to provide
increased compute capabilities during periods of heavy utilization**.**

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops12-bp01.html*

---

# EUCOPS12-BP02 Define and maintain an alerting chain of command that quickly communicates issues in real time

As important as gathering relevant service metrics and alerts is expediting the
propagation of those alerts to the right teams, individuals, or automated processes. This
propagation helps you quickly surface and remediate associated issues.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Accelerate the awareness of key events, and check that the notification to initiate
the appropriate process of remediation is quickly followed.

There are several ways to verify that both operations and support teams in addition
to internal and external users and management teams are appraised of service health:

- **Health dashboards**: Build a set of centralized service
health dashboards that are tailored to provide the right information to the right
people from operations, support, users, or management. Dashboards help your teams
quickly identify and track issues to resolution. User-level dashboards promote
transparency, reduce support calls, and increase user engagement as new production
services are introduced.
- **Effective communication**: Develop a communications
protocol to effectively communicate about extended outages as they are identified to
internal and external customers. Keeping customers informed, specifically around
outage timelines, is key to building trust and engagement.
- **Effective routing**: Automate the process of
prioritizing and effectively routing the right alerts to the right teams at the right
time, which increases operational efficiency and contributes to an improved user
experience and higher productivity.
- Consider the following factors when identifying roles and responsibilities for
event response, escalation, and propagation:

**Roles and responsibilities**: Define clear lines of
responsibility for escalation, problem resolution, and root cause analysis.
- **Incident assignment**: Identify alert categories so
that specific events can be directed to the team most appropriate to resolve. For
example, first, second, and third lines of support.
- **RPO and RTO requirements**: Involve the business in
understanding and calculating RTO and RPO requirements to prioritize problem
tracking and remediation accordingly.
- **Cost of outages**: Quantify the cost to the
business of specific categories of outage and use this data to inform the
escalation and notification process. It may be pertinent to revise support
processes to involve more skilled support teams to react to specific event types
that have higher business impact.
- **Tool**s: Map out a matrix that identifies the right
tools, metrics, and notification processes to verify that critical events are
surfaced and distributed effectively to the appropriate teams and individuals.
- **Alert fatigue**: Filter out duplicate alerts and
false positives, as they can lead to alert fatigue and loss of focus on important
issues.
- **Geographic reporting**: For multi-Region
deployments, dynamically adjust notification distribution lists to accommodate
support in applicable time zones and geographic areas.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops12-bp02.html*

---

# EUCOPS13 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS13-BP01 Perform regular service reviews to identify significant trends in performance, scalability, and availability

Perform regular reviews of service performance and capabilities to maintain visibility
of key issues and focus on service improvement and readiness.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

While real-time monitoring and alerting is essential in meeting business and
technical SLAs with internal and external customers, performing periodic review of logfile
and monitoring data can help to identify problem trends and to put in place remediation
steps to avoid future outages.

Along with incumbent monitoring tools, you can use Amazon CloudWatch and Amazon Kinesis to centrally
store data to use for retrospective performance and systems health analysis.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops13-bp01.html*

---

# EUCOPS14 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS14-BP01 Ingest log file data from multiple data sources to correlate key problem identifiers and trends

Identify and implement mechanisms to maintain a centralized source of EUC service data
that can be used for root cause analysis of cross service issues.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Store logs and metrics from AWS EUC services and their dependent services in a
centralized location to allow analysis tools to build a picture of cross system failures
that are affecting AWS EUC reliability. For example, expiry of a critical SSL
certificate on a load balancer or remote access tier may be the root cause of login
degradation or other failures at the AWS EUC service tier.

Use Amazon CloudWatch to gather metrics and logs, which are stored for subsequent analysis, to
identify problems or trends that have occurred over time.

Amazon Kinesis agents can be installed onto Amazon WorkSpaces or WorkSpaces Applications images to export log
file data in real time to a centralized location for retrospective analysis.

For larger environments, consider creating a data lake of key data from system logs,
performance monitoring, and security tools across all service lines. Develop analysis
capabilities using Amazon AI/ML tools to generate a more holistic insight into end to end
systems health and scalability.

Note
Review CloudWatch and Kinesis data retention policies and service charges to verify that
data availability and costs are within EUC project guidelines.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops14-bp01.html*

---

# EUCOPS15 — Evolve

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS15-BP01 Update your solution design documentation over time, and use version control to track changes

Keep key architectural designs, operations handbooks, and support guides up to date,
maintaining a library of reference material that can be used by new personnel, partners, or
other support teams.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

For both Amazon WorkSpaces and WorkSpaces Applications, each service should have been deployed based
upon a design that resulted from the collected input of key technology and business
stakeholders. Evolving the solution design should be managed in a similarly inclusive
fashion. Agree and sign off on all changes to the initial design through a project board
before updating the solution. This approach verifies that invested parties have validated
the key metrics required to deliver the new service and that the updated solution meets
the requirements of both technical and business stakeholders.

Design documentation should be maintained as continually updated documents that
represent the state of the AWS EUC service deployments over time. It should capture the
rationale for each design decision in addition to the technical and architectural
solutions deployed to achieve each requirement. Maintain iterative versions of the design
as changes are made so that you can see a historical view of the deployment.

A design document is an essential piece of knowledge collateral which is invaluable
for training purposes, onboarding new technical team members, reviewing and implementing
changes to the infrastructure, and when working with partners to integrate new
technologies or handover support to new teams.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops15-bp01.html*

---

# EUCOPS16 — Evolve

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS16-BP01 Implement automated processes to verify that service updates can be repeatably deployed, updated, and rolled back

Selecting an automation toolset and defining the processes that facilitate repeatable,
predictable delivery and maintenance of AWS EUC services is key to achieving simplified
administration, reduced support overheads, end user satisfaction and positive business
outcomes.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Although Amazon WorkSpaces and Amazon WorkSpaces Applications are fully managed services, there are a
number of touch points when maintenance the associated infrastructure and the desktop and
applications delivered by the service requires periodic updates.

Every AWS EUC environment is unique. Verify that you understand each area of your
AWS EUC deployment that may need to be updated over time and develop a formalized plan
on how each of these areas need to be managed.

The following questions and discussions can provide you steps for improvement.

**What updates are required?**

- **Amazon WorkSpaces**: For WorkSpaces, the custom bundles created to
deliver persistent desktops to users will require updates over time in the form of
operating system patches, hotfixes, and security and application updates. Once your
WorkSpaces have been deployed, they must be individually managed, as each WorkSpace can be
uniquely changed and reconfigured by its assigned user if they are given the
appropriate rights. The customer is responsible for making these changes. Amazon WorkSpaces
have a regular automatic maintenance schedule which keeps the WorkSpaces specific agents
aligned with the service control plane. For detail on the maintenance process for
Always-On and AutoStop WorkSpaces, see [Maintenance in WorkSpaces
Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html).
- **Amazon WorkSpaces Applications**: For WorkSpaces Applications, each private
image used to deploy a non-persistent desktop or application experience will
periodically require updates in the form of operating system patches, hotfixes, and
security and application updates. As WorkSpaces Applications instances are deployed from a
common image, only the private image for each fleet version needs to be updated. New
instances launched when users log in will automatically inherit the changes made to
the private image. The customer is responsible for making these changes.
- Maintenance of the agent software installed on each image can be automated or
controlled by the customer if specific versions are required. For more information on
the processes of maintaining agent versions for each image, see:

[Update Management
in Amazon WorkSpaces Applications PDF RSS Focus mode](https://docs.aws.amazon.com/appstream2/latest/developerguide/update-management.html)
- [Manage AppStream
2.0 Agent Versions](https://docs.aws.amazon.com/appstream2/latest/developerguide/base-images-agent.html)

- Amazon WorkSpaces Applications also offers an application delivery option called elastic
fleets that you can use to quickly deploy and manage portable applications. For more
information, see [Applications
Manager](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks-applications.html).

**How do you manage updates?**

Creating and delivering updates that are consistent and repeatable is the best way of
reducing problems and frustration for users when configuration changes are made to the
workloads delivered by AWS EUC services. You can use software deployment tools to build
new software packages, perform unit and interoperability testing, and roll out or roll
back changes without touching each desktop or application server individually. This form
of automation drastically reduces the chance of human error and configuration drift across
large desktop and application estates, saving on support costs, reducing downtime, and
maximizing productivity.

- **WorkSpaces**: Workspaces provides a management console and a
corresponding API, which can be used to create and configure new WorkSpace bundles.
Once created from a custom bundle, each WorkSpace is persistent but decoupled from the
custom image and requires discrete management and maintenance.
- To update existing WorkSpaces, use the customer-facing network interface attached to
each WorkSpace to integrate with software deployment toolsets such as AWS Systems Manager or
existing on-premises tools such as Microsoft Endpoint Configuration Manager (MECM),
Puppet Enterprise, or Ansible.

[Software deployment to Amazon WorkSpaces using AWS Systems Manager](https://aws.amazon.com/blogs/mt/software-deployment-to-amazon-workspaces-using-aws-systems-manager/)
- [Automatically create customized Amazon WorkSpaces Windows images](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-create-customized-amazon-workspaces-windows-images/)

- **WorkSpaces Applications**: WorkSpaces Applications provides a management
console and a corresponding API, which can be used to automate the delivery of an
image builder that updates each version of a private image. As the image builder has a
network interface in a customer-managed VPC, traditional software distribution tools
and automation frameworks can also be used to push updates to this instance from where
a new version of an image is created and assigned to fleets.
- WorkSpaces Applications also offers an automated option called Managed Image Updates, which
automates and simplifies the process of updating AppStream agent software and OS
patches. For more information, see the following:

[Administer Your Amazon WorkSpaces Applications Images](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html#keep-image-updated-managed-image-updates)
- [Automatically create customized WorkSpaces Applications Windows images](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-create-customized-appstream-2-0-windows-images/)
- [Automate the creation of WorkSpaces Applications resources using AWS CloudFormation](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation.html)

**How will you test and validate updates?**

- **WorkSpaces**: Before production rollout, any OS or
application updates need to be tested on a WorkSpace created from the same custom
bundle as the WorkSpace group being updated. Several custom bundles may exist with
different application combinations that need to be independently tested. Once testing
is complete, you can roll out changes to each WorkSpace created from the initial
custom bundle, either manually or using automation tools such as Microsoft WSUS or
Microsoft MECM (SCCM).
- If WorkSpace users have been given full administrative access to their desktop,
it is possible that they may have updated their WorkSpace OS or application
independently, making the process of applying consistent, reliable updates across the
WorkSpace estate challenging. Unless strictly necessary, we don't recommend allowing
users to update their own WorkSpaces.
- Should an update fail, a snapshot of the two WorkSpaces storage volumes is taken every
12 hours, which may provide a recovery position. WorkSpaces can be rebuilt or [recovered](https://docs.aws.amazon.com/workspaces/latest/adminguide/restore-workspace.html). For more information, see [Rebuild a WorkSpace in
WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/rebuild-workspace.html).

For more flexible backup and recovery options, consider using traditional backup and
recovery tools and techniques, or consider [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html).

- **WorkSpaces Applications**: As WorkSpaces Applications delivers tens,
hundreds, or thousands of instances from a common private image, testing can be done
by creating a single instance test or development fleet from a new version of an
image, allowing administrators to fully test changes before assigning the image to a
production fleet and making it available to users.
- Multiple fleets or fleet versions can be created from a private image, allowing
administrators to roll forward or roll back to a known operational state if problems
occur. Multiple versions of an image can also be deployed in parallel if extended user
testing is preferred.

**How do you track changes and manage releases?**

Track specific changes to your AWS EUC environments by date and time to maintain a
paper trail that can be used to pinpoint and cross reference if a specific change was
responsible for a positive or negative change in functionality or performance. For
example, creating a retrospective back-out or remediation plan in the event of an issue
that occurs days or weeks after a change is made to the environment will be much easier if
comprehensive change management is observed.

For both Amazon WorkSpaces and Amazon WorkSpaces Applications specifically, adopt a version numbering
scheme and capturing a log of changes made to each custom bundle or private image to trace
issues back to a specific image version, if required.

You can use AWS CloudTrail to log API calls used to make changes to both Amazon WorkSpaces and
WorkSpaces Applications environments.

- [Logging
WorkSpaces Applications API calls with AWS CloudTrail](https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-using-cloudtrail.html)
- [Logging WorkSpaces API Calls by Using CloudTrail](https://docs.aws.amazon.com/workspaces/latest/api/cloudtrail_logging.html)

**Automating changes to Amazon WorkSpaces and Amazon WorkSpaces Applications**

By using automation, you can avoid many of the configuration drift and image
consistency problems seen with manual deployments. The following articles provide some
options for automating the creation and management of AWS EUC services.

- [Automating the provisioning of AWS WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/automate-provisioning-of-amazon-workspaces-using-aws-lambda/)
- [Automatically create customized WorkSpaces Applications Windows images](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-create-customized-appstream-2-0-windows-images/)
- [Best practices for automating your AWS End User Computing deployments](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0210-EUC_Slide-Deck.pdf)
- [Amazon WorkSpaces and WorkSpaces Applications Terraform Resources](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Deploying and Managing Amazon WorkSpaces applications with Ansible](https://aws.amazon.com/blogs/desktop-and-application-streaming/deploying-and-managing-amazon-workspaces-applications-with-ansible/)
- [DXC Technology creates DevSecOps and CI/CD for mainframe and Java using Amazon
WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/dxc-technology-devsecops-cicd-mainframe-amazon-appstream-2-0/)
- [Announcing the Amazon WorkSpaces dynamic inventory plugin for Ansible®](https://aws.amazon.com/blogs/desktop-and-application-streaming/announcing-the-amazon-workspaces-dynamic-inventory-plugin-for-ansible/)
- [Terraform resources for AWS WorkSpaces](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/workspaces_workspace)
- [Automation of infrastructure and application deployment for Amazon WorkSpaces Applications
with Terraform](https://aws.amazon.com/blogs/desktop-and-application-streaming/automation-of-infrastructure-and-application-deployment-for-amazon-appstream-2-0-with-terraform/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops16-bp01.html*

---

# EUCOPS17 — Evolve

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS17-BP01 Provide time and resources for your teams to keep up to date with changes and feature updates

Provide ongoing training to keep key personnel up to date with changes that are
occurring in the industry and specifically in their domain of expertise.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Take advantage of new and improved capabilities of Amazon WorkSpaces and WorkSpaces Applications
services and deploy new updates to deliver incremental features and performance for your
desktops and applications delivered by those services. Staying up to date is key to
deliver business outcomes that provide a competitive advantage.

Perform periodic reviews of new service capabilities and improvements in desktop and
application delivery to maximize your investment.

You can continually improve service for Amazon WorkSpaces and WorkSpaces Applications in many ways,
including:

- **New features**: Identify, test, and implement new
service features that provide added value in order to deliver incremental end user and
customer benefits, sometimes at zero cost. Follow the [AWS Desktop and Application
Streaming Blog](https://aws.amazon.com/blogs/desktop-and-application-streaming/) to stay updated on the latest developments in this
area.

**Patching**: Regularly apply operating system patches,
hotfixes, and important updates to both the operating system and applications to avoid
known issues and vulnerabilities, which helps you avoid costly service outages.
- **Performance**: Periodically review performance logs to
scale your environment cost effectively and maintain a compelling user or customer
experience.
- **Service review**: Periodically review all support
tickets related to the AWS EUC deployment to understand root cause and identify
problem trends, helping you avoid future outages and associated costs.
- **Change management**: Involve your AWS EUC team in the
change board for all dependent technology areas (such as compute, storage, networking,
and security). Provide visibility of changes in other technology domains to guide and
inform improvements in the delivery of desktops and applications.
- **Industry awareness**: Attend key EUC industry events to
identify new industry trends and partners who provide added value. The opportunity to
attend industry events is also an opportunity to meet other users of AWS EUC
services and learn from their valuable experiences.
- **Expert roundtables**: Promote the use of and
participation in regular expert roundtables where technology teams can present
improvements and advances across diverse areas of expertise. This helps the EUC team
identify where they can apply improvements in other areas to improve AWS EUC service
delivery.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops17-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
