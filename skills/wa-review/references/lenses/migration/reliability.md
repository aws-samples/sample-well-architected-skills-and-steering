# Reliability

**Pages**: 3

---

# Assess

The Assess phase involves evaluating the current state of the
workloads that are targeted for the migration. To achieve this, we
will focus on assessing the existing workloads for any potential
points of failure during the migration process.

MIG-REL-01: Do you have any existing compliance requirements around service availability or service-level agreements (SLA) that apply to applications within the migration scope?

Existing applications have current service levels which must be
maintained during migration. During migration assessment, it is
important to understand the existing availability requirements,
and then define the migration strategy and target architecture.

## MIG-REL-BP-1.1: Define SLAs across all applications or environments (like production, development, or test) and confirm them with your business team

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion
1.1.1:** Evaluate the unique aspects of
your applications to understand if you have different
availability requirements for each application.

Define goals for each application based on
[availability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html).

## MIG-REL-BP-1.2: Define and automate runbooks and communicate them to your teams

This BP applies to the following best practice areas: Foundations

### Implementation guidance

**Suggestion
1.2.1:** Prepare, document and validate
procedures for your workload to minimize the disruption of
your workload during events.

It is recommended to automate runbook procedures so runbook
activities are performed consistently. For more detail, see
[OPS07-BP03
Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html).

## MIG-REL-BP-1.3: Map AWS Global Infrastructure to your business SLAs before migrations starts

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion
1.3.1:** Understand
[AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) terminology and definitions.

If you operate multiple datacenters on-premises today, how does this map to AWS infrastructure and your existing availability requirements?

