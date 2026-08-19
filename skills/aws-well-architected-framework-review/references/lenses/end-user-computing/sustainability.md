# Sustainability

**Pillar**: Sustainability  
**Questions**: 8

---

# EUCSUS01 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 2

---

# EUCSUS01-BP01 Choose the appropriate fleet type

By selecting [Always-On instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html) in WorkSpaces Applications, your instances are constantly kept running and
ready to receive user connection. With [On-Demand](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html), your instances will be provisioned based on your scaling policies, but
instances start only when users initiate the connection. [Elastic
fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html) is a fleet of instances managed by AWS directly, and you only pay when your
user is launching a new session and there is no scaling management.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Encourage the usage of On-Demand fleet type. With On-Demand, streaming instances run
only when users are streaming and therefore have a lower carbon footprint in comparison to
Always-On fleets. The number of streaming instances will still require auto scaling rules.
Once the user disconnects, the instance is terminated.

An additional option is to select a multi-session fleet according to the performance
pillar to select the right instances type.

Elastic fleets offer a pool of streaming instances managed by WorkSpaces Applications service. When you
use Elastic fleets, an app block (also known as a virtual hard disk) will be downloaded
and mounted from Amazon S3. You do not have to configure scaling policies, so you will not
consume and reserve unnecessary resources. Elastic fleets do not support domain join, for
further details see: [Using Active Directory with WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus01-bp01.title.html*

---

# EUCSUS01-BP02 Choose the appropriate running mode for your Amazon WorkSpaces

The running mode of a WorkSpace determines its immediate
availability and how you pay for it (monthly or hourly). You can
choose between the following running modes when you create the
WorkSpace:

- **AlwaysOn:** You are paying
a fixed monthly fee for unlimited usage of your WorkSpaces.
This mode is best for users who use their WorkSpace full
time as their primary desktop.
- **AutoStop:** You are paying
for your WorkSpaces by the hour. With this mode, your
WorkSpaces stop after a specified period of disconnection,
and the state of apps and data is saved.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

AutoStop instances are stopped when users disconnect and
therefore help lower the carbon footprint associated with
WorkSpace instances in comparison to AlwaysOn instances. Below
a certain threshold, which depends on the bundle selected, we
recommend AutoStop mode.

Use
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/) to set the
[appropriate
running mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html) of a WorkSpaces based on past usage and
improve the sustainability position for WorkSpace
environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus01-bp02.html*

---

# EUCSUS02 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 1

---

# EUCSUS02-BP01 Select the instance type or bundle to match software requirement and user personas

Consider the performance needs, cost implications, and any
specific workload characteristics (for example, GPU
requirements). Benchmark and test different instance types to
find the best fit for your workload. Regularly review and adjust
your instance type selection as your application's demands
change over time.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

