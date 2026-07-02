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