**Suggestion 1.3.2** Identify the services you plan to use when you migrate and compare the [AWS Service Level Agreements](https://aws.amazon.com/legal/service-level-agreements/) to your existing business SLAs.

Your existing SLAs may need to be updated based on AWS
Service Level Agreements.

## MIG-REL-BP-1.4: Select tools to monitor SLAs and notify you in case thresholds are exceeded

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion
1.4.1:** Reduce communication to
on-premises monitoring tools.

If you choose to use existing monitoring tools on your migrated workloads, you should optimize data egress to systems which are remaining on-premises. This is achieved differently by different tools, but a common method is to deploy a collector within AWS that optimizes communication. When migrating to AWS, there may be agents which are no longer needed (for example, VMware Tools and tools for physical hardware monitoring). Use [custom post-launch actions](https://docs.aws.amazon.com/mgn/latest/ug/post-launch-settings-custom-actions.html) to remove these agents during migration with AWS Application Migration Service.

**Suggestion 1.4.2:** Use managed services to reduce operational overhead and save licensing costs.

Before migrating, assess if changing monitoring tools for AWS Managed Services like [Amazon Cloudwatch](https://aws.amazon.com/cloudwatch/) and [AWS Systems Manager](https://aws.amazon.com/systems-manager/) could reduce the overhead of running these tools and the licensing costs from those tools.

**Suggestion 1.4.3:** Monitor networking links during migration.

Measure the additional migration related network traffic and prevent this traffic from affecting business applications. For example, if you are using AWS Direct Connect between your on-premises solution and AWS, you can monitor the throughput of the migrated workload using [AWS Direct Connect resources](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-overview.html) and set up [Amazon CloudWatch alarm throughput notification](https://repost.aws/knowledge-center/cloudwatch-throughput-direct-connect).

**Suggestion 1.4.4:** Use metrics and logs from AWS Migration Services to monitor inflight migrations.

For more detail, see
[Monitoring
Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/monitoring-overview.html) and

[Monitoring
AWS DMS tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html).

MIG-REL-02: What is your business continuity plan for the migrated workload?

Each organization has different set of requirements to build a business continuity plan (BCP) or disaster recovery (DR) plan. The BCP needs to be updated during migration, as the locations of workloads are changing. The risks associated with cloud services need to be added to the BCP. For more detail, see [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html).

## MIG-REL-BP-2.1: Keep your business impact analysis up-to-date

This BP applies to the following best practice areas: Failure management

### Implementation guidance

**Suggestion
2.1.1:** Check that your portfolio and
CMDB data is correct.

Keeping application metadata up-to-date is challenging.
Commonly, application metadata (for example, number of users)
is only updated periodically. Additionally, applications which
were once important might not be so critical as alternatives
become available. The application metadata should be verified
so the correct BCP is put in place as part of the migration
project.

## MIG-REL-BP-2.2: Update the risk assessment for the type of disaster events covered by your BCP

This BP applies to the following best practice areas: Failure
management

### Implementation guidance

**Suggestion
2.2.1:** Add new events for your cloud
environment.

Various events in the cloud environment for example complete
loss of AWS Region, complete loss of an AWS Availability zone
or service degradation of a single AWS service need a risk
assessment. A risk assessment measures how likely an event
will occur vs the impact of that event to business
applications and helps determine the recovery targets for
certain events.

## MIG-REL-BP-2.3: Define the recovery point objective (RPO) and recovery time objective (RTO) targets

This BP applies to the following best practice areas: Failure
management

### Implementation guidance

**Suggestion 2.3.1:** Create a small number of different RPO and RTO classes.

Migrations can have hundreds of applications in scope, and
creating many different RPO or RTO targets which map to
different disaster recovery strategies can increase the
complexity of migration.

## MIG-REL-BP-2.4: Select a disaster recovery strategy based on cloud best practices

****This BP applies to the following best practice areas: Failure management

### Implementation guidance

**Suggestion
2.4.1:** Familiarize yourself with
[disaster
recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

You must a select disaster recovery option which meets your RPO and RTO targets and addresses risks defined in your BCP. For example, [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) replicates Amazon EC2 instances to another AWS Availability Zone (or another Region) to address the risk of disasters within AWS.

**Suggestion 2.4.2:** Automate disaster recovery options to be implemented as migrations occur.

For example, in migrations using AWS Application Migration
Service, there is a post-launch action to
[configure AWS Elastic Disaster Recovery (AWS DRS)](https://docs.aws.amazon.com/mgn/latest/ug/predefined-post-launch-actions.html#predefined-elastic-disaster-recovery).

MIG-REL-03: What is the maintenance window for the migration cutover?

During migration activity, business process may not be resilient
to extend downtime windows. Align the migration event based on
your business need.

## MIG-REL-BP-3.1: Estimate the required maintenance window

This BP applies to the following best practice areas: Change
management

### Implementation guidance

**Suggestion 3.1.1:** Migration to AWS could involve a brief or
extended outage of service during the cutover from the
current environment.

A typical application cutover involves shutting down the
source application, then running a final synchronization of
data. The amount of data in the final synchronization,
combined with the speed of network links, determines the
outage period required for the migration. For example,
database migrations can be performed using a
[backup
and restore method or AWS Database Migration Service](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/dms.html).
These methods offer different cutover windows. Users of the
applications being migrated need to be informed of the
accurate outage period, with appropriate lead time to assess
the impact and plan contingencies.

## MIG-REL-BP-3.2: Test the migration window and impact

This BP applies to the following best practice areas: Change
management

### Implementation guidance

**Suggestion
3.2.1:** Dry-run the migration
activities to validate that they can be completed in the
defined maintenance window.

Perform dry-run tests in environments with similar data volume or anticipate the additional volume of data that the production environment has compared to non-production testing (usually significant). Monitoring tools can help provide accurate data change rates. For more detail, see [Running a proof of concept](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html#CHAP_BestPractices.RunPOC).

**Suggestion 3.2.2:** In case the migration data synchronization activities or testing take longer than the defined maintenance window, define a process to measure the impact on your business and set a contingency plan.

For some applications, it may be fine to extend the
maintenance period, but for others, immediate rollback of
the migration is required. For more detail, see
[Developing
a cutover plan](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/pre-cutover-stage.html#cutover-plan).

## MIG-REL-BP-3.3: Plan for failure

This BP applies to the following best practice areas: Change
management

### Implementation guidance

**Suggestion
3.3.1:** Calculate and document the time
required to rollback.

A migration checkpoint should be put in place to enable rollback to be performed within the defined maintenance window. For more detail, see [Rollback](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/cutover-stage.html#rollback).

**Suggestion 3.3.2:** Define a communication channel for the migration event and communication intervals agreed with stakeholders.

Communication channels should be used to make decisions during unexpected events. For example, if the maintenance window needs to be extended, a message can be sent to application owners to approve extension or initiate rollback. For more detail, see [Communication and governance planning](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/communication-governance-planning.html).

**Suggestion 3.3.3:** Determine how data can be copied back to the source environment.

After deciding to rollback a migration, you may need to copy
data back to the source environment. For EC2 instances, AWS
Elastic Disaster Recovery can be used to
[perform
a failback](https://docs.aws.amazon.com/drs/latest/userguide/failback-performing-main.html) from AWS to on-premises environments. For
databases, depending on the amount of data to be
synchronized, native replication tools can be used, or a
database backup and restore can be performed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/assess-rel.html*

---

# Mobilize

The mobilize phase involves setting up the resources and tools
needed for the migration. During this phase, the team impacted by
the migration are trained to handle the migration. Have a backup
plan ready in case anything unexpected happens.

MIG-REL-04: Have you reviewed service quotas and constraints for new migrated resources?

Service quotas exist to prevent accidentally provisioning more
resources than you need, and to limit request rates on API
operations so as to protect services from abuse. For more
detail, see
[Manage
service quotas and constraints](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/manage-service-quotas-and-constraints.html). Migrations can add new
resources to existing accounts and therefore affect service
quotas. Migration services have quotas which can affect the
speed migrations can be performed.

## MIG-REL-BP-4.1: Be aware of service quotas and constraints for migration services

This BP applies to the following best practice areas: Foundations

### Implementation guidance

**Suggestion
4.1.1:** Review service quotes for
[AWS Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/MGN-service-limits.html) and

[AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Limits.html), as these can affect the sizing of your migration
waves and number of operations which can be performed
simultaneously.

For example, you can only migrate 200 servers within one
job. Hitting limits for these services can disrupt migration
plans.

## MIG-REL-BP-4.2: Estimate the impact of new workloads on existing service quotas across accounts and Regions

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion
4.2.1:** Review service quota values
that would breach if new migration workloads are added to an
account.

For example, adding many new EC2 instances into a VPC can
cause the soft limit network interfaces per Region (default
5000) to be reached. Request limit increases for such quotas
before your migration events.

## MIG-REL-BP-4.3: Be aware of unchangeable service quotas and how you determine which accounts or VPCs workloads use

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion
4.3.1:** Depending on the migration
scope, you may have to split workloads into multiple AWS accounts or VPCs to avoid hitting unchangeable service
quotas.

MIG-REL-05: How do you plan your network topology for migration activity?

Workloads often exist in multiple environments. It could be
between multiple cloud environments and your existing data
center. During the migration planning phase, include network
considerations, such as intra-system and intersystem
connectivity, public IP address management, private IP address
management, and domain name resolution.

## MIG-REL-BP-5.1: Provide sufficient bandwidth for normal and traffic from data replication

This BP applies to the following best practice areas: Foundations

### Implementation guidance

**Suggestion
5.1.1:** Replication traffic may need to
be throttled so it does not overwhelm network links.

For more detail, see [Data routing and throttling](https://docs.aws.amazon.com/mgn/latest/ug/data-routing.html) and [Improving the performance of an AWS DMS migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html#CHAP_BestPractices.Performance).

## MIG-REL-BP-5.2: Assure that links and equipment to on-premises are highly available

This BP applies to the following best practice areas: Foundations

### Implementation guidance

**Suggestion
5.2.1:** If network connectivity is
disrupted, migration replication may need to be restarted. Use
multiple
AWS Direct Connect connections or VPN tunnels between
separately deployed private networks.

Use multiple Direct Connect locations for high
availability.
If using multiple AWS Regions, ensure redundancy in at least two of them. You
might want to evaluate AWS Marketplace appliances that terminate VPNs. If you use AWS Marketplace appliances, deploy redundant instances for
high availability in different Availability Zones.

## MIG-REL-BP-5.3: Verify that your network design enables communication between on-premises and cloud networks

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion
5.3.1:** Design networks to prevent
overlapping IP addresses with your on-premises network.

Select new IP ranges to be assigned to AWS VPCs which do not clash with any existing networks. Even though some networks may eventually by freed by the migration, both networks are in use during the migration and difficult to free up until the end of the migration.

**Suggestion 5.3.2:** Not all networks need to be routable to on-premises.

To preserve routable IP space, non-routable CIDR ranges can
be used. For more detail ,see
[Preserve
routable IP space in multi-account VPC designs for
non-workload subnets](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets.html).

## MIG-REL-BP-5.4: Use an IP scheme that allows for sufficient growth within cloud workloads and burst auto-scaling

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion
5.4.1:**
Amazon VPC IP address ranges must be large enough to
accommodate

workload
requirements, including factoring in future expansion and
allocation of IP addresses to subnets across

Availability
Zones.

This includes load balancers,
EC2
instances, and container-based applications.

## MIG-REL-BP-5.5: Complete a reliable DNS design that enables resolutions to existing domains, plus new domains in AWS

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion 5.5.1**: DNS resolution between multiple AWS Accounts and on-premises is fundamental for application communication.

For more detail, see designs for [single-accoun](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment.html)t and [multi-account](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment.html) hybrid DNS resolutions. During any multi-phase migration, on-premises applications need to talk to migrated applications through DNS, and migrated applications need to talk to on-premises applications. For more detail, see [Automating DNS infrastructure using Route 53 Resolver endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/automating-dns-infrastructure-using-route-53-resolver-endpoints/).

**Suggestion 5.5.2**: Windows workloads require DNS for active directory (AD).

For rehost (lift and shift) migrations, the same AD domain needs to be resolvable in both on-premises and cloud environments. To avoid affecting the production environment during testing windows server migrations, [machine password rotation and dynamic DNS updates should be disabled](https://aws.amazon.com/blogs/architecture/avoid-affecting-your-production-environment-during-migration-with-aws-application-migration-service/).

**Suggestion 5.5.3:** Plan for how to update DNS records during migration testing and cutovers.

Some systems (like Windows) can update dynamically, while
others require manual updates. Provide the migration team
access to update DNS records or develop automated processes.

## MIG-REL-BP-5.6: Test network performance prior to migration

This BP applies to the following best practice areas: Foundations

### Implementation guidance

**Suggestion
5.6.1:** Network latency has varying effects
on applications.

Testing how migrated applications respond to the new networking
environment can be performed using distributed load testing and
monitoring performance metrics.

## MIG-REL-BP-5.7: Test network component failure

This BP applies to the following best practice areas:
Foundations

### Implementation guidance

**Suggestion
5.7.1:** Network outages have varying
effects on applications.

Testing how applications respond to connectivity events can be
performed using AWS Fault Injection Service. For more
detail, see
[Tutorial:
Simulate a connectivity event](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-disrupt-connectivity.html).

MIG-REL-06: How do you back up data on migrated workloads?

Back up data, applications, and configuration to meet
requirements for recovery time objectives (RTO) and recovery
point objectives (RPO). Backup capabilities of cloud environment
will differ from on-premises.

## MIG-REL-BP-6.1: Identify and back up all data that needs to be backed up, or reproduce the data from sources

This BP applies to the following best practice areas: Workload
architecture

### Implementation guidance

**Suggestion
6.1.1:**
Validate that your backup process implementation meets your
recovery time objectives (RTO) and recovery point objectives
(RPO) by performing a recovery test both before and after
the migration.

For more detail, see the following:

- [Identify and back up all data that needs to be backed up, or reproduce the data from sources](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_identified_backups_data.html)
- [Secure
and encrypt backups](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_secured_backups_data.html)
- [Perform
data backup automatically](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_automated_backups_data.html)
- [Perform periodic recovery of the data to verify backup integrity and processes](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html)

MIG-REL-07: Are your migrated workloads utilizing fault isolation?

Your workload must operate reliably despite data loss or latency
in these networks. Components of a migrated workload can use AWS
capabilities to design the workloads in more fault-tolerate
ways. Follow these best practices to ensure your migrated
workloads are fault-tolerant.

## MIG-REL-BP-7.1: Deploy the workload to multiple locations

This BP applies to the following best practice areas: Workload
architecture

### Implementation guidance

**Suggestion 7.1.1:**
Follow the best practices (BPs) in the [Reliability
pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-reliability.html) to distribute workload data and resources
across multiple Availability Zones or, where necessary,
across AWS Regions.

These locations can vary as required by
your business requirements. Always (when possible) deploy
your workload components to multiple AZs for high
availability. For components that can only run in a single
AZ, implement the capability to do a complete rebuild of the
workload within your defined recovery objectives.

For more detail, see the following:

- [Deploy
the workload to multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)
- [Automate recovery for components constrained to a single location](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_single_az_system.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/mobilize-rel.html*

---

# Migrate

The migrate phase is where the actual migration of the workload
takes place. In this phase, we perform migration as planned,
monitor the migration process, and keep a plan in place to
rollback in case issues encountered during the migration.

MIG-REL-08: Have you tested high availability (HA), fault tolerance (FT), and disaster recovery (DR)?

Test to validate that your workload meets functional and non-functional requirements before and after migration cutover. It is important to validate and update existing reliability components, which may be different in the new cloud environment.

## MIG-REL-BP-8.1 Before the cut-over, test HA and FT for the migrated workloads, and perform a DR dry-run after the migration

This BP applies to the following best practice areas: Failure
management

### Implementation guidance

**Suggestion 8.1.1:** Follow the best practices (BPs) in the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html?) to complete the failure management testing for the migrated workloads.

This includes using playbooks to investigate failures, performing post-incident analysis, testing functional requirements for the migrated applications, testing scaling and performance, and testing resilience using chaos engineering.

For more detail, see [How
do you test reliability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-12.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migrate-rel.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
