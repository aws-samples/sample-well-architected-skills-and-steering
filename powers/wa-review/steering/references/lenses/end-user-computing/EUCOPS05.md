# EUCOPS05 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# EUCOPS05-BP01 Identify monitoring tools to provide the expected levels of insight into operational performance

While existing, familiar tools can be used to monitor an AWS EUC deployment, there
are many AWS services, such as automatic Amazon CloudWatch dashboards for Amazon WorkSpaces and Amazon
AppStream, AWS CloudTrail for API call monitoring, and Amazon Kinesis for log propagation and
centralized log storage.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Implement proactive monitoring of the health of all aspects of an AWS EUC
deployment to quickly identify and remediate problems that affect the user population,
their productivity, and any impact this may have on the business.

For both Amazon WorkSpaces and Amazon WorkSpaces Applications, it is important to monitor both the
service itself in addition to any external service dependencies. Consider the following
monitoring tools:

**Amazon WorkSpaces**

Amazon CloudWatch provides an automatic dashboard which gives an overview of overall service
health, including:

- Available or unhealthy WorkSpaces
- Session launch times
- Connection success and failure
- Session latency
- Users connected, disconnected, stopped, or in maintenance

Additional metrics, such as instance specific CPU, memory, and disk performance can
also be viewed. Develop custom CloudWatch widgets to fine tune the monitoring of specific groups
of WorkSpaces.

[Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-monitoring-alerting.html)

Amazon CloudWatch provides an automatic dashboard which gives an overview of overall service
health, including fleet capacity and utilization.

CloudWatch alarms can be configured to send alerts when specific thresholds are met.

Each WorkSpaces and Amazon WorkSpaces Applications instance exposes a network interface in the
customers managed VPC which can be addressed by third party monitoring tools for
traditional management.

As AppStream instances are ephemeral, logs required for compliance or historical
monitoring, such as event logs, can be harvested at user logoff or shutdown using session
scripts or in real time using services such as Amazon Kinesis.

**External dependencies**

Monitoring should also be in place for:

- Internet connectivity (user to Amazon WorkSpaces or Amazon WorkSpaces Applications service)
- Amazon networking
- Active directory
- RADIUS (or other MFA provider)
- Microsoft PKI (If certificate-based authentication is in use)
- SAML 2.0 Identity Provider (IdP) availability (If SAML 2.0 authentication is in
use)
- Private certificate authority (if certificate-based authentication is in use)
- User data repositories (like file shares and profile stores)
- Application web tiers
- Application database tiers
- Application licensing servers
- Web proxies
- Anti-virus infrastructure

If these services are hosted on Amazon EC2, Amazon CloudWatch can be used to monitor key health
metrics and alert when service degradation is detected.

For services still hosted on-premises, Amazon CloudWatch agents can be installed which send
key metrics to Amazon CloudWatch.

**Log propagation**

For centralized gathering of log files for troubleshooting and retrospective
analysis, Amazon Kinesis agents can be deployed on WorkSpaces or WorkSpaces Applications to deliver real-time
propagation of OS and application-level logs to a central location.

For Amazon WorkSpaces Applications, propagating instance log files in real time to a
centralized location is essential if you need to store logs for compliance purposes, as
AppStream instances are destroyed at the end of each session. For more detail, see [Using the Kinesis Agent to store WorkSpaces Applications Windows event logs](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-kinesis-agent-for-microsoft-windows-to-store-appstream-2-0-windows-event-logs/).

**AWS Health dashboard**

The [AWS Health
dashboard](https://health.aws.amazon.com/health/status) provides insight into the health and availability of AWS services
running across regions. Individual regional services can be filtered in the web page or
added to an RSS feed reader for additional visibility.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops05-bp01.html*

---

# EUCOPS05-BP02 Store and regularly analyze log files to detect anomalous activity and behaviors

Maintaining a central store of log data and performance metrics is frequently a
mandatory requirement if specific compliance standards need to be maintained. Even in the
absence of compliance requirements, maintaining a central store of data facilitates a better
understanding of service scaling, performance, and security enables analysis, which improves
root cause analysis and drives incremental service improvement.

Review the available data sources that provide key insight into the usage of your EUC
environment.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Extracting performance data and log files from both WorkSpaces and WorkSpaces Applications and
storing it centrally is essential if you need to adhere to specific industry compliance
standards or if you want to perform retrospective analysis of data for troubleshooting
purposes, root cause analysis, or predicting service scalability and requirements.

Amazon CloudWatch can be used to capture specific metrics and store the data longer term in
Amazon S3. Amazon Kinesis agents can also be installed on WorkSpaces or WorkSpaces Applications instances to
propagate system logs in real time to a centralized location. For more detail, see [Using Amazon Kinesis Agents to Store AppStream Event Logs](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-kinesis-agent-for-microsoft-windows-to-store-appstream-2-0-windows-event-logs/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops05-bp02.html*

---