WorkSpaces Applications offers eight [instance families](https://docs.aws.amazon.com/appstream2/latest/developerguide/instance-types.html) and
a set of instance types per family. Explore these instance families and types to identify
the appropriate requirement for each use case. For graphics workloads, use Graphics G4dn
and Graphics G5. Once you have defined the instance family, you can benchmark at least two
instances type to identify the best choice.

Amazon WorkSpaces offers
[nine
bundles](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundle-options.html), from value to GraphicsPro.g4dn. Once you have
selected applications and usage for each use case, identify
the requirement in term of CPU, memory, and GPU for each of
them.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus02-bp01.html*

---

# EUCSUS03 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 2

---

# EUCSUS03-BP01 Adapt your WorkSpaces Applications fleet timeout

Configure timeouts for WorkSpaces Applications fleets to minimize unnecessary resource consumption
whilst also factoring in usability. Minimize resource consumption by verifying that
instances are not consuming resources unnecessarily when users are not using them or
unlikely to use them.

Usability is an important consideration when shortening
timeouts. Setting them too low results in sessions being
terminated too early with the risk of impacting user
productivity, whereas setting them too high results in instances
running without any users, which incurs a higher carbon
footprint as well as higher costs.

Strike an appropriate balance in timeout durations to maintain
user productivity while reducing resource consumption in periods
of low usage.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

You can select a session duration to configure a maximum active session for a user,
which defaults to 16 hours. Disconnect timeout and idle disconnect timeout determine when
to log off an existing user session. By default, they are both configured at 15 minutes
each. The default value can be reduced without disrupting the end user experience.

For example, you can set the idle disconnect timeout for five minutes. You can set
timecout configurations in the [fleet console](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus03-bp01.html*

---

# EUCSUS03-BP02 Adapt the AutoStop timeout and idle disconnect timeout for Amazon DCV

The AutoStop timeout in WorkSpaces is only available with AutoStop. This is not applicable
to AlwaysOn WorkSpaces. In WorkSpaces, you can configure how long a user can be inactive while
connected to a WorkSpace before they are disconnected. Amazon DCV (Desktop Cloud Virtualization)
is the remote display protocol used by Amazon WorkSpaces to stream pixels, keystrokes and mouse
movements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

By default, AutoStop time (in
hours**)** is set to one hour,
which means that the WorkSpace stops automatically an hour
after the WorkSpace is disconnected.  Keep the AutoStop time
at the default value, as this is the lowest value offered.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus03-bp02.html*

---

# EUCSUS04 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 1

---

# EUCSUS04-BP01 Implement a scaling methodology in WorkSpaces Applications

Scaling policies improve resource utilization and cost
management for application streaming workloads.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Either fleet type (On-Demand or Always-On) requires a
methodology to verify that the appropriate number of instances
are available when users initiate a connection.

A combination of step scaling, scheduled scaling, or target
tracking scaling is recommended to match each fleet usage. To
avoid extra consumption of instances, monitor your fleet usage
and modify your scaling policies accordingly. The following
resources describe in further detail the differences between
the types of scaling and how to configure them to align with
the pattern of usage for the applications being delivered.
Keep in mind that the fleet type choice is only available
during the fleet creation process.

- [WorkSpaces Applications Fleet Types](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html)
- [Fleet Auto Scaling for Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html)
- [Scaling Your Desktop Application Streams with Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/compute/scaling-your-desktop-application-streams-with-amazon-appstream-2-0/)
- [Scale your Amazon WorkSpaces Applications fleets](https://aws.amazon.com/blogs/desktop-and-application-streaming/scale-your-amazon-appstream-2-0-fleets/)
- [Monitoring Amazon WorkSpaces Applications Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus04-bp01.html*

---

# EUCSUS05 — Software and architecture

**Pillar**: Sustainability  
**Best Practices**: 1

---

# EUCSUS05-BP01 Optimize machine image creation, copying, and sharing to each environment (like development, testing, and production)

Using automation with machine images facilitates scalability and
elasticity, minimizing over-provisioning and associated energy
consumption. Centralized management and compliance reporting
further support sustainability initiatives. Overall, automation
pipelines contribute to lower environmental impact and improved
resource optimization.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Use a dedicated and separate account to create your Amazon AppStream images to manage your
changes and your image history. Push the image (copy or share) with other development or
production AWS accounts. For more detail, see [UpdateImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateImagePermissions.html) and [UpdateWorkspaceImagePermission](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus05-bp01.html*

---

# EUCSUS06 — Software and architecture

**Pillar**: Sustainability  
**Best Practices**: 2

---

# EUCSUS06-BP01 Stop image builders and app block builders when not in use

In WorkSpaces Applications, image builders and app block builders are two instances used only when
creating your baseline image or application package. There is no requirement to keep them
running.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

The [Cost Optimizer for Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/cost-optimizer-for-amazon-appstream-2-0-on-the-solutionist/) monitors your WorkSpaces Applications image builders, notifying
you and halting them when they are active for longer than specified thresholds.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus06-bp01.html*

---

# EUCSUS06-BP02 Implement the Cost Optimizer for Amazon WorkSpaces

The
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/) analyzes your Amazon WorkSpaces usage data and automatically converts the WorkSpace
to the most cost-effective billing option (hourly or monthly),
depending on your individual usage.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

This solution analyzes your Amazon WorkSpaces usage data and
automatically converts WorkSpaces to the most cost-effective
billing option (hourly or monthly). This verifies that the
lowest carbon footprint and cost is associated with each
individual WorkSpace instance based on the unique usage
pattern for each user. This data provides the opportunity to
identify usage of WorkSpaces and delete unused WorkSpaces
through the definition of a rule.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus06-bp02.html*

---

# EUCSUS07 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# EUCSUS07-BP01 Identify the volume and data requirement for your user profiles

Each user persona may require different volume and performance to
align with your business case.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Limit user data to application data and mandatory user data
profile. It is a best practice to monitor the storage usage of
home folders, application settings persistence, or other storage
solutions like FSLogix, OneDrive, and Google Drive. With
FSLogix, enable de-duplication in FSx and VHD disk compaction.
Fsx for Windows / Fsx on tap.

For more information, see:

- [How
Application Settings Persistence Works](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-it-works-app-settings-persistence.html)
- [Use
Amazon FSx for Windows File Server and FSLogix to Optimize Application Settings Persistence on Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/use-amazon-fsx-and-fslogix-to-optimize-application-settings-persistence-on-amazon-appstream-2-0/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus07-bp01.html*

---

# EUCSUS08 — Hardware and services

**Pillar**: Sustainability  
**Best Practices**: 2

---

# EUCSUS08-BP01 Extend device lifecycle, and review a bring your own device (BYOD) strategy

The strategy defines policies for device usage, security, and
compliance while optimizing costs through efficient lifecycle
management. Implementing a robust device lifecycle strategy
fosters standardization, security, and productivity across an
organization's device fleet.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

By using either WorkSpaces Applications or WorkSpaces, you can extend your device lifecycle. The
performance of the local device will not be affected, and a low-performance device can
connect and stream an intensive application. Examples of this strategy include Windows
laptops, Chromebooks, or other user-owned devices.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus08-bp01.html*

---

# EUCSUS08-BP02 Migrate end users to a thin client or web-based client device

Thin client or web-based client devices can reduce investment
and are aligned to the previous best practice.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

With WorkSpaces Thin Client, you can offer a device with a direct connection to WorkSpaces Applications or
WorkSpaces and WorkSpaces Secure Browser. The total lifecycle carbon emission for Amazon WorkSpaces Thin
Client is 77kg CO2e as verified by the Carbon Trust. For more information, see [Amazon WorkSpaces Thin Client has received Carbon Trust verification for the product's carbon
footprint](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-workspaces-thin-client-carbon-trust-verification/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus08-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
