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
