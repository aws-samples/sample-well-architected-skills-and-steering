# Reliability

**Pillar**: Reliability  
**Questions**: 6

---

# HNREL01 — Foundations

**Pillar**: Reliability  
**Best Practices**: 2

---

# HNREL01-BP01 Implement redundant power infrastructure

Deploy dual power feeds, redundant uninterruptible power supply
(UPS) systems, and backup generators for all critical network
equipment. Regularly test and maintain power systems to ensure
continuous operation during outages.

**Desired outcome:** Sustain
on-premises operations and prevent downtime during power failures.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Avoid unexpected outages due to power disruptions
- Supports continuous network connectivity to cloud
- Satisfies disaster recovery and business continuity requirements
- Prevents a single-point power failure

## Implementation guidance

- Use dual utility or grid power where available
- Maintain redundant UPS and generator systems
- Schedule and document periodic power failover drills

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel01-bp01.html*

---

# HNREL01-BP02 Maintain effective life cycle management for on-premises network equipment

Implement a structured life cycle management process for all
on-premises networking equipment, including routers, switches, and
cabling. Track equipment age, support contracts, firmware, and plan
for timely refreshes and replacement to avoid end-of-life risks.

**Desired outcome:** All network
hardware supporting hybrid connectivity remains supported, secure,
and reliable throughout its operational life.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Reduces risk of unplanned outages due to equipment failure
- Ensure continued vendor support and security patching
- Simplifies compliance and audit for critical infrastructure
- Prevents operational surprises from obsolete hardware

## Implementation guidance

- Maintain an asset inventory with warranty or support
expiration dates
- Monitor firmware and software for patches and end-of-support
notices
- Budget for regular equipment refresh and upgrade cycles
- Retire or replace equipment before it reaches end-of-life
- Document and regularly review network equipment management
procedures

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel01-bp02.html*

---

# HNREL02 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# HNREL02-BP01 Monitor network service provider maintenance events

Implementing a proactive monitoring and response system for
scheduled network maintenance activities is crucial for minimizing
service disruptions. By establishing a methodical framework to track
maintenance notifications and planned network events, teams can
prepare effectively, strategically schedule necessary changes during
designated maintenance windows, and ensure continuous network
connectivity throughout the process. This systematic approach
enhances operational resilience while reducing the impact of
essential maintenance on critical services

**Desired outcome:**

- Get timely notifications about links connecting the on-premises
data center to the cloud.
- Enables proper planning for scheduled activities, minimizes
service disruptions, and ensures optimal management of hybrid
network connectivity.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Proactive maintenance planning and reduces the risk of
unexpected service disruptions.
- Better coordination during maintenance windows with business
operations, minimizing impact on critical workloads.
- Enhanced visibility into service health and upcoming changes

## Implementation guidance

- Integrate service provider notifications into monitoring and
observability platforms. For example, you can achieve this
using Amazon EventBridge to send AWS Direct Connect
maintenance messages.

## Resources

