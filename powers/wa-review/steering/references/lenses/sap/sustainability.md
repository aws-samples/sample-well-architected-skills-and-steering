# Sustainability

**Pages**: 3

---

# Best Practice 21.1 - Understand and influence business requirements to make sustainability-centric SAP design decisions

Business leaders and SAP architecture teams must make conscious decisions to design
their SAP environments in a more sustainable fashion. They must understand and justify the
rationale behind those choices. If business leaders cannot describe what tradeoffs they must
make in the language of sustainability and energy efficiency, they will have difficulty
making decisions based on those criteria.

Production SAP workloads are mission critical to most businesses who run SAP, with
companies often prioritizing reliability and performance efficiency over infrastructure
costs. While prioritizing sustainability almost always results in cloud infrastructure cost
reductions, it might not create overall cost savings for an SAP workload. Running SAP
workloads in a more sustainable fashion in AWS can increase the costs of software,
personnel, or overall business functions. To meet sustainability goals, these tradeoffs
along with other priorities must be clearly articulated, agreed upon, and measurable.

**Suggestion 21.1.1 – Define criteria to measure and understand
your sustainability impact**

Understanding your sustainability goals is the first step to ensuring that you focus
on the factors needed to meet those goals. Defining such criteria involves adopting
metrics that can be used to measure and evaluate your current sustainability posture,
report progress against goals, and accelerate improvements. By analyzing the current
environmental impact of the underlying cloud-based SAP infrastructure, you can quantify
the tradeoffs and changes required to meet your sustainability objectives.

For example, the sustainability pillar of the AWS Well-Architected Framework
provides an introduction to emissions accounting, including examples of the scopes defined
by the Greenhouse Gas Protocol. Keep in mind that emissions from your SAP workloads in
AWS would count as a portion of your indirect Scope 3 emissions under these definitions.
Scope 3 emissions can be measured by a sustainability metric known as CO2e (carbon dioxide
equivalent). While not the only measure of sustainability, CO2e is commonly used to
measure and compare emissions from greenhouse gases based on how severely they contribute
to global warming, and shows how much a particular gas would contribute to global warming
if it were carbon dioxide.

Given that the previously mentioned data is not directly obtainable in most SAP
monitoring scenarios, you can use sustainability proxy metrics instead. Proxy metrics
allow SAP architecture teams to evaluate correlated improvements made to a workload
instead of real-time carbon metrics. Defining proxy metrics across compute, storage, and
network infrastructure can help you understand how infrastructure changes can impact
sustainability results. Example proxy metrics include vCPU minutes for compute, GBs
provisioned for storage, and GBs transferred for network traffic. Proxy metrics combined
with business metrics can define sustainability KPIs, which can be used to drive
sustainability optimizations while keeping business needs in focus. One example would be
to measure vCPU minutes per transaction and define an improvement goal to minimize this
metric. Business stakeholders would have to weigh the cost, as reducing vCPUs could
ultimately become detrimental to delivering on business needs. When running SAP workloads
in AWS, the change in these measured resources correlates with a similar change in cost
(except as noted in the following), making overall infrastructure spend a useful proxy
metric.

By agreeing on a set of sustainability metrics, the SAP architect team can evaluate
different technical approaches to reduce environmental impact. A small gap between the
current and target sustainability goals and your chosen metrics might result in small
architectural changes, while a large gap would require more drastic measures.

- Well-Architected Framework [Sustainability]: [Cloud
sustainability](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/cloud-sustainability.html)
- Well-Architected Framework [Sustainability]: [Evaluate specific improvements](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html)

**Suggestion 21.1.2 – Work with the business to establish more
sustainable SLAs and only architect for the SLA negotiated**

