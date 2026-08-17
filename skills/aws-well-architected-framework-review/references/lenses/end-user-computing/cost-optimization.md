# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 8

---

# EUCCOST01 — Practice Cloud Financial Management

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# EUCCOST01-BP01 Evaluate EUC specific cost model awareness in your cloud business

You may have a cloud business office, Cloud Center of
Excellence, or a FinOps team that is responsible for
establishing and maintaining cost awareness across your
organization. However, AWS EUC services often use many other
services and may require a solid understanding of Microsoft
licensing to optimize the cost. If you are using the ITIL
framework, you may already have defined service owners for
individual services who own the financials for their services.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Evaluate the required domain knowledge in your cloud business office. We recommend
you evaluate the required EUC domain knowledge in your cloud business office to understand
if the team is ready to support cost optimization for EUC services. These individuals need
to be intimately familiar with the cost optimization levers specific to EUC services, such
as Microsoft licensing, WorkSpaces running modes, WorkSpaces bundles, WorkSpaces Applications Fleet types, and
WorkSpaces Applicationsinstances. Provide EUC-specific cloud financial training to them if there is a
knowledge gap.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost01-bp01.html*

---

# EUCCOST01-BP02 Increase awareness of the EUC cost model in your cloud business office to promote cost optimization

In case your cloud business office lacks the required knowledge
in the EUC domain, consider additional training and enablement
to close these gaps.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

If an existing team is tasked with cost optimization of AWS EUC services, train
these individuals on the specifics of the EUC services so they can perform their duties.
This includes training on the services, generic training on how a typical EUC environment
(virtual or physical) operates, and specifically how to identify resource under- and
over-provisioning.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost01-bp02.html*

---

# EUCCOST02 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# EUCCOST02-BP01 Monitor your EUC cost and usage proactively

[AWS Cost and Usage
Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html) help you gain detailed insights onboth your WorkSpaces Applications and your WorkSpaces service
usage and cost. In addition, WorkSpaces Applications offers separate [Usage Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-usage-reports.html)
with further detail. Amazon WorkSpaces comes with a [WorkSpaces CloudWatch automatic
dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html) that provides insight into the performance of your WorkSpaces resources and
helps you identify performance issues. [Amazon WorkSpaces Applications Fleet Usage and
Instance/Session Performance Metrics](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html) are available in the WorkSpaces Applications Console and
Amazon CloudWatch.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

For WorkSpaces, enable [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html) with
resource IDs to analyze and visualize your cost and usage. Resource IDs help you see the
cost and usage data for an individual WorkSpace. Consider building an [Build an enterprise cost and usage dashboard for Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/build-an-enterprise-cost-and-usage-dashboard-for-amazon-workspaces/).