- [AWS Direct Connect maintenance](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dx-maintenance.html)
- [Monitoring
events in AWS Health with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
- [How
can I get notifications for AWS Direct Connect scheduled
maintenance or events](https://aws.amazon.com/premiumsupport/knowledge-center/get-direct-connect-notifications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel02-bp01.html*

---

# HNREL03 — Change management

**Pillar**: Reliability  
**Best Practices**: 2

---

# HNREL03-BP01 Monitor the bandwidth and scale the bandwidth as needed

Regularly monitor the bandwidth usage of your dedicated connection.
If usage consistently approaches the connection limit, order
additional dedicated connections and aggregate them into a LAG to
increase bandwidth and resilience with minimal downtime.

**Desired outcome:** Avoid service
degradation or outages due to bandwidth limitations by proactively
scaling your hybrid connectivity.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Prevent performance bottlenecks and dropped traffic
- Enables cost-effective scaling of hybrid network connectivity
- Supports growth in hybrid workload demand
- Ensures seamless failover and aggregation

## Implementation guidance

- Monitor metrics for all dedicated connection and IPSec VPN
links.
- Create alarms for sustained high utilization.
- Plan and implement LAG to aggregate bandwidth and connections.

## Resources

- [How
can I migrate virtual Interfaces to Direct Connect connections
or LAG bundles?](https://repost.aws/knowledge-center/migrate-virtual-interface-dx-lag)
- [Direct
Connect link aggregation groups (LAGs)](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html)
- [Monitoring
Direct Connect with CloudWatch](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel03-bp01.html*

---

# HNREL03-BP02 Monitor logs and metrics for insights of hybrid networking resources

Monitor dedicated connection and VPN logs and metrics to gain
insight into the health and status of your hybrid connectivity. Use
monitoring service to create alarms and notifications when
thresholds are breached or significant events occur.

**Desired outcome:** Gain
comprehensive insights that improve the performance, reliability,
and security of hybrid network environments.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables proactive detection and alert on connectivity or
capacity issues
- Supports troubleshooting and root-cause analysis
- Improves operational visibility and service reliability
- Reduces time to resolution for incidents

## Implementation guidance

- Set up alarms for key metrics of dedicated connection and
IPSec VPNs.
- Monitor logs for anomalies, errors, or connection state
changes.
- Use automation for incident response when alarms are
triggered.

**Resources:**

- [AWS Direct Connect: Monitor with Amazon CloudWatch](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)
- [Monitor
AWS Site-to-Site VPN tunnels using Amazon CloudWatch](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-cloudwatch-vpn.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel03-bp02.html*

---

# HNREL04 — Failure management

**Pillar**: Reliability  
**Best Practices**: 4

---

# HNREL04-BP01 Use physical location redundancy to host dedicated connections

Design dedicated connections hosted at multiple geographically
separated data centers or colocation facilities to provide physical
location redundancy. This design ensures that your connectivity to
cloud remains available even if one location is affected by an
outage or disaster.

**Desired outcome:** Maintain high
availability and business continuity for hybrid connectivity, even
in the event of a site-level failure.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Minimizes the risk of a single point of failure
- Enhance disaster recovery capabilities
- Supports compliance and uptime requirements
- Increases overall hybrid network resilience

## Implementation guidance

- Deploy Direct Connect connections in at least two
geographically distinct locations.
- Route traffic dynamically between locations for failover.
- Test failover scenarios regularly to validate resilience.

**Resources:**

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp01.html*

---

# HNREL04-BP02 Use redundant hardware and telecommunication providers

When designing remote connections to your cloud provider, use
redundant on-premises hardware and diverse telecommunications
providers. Ensure your last-mile connectivity has diverse physical
paths and that providers offer SLAs that meet your uptime
requirements.

**Desired outcome:** Reduce the risk
of connectivity loss due to hardware failure or carrier issues,
supporting continuous access to cloud resources.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Mitigates risks from hardware or provider outages
- Increases fault tolerance and connection reliability
- Supports compliance with high-availability SLAs
- Provides business continuity during provider-specific
disruptions

## Implementation guidance

- Use at least two separate routers, switches, and cabling for
each Direct Connect location.
- Contract with multiple telecommunications providers for
circuit diversity.
- Periodically review provider SLAs and test failover.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp02.html*

---

# HNREL04-BP03 Use dynamic routing for automatic failover

Implement dynamically routing for dedicated connections and IPSec
VPN connections using BGP to enable automatic load balancing and
failover across redundant links.

**Desired outcome:** Ensure seamless
failover and traffic distribution across all available network
paths, minimizing downtime and manual intervention.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables automatic failover in the event of a connection failure
- Balances network traffic for optimal performance
- Reduces manual intervention and operational overhead
- Increases resilience of hybrid connectivity

## Implementation guidance

- Use BGP for dynamic routing between on-premises and cloud
networks.
- Regularly validate routing and failover with controlled tests.

## Resources

- [BGP
Negotiation over AWS Site-to-Site VPN and Direct Connect:
Troubleshooting Strategies for Efficient Networking](https://repost.aws/articles/ARIKYhXEYyQQqtO2ulKERrbw/bgp-negotiation-over-aws-site-to-site-vpn-and-direct-connect-troubleshooting-strategies-for-efficient-networking)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp03.html*

---

# HNREL04-BP04 Provision sufficient network capacity

Provision enough network capacity so that the failure of a single
network connection does not overwhelm or degrade the remaining
redundant connections.

**Desired outcome:** Maintain
performance and service levels during network outages or planned
maintenance by ensuring available bandwidth meets business needs.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Avoids performance bottlenecks during failover
- Ensure sufficient capacity for critical workloads at all times
- Supports scalability and growth in hybrid environments
- Enhances customer and user experience

## Implementation guidance

- Analyze peak and average bandwidth requirements for hybrid
workloads.
- Size redundant connections so any one connection can handle
the full load if others fail.
- Monitor bandwidth usage and adjust capacity proactively.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp04.html*

---

# HNREL05 — Failure management

**Pillar**: Reliability  
**Best Practices**: 1

---

# HNREL05-BP01 Failover testing of dedicated connections

Regular failover testing of dedicated connections is essential for
ensuring the resilience and reliability of hybrid network
environments. Simulating various scenarios by temporarily disabling
BGP peering sessions between on-premises networks and cloud. By
regularly exercising these tests, organizations can validate their
recovery procedures, uncover latent bugs, and ensure their hybrid
network architecture performs as expected during failover scenarios.

**Desired outcome:** Verify that
failover and recovery procedures for Direct Connect connections work
as intended, minimizing downtime during real incidents.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Uncovers misconfigurations or gaps in failover processes
- Increases confidence in your recovery plans
- Enables you to proactively address weaknesses before actual
failures
- Reduces business impact of network outages

## Implementation guidance

- Simulated BGP failures of dedicated connections and observe
failover behavior, using services such as the AWS Direct Connect Resiliency Toolkit.
- Test all redundant dedicated connections and VPN links to
ensure expected failover behavior.
- Document and refine your recovery steps based on test
outcomes.
- Repeat testing regularly and after significant changes.

## Resources

- [AWS Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel05-bp01.html*

---

# HNREL06 — Failure management

**Pillar**: Reliability  
**Best Practices**: 2

---

# HNREL06-BP01 Use multiple data centers for physical location redundancy

Connect from multiple geographically separate data centers or
colocation sites to cloud for true physical location redundancy. Use
dynamically routed, Active/Active connections across these sites to
enable automatic load balancing and failover.

**Desired outcome:** Ensure network
connectivity to cloud remains available even if one location
experiences an outage or disaster.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Eliminates single points of failure at the physical site level
- Enables business continuity and disaster recovery
- Supports high availability and compliance requirements
- Improves resilience to disasters or unplanned events

## Implementation guidance

- Deploy dedicated connections from at least two geographically
distinct facilities.
- Use dynamic routing BGP for automatic failover.
- Test failover regularly to validate resiliency.

## Resources

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel06-bp01.html*

---

# HNREL06-BP02 Ensure service continuity with redundant hardware and diverse telecommunications providers

Implementing redundant hardware components across geographic
locations, organizations can mitigate single points of failure that
threaten critical workloads. This resilience strategy should extend
beyond computing resources to include diverse telecommunications
providers, creating independent network paths that remain
operational even when regional carriers experience outages. The
combination of hardware redundancy and carrier diversity creates a
robust foundation that enables businesses to maintain operations
through localized disruptions, ensuring that customers experience
minimal service interruptions and that service level agreements
remain intact despite infrastructure challenges.

**Desired outcome:** Reduce risk of
connectivity loss due to hardware or carrier failures, maintaining
consistent hybrid network availability.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Increases fault tolerance and uptime
- Minimizes downtime from single hardware or carrier outages
- Supports disaster recovery planning
- Helps meet or exceed AWS and provider SLA commitments

## Implementation guidance

- Use separate network devices and cables for each connection.
- Engage more than one telecom provider with diverse paths for
"last mile" connections.
- Periodically review and test infrastructure and SLAs.

## Resources

- [AWS Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel06-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
