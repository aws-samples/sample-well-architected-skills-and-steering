# EUCPERF01 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# EUCPERF01-BP01 Check Regional support for the required EUC services

Not all AWS regions support EUC services such as WorkSpaces Applications, WorkSpaces and WorkSpaces
Secure Browser.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Check to see if the relevant AWS EUC service is available in your most proximal
Region. If the required service is not available in this Region, check to be sure that you
can deliver the required performance from the Region closest to you or with lowest
latency. For information on EUC Regional support, see:

- [WorkSpaces Regional Support](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html)
- [WorkSpaces Applications Regional
Support](https://www.aws-services.info/appstream.html)
- [WorkSpaces Secure Browser
Regional Support](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html)

The [WorkSpaces Connection
Health Checker](https://clients.amazonworkspaces.com/Health.html) details the latency between a specific endpoint device and the
WorkSpaces service running in each available Region. This data is also a good indicator of
latency for WorkSpaces Secure Browser and WorkSpaces Applications if they are running in the same Region.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf01-bp01.html*

---

# EUCPERF01-BP02 Consider the requirements of your Availability Zones when architecting your AWS EUC services

Within each Region, only select Availability Zones support each AWS EUC service. This
is important if you are architecting solutions with extreme performance or security
requirements that demand that applications and desktops reside on the same subnet as the
user data they need to access.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

For the WorkSpaces service line, explore the Availability Zone information.

- [Amazon WorkSpaces Availability Zone Support](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html)
- [Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html)

For WorkSpaces Applications, selecting a subnet when creating a new fleet automatically checks
if the associated Availability Zone can support the requested requirements, which are
based on several criteria such as instance type and availability.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf01-bp02.html*

---

# EUCPERF01-BP03 Consider disaster recovery (DR) requirements when architecting your AWS EUC solution

Will a secondary Region support the latency that is acceptable to support the selected
AWS EUC service in a DR scenario, or can you accept degraded performance and relaxed
service level agreements to continue to do business?

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

For WorkSpaces, the use of cross-Region redirection or Multi-Region Resilience allows the
manual or partially automated process of using alternate regions to support your WorkSpaces
users in the event of a serious outage.

For WorkSpaces Applications, the master images created in one Region can be copied to a
secondary Region to enable the configuration of identical regional deployment for DR
purposes.

Review each of these DR features to be sure that they offer adequate performance and
capabilities depending on the Region that is selected for the purpose.

You should also replicate user data and other critical backend services in each
Region to provide localized access if similar levels of performance are expected in a DR
scenario.

For more detail on Cross-Region redirection and Multi-Region Resilience, see [Business continuity for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/business-continuity.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf01-bp03.html*

---
