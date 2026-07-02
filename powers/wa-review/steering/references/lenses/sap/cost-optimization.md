# Cost optimization

**Pages**: 22

---

## 17 – Evaluate SAP architecture patterns for cost efficiency

# Best Practice 17.1 – Evaluate your use of SAP managed service offerings

Per the AWS shared responsibility model, the customer has the responsibility of
managing their SAP workloads on AWS. Optionally, a service provider can be used to
manage your SAP workloads on AWS. When evaluating a service provider, the responsibility
of both upfront and ongoing cost management should be delegated appropriately and should
be treated as an ongoing process.

**Suggestion 17.1.1 – Evaluate and understand available managed service
offerings**

A number of AWS and SAP partners provide services for the deployment and operation
of your SAP landscape. The scope and maturity of services provided varies across partners.
These types of services can provide efficiencies, for example, centralized support, bundled
licenses, or automated deployment services. These can reduce your overall costs and should
be evaluated based on your specific business requirements. Evaluate partners for AWS
competencies including those with the [AWS SAP Competency](https://aws.amazon.com/sap/partner-solutions/) or belonging to the AWS Partner Network (APN).

SAP offers [RISE with SAP](https://www.sap.com/products/rise.html), a
single-tenant, SAP-managed S/4HANA solution that also includes SAP Business Technology
Platform (BTP) and other SAP software in a single contract. AWS supports customer choice
and hosts many customers on the SAP RISE platform. SAP RISE can be hosted on AWS and
combined with SAP BTP on AWS and other AWS workloads. When choosing AWS for RISE and
BTP, you have options to simplify the architecture, improve connectivity, improve security,
and reduce costs.

- AWS Blog: [Your ERP environment, your choice: RISE with SAP presents another ERP modernization
path for AWS customers](https://aws.amazon.com/blogs/awsforsap/your-erp-environment-your-choice-rise-with-sap-presents-another-erp-modernization-path-for-aws-customers/)
- AWS Blog: [How to connect SAP solutions running on AWS with AWS accounts and
services](https://aws.amazon.com/blogs/awsforsap/how-to-connect-sap-solutions-running-on-aws-with-aws-accounts-and-services/)

**Suggestion 17.1.2 – Understand the roles and responsibilities related
to cost control**

Different managed service offerings have different cost models to cover
infrastructure, licensing, and services. Decide where the responsibility for cost control
lies. The following questions can be asked as part of this process.

- Are the costs from the provider:

Based on a percentage of infrastructure spend?
- Based on an agreed total cost of ownership (TCO)?
- Variable (both up and down) according to changed business conditions?

- T-shirt sized (small, medium, large)? Is there an appropriate change control
process in place to ensure that costs are controlled and understood?
- Is there sufficient visibility and transparency of the infrastructure
costs?
- Does cost governance limit innovation and flexibility?

**Suggestion 17.1.3 – Agree on an approach to cost management and
optimization with all parties**

When evaluating the different managed service offerings available, understand the
managed services partner’s approach to cost management. How can you work together to drive
on-going cost optimization for your organization?

This evaluation should include a regular review process. It might also benefit from
incentives, such as a shared reward model, that encourage the partner to take ownership so
that both parties financially benefit from the cost savings achieved.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-17-1.html*

---

# Best Practice 17.2 – Evaluate the cost characteristics of your SAP application architecture pattern

As you develop the architecture of your SAP landscape, consider the cost of the number
of infrastructure components in addition to their size and location. By establishing the
business requirements of the solution, acknowledging risk, and finding opportunities to
optimize, you can realize significant cost savings

**Suggestion 17.2.1 – Review your selected SAP installation
patterns**

For each SAP application, define a deployment pattern, such as standalone,
distributed, or high availability (HA). Select the architectural pattern that best
balances the cost and reliability characteristics to meet your business requirements. A
useful approach is to quantify the cost of an outage to your business and work backwards
from that. Balance the risk of an individual failure impacting availability against the
cost of reducing that risk.

Additionally, consider whether your architecture has the flexibility for right sizing.
There can be cost savings with operating system licensing, storage, and managing multiple
application servers on a single host. For the application tier, instance sizes are
available with fine granularity for CPU and memory, with near linear pricing in the
supported instance families. Deploying multiple smaller instance sizes can provide more
options for instance reuse and workload-based scaling.

Evaluate logical groupings and consider the effect of combining components, systems
(SIDs), or landscapes. Would these activities increase operational complexity and decrease
reliability?

- AWS Documentation: [Architecture Guidance for Availability and Reliability of SAP on AWS](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html)
- SAP Lens [Reliability]: [Reliability design
principles](./reliability.html)
- AWS Well-Architected Framework [Reliability]: [Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

**Suggestion 17.2.2 – Evaluate exceptions for the use of multitenancy or
hosting multiple databases in a single host**

For most databases, size each system independently and take advantage of flexible
instance sizing to match requirements for those systems. In some cases, it might make
sense to deviate from that recommendation in the interest of cost. For example:

- When a HANA-based component requires less memory than the smallest EC2 instance
size available, consider the use of [SAP HANA Multitenant Database Containers](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/623afd167e6b48bf956ebb7f2142f058.html). Hosting with other components
allows for efficient use of the compute resources.
- Core-based database licensing models for relational databases, including Oracle
and SQL Server
- Applications that are, or can be, tightly coupled for uptime requirements and
version dependencies. This includes management tools (for example Solution Manager and
SAP HANA Cockpit) and some SAP NetWeaver Gateway Deployment options (Fiori and
ECC).

**Suggestion 17.2.3 – Evaluate the use of the single host installation
pattern for systems that do not require resiliency and scalability**

For individual applications or environments, you should consider the advantages of a
single host model. This can help save operating system costs, storage duplication,
software license costs, and managed service costs. Common architectural options,
particularly for non-production landscapes, include:

- Co-hosting database, application, and SAP central services
- Separate database (to minimize database licensing). Refer to [Cost Optimization]:
[Best Practice 18.3 - Evaluate licensing impact
and optimization options](./best-practice-18-3.html).
- Combined application and SAP Central Services

**Suggestion 17.2.4 – Choose the most cost-effective Region that meets
your requirements**

The primary drivers for SAP Region selection are proximity, data residency, and
service availability. For deployments where a choice exists, be aware that each AWS
Region offers pricing based on local market conditions. AWS service pricing is therefore
different in each Region. Review any price differences and their potential impact.

**Suggestion 17.2.5 – Use architectures that can be scaled in the
event of a failure**

Recovery mechanisms and the elasticity of the cloud allow for a design where redundant
resources do not need to be active and at 100% capacity. If your business requirements
allow for a more flexible RTO or RPO, consider the following.

For the database:

- If your recovery point objectives allow, consider a secondary or standby database
node that does not require equivalent compute capacity to apply changes from the
primary. With an awareness on the recovery time impact, consider the cost advantages
of deploying a smaller or shared instance for your secondary, and scale up only when
required. Use of a smaller instance maintains the 1:1 relationship between primary and
secondary system instances. A shared instance architecture pools the secondary
database with a non-replicated system database onto a single instance. In the event of
a failure, the non-replicated system must be stopped before a takeover can occur. This
will increase the RTO.
- If using a smaller instance for the secondary SAP HANA database, turn off memory
preload to accommodate a smaller memory footprint on the standby and reduce cost. SAP
estimates the memory requirements in the help document for [Secondary System Usage](https://help.sap.com/viewer/4e9b18c116aa42fc84c7dbfd02111aba/2.0.05/en-US/9d62b8108063497f9d6aab08902b2e04.html).

SUSE Documentation: [SAP HANA System Replication Scale-Up - Cost Optimized Scenario | SUSE](https://documentation.suse.com/sbp/all/html/SLES4SAP-hana-sr-guide-CostOpt-12/index.html)

- If your recovery time objective and resiliency requirements allow, consider data
and log backup approaches that use Multi-AZ storage (such as Amazon FSx, Amazon EFS,
or Amazon S3). These approaches allow for geographic protection of data without
requiring redundant secondary resources. In the event of failure, secondary resources
can be created on demand and quickly restored from cross-location backups and log
storage.

SAP on AWS Blog: [How to use snapshots to create an automated recovery procedure for SAP ASE
databases](https://aws.amazon.com/blogs/awsforsap/how-to-use-snapshots-to-create-an-automated-recovery-procedure-for-sap-ase-databases/)

For the application:

- [AWS instance recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) uses a CloudWatch alarm to monitor an Amazon EC2
instance. It automatically recovers the instance if it becomes impaired due to an
underlying hardware failure. Evaluate if the failure scenarios covered provide
sufficient protection.
- For scenarios in which an application server needs to be quickly recreated,
options include EC2 instances that are provisioned but not running, templated AMIs,
storage replication using common staging servers, or infrastructure as code
(IaC).

**Suggestion 17.2.6 – Consider the cost of minimum compute capacity
during a failure**

Distributing SAP components across Availability Zones can reduce the costs incurred
for capacity reservations in the event of failure. By distributing components across
Availability Zones, you avoid the need for excess capacity because you already have part
of your workload geographically spread. This minimizes the scope of impact in the event of
an AZ failure.

For example, if 100% capacity is an availability requirement for failure scenarios
including the loss of an Availability Zone, instead of provisioning 200% capacity across
two Availability Zones, provision 150% capacity across three.

*Example of a three Availability Zone architecture with 150% of capacity
in normal operations*

**Suggestion 17.2.7 – Evaluate the use of storage-only based recovery
options**

In general on AWS, we recommend database replication over storage replication to
ensure protection from the broadest range of failure scenarios. For the application layer
or for less critical instances, a DR solution that uses storage replication without the
need for compute can reduce costs. It also minimizes the complexity associated with
managing change.

- AWS Documentation: [AWS Elastic Disaster Recovery -
Amazon Web Services](https://aws.amazon.com/disaster-recovery/)
- AWS Documentation: [Creating backup copies across Regions - AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html)

**Suggestion 17.2.8 – Understand networking-related costs**

SAP customers often require a secure connection between their on-premises network and
Amazon VPC. Using an appropriately sized Direct Connect, a VPN connection, or both, it is
possible to meet performance and reliability requirements while minimizing cost.

Data transfer costs will be impacted by Region, VPC, and Availability Zone design.
Evaluate how the distribution and replication of your SAP components can be optimized
without compromising reliability.

For example, if two systems that transfer large amounts of data are in separate
locations, consider the impact on data transfer costs.

- AWS Documentation: [EC2 On-Demand Instance Pricing – Amazon Web Services](https://aws.amazon.com/ec2/pricing/on-demand/)
- AWS Documentation: [Architecture Patterns - General SAP Guides](https://docs.aws.amazon.com/sap/latest/general/arch-guide-architecture-patterns.html)

Further guidance can be found in the Cost Pillar of the Well-Architected Framework
Review [Plan for Data Transfer - Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/plan-for-data-transfer.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-17-2.html*

---

# Best Practice 17.3 – Understand business requirements to make cost-optimized design decisions per environment

Optimize the cost of each system or environment individually based on its differing
characteristics. Consider capacity, performance, reliability and operating hours to match
business requirements. For environments or applications that are less critical for the
experience of end users or business processes, minimize storage, compute, and operating
hours to reduce cost. Balance the cost savings of a reduced configuration with operational
requirements for testing or support.

**Suggestion 17.3.1 – Evaluate if non-production environments need a
full copy of production data**

Having full copies of production data in non-production will greatly impact your
storage and compute costs. Consider minimizing the number of copies of production data
while still meeting your testing requirements. Options to minimize costs of non-production
environment data storage include:

- Using less storage capacity for development and test systems.
- Using data slicing tools to carve out a smaller subset of test data in
non-production systems.
- Consider the use of temporary production copies. These copies can be created
on-demand and then quickly decommissioned, or archived, after the business need or
test has passed.
- Evaluate if the SAP recommendation for SAP HANA databases of 50% working memory is
required in non-production systems.

**Suggestion 17.3.2 – Evaluate if non-production environments always
need to have the same performance as production**

Non-production systems and some support systems are likely to have a smaller set of
users, handle significantly lower transaction volumes, or have flexible response time
requirements. Consider the following:

- Reducing the SAP Application Performance Standard (SAPS) for your workload by
using smaller EC2 instance types.
- Using fewer application servers.
- Using lower cost Amazon EBS storage types, for example, `gp3` instead
of `io2` .
- Using reduced performance characteristics for non-production systems volumes, for
example, 3,000 IOPS instead of 10,000 IOPS.
- The elasticity of the cloud means that you can scale up your non-production
testing resources that require production-like performance, such as load or scaling
tests.

**Suggestion 17.3.3 – Evaluate if non-production environments need the
same operating hours as production**

Non-production environments like test, training, and sandbox systems, might have
reduced operating hours compared with production. Consider time zones and the working
hours of your support teams to determine whether all systems are required 24 x 7. Use this
information to select the lowest pricing model.

For example, running your SAP training system for 40 hours a week with an on-demand
pricing model (~23% uptime) will be cheaper than running it always on at 100% with a 3-year
Reserved Instance or Savings Plan.

**Suggestion 17.3.4 – Evaluate if non-production environments
consistently need the same reliability as production**

Choose the most cost-effective architecture to match each system’s individual
reliability requirements. See [Reliability]: [Best
Practice 10.1 - Agree on SAP workload availability goals that align with your business
requirements](./best-practice-10-1.html). Further guidance can be found in the [Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) of the AWS Well-Architected Framework.

Where a production-like architecture exists solely for testing purposes, consider how
often it needs to mirror production. If database high availability is needed in a
non-production environment for reliability or performance testing, you can choose to shut
down or scale down the secondary instance outside of these testing windows to save
cost.

Cost benefits can be realized through the use of automation and by using on-demand
pricing for environments that don’t need production-like performance at all times.

**Suggestion 17.3.5 – Evaluate the business requirements for non-core
systems including support and legacy systems**

If environments exist for reference purposes only, or have a less critical business
role, evaluate the uptime, performance, and reliability requirements needed compared to
your core production systems.

For example, a legacy ERP system might require being kept for reference purposes from
a prior application conversion or business restructure. Costs for this system can be
optimized by running the EC2 instances only when required, thus only paying for Amazon EBS
storage. A more cost-effective solution could be archiving the system via backup to Amazon
S3 and Amazon S3 Glacier.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-17-3.html*

---

# Best Practice 17.4 – Review the size, granularity, and latest available EC2 instances for SAP components

Smaller EC2 instances provide greater cost flexibility in SAP workloads. They
introduce options for horizontal scaling that allow for compute to be switched off when
not in use or scaled up only during peak loads. Adopting a consistent EC2 instance size at
the application tier will help you maximize the benefits of Reserved Instance and Savings
Plans commitments across all workloads. Take into account the latest available AWS SAP
certified instances. The operational impact, license costs, support, sharing and
reusability for each component should also be evaluated.

**Suggestion 17.4.1 – Evaluate the cost benefits of multiple smaller
application servers to provide flexibility**

For many SAP workloads, application servers can be designed to be immutable. Having a
standard application server configuration, which is scaled horizontally by replicating the
base unit, gives options for consistent repeatable units. The advantages are reusability,
compute utilization, reservations, and automation. Per-unit requirements, such as
operating system licensing, storage duplication, and management costs, should be factored
into the evaluation.

Consider the following:

- SAP on AWS Blog: [DevOps for SAP – Driving Innovation and Lowering Costs](https://aws.amazon.com/blogs/awsforsap/devops-for-sap-driving-innovation-and-lowering-costs/).
- SAP on AWS Blog: [Using AWS to allow SAP Application Auto Scaling](https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/)

**Suggestion 17.4.2 – Evaluate the cost benefits of an SAP HANA
scale-out configuration where supported**

SAP OLAP workloads can be deployed in both [scale-up and scale-out](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/a165e192ba374c2a8b17566f89fe8419.html) configurations. SAP recommends to scale-up before scaling
out to reduce operational complexity. However, scale-out implementations might be applicable
for larger analytical or native SAP HANA workloads, which require significant compute
(SAPS).

In certain cases, S/4HANA also supports scale-out configuration but with
restrictions. See SAP Note: [2408419 - SAP S/4HANA - Multi-Node Support](https://launchpad.support.sap.com/#/notes/2408419) [Requires SAP Portal Access].

When considering scale-up vs. scale-out consider the following:

- [Certified EC2 instance sizes](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23;v:105) available for scale-up and scale-out
- The cost per GiB of EC2 memory for each instance family. Larger EC2 instances
typically have a higher cost per GiB than smaller instances.
- The added complexity and operational overhead of managing data distribution in
scale-out deployments. See SAP Note: [2081591 - FAQ: SAP HANA
Table Distribution](https://launchpad.support.sap.com/#/notes/2081591) [Requires SAP Portal Access]

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-17-4.html*

---

# Best Practice 17.5 – Consider using on-demand capacity to improve cost efficiency

The on-demand pricing model is suitable for SAP workloads needing reduced operating
hours, short-term projects, experimentation, or expanded capacity for small periods of
time (for example, performance testing). Determine where you can use on-demand pricing in
your SAP architecture.

**Suggestion 17.5.1 – Evaluate the use of on-demand for SAP systems
needing less than 24/7 operating hours**

Based on the break-even point between the use of on-demand and other pricing models.
(See [Reliability]: [Best Practice 18.1 - Understand the
payment and commitment options available for Amazon EC2](./best-practice-18-1.html) ), evaluate if on-demand
will provide the lowest cost. As part of this evaluation, consider the overall Savings Plan
commitment.

Common use cases include non-production systems that are not needed outside of
extended business hours or short-term business experiments, such as trial upgrades and
proofs of concept (POCs).

- SAP on AWS Blog: [Automate Start or Stop of Distributed SAP HANA systems using AWS Systems
Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/)

**Suggestion 17.5.2 - Evaluate scheduled or dynamic scaling options
for peak loads**

On-demand capacity is commonly used in SAP workloads for peaks where capacity
requirements spike for a short period of time. Consider the following:

- Use schedule-based SAP application server scaling for known usage pattern peaks
such as period, month-end, year-end, or seasonal peaks.
- Use dynamic scaling of the application tier where peaks are less certain and need
to be scaled based on real-time user load. Explore mechanisms which are SAP-aware and
provide the required governance and controls.

**Note:** When evaluating dynamic scaling of the application
tier, consider the impact on user connections and batch jobs if an SAP application server
is shut down due to the stateful nature of SAP components. AWS, SAP, and APN
partner-developed tools can help address this requirement.

- AWS Documentation: [Systems Manager Automation actions reference](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-actions.html)
- SAP Documentation: [SAP Landscape
Management](https://www.sap.com/products/landscape-management.html)
- SAP on AWS Blog: [Using AWS to enable SAP Application Auto Scaling](https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-17-5.html*

---

# Best Practice 17.6 – Evaluate cost benefits and impact of shared services and solutions

Where the same function is required by multiple SAP systems, it can be a
cost-effective option to centralize the management and costs by using existing solutions,
sharing components, or both. Monitoring, backups, and connectivity are common functions
that can be managed either within an AWS account boundary or in a dedicated account.
Standardization, reducing duplication, and reducing complexity reduces cost.

Find appropriate ways to share resources for cost reduction while still maintaining
appropriate isolation and without introducing dependencies that might impact
operations.

**Suggestion 17.6.1 – Evaluate the cost benefit of a 1-to-1 versus a
1-to-many setup for each shared service**

A standard pattern for SAP landscapes is to isolate non-production and production
workloads in separate accounts as part of a multi-account strategy. This can be a logical
boundary for some services. Consider complexity and operational costs for each scenario
including management boundaries which enforce segmentation, and any data transfer cost
impact across Regions, AZs, VPCs, or accounts.

In a multi-account design, some AWS services can be hosted centrally and accessed
by several applications and accounts in a hub and spoke design to save cost. Such services
include:

- Dedicated VPC with NAT gateway for all outbound traffic from spoke VPCs
- Centralized model for load balancers and Web Dispatchers
- Shared Amazon EFS or Amazon FSx for transports and other file sharing needs

**Suggestion 17.6.2 – Evaluate where reuse of existing services can
reduce costs**

This suggestion applies across a number of levels:

- Where AWS provides services, these often minimize overhead and work with
consumption-based pricing. Some examples include Amazon EFS, AWS Backint Agent for SAP
HANA, and AWS Backup.
- Your business might have an enterprise-wide standard for some functions (for
example, enterprise backup) which should be used for operational consistency and
economies of scale.
- AWS Partner solutions might be available through the AWS Marketplace or BYOL (bring your own
license) based on your specific business requirements.
- License-included AWS Marketplace machine images might help reduce upfront costs. Licensing
restrictions should be considered in this scenario as they could impact solution
flexibility by restricting portability to different instance types.

**Suggestion 17.6.3 – Understand the impacts of using build vs. buy
vs. open source approaches**

Whether this is AWS or APN partner solution, there are varying degrees of build it
yourself vs. open source vs. off the shelf product. Examples include backup solutions,
high availability (HA) solutions, and shared storage solutions.

When considering a build-it-yourself approach or the use of an open source solution,
you should consider the following:

- Service level agreements
- Required skills to build and maintain
- Business impact of a service outage

You should also evaluate the available commercial models for any solutions you intend
to buy based on your specific business requirements and functionality each solution
provides. Consider the terms of any commercial model, for example, the right to use vs.
pay per use charges and how any such charges are calculated.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-17-6.html*

---

# Best Practice 17.7 – Evaluate the cost benefits of automation

The benefits of adopting automation in AWS can include improved efficiency and
productivity, which can translate into lower costs for your organization.

**Suggestion 17.7.1 – Evaluate build automation
efficiencies**

Automation of the build process by using infrastructure as code has cost efficiencies
which can improve your time to market and productivity. The advantages of quality,
consistency, repeatability, and recoverability that DevOps best practices can introduce
need to be balanced against a higher upfront investment in the development of
automation.

Working with AWS Professional Services or an AWS Partner can reduce the overall
effort by leveraging their experience.

AWS Launch Wizard for SAP can accelerate SAP deployments with automation. It’s a
service that guides you through the sizing, configuration and deployment of SAP HANA
applications on AWS following SAP best practice. The service is available at no
additional cost, with support provided by AWS.

- AWS Documentation: [Infrastructure as Code](https://docs.aws.amazon.com//whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)
- AWS Documentation: [CloudFormation](https://aws.amazon.com/cloudformation/)
- AWS Documentation: [AWS Launch Wizard for SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/what-is-launch-wizard-sap.html)
- SAP on AWS Blog: [AWS for SAP DevOps](https://aws.amazon.com/blogs/awsforsap/category/devops/)

**Suggestion 17.7.2 – Evaluate automation efficiencies for
operations**

Reduce the cost and manual effort of repeatable tasks by investigating how AWS and
third-party tools could be used to automate the running and monitoring of operations.
Consider the following:

- AWS Service: [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

Further guidance can be found in [Operational Excellence] [Best Practice 3.6 - Use automation to perform SAP landscape
operations](./best-practice-3-6.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-17-7.html*

---

## 18 – Evaluate SAP compute resources for cost efficiency

# Best Practice 18.1 – Understand the payment and commitment options available for Amazon EC2

Consider the use of Reserved Instances and Savings Plans to provide a significant
discount compared to on-demand pricing. They are available with 1-year and 3-year
commitment terms with three payment options: All Upfront, Partial Upfront, and No
Upfront.

**Suggestion 18.1.1 – Understand the breakeven points between pricing
models**

[Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html) are categorized into Standard Reserved Instances (up to 72%
discount off on-demand rates) and Convertible Reserved Instances (up to 54% discount off
on-demand rates). [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html#plan-types) are categorized into Compute Savings Plans (up to 66% discount
off on-demand rates) and EC2 Instance Savings Plans (up to 72% discount off on-demand
rates).

The discount off the Amazon EC2 on-demand hourly rate you can achieve will depend on
the following factors:

- Commitment term selected
- Payment option selected
- Reserved Instance or Savings Plan type selected
- Instance family

Memory-optimized instance families, such as `X2`, `X1`, and
`X1e`, provide higher savings for commitment. Therefore, understanding pricing
options is important for SAP, particularly for SAP HANA workloads.

Use the advanced option within the AWS Pricing Calculator to determine the
break-even point. You should be aware of the assumptions used by this calculator. To
illustrate this, consider the example where we use the following formula to determine the
point using a Reserved Instance or Savings Plan will provide a lower TCO than using
on-demand for each instance family.

*(Effective Hourly rate of Commitment / Hourly rate of On-Demand) * 730
hours*

Reference the effective hourly rate for each [RI commitment term
and type](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/) and for each [Savings Plan commitment period and type](https://aws.amazon.com/savingsplans/pricing/). Compare and contrast the following
examples illustrating different break-even points:

*Example 1: In North Virginia (us-east-1), for the M5 family, the breakeven where
a 3 year no upfront Standard Reserved Instance or EC2 Savings Plan would offer a lower
TCO is 315 hours per month (~16 hrs a day, Monday to Friday).*

*Example 2: In North Virginia (us-east-1), for the X1 instance family, the
breakeven where a 3 year no upfront Standard Reserved Instance or EC2 Savings Plan would
offer a lower TCO is 235 hours per month (~12 hrs a day, Monday to Friday).*

Use comprehensive guidance on [cost management](https://aws.amazon.com/aws-cost-management/) and the
Well-Architected Framework [Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html). The following [SAP on
AWS Pricing Guide](https://docs.aws.amazon.com/sap/latest/general/sap-on-aws-pricing-guide.html) also provides guidance specific to SAP workloads running on
AWS. When analyzing costs, be aware that all AWS pricing (with the exception of the
AWS China Regions) is in US dollars (USD). However, it is possible to select an
alternative currency for payment: [currencies AWS currently supports](https://aws.amazon.com/premiumsupport/knowledge-center/supported-aws-currencies/).

- AWS Documentation: [Savings Plans - Compute Savings Plans and Reserved Instances](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html#sp-ris)
- AWS Documentation: [Savings Plans - Plan Types](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html#plan-types)
- AWS Documentation: [Types of Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html)

**Suggestion 18.1.2 – Understand the considerations of each pricing
model relevant to SAP**

In addition to the hourly rate discount, there are other benefits of Reserved
Instances and Savings Plans you should consider. This AWS Documentation: [Comparing Savings Plans to RIs table](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html#sp-ris) provides a comparison of Reserved
Instances and Savings Plans.

[Zonal Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-scope.html) can be used to provide capacity reservations within a
specific Availability Zone. Savings Plans do not provide a capacity reservation but you
can combine with [On-demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) to provide the same features of a Zonal
Reserved Instance. See [Reliability]: [Best Practice
10.2 - Select an architecture suitable for your availability and capacity
requirements](./best-practice-10-2.html), for further information on capacity strategies.

[Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot) let you
take advantage of unused EC2 capacity in the AWS Cloud. Spot Instances are available at
up to a 90% discount compared to On-Demand Instance prices. Spot Instances can be
reclaimed by AWS with two-minutes notice when AWS requires the capacity. Therefore,
Spot Instances are not generally suited for running SAP workloads.

When using [on-demand instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html), you should consider the additional operational impact of
stopping and starting the SAP systems and underlying EC2 instances based on the required
operating hours in addition to application performance impact each time the system is
started.

**Suggestion 18.1.3 – Evaluate your enterprise strategy for
consolidated billing and sharing of Reserved Instance and Savings Plans
commitment**

With [Consolidated Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html), Reserved Instances and Savings Plans are applied to
usage across all accounts within an AWS Organization. The management account of an
organization can turn off the Reserved Instance discount and Savings Plans discount
sharing for any accounts in that organization, including the management account. This
means that Reserved Instances and Savings Plans discounts aren't shared between any
accounts that have sharing turned off. To share a Reserved Instances or Savings Plans
discount with an account, both accounts must have sharing turned on. This preference isn't
permanent, and you can change it at any time.

- AWS Documentation: [Consolidated billing for AWS Organizations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)
- AWS Documentation: [Turning off reserved instances and Savings Plans discount sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html)

A key factor that will determine your strategy for sharing of commitment will be the
overall [AWS account strategy](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) your organization has adopted. Whether your SAP
workloads are running in their own dedicated AWS accounts or along with other workloads
hosted in AWS should also be considered. To understand how discounts for Reserved
Instances and Savings Plans are applied across your organization’s consolidated bill refer
to:

- AWS Documentation: [Understanding Consolidated Bills](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/con-bill-blended-rates.html#Instance_Reservations)

As detailed in SAP note: [1656250 - SAP on AWS: Support
prerequisites](https://launchpad.support.sap.com/#/notes/1656250) [Requires SAP Portal Access], SAP on AWS is only supported if a
fee-based [Support agreement](https://aws.amazon.com/premiumsupport/)
(Business support or higher) is in place. Determine the appropriate support plan based on
cost and requirements.

- AWS Documentation: [Compare Support Plans](https://aws.amazon.com/premiumsupport/plans/)

Be aware that AWS calculates support fees independently for each member account
within an organization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-18-1.html*

---

# Best Practice 18.2 – Use cost as a key consideration for EC2 instance selection

By selecting the appropriate SAP Certified EC2 instances for your workload, it is
possible to optimize for cost. Perform a thorough analysis of each system, ensuring that
decisions are data driven where possible. Generic guidance can be found in the
Well-Architected Framework [Cost Optimization Pillar - Cost-Effective Resources](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-cost-effective-resources.html).

**Suggestion 18.2.1 – Select the latest generation instances available
within your Region**

The latest generation of Amazon EC2 instances often offers the lowest cost with
better performance and should be used if available and certified for the deployment
scenario.

- AWS Documentation: [Amazon EC2 Instance Types for SAP](https://docs.aws.amazon.com/sap/latest/general/ec2-instance-types-sap.html) (includes how to check for instance type
availability)

Note
Some Amazon EC2 instance families (for example `X1` and High Memory) might not
be available across all Availability Zones within a Region. During planning, confirm that
the instance types you require for your SAP workload are available in your target
Availability Zones.

**Suggestion 18.2.2 – Balance cost with performance
requirements**

Each SAP supported Amazon EC2 instance family will provide specific performance measured
in [SAPS](https://www.sap.com/about/benchmark/measuring.html#:~:text=SAP%20Application%20Performance%20Standard%20(SAPS)%20is%20a%20hardware%2Dindependent,order%20line%20items%20per%20hour.). You should evaluate each instance family based on your performance
requirements. An understanding of the cost per SAPS and cost per GiB ratios is recommended.

Compute-optimized (`C*`)
General Purpose (`M*`)
Memory-optimized (`R*`)

1 vCPU: 2 GiB
1 vCPU: 4 GiB
1 vCPU: 8 GiB

If a workload component requires more memory over [SAPS](https://www.sap.com/about/benchmark/measuring.html#:~:text=SAP%20Application%20Performance%20Standard%20(SAPS)%20is%20a%20hardware%2Dindependent,order%20line%20items%20per%20hour.) (CPU), you should select the instance family that provides the lowest cost
per GiB memory. If the component requires more SAPS (CPU) over memory, you should select
the instance family that provides the lowest cost per SAPS.

SAP Certified instance families powered by an AMD processor typically provide a 10%
cost saving over the comparable Intel-based EC2. For example, the `C5a` is 10%
lower cost than the `C5` family for the same performance KPIs.

For non-production SAP HANA workloads consider using one of the instance families
that meets the requirements detailed in SAP Note: [2271345 - Cost-Optimized SAP
HANA Hardware for Non-Production Usage](https://launchpad.support.sap.com/#/notes/2271345) [Requires SAP Portal Access].

**Suggestion 18.2.3 – Review the predictability of your growth profile
and peak capacity requirements**

An existing SAP landscape on AWS or a homogeneous migration is likely to have more
predictable growth and usage patterns than a new greenfield implementation or
heterogeneous migration.

For systems where you lack data on historical growth, you should consider the cost
benefits of selecting an EC2 instance size sufficient for the short or medium term growth.
Plan to scale the instance size as your requirement changes. You should ensure that your
architecture design provides the flexibility to move between different EC2 instance
families as your resource consumption changes.

Similarly, you should evaluate that changes to peak capacity have been accounted
for.

When sizing an SAP HANA environment consider not only the database size but also the
working memory requirement. Consult SAP HANA sizing reports and tools to estimate your
size and usage.

**Suggestion 18.2.4 – Consider instance commitment
flexibility**

When a component (for example, SAP HANA database) needs to scale up during the
commitment period, evaluate if this will result in moving to a different instance family.
This will impact your pricing model selection.

- AWS Documentation: [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-18-2.html*

---

# Best Practice 18.3 – Evaluate licensing impact and optimization options

When moving SAP workloads to AWS, there might be commercial impacts with the software
licenses your SAP workloads require. You should understand these impacts and the options
available to you.
Disclaimer
Any discussion of Database licensing policies in this document is for informational
purposes only and is based on the information available at the time of publication. For
more specific information, users should consult their own license agreements with the
specific Database Vendor.

**Suggestion 18.3.1 – Understand the impact of CPU and memory on
software license**

Evaluate the different vCPU and memory ratios available with the supported [Amazon EC2 Instance Types](https://aws.amazon.com/sap/instance-types/) for
SAP to optimize license costs.

- SAP Documentation: [SAP HANA Allocated Memory Pools and Allocation Limits](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/bd43f1c0bb571014bf5acf22f379fd3d.html)

For Oracle based environments, review:

- [Oracle License Considerations, Licensing Oracle Software in the Cloud Computing
Environment](http://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf)
- Oracle Premium Support requirements detailed in SAP Note: [2069760 - Oracle Linux 7.x
SAP Installation and Upgrade](https://launchpad.support.sap.com/#/notes/2069760) [Requires SAP Portal Access]

For Microsoft Windows and SQL Server environments, review:

- AWS Documentation: [Microsoft Licensing on
AWS](https://aws.amazon.com/windows/resources/licensing/)
- SAP Note: [2139358
- Effect of changes in licensing terms of SQL Server](https://launchpad.support.sap.com/#/notes/2139358) [Requires SAP Portal
Access]

For IBM Db2 environments, review:

- [Eligible Public Cloud BYOSL Policy](https://www.ibm.com/software/passportadvantage/eligible_public_cloud_BYOSL_policy.html)
- AWS Documentation: [Track IBM license usage with AWS License Manager](https://aws.amazon.com/blogs/mt/track-ibm-license-usage-with-aws-license-manager/)

Understand the impact for ISV and third-party products licensed by CPU or memory:

- Consider the use of the [Optimize CPU](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) feature to optimize license costs
- Consider the use of [AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html) to manage your software licenses and associated costs
- AWS Documentation: [Physical Cores by Amazon EC2 Instance Type](https://aws.amazon.com/ec2/physicalcores/)

**Suggestion 18.3.2 – Understand operating system purchasing
options**

For each of the SAP supported operating systems, there is a set of purchasing options
available.

- Amazon EC2 provided license
- AWS Marketplace provided license
- Bring your own licenses (BYOL)

Not all options are available for each operating system. You should evaluate your
requirements and licensing agreements to determine which option is the most cost
effective. You can include the costs of the following operating systems as part of the
Amazon EC2 cost:

- Windows Server
- Red Hat Enterprise Linux
- SUSE Linux Enterprise Server

You can purchase the following operating systems via the AWS Marketplace:

- Red Hat Enterprise Linux for SAP (based on Red Hat Enterprise Linux base EC2
cost)
- SUSE Linux Enterprise Server for SAP (based on Amazon Linux base EC2 cost)

You use bring your own licenses (BYOL) for the following operating systems:

- Windows Server
- Red Hat Enterprise Linux1
- SUSE Linux Enterprise Server
- Red Hat Enterprise Linux for SAP2
- SUSE Linux Enterprise Server for SAP2
- Oracle Enterprise Linux (Oracle Premium Support requirements are detailed in SAP
Note: [2069760 - Oracle
Linux 7.x SAP Installation and Upgrade](https://launchpad.support.sap.com/#/notes/2069760) ) [Requires SAP Portal Access]

1 Consider SAP Note: [2871484 - SAP supported
variants of Red Hat Enterprise Linux](https://launchpad.support.sap.com/#/notes/0002871484) [Requires SAP Portal Access] as SAP no
longer supports standard Red Hat Enterprise Linux for any SAP workloads as of RHEL 8.

2 These products have a longer term support which might
reduce your operational costs for upgrades – see SUSE Documentation: [SUSE Enterprise Support
Policy](https://www.suse.com/support/policy-products/) and Red Hat Documentation: [Red Hat
Enterprise Support Policy](https://access.redhat.com/support/policy/updates/errata/#Long_Support) for more details.

**Suggestion 18.3.3 – Consider the use of Amazon EC2 Dedicated Hosts
to mitigate licensing restrictions**

Amazon EC2 offers Dedicated Hosts, which allow you to access hardware that's fully
dedicated for your use. You can use [your own licensed software](https://aws.amazon.com/windows/resources/licensing/#Bring_existing_licenses_to_Dedicated_Hosts) on dedicated infrastructure. Amazon EC2 Dedicated
Hosts integrate with [AWS License
Manager](https://aws.amazon.com/license-manager/), a service which helps you manage your software licenses, including
Windows Server and SQL Server licenses.

**Suggestion 18.3.4 – Evaluate the cost benefits of moving away from a
per gigabyte or per core licensing model**

As part of your migration to cloud, consider use of the SAP Runtime database licensing
model.

SAP provides the ability for customers to license SAP HANA, SAP ASE and third-party
databases under their Runtime database license model. Runtime databases licensed from SAP
are solely to support software and SAP named users licensed from SAP. Runtime databases
from SAP are licensed as a percentage of the SAP software fee, commonly referred to as the
SAP Application Value (SAV).

Runtime licenses are not based on number of gigabytes of memory or CPU cores and
therefore can provide a cost benefit over per gigabyte or per core licensing models,
particularly when you have multiple non-production systems, as the SAP Runtime database
license applies to all environments covered under your SAP license agreement.

If you already have the right to use the SAP HANA Database Runtime license within
your SAP license agreement, you should determine if you additionally have the right to use
the SAP ASE Database Runtime license for SAP components that cannot use SAP HANA as the
underlying database or to reduce the infrastructure costs associated with using SAP HANA
for that component.

- Refer to the SAP Documentation: [SAP Product Use and Support Guide](https://www.sap.com/uk/about/trust-center/agreements/on-premise/product-use-and-support-terms.html?sort=latest_desc&tag=agreements:product-use-support-terms/on-premise-software/software-use-rights), or consult with your SAP account
team

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-18-3.html*

---

# Best Practice 18.4 – Evaluate the cost impact of storage options based on the required characteristics

Select from object storage, file storage, and block storage services to host, archive,
and secure your SAP system. Design your storage to reduce cost and increase
agility.

**Suggestion 18.4.1 – Evaluate the most cost-effective way to design
for the I/O and throughput requirements of your workload**

For most SAP requirements, solid state drives (SSDs) are recommended for your EBS
volumes. To ensure a flexible, cost-effective selection, we recommend starting with the
General Purpose Amazon EBS type `gp3`, if supported by the instance family. Over time,
review the usage using CloudWatch metrics and application/database monitoring. If higher
durability or I/O rates greater than 16,000 per volume are required, consider the
Provisioned IOPS Amazon EBS type.

- AWS Documentation: [Amazon EBS
volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)

To balance cost and performance considerations, the storage configuration used for
SAP HANA data and log volumes should meet the SAP storage KPI. The storage layouts
outlined in the following document have been tested for the SAP TDI guidelines: [SAP HANA Tailored Data Center Integration](https://www.sap.com/documents/2016/05/e8705aae-717c-0010-82c7-eda71af511fa.html)

- AWS Documentation: [Storage Configuration for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-storage-config.html)

**Suggestion 18.4.2 – Plan for dynamic changes to storage size and
configuration**

Optimize storage costs by right sizing storage according to data usage or IOPS
requirements.

Extend volume size dynamically as required. Evaluate the option of changing volume
types during activities that require increased performance such as application upgrades.

- AWS Documentation: [Requesting Volume Modifications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html)

Ensure all orphaned or unused volumes are reviewed regularly to ensure cost control.

- AWS Documentation: [List Amazon EBS volume or snapshot information](https://aws.amazon.com/premiumsupport/knowledge-center/ebs-volume-snapshot-ec2-instance/)

**Suggestion 18.4.3 – Evaluate the cost benefits for object
storage**

The core data for an SAP system is contained within the database and resides on
Amazon EBS. Amazon S3 can provide low-cost object storage for auxiliary data, such as
backups or archives and large objects such as images or documents. Cost can be further
optimized by selecting the appropriate [storage
type](https://aws.amazon.com/s3/) for your retention and durability needs.

**Suggestion 18.4.4 – Evaluate the cost benefits for shared file
systems**

Amazon Elastic File System (Amazon EFS) provides a serverless, set-and-forget, elastic
file system that lets you share file data without provisioning or managing storage. Cost
can be further optimized by selecting the appropriate storage class based on your
performance and availability requirement.

Amazon FSx provides a fully managed highly available and durable file storage solution
built on Windows Server. Data deduplication allows you to optimize costs even further by
removing redundant data.

Common SAP use cases for Amazon EFS or Amazon FSx include `sapmnt`,
transports, interface files, storing backups, and software. Use of Amazon EFS or Amazon
FSx can provide cost benefits over deploying your own highly available NFS solution.

- AWS Documentation: [Amazon EFS](https://aws.amazon.com/efs/)
- AWS Documentation: [Amazon FSx](https://aws.amazon.com/fsx/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-18-4.html*

---

## 19 – Optimize SAP data usage for storage cost efficiency

# Best Practice 19.1 – Understand access and retention requirements

Understand the ways in which you access and retain data. Consider active data,
document management systems, and backups.

**Suggestion 19.1.1 – Categorize the different types of business data
in the SAP system**

By categorizing the different types of data and how frequently data is accessed (data
temperature) from a business perspective, it is possible to identify opportunities to
archive or offload data from your SAP system to optimize cost.

The following are some of the common data types found in an SAP system:

- **Reference** — Data for which the values change
infrequently, for example, city, country, and exchange rates
- **SAP Master Data** — Data for which the values
change rarely, for example, SAP Customer Master, product
- **Audit** — Data kept for audit purposes, for
example, change logs
- **Transaction** — Data created as part of day-to-day
business operations, for example, sales orders
- **Analytical** — Data created to support analysis and
decision making, for example, monthly sales reporting

Classify the data temperature as follows:

- **Hot** — Data is accessed frequently
- **Warm** — Data is not accessed frequently
- **Cold** — Data is only accessed sporadically

Classify retention requirements as follows:

- Retain for disaster recovery (DR) purposes
- Retain for reference purposes
- Retain for compliance or audit purposes

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-19-1.html*

---

# Best Practice 19.2 – Delete unnecessary data through regular housekeeping

Reduce your data footprint to save costs by minimizing database size and other
filesystem usage through regular housekeeping and reorganization activities.

**Suggestion 19.2.1 – Review sizing and perform regular housekeeping
on SAP technical tables**

SAP provides comprehensive guidance on the data management of technical tables. By
identifying and addressing the growth of these tables, it is possible to reduce storage
and compute costs. This is especially relevant for SAP HANA instances because of the
direct relationship between database size and memory requirements.

- SAP Note: [2388483
- How-To: Data Management for Technical Tables](https://launchpad.support.sap.com/#/notes/2388483) [Requires SAP Portal Access]

Use the "largest table" SQL Statements referenced to get comparative table sizes, in
particular those marked as Basis tables. A frequent example in established SAP customers is
the high number of completed SAP workflow items which could be deleted or archived.
Housekeeping prior to a migration can also improve timelines and performance. If using SAP
HANA, the report `/SDF/HDB_SIZING` can provide cleanup details and anticipated
disk requirement.

**Suggestion 19.2.2 – Control filesystem growth through automatic or
regular cleanup of logs, traces, interface files, and backups**

As storage costs are driven by usage, there are opportunities to optimize the
baseline usage, in addition to the multiplier effect of copies and backups of files which
are no longer useful for fault analysis.

- SAP Note: [2399996
- How-To: Configuring automatic SAP HANA Cleanup with SAP HANACleaner](https://launchpad.support.sap.com/#/notes/2399996)
[Requires SAP Portal Access]

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-19-2.html*

---

# Best Practice 19.3 – Use compression, reorganization, and reclaim strategies

All databases supported by SAP provide mechanisms for reclaiming space. These
mechanisms should be part of regular maintenance activities to minimize cost increases
associated with extending memory or EBS volumes.

**Suggestion 19.3.1 – Use database compression**

Compression is a default characteristic in SAP HANA. Use of compression in other
databases might require additional licenses but should be explored for cost and
performance benefits. The following notes provide a starting point for the various
databases, but refer to SAP and database documentation for additional information.

Database
SAP Documentation or SAP Notes

SAP HANA
SAP Note: [2112604 - FAQ: SAP HANA
Compression](https://launchpad.support.sap.com/#/notes/2112604) [Requires SAP Portal Access]

SAP ASE
(Consult SAP or Vendor documentation for guidance)

IBM Db2
SAP Note: [1555903 - DB6: Supported
IBM Db2 Database Features](https://launchpad.support.sap.com/#/notes/1555903) [Requires SAP Portal Access]

Oracle
SAP Note: [1289494 - FAQ: Oracle
compression](https://launchpad.support.sap.com/#/notes/1289494) [Requires SAP Portal Access]

Microsoft SQL Server
SAP Note: [1488135 - Database
compression for SQL Server](https://launchpad.support.sap.com/#/notes/1488135) [Requires SAP Portal Access]

SAP MaxDB
(Consult SAP or Vendor documentation for guidance)

**Suggestion 19.3.2 – Use database reorganizations and reclaim
operations**

Space which is unused within the database, due to organic use or targeted archive and
cleanup activities, might require a reorganization or reclaim operation to realize the
space savings. By reclaiming space regularly, you will reduce the overall growth and
requirement for additional storage or memory. The following notes provide a starting point
for the various databases, but refer to SAP and database documentation:

Database
SAP Documentation or SAP Notes

SAP HANA
SAP Note: [2499913 - How to shrink
SAP HANA Data Volume size](https://launchpad.support.sap.com/#/notes/2499913) [Requires SAP Portal Access]

SAP ASE
SAP Note: [2543407 - reorg rebuild
with online - SAP ASE for Business Suite](https://launchpad.support.sap.com/#/notes/2543407) [Requires SAP Portal Access]

IBM Db2
SAP Note: [1942183 - DB6: When to
consider a table or index reorganization](https://launchpad.support.sap.com/#/notes/1942183) [Requires SAP Portal Access]

Oracle
SAP Note: [541538 - FAQ:
Reorganization](https://launchpad.support.sap.com/#/notes/541538) [Requires SAP Portal Access]

Microsoft SQL Server
SAP Note: [1721843 - MSSQL:
Post-steps after archiving, deleting or compression](https://launchpad.support.sap.com/#/notes/1721843) [Requires SAP Portal
Access]

SAP MaxDB
(Consult SAP or Vendor documentation for guidance)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-19-3.html*

---

# Best Practice 19.4 – Review backup strategy for improvements

When running SAP on AWS, you should evaluate your approach to backups and retention
to optimize the costs associated with location, retention, and recovery.

**Suggestion 19.4.1 – Evaluate the locations of your
backups**

Amazon S3 is the suggested long-term storage solution for your SAP system backups for
its low cost, durability, and storage class options. To copy the data on your Amazon EBS
volumes to Amazon S3, you can use point in time snapshots, integrated database tools, or
direct API calls to transfer data.

Snapshots are *incremental* backups, which means that only the
blocks on the device that have changed after your most recent snapshot are saved. This
minimizes the time required to create the snapshot and saves storage costs by not
duplicating data.

Database backup solutions require a knowledge of database state to ensure
consistency. AWS provides an SAP HANA backup solution (AWS Backint Agent for SAP HANA)
at no additional cost which integrates directly with Amazon S3. For other SAP supported
databases, there are database vendors or third-party provided backup tools available which
support backing up directly to Amazon S3.

- SAP Documentation: [Featured backup solutions](https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?search=backup)

For ad-hoc requirements or as a staging area, it might be necessary to first back up
to Amazon EBS. For these use cases, an `ST1` volume type is a low-cost HDD
volume which provides throughput and performance characteristics suitable for backups.
Selecting `ST1` can reduce your overall storage costs when the need to back up
the SAP database to disk is required.

- AWS Documentation: [Amazon EBS volume
types](https://aws.amazon.com/ebs/features/#Amazon_EBS_volume_types)

If using Amazon EFS for backups, consider EFS-Infrequent Access. This storage class
reduces storage costs for files that are not accessed every day. Amazon EFS One
Zone-Infrequent Access is not recommended for backups due to the data only residing in one
Availability Zone.

**Suggestion 19.4.2 – Review and implement a retention policy for
standard backups**

To control costs, you need to implement a retention policy aligned with your business
requirements that covers the storage services in use.

Amazon S3 offers a range of storage classes designed for different use cases with
characteristics such as cost per GB, minimum storage duration charge, and retrieval fee
(where applicable). Understanding the retention and access requirements for your backups
will help determine which storage class is most suitable to meet your requirements.

S3 Lifecycle policies can be used to automatically transfer to a different storage
class without any changes to your application. For example, backups with shorter retention
periods might be better suited to S3 Standard than S3-IA or Amazon Glacier options due to the
minimum storage duration charges and retrieval fees associated with these classes. Backups
with longer retention periods such as monthly backups for audit purposes are better suited
to S3-IA or Amazon Glacier dependent on the required retention period.

Amazon Data Lifecycle Manager can be used to automate the creation, retention, and deletion of EBS snapshots
and EBS-backed AMIs.

Amazon EFS lifecycle management automatically manages cost-effective file storage for your
file systems.

- AWS Documentation: [Amazon S3
Storage Classes](https://aws.amazon.com/s3/storage-classes)
- AWS Documentation: [Amazon S3 Storage Classes
Infographic](https://aws.amazon.com/s3/storage-classes-infographic/)
- AWS Service: [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) for EBS
snapshots and EBS-backed AMIs
- AWS Documentation: [Amazon EFS
Lifecycle Management](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)
- AWS Service: [AWS Backup](https://aws.amazon.com/backup/)

**Suggestion 19.4.3 – Create a strategy for ad-hoc backups**

Ad-hoc backups of a system or component might be required prior to a change or as a
reference for system state at a particular point in time. When the required retention does
not align with your standard lifecycle policy, you might need to adopt a separate schedule
or process for ensuring that storage usage and deletion is cost eﬀective for the individual
requirements of that backup.

- AWS Documentation: [Amazon S3 Storage Lifecycle
Management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- AWS Documentation: [Amazon EBS Snapshots
Archive](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-archive.html)

**Suggestion 19.4.4 – Review backup setup against recovery
approach**

Backups are used to revert a system to a previous point in time and to guard against
failure scenarios. Ensuring cost efficiency through a robust, but not excessive, use of
backup storage requires that you review the recovery approach. Challenge assumptions on
requirements for older more granular backups. Determine if these earlier backups would be
required in the event of a recovery.

For example, it is a valid strategy to use both database and file system backups.
However, if the primary mechanism for recovery is using database restore tools, there
might be opportunities to optimize costs by reducing the retention or deleting snapshot
backups for some volumes.

- AWS Documentation: [Amazon
EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
- AWS Documentation: [AWS Trusted Advisor best practice checklist](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-19-4.html*

---

# Best Practice 19.5 – Consider tiering options for live data

The primary driver of compute cost with SAP HANA is the amount of memory required.
Therefore, the use of data offload and tiering options can drive the compute costs down.
Although other databases might have tiering options, these have not been highlighted here.
Consult with your database provider to understand the available options.

**Suggestion 19.5.1 – Evaluate dynamic tiering, extension nodes, and
near-line storage (NLS) for SAP HANA OLAP-based workloads**

SAP HANA dynamic tiering is an optional add-on to the SAP HANA database to manage
historical data. The purpose of dynamic tiering is to extend SAP HANA memory with a
disk-centric columnar store (as opposed to SAP HANA’s in-memory store) for managing
infrequently accessed data. Dynamic tiering can only be used for native SAP HANA use cases
and not Business Warehouse (BW) on HANA or BW/4 HANA use cases

An SAP HANA extension node is a special purpose SAP HANA worker node that is
specifically set up and reserved for storing warm data. An SAP HANA extension node allows
you to store warm data for your SAP Business Warehouse (BW) or native SAP HANA analytics
use cases. The total amount of data that can be stored on the SAP HANA extension node
ranges from 1x to 2x of the total amount of memory of your extension node.

SAP BW Near-Line Storage (NLS) with SAP IQ allows you to store cold data outside of
the BW on HANA or BW/4 HANA database. NLS moves the cold data from the HANA database to
store on storage on the SAP IQ Server.

- AWS Documentation: [SAP Data
Tiering](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-data-tiering.html)

**Suggestion 19.5.2 – Evaluate data aging and SAP HANA Native Storage
Extension (NSE) for OLTP-based workloads**

Data aging helps free-up SAP HANA memory by storing less frequently accessed data in
the disk area.

- AWS Documentation: [SAP Data
Tiering](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-data-tiering.html)

**Suggestion 19.5.3 – Consider the use of data lakes for large volumes
of analytical data**

When analyzing SAP and non-SAP data, S3-based data lakes provide a cost-effective
option for data storage.

- AWS Documentation: [SAP OData
connector for Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/sapodata.html)
- SAP on AWS Blog: [Building data lakes with SAP on AWS](https://aws.amazon.com/blogs/wsforsap/building-data-lakes-with-sap-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-19-5.html*

---

# Best Practice 19.6 – Evaluate archiving and offloading options

By considering options to archive infrequently accessed data or offload large objects
to near-line storage, you can reduce your infrastructure and backup costs.

**Suggestion 19.6.1 – Implement archiving for large tables with
infrequently accessed data**

Specifically for SAP HANA databases, there are cost benefits of managing your
database growth using archiving strategies.

- SAP Documentation: [Data
Archiving](https://help.sap.com/viewer/6c8d90ed795242279e9103a8acad9cbe/LATEST)

**Suggestion 19.6.2 – Evaluate the archiving tools that support Amazon
S3 as a destination**

Amazon S3 is designed to be highly available and durable and offers a wide range of
cost-effective storage classes. This makes it ideal for storing SAP archive data with the
lowest total cost of ownership (TCO).

- AWS Documentation: [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes)
- SAP Documentation: [SAP
Certified Archiving Solutions](https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?filters=v:296)

**Suggestion 19.6.3 – Use a data management system for large
objects**

Understand the options and cost benefits for offloading and managing data outside of
the SAP database for large objects, such as invoices and images. Consider the business
requirements for accessing the data, the implementation effort and the ongoing management
complexity.

Large objects will increase your database size, inflating resource and backup costs.
Data management system options might provide a lower-cost storage solution.

- SAP Documentation: [SAP Document Management](https://help.sap.com/viewer/0f3e26f224d9419688b3d25d7c2e46fe/LATEST/en-US/4af6e75227db9972e10000000a4450e5.html)
- SAP Documentation: [Search
for Certified ILM Solutions](https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?search=BC-ILM)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-19-6.html*

---

## 20 – Manage costs with visibility, planning, and governance

# Best Practice 20.1 – Plan consumption model and environment usage during project phases

During projects, including but not limited to migration or implementation projects,
there is often a phased approach to how you deploy systems. There is also a stabilization
period where you establish the sizing and usage profile. Take advantage of the flexibility
and On-Demand Instance capabilities to minimize your costs during this period.

**Suggestion 20.1.1 – Plan to deploy systems only as
required**

Reduced lead times should give you options to deploy systems only as required. For
short lived project systems, use On-Demand Instances to build project systems for the
duration of the requirement.

**Suggestion 20.1.2 – Evaluate pricing options according to expected
duration and usage profile**

Project duration and working hours influence the pricing model. An on-demand pricing
model is often the default choice at the beginning of a project. Ensure that a budget is
defined and evaluated to adapt to cheaper options when appropriate.

**Suggestion 20.1.3 – Plan to suspend or decommission systems when not
in use**

When projects are no longer active or have achieved their objectives, consider the
cost savings from shutting down instances, in addition to the storage savings from
decommissioning. Typically, a project will make multiple copies of a system during
migration. Remember to shut down systems when they are not being used.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-20-1.html*

---

# Best Practice 20.2 – Establish a multi-year planned cost model taking advantage of different pricing approaches

Establish a multi-year plan of your capacity requirements to ensure that you are
taking full advantage of pricing models to maximize any discounts available from AWS.
Baseline and track your costs. Cloud pricing models provide flexibility that allows you to
elastically match your infrastructure to changing business requirements. Before making
commitments to long-term Savings Plans or Reserved Instances, understand and plan your
expected SAP system usage over at least a 3-year horizon. Use testing, SAP Quick Sizer
outputs, and growth forecasts to inform a commitment plan and take advantage of the
maximum discounts for your workload.

**Suggestion 20.2.1 – Establish a capacity estimate with understanding
of your key business events**

SAP workloads are generally stable, with known usage patterns and hours of operation.
Establish a well understood steady state capacity baseline for your SAP systems. This can
be done through performance testing and monitoring your production environment during the
initial weeks of your deployment.

Extend your steady state capacity estimate to at least a three-year horizon,
considering the following:

- Major business events, such as mergers, acquisitions, and divestment
- Regulation change that might affect data storage requirements or business process
frequency
- Data growth due to normal business operations (particularly important for
in-memory databases like SAP HANA as data affects compute sizing in addition to
storage sizing)
- Major system upgrades, system replacement, or decommissioning

**Suggestion 20.2.2 – Evaluate whether 1-year or 3-year commitments
are appropriate**

Evaluate how much of your SAP workload could take advantage of three-year committed
compute and maximize available discounts by using your capacity estimate. Consider the
following:

- Can you consider a three-year commitment for all compute needs of your SAP
workload?
- Can you consider a three-year commitment for a subset of your needs which you are
confident will not change? For example, SAP primary application servers or database
primaries.
- Is your SAP workload part of a broader AWS Organization which could use excess
compute commitments when changes in your SAP capacity requirements reduce the need for
compute at a future point in time?
- Is your SAP workload part of a broader AWS Organization and could share compute
commitments for non-production environments which do not need to be operating
24/7?
- For medium term capacity changes, does the benefit of committing to a 3-year
compute plan out-weigh any excess or unused capacity wastage (for example, the
break-even point versus a shorter-term commitment is in month 20)?
- Can you consider shorter term commitment (one year) for applications likely to be
affected by major business changes or replacement in the short term?
- Are currency fluctuations a concern you need to consider? AWS pricing (with the
exception of AWS China) is in US dollars (USD). If a fixed exchange rate is
desirable, you might want to consider All Upfront pricing models, if possible.

Establish a plan to match workload capacity requirements with commitment duration to
maximize discount.

*Example timeline of planning SAP on AWS compute
commitments*

**Suggestion 20.2.3 – Evaluate whether fixing compute types for
greater discounts is appropriate**

SAP workloads generally only use a limited set of AWS compute types and thus you
should consider whether committing to specific compute families or specific instance types
is appropriate for your workload to maximize discount. The two highest discount pricing
approaches for compute are EC2 Instance Savings Plans and Standard Reserved
Instances.

Consider the following:

- Identify frequently used compute types in your landscape and consider purchasing
specific EC2 instance Savings Plans or Standard Reserved Instances for these. For
example, if you are using `m5.xlarge` for your application servers across
multiple SAP applications. This is a good candidate for an EC2 specific savings plan
or Standard Reserved Instance as it is highly likely that you will always be using
this commitment.
- Identify compute components which are highly likely to change EC2 families due to
growth workloads or business events. Consider purchasing more generic compute savings
plans or Convertible Reserved Instances for these items. For example, if you have an
SAP HANA database which needs to move between an EC2 `r5` and
`x1e` compute family due to a size increase after only 6 months. This is
a good candidate for a short-term Convertible Reserved Instance or compute savings
plan.
- Identify break-even points for general compute vs. specific compute pricing and
take this into account when choosing your commitment type. For example, it might be
cheaper to purchase a Standard Reserved Instance for three years rather than choose a
3-year Convertible Reserved Instance if your sizing change is in year 3. You might
also consider selling the residual Reserved Instance value on the AWS Reserved
Instance Marketplace.
- Before changing instance types, identify use of AWS Marketplace seller private
offer or annual subscription software. This will avoid incurring additional software
costs. Both plans offer savings by allowing you to commit to running software products
on an Amazon EC2 Instance for specified duration. For example, the purchase of an
annual subscription for software to run on an `r4.xlarge` instance. You
decided to change the instance type to `r5.xlarge` . The annual
subscription is no longer linked to the instance but is still active. This results in
additional on-demand pricing for the software on the `r5.xlarge` . Consider
waiting for the annual subscription to expire before changing the instance size.

**Suggestion 20.2.4 – Evaluate whether Savings Plans, Reserved
Instances, or both are more appropriate**

Choose a mixture of both Savings Plans and Reserved Instances, to obtain benefits from
the different models, if appropriate for your SAP workload. Determine your commitment
periods and compute requirements holistically and then select your pricing model.

Further information on the differences between Savings Plans and Reserved Instances
can be found in [Cost Optimization]: [Best Practice 18.1
- Understand the payment and commitment options available for Amazon EC2](./best-practice-18-1.html) and in
[Compute Savings Plans and Reserved Instances](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html#sp-ris).

Consider [Reliability]: [Best Practice 10.2 -
Select an architecture suitable for your availability and capacity requirements](./best-practice-10-2.html).
It discusses the capacity reservation differences and tradeoffs between Savings Plans and
Reserved Instances.

**Suggestion 20.2.5 – Convert your capacity plan into a cost model for
budgeting and tracking purposes**

Convert your Savings Plans, Reserved Instance choices, and on-demand budget into a
cost plan that estimates your AWS spend for your SAP landscape over at least three
years. Combine your compute estimate with other AWS costs to finalize your SAP workload
cost model for budgeting and tracking purposes.

When estimating your SAP costs, remember to include the following:

- Compute-attached storage costs (such as Amazon EBS volumes)
- Shared file storage costs (such as Amazon EFS, and Amazon FSx)
- Backup storage costs (such as Amazon S3, and Amazon S3 Glacier)
- Network and VPC costs (such as Elastic Load Balancers, NAT gateways, Transit
Gateways, Network outbound costs, Direct Connect, and VPN)
- Management and governance service costs (such as CloudWatch detailed metrics,
AWS CloudTrail, and AWS Config)
- Security service costs (such as AWS WAF, Amazon GuardDuty, and AWS
Shield)
- AWS Support Costs (Business or higher)
- Consider enterprise discount programs or volume discounts that you might be
eligible for (speak to your AWS account manager for further details)
- Currency: Be aware that AWS prices are in US dollars (USD). You can choose a
billing currency and your bills will be computed in USD and converted to your
preferred currency at a competitive exchange rate

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-20-2.html*

---

# Best Practice 20.3 – Establish a budget and mechanisms for cost allocation and tracking including anomaly detection

There are [guidelines](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/expenditure-and-usage-awareness.html) in the Well-Architected Framework for implementing financial
management. Set expectations around cloud costs with annual, quarterly, monthly, or even
daily budgets depending on your business needs. Adjust forecasts regularly to align with
usage, and identify patterns and anomalies. Establish mechanisms for cost allocation using
account and tagging strategies.

**Suggestion 20.3.1 – Use cost and billing tools to gain spend
visibility**

SAP systems are often static in their usage patterns once established. If you use an
on-demand pricing model, either on a permanent basis or during project phases, you might
see a fluctuation in Amazon EC2 costs. If data volume management strategies are not put in
place, Amazon EBS and Amazon S3 costs might be higher than expected.

AWS provide a suite of [Cloud
Financial Management Services](https://aws.amazon.com/aws-cost-management/) including the following:

- [AWS Billing Conductor](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/) allows you to construct a cost allocation strategy that aligns
with your business logic.
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) can be used to set custom budget based on your expected
usage and notify you when a threshold is exceeded.
- [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) uses advanced machine learning (ML) technologies to identify
anomalous spend and root causes.
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/?track=costop_bottom)
provide tools for visibility and analysis.

Further guidance can be found in the Well-Architected Framework [Cost Optimization]:
[Expenditure and Usage Awareness](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/expenditure-and-usage-awareness.html).

**Suggestion 20.3.2 – Analyze and allocate spend using tags**

You can create [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what) that help identify pricing of AWS resources based on
individual accounts, resources, business units, and SAP environments. These tags are then
visible within the AWS billing reports and can be analyzed using Cost Explorer. You can
use cost allocation tags to determine the costs associated with individual SAP
environments. They help inform if action should be taken to reduce or remove costs
associated with specific environments, such as temporary environments or project
environments that are no longer required. You should have a process to identify resources
that do not have cost allocation tags attached. Implement the actions required to add cost
allocation tags to these resources.

- SAP on AWS Blog: [Tagging recommendations for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-20-3.html*

---

# Best Practice 20.4 – Establish cost-related procedures and controls

It might be necessary to adapt traditional cost assessment processes to be cloud
ready. Gain familiarity with how to implement the right financial practices and policies
by reviewing the [AWS Cloud Financial Management Guide](https://aws.amazon.com/executive-insights/content/cloud-financial-management-reference-guide).

**Suggestion 20.4.1 – Educate administrators on cost
implications**

Introduce mechanisms to assign accountability and provide incentives for cost
optimization.

**Suggestion 20.4.2 – Only allow certain users the ability to
provision instances using IAM controls**

Use IAM policies aligned with resource type and job function within account boundaries
to ensure cost control. For example, you might allow additional small-scale systems in a
sandbox account to be controlled within a project team but have an additional approval
process and restricted access for larger instances in a production account.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-20-4.html*

---

# Best Practice 20.5 – Review usage for opportunities to optimize

Review your SAP workload periodically to identify opportunities to optimize cost.
Regular reviews should focus on: minimizing the differences and anomalies found between your
AWS bill and your SAP workload budget, checking that all your SAP cloud resources are
appropriately sized and not over-provisioned, and understanding any new AWS service
releases or cost reductions that could improve the cost effectiveness of your SAP
workload.

**Suggestion 20.5.1 – Minimize additional cost where your usage has
been higher than initially planned**

Your cloud usage might have grown outside of your estimated cost model due to
unplanned business events or additional performance required. Analyze these changes with a
view to optimizing the new cost. Consider additional Savings Plan commitments or Reserved
Instances if this is a sustained change.

Where additional capacity is required for only short periods, consider horizontal
scaling mechanisms (for example, additional SAP application servers) using automatic
scaling or scheduled On-Demand Instance capacity to minimize cost further.

**Suggestion 20.5.2 – Review SAP workload usage metrics and further
right-size where possible**

Regularly review the components supporting your SAP system to ensure they are
right-sized. Use CloudWatch metrics to consider:

- Is the SAP EC2 compute the right size? Is CPU or memory utilization low? Could you
move to a smaller EC2 instance size?
- Is SAP storage the right size? Is there excess space provisioned but unused? Could
you reduce volume sizes?
- Is SAP storage appropriately performant? Is there excess IOPS or MBPS provisioned
which could be reduced?
- Are backup and snapshots being managed appropriately? Do you have too many backup
copies on S3 Standard which could be archived to Amazon S3 Infrequently Accessed or
Amazon Glacier?
- Use tools such as [AWS
Compute Optimizer](https://aws.amazon.com/compute-optimizer/) and [AWS
Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) to identify additional areas for optimization. Be aware of
SAP specific compute and storage restrictions as per SAP note: [1656099 - SAP Applications
on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099) [Requires SAP Portal
Access].

Use your findings to continually right-size your SAP workload components on a regular
basis and maximize your use of Savings Plans and Reserved Instances.

**Suggestion 20.5.3 – Understand new AWS services and plan to
implement where further cost optimization can be achieved**

AWS regularly releases new services and periodically reduces prices. Review new SAP
on AWS service announcements and plan to take advantage of these in your architecture at
a minimum every 12 months. If you have a technical account manager (TAM) as part of an
Enterprise Support agreement with AWS, they can assist you in a regular new service
briefing and optimization discussion.

Subscribe to the [SAP on AWS
blog](https://aws.amazon.com/blogs/awsforsap/) and the [What’s New](https://aws.amazon.com/new/) feed
for the latest announcements and news.

See [Operational Excellence]: [Best Practice 4.4 -
Perform regular workload reviews to optimize for resiliency, performance, agility, and
cost](./best-practice-4-4.html) for further information on continued optimization of your SAP workload.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-20-5.html*

---
