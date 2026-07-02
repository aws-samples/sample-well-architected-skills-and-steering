# EUCOPS11 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS11-BP01 Create EUC health metrics that allow you to meet your operational goals

Spend time reviewing the available metrics which provide quick and insightful
information into the health of your end-to-end EUC deployment.

**Level of risk exposed if this best practice is not
established:** High

## Implementation Guidance

While the tools and processes required to monitor AWS EUC service health are
discussed earlier, from an operational perspective there are key metrics which, at a
minimum, should be gathered to build a baseline for systems health across the tiers of an
Amazon WorkSpaces or WorkSpaces Applications deployment.

The following guidance discusses both the service specific metrics which should be
gathered in addition to the monitoring other key services which contribute to AWS EUC
service:

**Amazon WorkSpaces and WorkSpaces Applications Service or Instance metrics**

Insight into both service level and instance-based performance metrics are key to
identifying availability problems, performance problems or trends and to provide data for
retrospective problem analysis. Consider gathering the following data, at a minimum, in
order to maximize service efficiency and performance:

**Amazon WorkSpaces:** Amazon CloudWatch provides an automatic dashboard
which gives an overview of overall service health for Amazon WorkSpaces, including:

**Service metrics:**

- Available or unhealthy WorkSpaces
- Session launch times
- Connection success or failure
- Session latency
- Users connected, disconnected, stopped, or in maintenance

**Instance metrics:**

- In-session latency
- Network nealth
- CPU usage
- Memory usage
- Root or user volume space usage

Custom dashboards can also be created which use these metrics to focus on a specific
subset of your WorkSpaces.

- [Monitor WorkSpaces
Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-monitoring.html)
- [Monitor your WorkSpaces using CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html)
- [Creating Custom CloudWatch dashboards for Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-custom-amazon-cloudwatch-dashboards-and-widgets-for-amazon-workspaces/)

CloudWatch Alarms can also be configured to send alerts when specific thresholds are met.
For more information, see [Creating CloudWatch
Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).

**Amazon WorkSpaces Applications:** Amazon CloudWatch provides an automatic
dashboard which gives an overview of overall Amazon WorkSpaces Applications service health,
including:

**Service metrics:**

- Fleet capacity or utilization
- Insufficient capacity errors
- Average actual capacity
- Average available capacity
- Average desired capacity
- Average in use capacity
- Average pending capacity

For multi-session AppStream deployments, additional performance metrics can be viewed
for each instance or session, these metrics will also be available for single session
fleets over time.

**Instance metrics:**

- Instance CPU utilization
- Instance memory utilization
- `PagingFileUtilizationInstance`
- Instance disk utilization

**Session metrics:**

- Session CPU utilization
- Session memory utilization

For more information, see [Viewing Instance and Session Performance Metrics Using the Console](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-instance-session-performance.html).

CloudWatch Alarms can also be configured to send alarms when specific thresholds are met.