Furthermore, the [Cloud
Intelligence Dashboards](https://www.wellarchitectedlabs.com/cloud-intelligence-dashboards/) section of AWS Well-Architected Labs explores how to
build a CUDOS Dashboard that includes Amazon WorkSpaces cost and usage data. The Cost
Optimizer for Amazon WorkSpaces referred to in EUCCOST-BP05 also generates basic usage
reports in Amazon S3.

WorkSpaces Applications also offers built-in usage reports. Enable [WorkSpaces Applications Usage
Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-usage-reports.html) to gain valuable insights into your WorkSpaces Applications usage. For details on
visualizing your WorkSpaces Applications usage, see [Analyze your WorkSpaces Applications usage reports using Amazon Athena and Quick](https://aws.amazon.com/blogs/desktop-and-application-streaming/analyze-your-amazon-appstream-2-0-usage-reports-using-amazon-athena-and-amazon-quicksight/). If you are using
Amazon WorkSpaces Applications features such as [Enable Application
Settings Persistence for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html) or [Enable and Administer Home
Folders for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders.html), include the underlying Amazon S3 buckets in
your cost and usage monitoring.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost02-bp01.html*

---

# EUCCOST03 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# EUCCOST03-BP01 Determine the level of self-service capabilities to provide your users

Amazon WorkSpaces offers self-service capabilities that you can
enable for your users. Assess the impact of granting access to
these self-service capabilities and selectively disable or
enable them based on your requirements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Evaluate the cost impact of enabling certain self-service WorkSpaces management
capabilities for your users, and then select which of these self-service capabilities you
want to provide to your users. For more information, see [Enable self-service WorkSpaces management capabilities for your users in WorkSpaces
Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html) . Consider creating internal policies to govern which capabilities are
allowed. Changing the compute type (bundle), increasing the root and user volume size, and
changing the running mode may increase your cost. Instead of enabling these capabilities
for your users, you may consider providing these capabilities through your IT service
management so that changes requested by a user requires prior approval.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost03-bp01.html*

---

# EUCCOST03-BP02 Use a self-service portal to request your ITSM

Instead of enabling self-service capabilities for your users, use a self-service portal to allow users to request resources, or enable workflow-based request for EUC resources with your ITSM. This gives you better control and limits the exposure to unforeseen cost increases.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Consider implementing a self-service portal to request
WorkSpaces or changes to your existing WorkSpaces, like
running mode, bundle, or storage. A self-service portal can
allow your users to provision and terminate their EUC services
as required. For an example for Amazon WorkSpaces, see
[Creating
a self-service portal for Amazon WorkSpaces end users](https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-a-self-service-portal-for-amazon-workspaces-end-users/).

Additionally, consider using your ITSM solution to enable
workflow-based requests for new WorkSpaces or changes to
existing WorkSpaces, like running mode, bundle, or storage.
For examples of integrating with ServiceNow, see
[How
to enable self-service Amazon WorkSpaces by using Service Catalog Connector for ServiceNow](https://aws.amazon.com/blogs/mt/how-to-enable-self-service-amazon-workspaces-by-using-aws-service-catalog-connector-for-servicenow/) and

[Managing
Amazon WorkSpaces by integrating Service Catalog with ServiceNow](https://aws.amazon.com/blogs/mt/managing-amazon-workspaces-by-integrating-aws-service-catalog-with-servicenow/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost03-bp02.html*

---

# EUCCOST04 — Cost effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# EUCCOST04-BP01 Tag your Amazon WorkSpaces and Amazon WorkSpaces Applications resources

[Tagging your Amazon WorkSpaces Applications resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html) or [tagging WorkSpaces
resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html) helps you allocate your cost to logical groups, such as departments or
business entities.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Plan your tagging strategy before you start deploying your EUC resources. You may
think of tagging EUC resources with information such as cost center, department,
usernames, projects, location, or deployment types (like development, test, and
production). The more dimensions you add with your tags, the easier it will be to report
and break down the cost once you are in production.

If you already use tagging in your organization, implement a standardized approach
for tagging that aligns with the approach being used by the rest of the organization,
which results in a standardized format for the key value pairs being used for tags in the
organization. Using [Service control
policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) with AWS Organizations enforces tags to restrict resource creation
unless they are correctly tagged.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost04-bp01.html*

---

# EUCCOST05 — Cost effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# EUCCOST05-BP01 Gather usage data and hardware requirements in your existing environment

Before selecting a service for your EUC workload, gather usage
data in your existing EUC environment. Collect data in different
areas, like usage patterns and resource utilization. Usage
patterns portray how intensively your applications are being
used (for example, hours per day and days per week). Resource
utilization details how efficiently your compute resources are
being used by these applications (like CPU, RAM, GPU, disk
space, and disk IO). Both areas help you select the optimal
service for a given application or set of applications. You can
gather this data using OS or third-party tools.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

If you use a desktop virtualization Environment, your VDI
solution may include reporting tools that can provide you with
the required data. Tools like
[Citrix
Director](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/director.html) or

[VMware
vRealize Operations Manager](https://docs.vmware.com/en/vRealize-Operations/index.html) can be used for this.

Alternatively, you may use scripting to wrap application launches and log the usage
of applications using these scripts in a file or database that you can use later to
analyze the data. Your OS may include tools to visualize and log the resource utilization
of your applications.

For example, Windows offers the [Windows Performance Monitor](https://techcommunity.microsoft.com/t5/ask-the-performance-team/windows-performance-monitor-overview/ba-p/375481) to capture performance metrics over an elapsed
period of time.

If you do not have any tools available to gather usage patterns, you can conduct a
survey with a representative selection of users to understand their usage of your
applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost05-bp01.html*

---

# EUCCOST05-BP02 Select the most cost-effective service for your EUC workload

Invest time into planning your EUC deployment. A persistent Amazon WorkSpaces, for example, is
a desktop as a service assigned to a named user. If this named user needs to run a certain
resource-intensive application only occasionally, it is not recommended to over-provision
the hardware resources for this WorkSpace to meet the application requirements, as these
resources will be under-utilized most of the time. Instead, consider deploying this
application to an Amazon WorkSpaces Applications fleet, where you have a more granular choice of instance types
and are charged for the actual usage only per hour or even per second.

The usage patterns and usage data collected help you govern your
application landscape and select the most appropriate service
and bundle and instance for each of your applications.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Amazon WorkSpaces offers a variety of different bundles to
choose from, and each one has a different hardware
configuration (vCPU and RAM), some of which supporting a GPU.
In total, you have the choice between five non-GPU bundles and
four GPU-enabled bundles.

With Amazon WorkSpaces Applications, you have a more granular choice from many non-GPU and GPU-enabled
instance types. Review your application workloads and match them to the most appropriate
service and bundle or instance type to avoid over-provisioning of resources.

Consider Amazon WorkSpaces Applications with appropriate instance types for workloads that can be
characterized as CPU-intensive or RAM-intensive or requires a GPU and that typically shows
a lower utilization.

In a typical EUC environment, users are often using certain applications permanently
over the course of a day and other applications only occasionally. For a CPU-intensive or
RAM-intensive workload, or for applications requiring a GPU, Amazon WorkSpaces Applications can be the more
cost-effective solution, especially if the application is only used occasionally. If you
have any usage data (usage patterns) on these applications, we recommend you review these
and calculate a cost estimate of the usage on Amazon WorkSpaces Applicationsusing these usage patterns.
This helps you understand if provisioning the application on Amazon WorkSpaces Applications will be more
cost-effective than provisioning it on Amazon WorkSpaces if choosing a more powerful bundle.

Even the combined usage of a less powerful WorkSpaces instance for standard applications
and WorkSpaces Applications for more demanding workloads can come at a lower cost compared to a more
powerful WorkSpaces bundle as the only service. If there isn't enough data to make a decisive
decision, identify a mechanism to capture this data in your existing environment or
perform a proof of concept (PoC) to capture this data.

If your users only need to access web-based applications,
consider using Amazon WorkSpaces Secure Browser. Examples of
web-based applications are Salesforce, SAP-Fiori, Confluence,
or your intranet websites. WorkSpaces Secure Browser
service is a low cost, fully-managed, Linux-based service
designed to provide secure browser access to internal websites
SaaS applications for up to 200 streaming hours.

If you need a persistent environment with users who require a high degree of
flexibility in customizing their environment and installing their own applications,
Amazon WorkSpaces Personal is your best option. As opposed to Amazon WorkSpaces Personal, Amazon WorkSpaces Applications is
not designed to allow users to install their own software due to the non-persistent nature
of the WorkSpaces Applications fleet.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost05-bp02.html*

---

# EUCCOST05-BP03 Rightsize your EUC resources

Choosing the right Amazon WorkSpaces bundle or Amazon WorkSpaces Applications instance type for your EUC
workloads is important to operate your EUC environment in a cost-effective manner. The
chosen configuration needs to support the hardware requirements of your applications, while
at the same time avoiding over-provisioning resources.

Capture metrics in an existing reference environment (physical
machines or virtual desktops) to understand how the existing
resources are being used. This data helps you choose the right
bundles and instance types with AWS EUC services. To capture
these metrics, use tools like
[Microsoft
Performance Monitor](https://techcommunity.microsoft.com/t5/ask-the-performance-team/windows-performance-monitor-overview/ba-p/375481) or third-party solutions like

[Liquidware
Stratusphere UX](https://www.liquidware.com/products/stratusphere-ux) and

[Control-Up DX
solutions](https://www.controlup.com/).

Once your workload is in production, continually monitor relevant metrics, helping you
react to changing requirements by adjusting the bundle and instance type.  [Monitor
your WorkSpaces health using the WorkSpaces CloudWatch automatic dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html), which provides
insight into the performance of your WorkSpaces resources and helps you identify performance
issues. [Amazon WorkSpaces Applications fleet usage, instance, and session Performance Metrics](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html) are available in
the WorkSpaces Applications console and Amazon CloudWatch.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

AWS EUC services offer a variety of different bundles and instance types, including
GPU-enabled choices. Assuming you have captured and analyzed your metrics in an existing
reference environment, you can map your workloads to the most cost-effective Amazon WorkSpaces or
WorkSpaces Applications bundles and instance types. If you have use cases that require a GPU and are
heavily utilized (high number of hours per month), consider using WorkSpaces Applications, which gives you
a more granular choice of GPU-enabled instances. Use the [AWS Pricing Calculator](https://calculator.aws/#/) or the [Amazon WorkSpaces Applications Pricing](https://aws.amazon.com/appstream2/pricing/?nc1=h_ls) tool to determine which of
the two solutions is more cost-effective for your specific workload.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost05-bp03.html*

---

# EUCCOST05-BP04 Choose an appropriate running mode for your EUC workload where applicable

Amazon WorkSpaces can be used with monthly and hourly pricing, while Amazon WorkSpaces Applications supports
Always-On, On-Demand, and Elastic fleets. Choosing an appropriate running mode can
significantly impact the cost of your EUC services. Historical usage data (usage patterns)
of a reference environment can help you assess which running mode to use for your EUC
workloads.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

When you use Amazon WorkSpaces, you can choose between
Always-On and On-Demand running modes, which translate into
monthly and hourly billing respectively. For the non-GPU
bundles, there is a breakeven point at roughly 80 hours of
usage per month, at which point the Always-On WorkSpace will
be more cost-effective. If your users use their WorkSpace for
less than 80 hours per month, the On-Demand running mode is
usually the more cost-effective model for non-GPU bundles.

You can deploy the
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/) to get reports with
recommendations on which running mode to select for your
WorkSpaces and automatically convert your WorkSpaces to the
most cost-effective running mode. For the GPU bundles,
the breakeven point varies from bundle to bundle. The
[Amazon WorkSpaces
Pricing](https://aws.amazon.com/workspaces/pricing/) page helps you calculate the breakeven point
for these bundles.

Amazon WorkSpaces Applications offers three different fleet types: Always-On, On-Demand, and Elastic.
Explore the fleet types to determine the right balance between cost-effective operation
and desired user experience.

- With Always-On fleets, your fleet instances will
constantly be running while the fleet is in a started
state, and you'll be charged the respective instance fee
per hour per instance in your fleet.
- On-Demand fleets have those fleet instances not in use in
a stopped state, for which you'll be charged the lower
stopped instance fee per hour per stopped instance in your
fleet.

This can make a significant difference to your cost,
especially when your fleet instances are higher-end
instances.
- However, using On-Demand fleets will prolong the logon
time by up to 120 seconds.
- Both Always-On and On-Demand fleet instances are
charged on one-hour increments, while Elastic Fleet
instances are charged on one second increments, with a
minimum of 15 minutes.

- As opposed to Always-On and On-Demand, Elastic fleets do
not require you to manage scaling policies and provision
buffer capacity, since the pool of Instances in an Elastic
fleet is managed by WorkSpaces Applications.

Amazon WorkSpaces Applications offers multi-session fleets, which allow multiple users to use a single
WorkSpaces Applications fleet instance. Depending on the user density you can achieve on a given instance,
you may be able to further optimize your WorkSpaces Applications costs compared to a single-session fleet.
If you plan to use multi-session fleets, consider resource requirements, instance
specifications, and user behavior. For specific guidance, see [Multi-Session
Recommendations](https://docs.aws.amazon.com/appstream2/latest/developerguide/multi-session-recs.html) .

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost05-bp04.html*

---

# EUCCOST06 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# EUCCOST06-BP01 Explore a bring your own license (BYOL) approach

If you already have suitable license agreements with Microsoft
in place for Operating Systems or Microsoft Remote Desktop
Client Access Licenses, consider bringing these licenses for use
with AWS EUC services to reduce the cost.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

If you meet the requirements stated in [Amazon WorkSpaces FAQs](https://aws.amazon.com/workspaces/faqs/?nc1=h_ls#Windows_BYOL), Amazon WorkSpaces
allows you to [Bring Your Own Windows
desktop licenses in WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html) (BYOL) for Windows 10 and 11. This can reduce
your monthly or hourly WorkSpaces charges. When calculating the TCO, consider that BYOL
requires a certain minimum commitment of WorkSpaces per AWS Region that you want to deploy
in.

When using Amazon WorkSpaces Applications, you'll be charged a monthly user fee in the form of a
Microsoft RDS SAL fee. For more information , see [Amazon WorkSpaces Applications pricing](https://aws.amazon.com/appstream2/pricing/?nc1=h_ls). If you have
Microsoft License Mobility, you may be eligible to bring your own Microsoft RDS Client
Access License (CAL) licenses and use them with Amazon WorkSpaces Applications. For users covered by your own
licenses, you won't incur monthly WorkSpaces Applications user fees.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost06-bp01.html*

---

# EUCCOST07 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# EUCCOST07-BP01 Use the available cost optimizers for Amazon WorkSpaces and Amazon WorkSpaces Applications

Leverage available tools from AWS and partners to support you
with cost monitoring and optimization.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Amazon WorkSpaces Applications uses app block and image builders that are charged hourly or in one second
increments with a 15-minute minimum if you keep them running. You must explicitly stop
them to stop the billing. The [Cost Optimizer
for Amazon WorkSpaces Applications](https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2) can monitor your WorkSpaces Applications app block and image builders and notify
you or stop them when they are active for longer than specified thresholds.

Third-party tools like the [AppStream
Optimizer by Cambrian Technologies](https://www.cambriantechnologies.com/solutions/appstream-optimiser/) use machine learning to optimize your WorkSpaces Applications
Fleets and achieve a better utilization. This helps reduce your cost by reducing idle
capacity.

Deploy the
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/) to receive reports with
recommendations on which running mode to select for your
WorkSpaces and automatically convert your WorkSpaces to the
most cost-effective running mode.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost07-bp01.html*

---

# EUCCOST08 — Optimize over time

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# EUCCOST08-BP01 Monitor your Amazon WorkSpaces usage, and implement the Cost Optimizer for Amazon WorkSpaces

The Cost Optimizer for Amazon WorkSpaces generates reports you
can use to understand the usage of individual WorkSpaces. Based
on these reports, identify underutilized WorkSpaces or
WorkSpaces that are no longer in use so that you can assess
whether to terminate them.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Deploy the Cost Optimizer for Amazon WorkSpaces, and perform
regular reviews of your WorkSpaces usage reported by the Cost
Optimizer for Amazon WorkSpaces. Based on your findings,
decide which WorkSpaces to terminate, and initiate a
conversation with owners of underutilized WorkSpaces to
understand if these are still needed. Agree on how, when, and
by whom any changes are to be applied.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost08-bp01.html*

---

# EUCCOST08-BP02 Monitor your Amazon WorkSpaces Applications fleet utilization, and optimize scaling policies and buffer capacity

Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/?nc1=h_ls) to observe and
monitor your Amazon WorkSpaces Applications resources. Amazon WorkSpaces Applications publishes several [WorkSpaces Applications
Metrics and Dimensions](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-with-cloudwatch.html) to Amazon CloudWatch that you can visualize and use to check if you
are overprovisioning buffer capacity or if you are running into capacity shortages at times.
Use these metrics to adjust your WorkSpaces Applications Fleet capacity and scaling policies to minimize idle
capacity and reduce insufficient capacity errors where possible.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Create your own customized CloudWatch dashboards to visualize key WorkSpaces Applications metrics for your
WorkSpaces Applications fleets. These dashboards can contain several widgets that display a view of
selected metrics of a specific WorkSpaces Applications fleet or across multiple WorkSpaces Applications fleets. Review these
dashboards on a regular basis.

Additionally, use the EUC Toolkit to review Amazon CloudWatch and OS-level metrics. This
Toolkit also helps you manage large WorkSpaces and WorkSpaces Applications deployments at scale. After review of
the metrics, determine whether changes to the fleet capacity or scaling policies are
required, and plan for how to implement those changes. For more information, see [Use the EUC
Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost08-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
