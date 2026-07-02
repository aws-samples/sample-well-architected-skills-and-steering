# MIDASEC07 — Incident response

**Pillar**: Security  
**Best Practices**: 2

---

# MIDASEC07-BP01 Deploy continuous monitoring tools

Implement continuous monitoring of your industrial systems to detect and respond to
threats in real time. Monitoring should span cloud, edge, and on-premises systems across both
IT and OT environments.

**Desired outcome:** Security teams can detect anomalies and
threats early, reducing the impact of potential breaches.

**Benefits of establishing this best practice:** Enables
real-time visibility, faster incident response, and proactive threat mitigation.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS monitoring tools such as Amazon CloudWatch, AWS IoT Device Defender, and AWS Config to gather and analyze telemetry.

### Implementation steps

- Enable Amazon CloudWatch metrics and logs for all AWS workloads.
- Deploy AWS IoT Device Defender to monitor device behavior and audit
configurations.
- Use AWS Config to track configuration changes across resources.
- Integrate alerts with AWS SNS or AWS Security Hub CSPM for real-time response.

## Resources

- [What is AWS IoT Device Defender?](https://docs.aws.amazon.com/iot-device-defender/latest/ug/what-is.html)
- [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/what-is-aws-config.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec07-bp01.html*

---

# MIDASEC07-BP02 Implement SIEM systems

Aggregate and analyze logs from industrial and cloud systems using a security information
and event management (SIEM) system to help detect and respond to threats efficiently.

**Desired outcome:** Centralized visibility across hybrid
environments enables faster detection of coordinated threats or unusual activities.

**Benefits of establishing this best practice:** Improves
threat correlation, reduces alert fatigue, and strengthens compliance with audit trails.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use Amazon Security Lake or integrate with third-party SIEM tools such as Splunk or IBM
QRadar for advanced analytics and incident workflows.

### Implementation steps

- Set up Amazon Security Lake to collect and normalize logs from AWS and industrial
sources.
- Integrate with a SIEM system for event correlation and alerting.
- Define detection rules and dashboards tailored to OT and ICS environments.
- Automate incident response workflows with runbooks or SOAR integrations.

## Resources

- [Amazon Security Lake](https://aws.amazon.com/security-lake/)
- [AWS SIEM Partners](https://aws.amazon.com/partners/siem/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec07-bp02.html*

---