- [Using Amazon CloudWatch
alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [Monitoring Amazon WorkSpaces Applications Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html)

**Other key areas to monitor**

The following services, and associated metrics, at a minimum, should be monitored in
order to understand the end to end health and performance of AWS EUC services.

**Networking**

With any cloud hosted desktop and application delivery service such as Amazon WorkSpaces or
Amazon WorkSpaces Applications, users are connecting from a remote location, across a variety of
network types, to a service running in a cloud data center. Once they are connected and
logged in, they are dependent upon a number of backend services which are also connected
to the AWS EUC service using a variety of devices which each have their own performance
characteristics. Each part of the connection process and subsequent interaction with
backend services should ideally, be monitored.

**User endpoint device to AWS EUC service**

The following articles discuss the latency and bandwidth requirements for Amazon WorkSpaces
and Amazon WorkSpaces Applications and tools that can be used to validate service performance:

- [Client
network requirements for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-network-requirements.html)
- [AppStream Latency: Bandwidth Recommendations](https://docs.aws.amazon.com/appstream2/latest/developerguide/bandwidth-recommendations-user-connections.html)
- [Measuring Client to
AWS EUC region latency](https://clients.amazonworkspaces.com/Health.html)
- [Visualizing WorkSpaces Applications session latency metrics using AWS Lambda, Amazon Kinesis Data
Stream and Amazon OpenSearch Service](https://aws.amazon.com/blogs/desktop-and-application-streaming/visualizing-appstream-2-0-session-latency-metrics-using-aws-lambda-amazon-kinesis-data-stream-and-amazon-opensearch-service/)
- [CloudWatch Internet
Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)
- [Utilizing CloudWatch Internet Monitor with Amazon WorkSpaces Personal](https://aws.amazon.com/blogs/desktop-and-application-streaming/utilizing-cloudwatch-internet-monitor-with-amazon-workspaces-personal/)

**AWS EUC compute instance to backend services:**

Consider deploying third party tools which proactively monitor client to server
operations such as network flow between WorkSpaces, WorkSpaces Applications and supporting databases,
data feeds, web servers and file or print services. These data points can be used to
accurately determine service degradation or trends which might identify the need to scale
supporting infrastructure service up or down.

**AWS EUC compute instance to externally hosted services:**

While there are no simple ways to individually gather the performance of compute
instance to external service metrics, many third-party cloud providers provide API's which
can be leveraged to determine service status. Both Microsoft and Google for example,
expose API's that can be used to query individual cloud service availability. It should be
possible to architect a centrally hosted solution which pools key external resources and
uses the metrics gathered to align with internal service availability

**Backend service availability:**

Consider using network analysis tools which can identify the reachability of key
services using ICMP, TCP or application layer health probes. For Amazon WorkSpaces and Amazon
AppStream which are dependent on low latency and available bandwidth, built in client-side
network health tools will identify and notify the end user of performance degradation. In
general, the ability to identify performance baselines for network packet flow is crucial.
This applies to various supporting network infrastructures, including AWS-specific
connections through Direct Connect, as well as connections to and from third-party cloud
infrastructures.

**Storage**:

As discussed previously, both Amazon WorkSpaces and AppStream provide metrics which can
trigger alarms based on certain thresholds such as if disk space is running low, but these
do not include storage performance metrics. As part of your scalability testing during
adoption of AWS EUC services, consider testing disk performance if your application
workload is particularly disk i/o intensive. Some WorkSpaces and AppStream instance types are
'EBS Optimized' offering scalable disk throughput, for both services, GPU enabled
instances offer the highest throughput and additional instance storage. The DISKSPD
utility from Microsoft can be used to create synthetic disk i/o profiles for testing
purposes.

- [Amazon EBS
Optimized Volumes and Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#ebs-optimization-support)
- [Instance store temporary block storage for EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Microsoft: Use DISKSPD to test workload storage performance](https://learn.microsoft.com/en-us/azure-stack/hci/manage/diskspd-overview)

If specific issues arise that require deeper insight into Amazon WorkSpaces or Amazon
WorkSpaces Applications storage performance, consider using Windows Task Manager or Performance
Monitor, or iostat/iotop for Linux instances, to better understand disk i/o performance.

**Active Directory**

Active Directory performance is key to the user experience of Amazon WorkSpaces and AppStream
2.0 users as it directly affects the logon process. A badly performing Active Directory
infrastructure may add significant logon time as Group Policies and Logon Scripts are
processed. If AWS Managed Microsoft AD is being used, CloudWatch can be used to provide insights into
directory performance. For EC2 hosted domain controllers, CloudWatch can also be used to gather
most of the metrics required to identify service degradation. For on-premises AD
controllers, CloudWatch agents can be installed to centralize the collection of appropriate
metrics, such as CPU, Memory, disk I/O and network utilization.

For more information, see [Performance tuning for Active Directory Services](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/).

**SAML 2.0**

SAML integration with AWS EUC services is typically provided by external providers
such as Azure AD, Okta or Ping Identity. These systems usually provide an API which can be
used to extract service level heath metrics for propagation into an existing SIEM system.
Azure Monitor or the Okta System Log API, for example, can be used to understand
availability and performance.

**Certificate-based authentication (CBA)**

If end-to-end single sign-on is required for Amazon WorkSpaces or WorkSpaces Applications deployments
which are integrated with SAML, CBA can be used to emulate a virtual smart card login for
each user. While falling back to a standard AD username and password login is possible if
CBA is unavailable, if you do not elect to use this option it will be essential to
implement monitoring for CBA to avoid login failures. The AWS Private Certificate Authority is a resilient service
by default and presents operational metrics through CloudWatch:

- [Monitor
AWS Private CA with CloudWatch Events](https://docs.aws.amazon.com/privateca/latest/userguide/CloudWatchEvents.html)

As certificate-based authentication relies upon a private certificate authority (PCA)
which in turn requires a Microsoft Certificate Service infrastructure, refer to the
following documentation to understand which key metrics should be monitored:

- [Microsoft: Securing PKI: Appendix A: Events to Monitor](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn786423(v=ws.11))

**Network file services**

Amazon WorkSpaces Applications and WorkSpaces are typically integrated with backend network file
services which provide storage for user data and user profiles. These repositories are
typically critical to employee productivity and should form part of end-to-end service
monitoring. If Amazon FSx for Windows is being used for backend storage, a comprehensive
CloudWatch dashboard is available which exposes system performance. If traditional Windows file
servers are being used in EC2 or on-premises, Microsoft provides direction on how to use
the SMB performance metrics to gather the relevant performance statistics.

- [Monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-cloudwatch.html)
- [Performance tuning for SMB file servers](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/role/file-server/smb-file-server)

**RADIUS**

If RADIUS is being used with Amazon WorkSpaces, the documentation for the RADIUS provider in
use should be consulted as these can be Windows or Linux based and will expose performance
metrics in different ways.

**Application web tiers**

Availability and performance of web tiers that support the applications being
delivered from AWS EUC services is typically controlled by load balancers than can also
execute L2, L4 or L7 health probes to ascertain service health and optionally perform
auto-scaling if required. Refer to your web server vendors documentation for information
on monitoring your specific web tiers.

**Application database tiers**

Availability and performance of database tiers that support the applications being
delivered from AWS EUC services is also key to end-to-end service health. Refer to your
web server vendors documentation for information on monitoring your specific web tiers.

**Application licensing servers**

Monitoring license server availability and performance is critical as failure of
these servers can result in complete denial of service for a specific application tier.
Please refer to your license server or application vendors documentation for information
on monitoring these components.

**Web proxies or app firewalls**

Web proxy and app firewall tiers are typically load balanced and auto scaled for
resilience and scalability, but monitoring these is important as failure of this tier can
result in users being denied Internet access, the impact of which can be significant.
Please refer to your web proxy vendor documentation for information on monitoring these
components.

**Anti-virus infrastructure**

While anti-virus and anti-malware products are unlikely to cause systems outage, from
a security perspective, being sure that Amazon WorkSpaces and WorkSpaces Applications instances are being
effectively protected can avoid wider service outage due to intrusion and malign
interference from external bad actors. Furthermore, understanding and minimizing the
impact of anti-virus and anti-malware scans, is key.

**WorkSpaces and WorkSpaces Applications instance metrics**

Amazon WorkSpaces and WorkSpaces Applications compute instances are standard Windows Client/Server, or
Linux instance types. They each have a network interface exposed to a customer managed VPC
and can be managed and monitored in the same way as traditional desktops.

Amazon CloudWatch can be used to extract instance specific metrics such as CPU, Memory, Disk
or Network utilization, and existing third party tools can be used to extract similar
information.

Be aware that as WorkSpaces Applications is a non-persistent application and desktop delivery
service, instances are terminated and destroyed when the last user session is ended
(consider single session versus multi-session), this needs to be considered when gathering
performance statistics or system logs.

There are a number of utilities created by AWS employees that assist in the
gathering and presentation of AWS EUC instance metrics, the EUC Toolkit for example, can
be used for this purpose, the PowerShell code for this utility can also be downloaded and
used as a reference for building your own PowerShell management utilities.

- [Monitor your WorkSpaces using CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html)
- [Monitoring and Reporting for Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-monitoring-reporting.html)
- [Monitoring Amazon WorkSpaces
Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/monitoring-overview.html)
- [Use
the EUC Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/)

In summary, AWS EUC deployments are dependent on the reliability and performance of
both the Amazon WorkSpaces or WorkSpaces Applications services themselves and also many external systems,
taking a holistic approach to management of each component of the end to end deployment is
key to maintaining end user engagement and productivity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops11-bp01.html*

---
