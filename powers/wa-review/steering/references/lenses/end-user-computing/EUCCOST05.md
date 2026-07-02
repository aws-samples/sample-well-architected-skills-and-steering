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