Many businesses define their SAP Service Level Agreements (SLAs) based on demands for
minimal downtime, point-in-time recoverability, and response times that are as close to
instantaneous as possible. SAP architecture teams can overestimate the risks and impact of
downtime. As a result, they put in place SAP architectures that are likely to achieve a
much higher performance objective or availability target than the agreed-upon business
SLA. For example, a business might establish a [warm Regional standby disaster recovery landscape](https://docs.aws.amazon.com/sap/latest/general/arch-guide-multi-region-architecture-patterns.html#arch-guide-pattern-7-a-primary-region-with-two-azs-for-production-and-secondary-region-with-compute-and-storage-capacity-deployed-in-a-single-az) when local [cross-AZ (Availability Zone) high availability](https://docs.aws.amazon.com/sap/latest/general/arch-guide-multi-region-architecture-patterns.html#arch-guide-pattern-5-a-primary-region-with-one-az-for-production-and-secondary-region-containing-a-replica-of-backups-amis) with backups in another Region
would suffice to meet the RPO and RTO negotiated with the business. Similarly, retaining
multiple backups of SAP test systems that are easily re-created results in the use of
unneeded resources. This extra *insurance* increases the
environmental impact (along with the cost) beyond what is acceptable for risk mitigation
by the business.

SAP architecture teams can work with the business to negotiate SLAs with
sustainability in mind. For example, rather than having a goal of instantaneous response
for ad hoc queries on an S/4HANA system, a business can dictate that certain queries must
be submitted in batch mode with a much lower SLA for processing. These reports could then
run during periods of lower utilization, reducing the peak processing required and hence
the necessary size of the EC2 instances. As another example, operational SLAs that
prioritize response time over evaluating the environmental impact of the task, such as
overprovisioning storage to avoid having to do so again in the near future, should be
reconsidered with sustainability in mind.

While these changes also align with cost optimization pillar of the SAP Lens,
businesses often prefer higher infrastructure costs when faced with the potential for
lower productivity or increased risk that less stringent SLAs may bring. When a business
prioritizes sustainability, the higher cost of doing business may be acceptable.

- AWS Documentation: [Multi-Region Architecture Patterns](https://docs.aws.amazon.com/sap/latest/general/arch-guide-multi-region-architecture-patterns.html)
- SAP Lens [Performance Efficiency]: [Best Practice 13.1 – Evaluate or estimate performance requirements](./best-practice-13-1.html)
- Well-Architected Framework [Sustainability]: [Align SLAs with sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/align-slas-with-sustainability-goals.html)
- Well-Architected Framework [Sustainability]: [Optimize software and architecture for asynchronous and scheduled jobs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/optimize-software-and-architecture-for-asynchronous-and-scheduled-jobs.html)

**Suggestion 21.1.3 – Understand how changes to SAP end user
behavior can result in more sustainable SAP architectures**

Businesses who want to run SAP more sustainably must understand how their end users
are accessing the system regardless of negotiated SLAs. If all users arrive at 9:00 AM and
run large reports simultaneously, this can create a CPU peak that can require resizing to
larger EC2 instances. SAP architecture teams must understand the relationship between SAP
user access patterns and the associated hardware footprint to design an SAP architecture
that minimizes the correlated environmental impact of using more underlying
infrastructure. SAP architecture teams can work with business stakeholders to encourage
changes to user behavior (for example, staggered business start times and financial
chargeback penalties to those with the highest utilization) to promote more sustainable
SAP usage patterns and architectural designs.

Well-Architected Framework [Sustainability]: [User
behavior patterns](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/user-behavior-patterns.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-21.1.html*

---

# Best Practice 21.2 - Implement sustainability improvements for SAP software and underlying infrastructure

After the business requirements and criteria for sustainability improvements have
been defined, the SAP architect team must implement them. Given that in most cases with
standard SAP architectural patterns (except for those called out in the following sections),
the recommendations in the SAP Lens cost optimization pillar directly align with
sustainability best practices. We will not duplicate those suggestions here and refer you to
the cost optimization pillar for guidance.

**Suggestion 21.2.1 - Develop or redevelop your SAP code with
sustainability in mind**

Highly customized SAP systems require more resources to run as a general rule.
Complex, bespoke programs can lead to statements, transactions, and reports that require
additional CPU and memory beyond optimized native SAP transactions. Adopting sustainable
development best practices, despite the additional development time, can notably improve
the code performance and reduce infrastructure usage. This impact can be magnified for
frequently run code.

Avoiding bespoke development entirely and staying with standard, well-tuned SAP
transactions is one approach. Where development is required, optimize queries or use tools
such as the ABAP Test Cockpit to improve the performance of your code. As mentioned in
Suggestion 21.2.2, keep your SAP software version as current as is feasible. This helps
reduce the need for specialized development, which otherwise would not be necessary due to
newly introduced or improved functionality.

Well-Architected Framework [Sustainability]: [Optimize areas of code that consume the most time or resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/optimize-areas-of-code-that-consume-the-most-time-or-resources.html)

SAP Documentation: [ABAP Test Cockpit](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/491aa66f87041903e10000000a42189c.html?locale=en-US)

**Suggestion 21.2.2 – Perform regular patch
management**

Performing regular patch management ensures that your system will benefit from the
latest SAP performance enhancements while avoiding unnecessary development (see Suggestion
21.2.1). By keeping your SAP systems and related software up-to-date, SAP operations teams
can avoid more intensive patching and upgrade activities. These activities can require
additional temporary hardware, which would add to measurable environmental impact. This
suggestion is in direct alignment with the SAP Lens security and operational excellence
pillars suggestions regarding SAP patching activities.

- SAP Lens [Operational Excellence]: [Best Practice 4.2 –
Regularly perform patch management for software currency](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-4-2.html)
- SAP Lens [Security]: [Best Practice 6.4 –
Establish a plan for upgrading and patching all applicable software](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-6-4.html)

**Suggestion 21.2.3 - Implement data classification and
tiering**

As mentioned in the [cost optimization section of
this lens](./cost-optimization.html), storage optimization should be a focus for reducing costs but can also
be justified from a sustainability perspective. By default, data and objects in SAP
systems are not archived nor moved to more energy efficient storage classes (or out of
memory, in the case of HANA-based systems) as the data ages. Options such as HANA NSE Data
Tiering, HANA extension nodes, Data Tiering Optimization, and data archiving or deletion
should be evaluated. In addition, using lifecycle policies for database backups and
snapshots can automate maintaining a more sustainable data footprint, as can evaluating
whether the number of backups to retain is appropriate given the SLA. The use of tools
such as SAP TDMS can also reduce the footprint of non-production systems by reducing the
overall database footprint and associated storage.

- Well-Architected Framework [Sustainability]: [Implement a data classification policy](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/implement-a-data-classification-policy.html)
- SAP Lens [Cost Optimization]: [Best Practice
19.5 – Consider tiering options for live data](./best-practice-19-5.html)
- Well-Architected Framework [Sustainability]: [Use lifecycle policies to delete unnecessary data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-lifecycle-policies-to-delete-unnecessary-data.html)
- SAP Documentation: [SAP Test Data
Migration Server](https://help.sap.com/docs/SAP_TEST_DATA_MIGRATION_SERVER)

**Suggestion 21.2.4 - Favor scale-out architectures where
possible**

As described in the [Cost optimization](./cost-optimization.html) and [Performance efficiency](./performance-efficiency.html) pillars of this lens, scale-out architectures can
mitigate the risk of over-provisioning by adding smaller compute capacity whenever
required. SAP application servers inherently are scale-out, so plan to use this capability
most efficiently for the demand required. For databases, scale-out may or may not be
possible. In situations where it is, the sustainability characteristics of incremental
growth may outweigh the operational overhead of managing a scale-out environment.

- Well-Architected Framework [Sustainability]: [Scale infrastructure with user load](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/scale-infrastructure-with-user-load.html)
- SAP Lens [Performance Efficiency]: [Best
Practice 13.3 – Select architectures that allow for independent scaling of systems
or components](./best-practice-13-3.html)
- SAP Lens [Cost Optimization]: [Best Practice
17.4 – Review the size, granularity, and latest available EC2 instances for SAP
components](./best-practice-17-4.html)

**Suggestion 21.2.5 - Shut down or terminate EC2 instances covered
by Reserved Instances or Savings Plans even when there are no additional cost
savings**

Amazon EC2 Reserved Instances (RI) and Savings Plans provide lower prices compared to On-Demand
pricing in exchange for specific usage commitments. The possibility exists that your
compute usage could drop below this commitment at times, presenting the rare case for SAP
systems where a more sustainable architecture is not directly tied to reducing your AWS
spend. In such cases, your sustainability posture might still be improved despite no
additional cost savings when following standard cost optimization best practices. This
guidance includes shutting down unused non-production systems, scaling in application
servers during periods of low utilization, transitioning EC2 instances to the latest
generation to improve CPU utilization, and minimizing the size of pilot-light HA/DR
systems.

- SAP Lens [Cost Optimization]: [Best Practice 18.1 –
Understand the payment and commitment options available for Amazon EC2](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-18-1.html)
- SAP Lens [Cost Optimization]: [Best Practice 17.4 –
Review the size, granularity, and latest available EC2 instances for SAP
components](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-17-4.html)
- Well-Architected Framework [Sustainability]: [Use the minimum amount of hardware to meet your needs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-the-minimum-amount-of-hardware-to-meet-your-needs.html)

**Suggestion 21.2.6 – Consider sustainability when choosing
AWS Regions**

SAP landscapes are frequently deployed in AWS based on such factors as proximity to
end users, data residency requirements, infrastructure cost, and compliance with specific
governmental regulations. In a business that prioritizes sustainability, the environmental
impact of deploying SAP workloads should also be considered when choosing the appropriate
AWS Region. Regions that are near an Amazon renewable energy project may be more
desirable in such cases.

- SAP Lens [Performance efficiency]: [Best Practice 13.4 –
Choose Regions and Availability Zones to minimize latency](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-13-4.html)
- SAP Lens [Security]: [Best Practice 5.2 –
Classify the data within your SAP workloads](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-5-2.html)
- Well-Architected Framework [Sustainability]: [Region
selection](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/region-selection.html)

**Suggestion 21.2.7 - Leverage managed services whenever
possible**

A number of non-NetWeaver SAP products can be installed on AWS services that are
managed above the infrastructure layer in a more sustainable fashion. One such example is
the use of Amazon RDS for SAP BusinessObjects BI Platform. The use of managed services for
common SAP-related functions is also advisable. Some examples include using AWS Backup for
AMI and Amazon EBS snapshot management or using Amazon AppFlow for bidirectional data flow with your
Amazon S3-based data lake.

Using managed services can reduce capacity guesswork and allow for AWS internal
provisioning mechanisms to maximize underlying resource efficiency. As an example, where
the option exists for your SAP systems, use Amazon Elastic File System (Amazon EFS) instead of Amazon EBS. Amazon EFS
allows for the use of only the precise amount of storage required, while EBS uses
allocated space that can leave a portion unused. As another example, Amazon EC2 instances may
be removed from your environment and replaced by managed services, such as removing
bastion hosts in public subnets and instead using AWS Systems Manager Session Manager for direct
access.

- Well-Architected Framework [Sustainability]: [Use
managed services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-managed-services.html)
- AWS Documentation: [CMS and Audit Database Architecture Options](https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-architecture-options.html#bobi-linux-cms-and-audit-database-architecture-options)
- AWS Documentation: [SAP NetWeaver on AWS Backup
and Recovery](https://docs.aws.amazon.com/sap/latest/sap-netweaver/backup-and-recovery.html)
- AWS Documentation: [Amazon AppFlow
Integrations](https://aws.amazon.com/appflow/integrations/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-21.2.html*

---

# Best Practice 21.3 - Implement sustainability monitoring for infrastructure and SAP

Monitoring and reporting on the sustainability of SAP workloads in the AWS Cloud
provides a crucial feedback mechanism. Such monitors indicate how suggestions you’ve
implemented translate into quantifiable changes over time. This data also feeds into the
sustainability reporting that will be delivered to shareholders, regulators, and
sustainability-minded customers. Reports using the metrics discussed in [BP 21.1](./best-practice-21.1.html) (for example, cost and usage as proxy metrics)
can demonstrate improvements made in the operational sustainability of your SAP landscape.
This can demonstrate that you are successfully achieving the goals set by your overall
corporate sustainability strategy.

- Well-Architected Framework [Sustainability]: [Optimize areas of code that consume the most time or resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/optimize-areas-of-code-that-consume-the-most-time-or-resources.html)

**Suggestion 21.3.1 - Develop sustainability-centric monitoring and
reporting**

Monitoring is vital to understanding the impact of changes applied to your SAP
workloads to improve their overall sustainability. Establish a mechanism to monitor the
sustainability of your AWS Cloud consumption based on common, standardized metrics.
The [AWS Customer Carbon Footprint Tool](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/what-is-ccft.html) can be used to estimate the carbon emissions
of AWS products and services that underlie your SAP systems. Greenhouse gas emissions are
converted to the amount of carbon dioxide that would result in equivalent warming and are
denoted by the services to which they are associated. Given that this reporting is
AWS account-specific, separating your SAP systems into separate accounts from other
workloads might be necessary to achieve the maximum benefits of the tool. That being said, a
multi-account strategy is typically based on the security requirements of your organization,
so refer to the SAP Lens security pillar guidance on this topic.

SAP also provides their [SAP Sustainability
Control Tower](https://www.sap.com/products/sustainability-control-tower.html) solution to expand reporting beyond the underlying SAP
infrastructure costs to infrastructure costs and ultimately the overall business’s
sustainability posture.

- AWS Documentation: [Understanding your customer
carbon footprint tool](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/what-is-ccft.html)
- Well-Architected Framework [Sustainability]: [Evaluate specific improvements](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html)
- Well-Architected Framework [Security]: [Assess the
need for specific security controls for your SAP workloads](./best-practice-5-3.html)
- SAP Documentation: [SAP
Sustainability Control Tower](https://www.sap.com/products/sustainability-control-tower.html)

**Suggestion 21.3.2 - Periodically baseline and review reported
results**

As described in Suggestion 21.1.1, progress of an organization’s sustainability
initiative over time should be based on an initial reference position. As part of setting up
the relevant sustainability monitoring tools, establish the baseline configuration data and
reporting, from which progress will be tracked. Baselining should include the following
considerations:

- Tagging of relevant SAP workloads to allow for more granular reporting.
- Current carbon dioxide-equivalent (CO2e) or other proxy metric for workloads running
in AWS.

To ensure your organization’s use of AWS services for SAP and their sustainability
trajectory are monitored against established KPIs and overall business goals, establish a
periodic reporting review as part of an improvement process. This review should include the
following activities:

- Validate all relevant SAP workloads are being monitored appropriately, including new
workloads added since data gathering was last baselined.
- Measure the results, look for gaps, and replicate areas of success.

Aligning these activities with the best practices from the SAP Lens operational
excellence pillar can help you perform standardized sustainability reviews with other
periodic operational activities. For example, discovering and removing unused resources,
such as orphaned storage volumes or low-utilization instances, should be standard
operational review tasks that also reduce environmental impact.

- Well-Architected Framework [Sustainability]: [Improvement process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html)
- Well-Architected Framework [Sustainability]: [Measure results and replicate successes](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/measure-results-and-replicate-successes.html)
- Well-Architected Framework [Operational Excellence]: [Validate and improve your
SAP workload regularly](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-5-3.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-21.3.html*

---
