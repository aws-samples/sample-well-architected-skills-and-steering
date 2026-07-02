# EUCPERF02 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# EUCPERF02-BP01 Identify geographic distribution of end users and design to minimize latency

When migrating to or implementing AWS EUC services, consider the location of each
group of users with respect to the service endpoints for AWS WorkSpaces, WorkSpaces Applications, or
WorkSpaces Secure Browser. You should deliver services from the Region with the lowest latency to
most users.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Capture the location of each user group, and calculate the average latency between
each group and their most proximal AWS Region that supports the required AWS EUC
service. Due to Regional network routing and capabilities, it is possible the most
proximal AWS Region does not necessarily offer the lowest latency.

If you must deploy AWS EUC services in a non-optimal Region (which is sometimes
necessary to access other AWS services which have already been deployed), then be sure
that you test your application to verify that they offer acceptable performance at the
latency levels being experienced.

For an example of how latency might affect the user experience, see [EUC latency
trade-offs](https://guide.aws.dev/en/articles/ARiy3h1QGUSWePxGqdV_SYLA).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf02-bp01.html*

---

# EUCPERF02-BP02 Scale your EUC environment to accommodate the required number of end users

The number of users accessing the selected AWS EUC service should not affect the
performance of the service itself, as AWS provides both scale and resilience for the
components that affect authentication and streaming of user sessions. Many supporting
components, however, need to be scaled to support the user numbers you intend to deploy.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Understand the backend requirements for your deployment and scale them accordingly.
For example, a WorkSpaces compute instance with 2 vCPU and 4Gb of RAM may offer acceptable
performance to run a targeted application set, but if access to user data or an
application database backend is compromised by server performance or network constraints,
then the user may complain that WorkSpaces is performing badly. Ideally, perform end to end
testing for each application set using scalability testing tools to be sure that they will
deliver acceptable performance in production as the services scale.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf02-bp02.html*

---

# EUCPERF02-BP03 Evaluate external data sources that your environment integrates with, and assess its impact on performance

The location of user data and the services used to deliver access to this data are key
to providing the best performance for consumers of an AWS EUC deployment. Latency incurred
while accessing data sources may incur additional delays and contribute to end user
frustration and lack of engagement, as well as increased support calls.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Define a data architecture that describes how data is managed, from collection
through transformation, distribution, and consumption. This informs the EUC architects
where to place key application and desktop delivery services and where optimization may be
required to avoid performance degradation.

If migrating from an existing on-premises EUC architecture, you may need to deploy
[AWS Direct Connect](https://aws.amazon.com/directconnect/) or [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/) connections to provide
access between AWS and your on-premises infrastructure. For best practices related to
networking for Amazon WorkSpaces and descriptions for how and when to use Direct Connect and VPN
connections, see [Best Practices for VPCs and Networking in Amazon WorkSpaces Deployments](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf).

Be sure to architect network solutions with low enough latency and sufficient
bandwidth to support appropriate data access between desktops, applications, and any
on-premises data sources.

If your AWS EUC solution integrates with services offered by other cloud providers,
such as email, collaboration tools, or SaaS applications, be sure to size internet
connections or private networks accordingly to avoid high latency and bandwidth
constraints.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf02-bp03.html*

---
