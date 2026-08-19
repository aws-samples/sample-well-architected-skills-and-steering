# Observability

**Saga**: Observability  
**Best Practices**: 21

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.1] Automate alerts for security and performance issues

**Category:** FOUNDATIONAL

Alerts should automatically notify teams when there are indicators of malicious
activity, compromise, or performance degradation. Effective alerting accelerates incident
response times, enabling teams to quickly address and resolve issues before they can
significantly impact system performance or security. Without automatic alerting, teams can
suffer from delayed response times that can lead to prolonged system downtime or increased
exposure to security threats.

Implement centralized alerting mechanisms to track anomalous behavior across all
systems. Define specific conditions and thresholds that, when breached, will raise alerts.
Verify that the alerts are delivered to the appropriate teams by email, text message, or the
team's preferred notification system. Integrating these alerts into your centralized
incident management systems can also help in the automatic creation of tickets, aiding
faster resolution.

In a more advanced workflow, alerts can be integrated with automated governance
systems to start remediation actions immediately upon detection or to gather additional
insights that will aid investigations.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP06 Monitor
and alarm proactively](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_monitor_instances_post_launch_proactive.html)
- [AWS Well-Architected Reliability Pillar: REL06-BP03 Send
notifications (Real-time processing and alarming)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_notification_monitor.html)
- [What
is Anomaly Detection?](https://aws.amazon.com/what-is/anomaly-detection/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [AWS Health Aware](https://github.com/aws-samples/aws-health-aware/)
- [Amazon's
approach to high-availability deployment: Anomaly
detection](https://youtu.be/bCgD2bX1LI4?t=2493)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.1-automate-alerts-for-security-and-performance-issues.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.2] Plan for large scale events

**Category:** FOUNDATIONAL

A large scale event (LSE) is an incident that has a wide
impact, such as service outages or major security
incidents. Proper management of LSEs help to ensure business
continuity, maintain customer trust, and reduce the negative
impact of such events.

Prepare a detailed incident management plan, outlining the
roles, responsibilities, and processes to be followed in the
event of a large-scale incident. At a minimum, the plan should
outline how teams expect to maintain availability and
reliability of systems by having the capability to
automatically scale resources, re-route traffic, and failover
to backup systems when required.

**Related information:**

- [Disaster
Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- [Incident
management](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/incident-management.html)
- [Disaster
recovery plan](https://aws.amazon.com/disaster-recovery/faqs/#Core_concepts)
- [Amazon's
approach to security during development: Handling a
security incident](https://youtu.be/NeR7FhHqDGQ?t=1962)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.2-plan-for-large-scale-events.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.3] Conduct post-incident analysis for continuous improvement

**Category:** FOUNDATIONAL

Drive the continuous improvement of analysis and response mechanisms by holding
post-incident retrospectives. The post-incident retrospectives allow teams to identify gaps
and areas for improvement by analyzing the actions that were taken during an incident. These
retrospectives should not be used to place blame or point fingers at individuals. Instead,
they provide the time for teams to optimize their response process for future incidents and
helps ensure that they are continuously learning and improving their incident response
capabilities. This approach leads to more efficient and effective resolution of incidents
over time.

All relevant stakeholders involved with the incident and the system should attend the
retrospective. At a minimum, this should include the leaders and individual contributors who
support the system, the customer advocates, those who were impacted by the issue internally,
as well as those involved with the resolution of the issue. The post-incident retrospective
findings should be anonymized, as to not place blame onto any individuals, and should be
well documented and shared with the broader organization so that others may learn as well.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP02 Analyze
metrics when events or incidents occur](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_monitor_instances_post_launch_review_metrics.html)
- [AWS Well-Architected Reliability Pillar: REL12-BP02 Perform
post-incident analysis](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_rca_resiliency.html)
- [AWS Well-Architected Operational Excellence Pillar: OPS11-BP02
Perform post-incident analysis](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_perform_rca_process.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.3-conduct-post-incident-analysis-for-continuous-improvement.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.4] Report on business metrics to drive data-driven decision making

**Category:** FOUNDATIONAL

Business metrics for all systems should be accessible and
comprehensible to leaders and key stakeholders. These metrics
should inform key performance indicators (KPIs), service level
objectives (SLOs), service level agreement (SLA) adherence,
user engagement, conversion rates, and other metrics relevant
to the business sides of your operations.

Just like with technology metrics, continuous monitoring tools
should be used to detect when business metrics cross
predefined thresholds, triggering alerts that highlight
significant deviations or potential issues. These alerts
should inform timely and data-driven decision-making, helping
identify areas for improvement, optimizing system performance,
and aligning actions with overarching business goals.

Create dashboards or reports that present these metrics, as well as how they are
tracking against KPIs and SLAs, in a user-friendly, non-technical format. Ensure the data is
up-to-date, accurate, and accessible to less technical leaders so that it can be used to
make informed business decisions. Observability isn't merely about data collection—it is
about turning that data into actionable insights that drive better outcomes for both the
technology and business sides of the organization.

Fast feedback leads to success. Continuously monitoring and
alerting on business metrics is becoming foundational for
organizations committed to maximizing the value they get from
their technology investments and for maintaining the quality
of their digital services.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP05 Review
metrics at regular intervals](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_monitor_instances_post_launch_review_metrics_collected.html)
- [Operational
observability](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/operational-observability.html)
- [The
Amazon Software Development Process: Measure
Everything](https://youtu.be/52SC80SFPOw?t=1922)
- [Using
Cloud Fitness Functions to Drive Evolutionary
Architecture](https://aws.amazon.com/blogs/architecture/using-cloud-fitness-functions-to-drive-evolutionary-architecture/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.4-report-on-business-metrics-to-drive-data-driven-decision-making.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.5] Detect performance issues using application performance monitoring

**Category:** RECOMMENDED

Application Performance Monitoring (APM) refers to the use of
tools to monitor and manage the ongoing, real-time performance
and availability of systems in production environments. APM
tools help in maintaining the performance of systems by
identifying performance issues early on. This leads to quicker
resolution of issues, improved user experience, and reduced
downtime.

To comprehensively monitor application performance, implement
both Real-User Monitoring (RUM) and Synthetic Monitoring.
These APM tools are recommended detect and diagnose
performance issues in production systems. These APM tools
enable teams to proactively detect and diagnose complex
application performance problems to maintain an expected level
of service.

RUM captures performance metrics based on actual user interactions. Analyze real user
data to understand areas of the system that are frequently used and might benefit from
performance improvements. This data can then be used to identify and debug client-side
issues to optimize end-user experience.

On the other hand, Synthetic Monitoring involves writing
scripts that simulate user interactions, known as canaries, to
continuously monitor endpoints and APIs. Canaries follow the
same routes and perform the same actions as a customer,
allowing for the continuous verification of the customer
experience even in the absence of actual customer traffic. By
using insights from RUM, you can optimize which canaries to
run continuously, ensuring they closely mimic the most common
user paths. This strategy ensures potential issues are
identified before impacting users, offering a seamless user
experience.

Both tools collect metrics on response time, resource
utilization, and other performance-related indicators, forming
a holistic approach to continuous performance monitoring in
production environments.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF01-BP06 Benchmark
existing workloads](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_performing_architecture_benchmark.html)
- [What
is APM (Application Performance Monitoring)?](https://aws.amazon.com/what-is/application-performance-monitoring/)
- [Real-User
Monitoring (RUM) for Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
- [Amazon CloudWatch ServiceLens](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html)
- [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
- [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.5-detect-performance-issues-using-application-performance-monitoring.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.6] Gather user experience insights using digital experience monitoring

**Category:** RECOMMENDED

Digital Experience Monitoring (DEM) involves simulating user
interactions with applications to measure the performance and
availability of services from the perspective of end
users. DEM allows teams to proactively detect and resolve
issues that may impact user experience. It also helps in
validating that application updates or changes do not
negatively impact user experience.

Implement APM tools, such as synthetic transaction monitoring
using canaries to simulate user interactions with your
application and measure the response times and accuracy of the
results.

DEM is recommended as it provides important insights into the
user experience and helps detect issues that may impact user
experience

**Related information:**

- [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
- [AWS Marketplace - Digital Experience Monitoring](https://aws.amazon.com/marketplace/search/results?searchTerms=Digital+Experience+Monitoring)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.6-gather-user-experience-insights-using-digital-experience-monitoring.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.7] Visualize telemetry data in real-time

**Category:** RECOMMENDED

Visualization tools simplify the task of correlating and
understanding large, complex datasets. Using these tools,
teams are able to detect trends, patterns, and anomalies in
data in a readily available and easy to understand way.

Utilize visualization tools to correlate and comprehend large
sets of telemetry data in real-time. Visualization tools
support the uniquely human capability to discover patterns
that automated tools may otherwise miss. Choose a tool that
provides a clear view of system data at varying time
intervals, allowing teams to easily detect issues both during
or after they arise. Ensure that the tool is flexible and
customizable, so that teams can adjust the views and create
dashboards based on their unique needs.

**Related information:**

- [Building
dashboards for operational visibility](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility)
- [Building
Prowler into a QuickSight powered AWS Security
Dashboard](https://catalog.us-east-1.prod.workshops.aws/workshops/b1cdc52b-eb11-44ed-8dc8-9dfe5fb254f5/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.7-visualize-telemetry-data-in-real-time.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.8] Hold operational review meetings for data transparency

**Category:** RECOMMENDED

Operational review meetings are regular gatherings where teams
from across the organization come prepared with an operational
dashboard that showcases telemetry data, performance metrics,
and other insights into operations for their products. The aim
is present to the broad audience to share and gain different
perspectives on changes in the data, whether it is a spike,
dip, or trend. This promotes a culture of transparency,
preparedness, and continuous improvement throughout the
organization.

Amazon implements this by holding weekly Ops review meetings
and using the
[spinning
wheel](https://github.com/aws/aws-ops-wheel) as a random selection method for which team will
present. The randomness of the selection ensures that each
team comes prepared, as any team can be called upon to
present. When presenting, teams must be capable of deep diving
into the data, explaining root causes behind notable data
changes, and articulating the steps taken or planned to
rectify any anomalies. This pushes teams to maintain
high-quality operational dashboards that reflect the real-time
health and performance of their services.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP05 Review
metrics at regular intervals](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_monitor_instances_post_launch_review_metrics_collected.html)
- [AWS Well-Architected Reliability Pillar: REL06-BP06 Conduct
reviews regularly](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_review_monitoring.html)
- [AWS Ops Wheel](https://github.com/aws/aws-ops-wheel)
- [AWS Well-Architected Operational Excellence Pillar: OPS11-BP07
Perform operations metrics reviews](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_metrics_review.html)
- [The
Amazon Software Development Process: Monitor
Everything](https://youtu.be/52SC80SFPOw?t=1548)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.8-hold-operational-review-meetings-for-data-transparency.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.9] Optimize alerts to prevent fatigue and minimize monitoring costs

**Category:** RECOMMENDED

Reduce the number of ineffective alerts as well as the costs
associated with monitoring by optimizing rules and thresholds
for alerts based on business impact and issue severity. By
continuously refining rules and thresholds for alerts, teams
can minimize unnecessary notifications, reducing the time and
resources spent on non-critical issues. This helps teams focus
on high-impact issues, enhancing productivity and efficiency.

Set up alert rules and thresholds based on the severity and
business impact of potential issues. Teams should leverage
cost-effective methods for delivering notifications, and work
to reduce the amount of false positive notifications. Regular
reviews and adjustments of these rules and thresholds should
be done based on usage patterns to further minimize costs,
while still ensuring that teams are alerted to critical issues
in a timely and effective manner.

Implementing intelligent alerting strategies, such as alert
deduplication, aggregation, and comprehensive data
visualization can help to reduce cost, alert fatigue, and data
overload that comes with having too many alerts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.9-optimize-alerts-to-prevent-fatigue-and-minimize-monitoring-costs.html*

---

**Capability**: O.CM — Continuous monitoring

# [O.CM.10] Proactively detect issues using AI/ML

**Category:** OPTIONAL

Adopt data-driven AI/ML monitoring tools and techniques like Artificial Intelligence
Operations (AIOps), ML-powered anomaly detection, and predictive analytics solutions, to
detect issues and performance bottlenecks proactively—even before system performance is
impacted.

Choose a tool that can leverage data and analytics to
automatically infer predictions, and begin to feed data to it
and inject failure to test the validity of the tool. These
tools should have access to both historical and real-time
data. Once operational, the tool can automatically detect
issues, predict impending resource exhaustion, detail likely
causes, and recommend remediation actions to the team. Ensure
that there is a feedback loop to continuously train and refine
these models based on real-world data and incidents.

Start small when setting up alerts from these tools to avoid
alert fatigue and maintain trust in the system. As the tool
becomes more familiar with the data patterns, teams can
gradually increase the alerting scope. Regularly validate the
tool's predictions by injecting failures and observing the
responses.

**Related information:**

- [Machine-Learning-Powered
DevOps - Amazon DevOps Guru](https://aws.amazon.com/devops-guru/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Continuous
Monitoring and Threat Detection](https://aws.amazon.com/security/continuous-monitoring-threat-detection/)
- [Gaining
operational insights with AIOps using Amazon DevOps Guru
Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f92df379-6add-4101-8b4b-38b788e1222b/en-US)
- [What
Is Anomaly Detection?](https://aws.amazon.com/what-is/anomaly-detection)
- [What
Is Predictive Analytics?](https://aws.amazon.com/what-is/predictive-analytics)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.10-proactively-detect-issues-using-aiml.html*

---

**Capability**: O.DIP — Data ingestion and processing

# [O.DIP.1] Aggregate logs and events across workloads

**Category:** FOUNDATIONAL

Logs and events should be aggregated across multiple workloads
to provide a comprehensive view of the entire system. This
enables teams to troubleshoot, identify patterns, and resolve
operational issues.

Implement a log aggregation solution that supports collecting logs from various
sources and provides functions for filtering, searching, visualizing, and alerting. Make
sure the solution provides real-time data collection, supports necessary data sources, and
offers visualization options. The tool should be accessible to application teams, allowing
them to monitor and troubleshoot their system as needed.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL11-BP01 Monitor
all components of the workload to detect failures](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_monitoring_health.html)
- [Cross-account
cross-Region CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html)
- [Collect,
analyze, and display Amazon CloudWatch Logs in a single
dashboard with the Centralized Logging on AWS solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-on-aws/welcome.html)
- [Centralized
Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)
- [Sending
Logs Directly to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Sending-Logs-Directly-To-S3.html)
- [One
Observability Workshop](https://observability.workshop.aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.1-aggregate-logs-and-events-across-workloads.html*

---

**Capability**: O.DIP — Data ingestion and processing

# [O.DIP.2] Centralize logs for enhanced security investigations

**Category:** FOUNDATIONAL

Effective security investigations require the aggregation,
standardization, and centralization of logs and events so they
are readily accessible to investigation teams. Centralized
logs and event data enhance the ability of security teams to
conduct effective investigations, improve threat detection,
and accelerate incident response times.

Use cloud native tools or Security Information and Event Management (SIEM) solutions
to aggregate, standardize, and centralize logs and event data, while respecting regional
boundaries and data sovereignty requirements. These tools are designed to collect and
analyze logs and security events from various sources to provide a centralized view of an
organization's security posture. Centralizing, normalizing, deduping, and removing
unnecessary data allows security teams to use automation and scripted investigation tools
which leads to a faster and more efficient response process.

Given the sensitivity of this data, verify that the data is accessible only to
authorized security personnel and that strong access controls are in place to maintain data
security and confidentiality. Only grant least-privilege permission to the data so that it
is only accessible to authorized users with the minimum level of access required to perform
investigations. For instance, access to overwrite this data should be restricted.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP02 Analyze
metrics when events or incidents occur](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_monitor_instances_post_launch_review_metrics.html)
- [Collect,
analyze, and display Amazon CloudWatch Logs in a single
dashboard with the Centralized Logging on AWS solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-on-aws/welcome.html)
- [Cross-account
cross-Region CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html)
- [AWS Well-Architected Framework - Security Pillar -
Detection](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-detection.html)
- [Amazon
Security Lake](https://aws.amazon.com/security-lake/)
- [Centralized
Logging on AWS](https://aws.amazon.com/solutions/implementations/centralized-logging/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Centralized
Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)
- [AWS Marketplace: SIEM](https://aws.amazon.com/marketplace/solutions/security/siem)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.2-centralize-logs-for-enhanced-security-investigations.html*

---

**Capability**: O.DIP — Data ingestion and processing

# [O.DIP.3] Implement distributed tracing for system-wide request tracking

**Category:** RECOMMENDED

Distributed tracing is a method to track requests as they move through distributed
systems. It provides insights into system interactions across multiple services and
applications, enabling quicker issue identification and resolution.

Use a tracing solution that is scalable, provides real-time
data collection, and supports comprehensive visualization of
tracing data. Integrate this solution with the log and event
aggregation tools to enhance system-wide visibility. This
gives a comprehensive view of the entire system and its
dependencies, facilitating quick identification and resolution
of issues.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL06-BP07 Monitor
end-to-end tracing of requests through your system](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_end_to_end.html)
- [Distributed
Tracing System – AWS X-Ray](https://aws.amazon.com/xray/)
- [Amazon CloudWatch ServiceLens](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html)
- [Amazon Managed Grafana](https://aws.amazon.com/grafana/)
- [AWS X-Ray integration with Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/x-ray-data-source.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.3-implement-distributed-tracing-for-system-wide-request-tracking.html*

---

**Capability**: O.DIP — Data ingestion and processing

# [O.DIP.4] Aggregate health and status metrics across workloads

**Category:** RECOMMENDED

Aggregate health and status metrics across all workloads for a
unified view of the system's overall health. Aggregated health
metrics provide a snapshot of the system's overall health and
performance, aiding in proactive issue detection and efficient
resource management.

Use a monitoring solution that allows aggregation of health
metrics across all applications, supports real-time data
collection, and provides intuitive visualization of metrics
data. Integration with the logging, events, and tracing tools
can provide a comprehensive view of overall system health.

**Related information:**

- [Amazon Managed Grafana](https://aws.amazon.com/grafana/)
- [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/)
- [Application
Monitoring with Amazon CloudWatch](https://aws.amazon.com/solutions/implementations/application-monitoring-with-cloudwatch/)
- [AWS Health Aware](https://github.com/aws-samples/aws-health-aware/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.4-aggregate-health-and-status-metrics-across-workloads.html*

---

**Capability**: O.DIP — Data ingestion and processing

# [O.DIP.5] Optimize telemetry data storage and costs

**Category:** RECOMMENDED

Optimize costs associated with storing and processing large
amounts of telemetry data by using techniques like data
filtering and compression. When dealing with non-security
related telemetry data, data sampling can also be an effective
method to reduce costs.

Select cost-effective solutions and consumption-based resources for data storage. Be
strategic about data retention—remove unused or unnecessary data from storage regularly.
Also, be selective about which data sources are ingested and ensure they are required for
effective analysis to avoid unnecessary spend. Always remember that while managing costs
is important, it should not compromise the integrity and completeness of your data,
especially when it comes to security.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF03-BP01
Understand storage characteristics and requirements](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_right_storage_solution_understand_char.html)
- [AWS Well-Architected Sustainability Pillar: SUS04-BP05 Remove
unneeded or redundant data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a6.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.5-optimize-telemetry-data-storage-and-costs.html*

---

**Capability**: O.DIP — Data ingestion and processing

# [O.DIP.6] Standardize telemetry data with common formats

**Category:** RECOMMENDED

Normalize telemetry data using a common format or standard
schema to enhance consistency in data collection and
reporting. This facilitates seamless correlation and analysis
across multiple facets of observability, such as system
performance, user behaviors, and security events, improving
the overall speed and accuracy of detection and response in
any of these areas.

Two notable open-source projects supporting this goal are
OpenTelemetry and the Open Cybersecurity Alliance Schema
Framework (OCSF). OpenTelemetry provides a single set of APIs,
libraries, agents, and collector services to capture
distributed traces and metrics from your application and send
them to any observability platform. OCSF, on the other hand,
is an extensible, vendor-agnostic project designed to simplify
data ingestion and normalization specifically for
cybersecurity events.

Utilize a common telemetry format to streamline these
processes, reduce associated costs of data processing, and
allow teams to focus more on detecting and responding to
actionable events. Guidelines should be established for the
collection and reporting of data, enforcing consistency across
all teams. Adopting and effectively using standard schemas or
frameworks like OpenTelemetry and OCSF can provide
considerable advantages in achieving comprehensive
observability.

**Related information:**

- [OCSF
Schema](https://schema.ocsf.io/)
- [OCSF
GitHub](https://github.com/ocsf)
- [AWS Distro
for OpenTelemetry](https://aws.amazon.com/otel/)
- [OpenTelemetry](https://opentelemetry.io/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.6-standardize-telemetry-data-with-common-formats.html*

---

**Capability**: O.SI — Strategic instrumentation

# [O.SI.1] Center observability strategies around business and technical outcomes

**Category:** FOUNDATIONAL

To maximize the impact of observability, it should be closely
aligned with both business and technical goals. This means not
only monitoring system performance, uptime, or error rates but
also understanding how these factors directly or indirectly
influence business outcomes such as revenue, customer
satisfaction, and market growth.

Adopting the ethos that *"Everything fails, all the time"*,
famously stated by Werner Vogels, Amazon Chief Technology Officer, a successful
observability strategy acknowledges this reality and continuously iterates, adapting to
changes in business environments, technical architecture, user behaviors, and customer
needs. It is the shared responsibility of teams, leadership, and stakeholders to establish
relevant performance-related metrics to collect to measure established key performance
indicators (KPIs) and desired business outcomes. Effective KPIs must be based on the desired
business and technical outcomes and be relevant to the system being monitored.

An observability strategy must also identify the metrics,
logs, traces, and events necessary for collection and analysis
and prescribes appropriate tools and processes for gathering
this data. To enhance operational efficiency, the strategy
should propose guidelines for generating actionable alerts and
define escalation procedures. This way, teams can augment
these guidelines to suit their unique needs and contexts.

Use technical KPIs, such as the
[four
golden signals](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals) (latency, traffic, errors, and
saturation), to provide a set of minimum metrics to focus on
when monitoring user-facing systems. On the business side,
teams and leaders should meet regularly to assess how
technical metrics correlate with business outcomes and adapt
strategies accordingly. There is no one-size-fits-all approach
to defining these
KPIs. Discover
customer and stakeholder requirements and choose the
technical and business metrics and KPIs that best fit your
organization.

For example, one of the most important business-related KPIs for Amazon's e-commerce
segment is *orders per minute*. A dip below the expected
value for this metric could signify issues affecting customer experience or transactions,
which could affect revenue and customer satisfaction. Within Amazon, teams and leaders meet
regularly during weekly business reviews (WBRs) to assess the validity and quality of these
metrics against organizational goals. By continuously assessing metrics against business and
technical strategies, teams can proactively address potential issues before they affect the
bottom line.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF06-BP02 Define a
process to improve workload performance](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_continue_having_appropriate_resource_type_define_process.html)
- [AWS Well-Architected Sustainability Pillar: SUS02-BP02 Align
SLAs with sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a3.html)
- [AWS Well-Architected Reliability Pillar: REL11-BP07 Architect
your product to meet availability targets and uptime service level agreements (SLAs)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_service_level_agreements.html)
- [Monitoring
and Observability Implementation Priorities](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/implementation-priorities-5.html)
- [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/)
- [Instrumenting
distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/?did=ba_card&trk=ba_card)
- [The
Importance of Key Performance Indicators (KPIs) for
Large-Scale Cloud Migrations](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/)
- [What
is the difference between SLA and KPI?](https://aws.amazon.com/what-is/service-level-agreement/#seo-faq-pairs#sla-kpi)
- [The
Four Golden Signals](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals)
- [Amazon's
approach to high-availability deployment: Standard
metrics](https://youtu.be/bCgD2bX1LI4?t=2502)
- [The
Amazon Software Development Process: Measure
Everything](https://youtu.be/52SC80SFPOw?t=1922)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.1-center-observability-strategies-around-business-and-technical-outcomes.html*

---

**Capability**: O.SI — Strategic instrumentation

# [O.SI.2] Centralize tooling for streamlined system instrumentation and telemetry data interpretation

**Category:** FOUNDATIONAL

Centralized observability platforms are able to offer user-friendly, self-service
capabilities to individual teams that simplify embedding visibility into system components
and their dependencies. These tools streamline the onboarding process and offer
auto-instrumentation capabilities to automate the monitoring of applications.

Adopt an observability platform that provides observability to teams using the
*X as a Service* (XaaS) interaction mode as defined in the [Team Topologies](https://teamtopologies.com/) book by Matthew Skelton and
Manuel Pais. The platform needs to support ingesting the required data sources for effective
monitoring, and provide the desired level of visibility into the system components and their
dependencies.

Onboarding to the platform should be easy for teams, or support auto-instrumentation
to automatically monitor applications for a hands-off experience. This enables the
organization to achieve real-time visibility into system data and improve the ability to
identify and resolve issues quickly.

The observability platform should offer capabilities to follow
requests through the system, the services it interacts with,
the state of the infrastructure that these services run on,
and the impact of each of these on user experience. By
understanding the entire request pathway, teams can identify
where slowdowns or bottlenecks occur, whether this latency is
caused by hardware or dependencies between microservices that
weren't identified during development.

As the observability platform matures, it could begin to offer other capabilities
such as trend analysis, anomaly detection, and automated responses, ultimately aiming to
reduce the mean time to detect ([MTTD](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttd.html)) and the mean time to resolve ([MTTR](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.html)) any issues. This can lead to reduced downtime and improved ability to
achieve desired business outcomes.

**Related information:**

- [AWS observability tools](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/aws-observability-tools.html)
- [What
is Amazon CloudWatch Application Insights?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-what-is.html)
- [Integrated
observability partners](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/integrated-observability-partners.html)
- [Observability
Access Manager](https://github.com/aws-samples/cloudwatch-obervability-access-manager-terraform)
- [Apache
DevLake](https://devlake.apache.org/)
- [The
Amazon Software Development Process: Self-Service
Tools](https://youtu.be/52SC80SFPOw?t=579)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.2-centralize-tooling-for-streamlined-system-instrumentation-and-telemetry-data-interpretation.html*

---

**Capability**: O.SI — Strategic instrumentation

# [O.SI.3] Instrument all systems for comprehensive telemetry data collection

**Category:** FOUNDATIONAL

All systems should be fully-instrumented to collect the metrics, logs, events, and
traces necessary for meeting key performance indicators (KPIs), service level objectives,
and logging and monitoring strategies. Teams should integrate instrumentation libraries into
the components of new systems and feature enhancements to capture relevant data points,
while also ensuring that pipelines and associated tools used during build, testing,
deployment, and release of the system are also instrumented to track development lifecycle
metrics and best practices.

Chosen libraries and tools should support the efficient
collection, normalization, and aggregation of telemetry data.
Depending on the workload and existing instrumentation, this
could involve structured log-based metric reporting, or it
might rely on other established methods like using StatsD,
Prometheus exporters, or other monitoring solutions. The
chosen method should align with the workload's specific needs
and the complexity involved in instrumenting the solution.
Strike a balance between thorough monitoring and the amount of
work required to implement and maintain the monitoring
solution, to avoid falling into an anti-pattern of excessive
instrumentation.

Teams might also consider the use of auto-instrumentation tools to simplify the
process of collecting data across their systems with little to no manual intervention,
reducing the risk of human error and inconsistencies. Examples of auto-instrumentation
include embedding instrumentation tools in shared computer images like AMIs or containers
being used, automatically gathering telemetry from the compute runtime, or embedding
instrumentation tools into shared libraries and frameworks.

Regardless of how the team chooses to implement it, instrumentation should be
designed to accommodate the needs of the specific workload and business requirements. This
includes considering factors such as cost, security, data retention, access, compliance, and
governance requirements. All collected data must always be protected using appropriate
security measures, including encryption and least-privilege access controls.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF02-BP03 Collect
compute-related metrics](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_select_compute_collect_metrics.html)
- [AWS Well-Architected Reliability Pillar: REL06-BP01 Monitor
all components for the workload (Generation)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_monitor_resources.html)
- [AWS Well-Architected Cost Optimization Pillar: COST05-BP02
Analyze all components of the workload](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_analyze_all.html)
- [Instrumenting
distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/?did=ba_card&trk=ba_card)
- [AWS Observability Best Practices: Data Types](https://aws-observability.github.io/observability-best-practices)
- [Embedding
metrics within logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html)
- [Application
Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html)
- [Container
Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)
- [Lambda
Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html)
- [Powertools
for AWS Lambda](https://github.com/aws-powertools/powertools-lambda-python)
- [AWS Distro
for OpenTelemetry](https://aws-otel.github.io)
- [Build
an observability solution using managed AWS services and
the OpenTelemetry standard](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/)
- [The
Amazon Software Development Process: Monitor
Everything](https://youtu.be/52SC80SFPOw?t=1548)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.3-instrument-all-systems-for-comprehensive-telemetry-data-collection.html*

---

**Capability**: O.SI — Strategic instrumentation

# [O.SI.4] Build health checks into every service

**Category:** RECOMMENDED

Each service within a system should be configured to include a health check endpoint
which provides real-time insight into how the system and its dependencies are performing.
Usually manifested as a secure and private HTTP health endpoint (for example,
`/actuator/health`), this feature serves as a critical component in
monitoring the health status of the overall system, generally including information such
as operating status, versions of software running, database response time, and memory
consumption. By offering lightweight and fast-responding feedback, they enable sustaining
system reliability and availability, two attributes that directly impact customer
experience and service credibility.

Observability, governance, and testing tools can invoke these
health check endpoints periodically, ensuring the continuous
evaluation of system health. However, implementing them should
be done with precautionary measures like rate-limiting,
thresholding, and circuit breakers to avoid overwhelming the
system and to involve human intervention when required.

Integrating health check endpoints is highly recommended for
larger, more complex systems or any environment where system
availability and rapid issue resolution need to be
prioritized. In systems with high interoperability, such as
microservices architecture, the presence of health check
endpoints in every service becomes even more critical as they
help identify issues related to specific services in the
system. This can significantly reduce the debugging time and
enhance the efficiency of the development process.

For mission critical workloads it may be beneficial to explore
additional mitigation strategies to prevent widespread failure
due to faulty deployments. These strategies could include
alerting mechanisms when overall fleet size, load, latency, or
error rate are abnormal, and phased deployments to ensure
thorough testing before full-scale implementation. These
preventive deployment measures complement health check
endpoints and can prevent a potentially flawed deployment from
propagating throughout the entire system.

**Related information:**

- [Implementing
health checks](https://aws.amazon.com/builders-library/implementing-health-checks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.4-build-health-checks-into-every-service.html*

---

**Capability**: O.SI — Strategic instrumentation

# [O.SI.5] Set and monitor service level objectives against performance standards

**Category:** RECOMMENDED

Teams should define and document Service Level Objectives (SLOs) for every service,
regardless of whether it is directly consumed by external customers or used internally.
SLOs should be accessible and clearly communicate the expected standard of performance and
availability for the service. While Service Level Agreements (SLAs), which define a
contract that must be met for service availability, are typically defined and published
for services that are directly consumed by customers, it is equally important to establish
SLOs for services consumed internally. Such SLOs help ensure performance standards are
met, even in the absence of formal SLAs, and can also act as data points for meeting Key
Performance Indicators (KPIs).

The creation of SLOs should be a collaborative effort
involving both the business and technical teams. The technical
team must provide realistic estimations based on the system's
capabilities and constraints, while the business team ensures
these align with the company's business objectives and
internal standards.

SLOs should be SMART (Specific, Measurable, Achievable,
Relevant, and Time-bound). This means that they should clearly
define what is to be achieved, provide a way to measure the
progress, ensure that the goals can realistically be achieved
given the current resources and capabilities, align with
business objectives, and set a time frame for the achievement
of these goals.

When defining SLOs, rather than using averages, it is
preferable to use percentiles for measurement. Percentiles are
more reliable in detecting outliers and provide a more
accurate representation of the system's performance. For
example, a 99th percentile latency SLO means that 99% of
requests should be faster than a specific threshold, providing
a much more accurate depiction of the service's performance
than an average would.

Teams internally measure and monitor their SLOs to ensure they
are meeting the defined business and technical objectives.
When measuring against a SLO, teams produce Service Level
Indicators (SLIs), which are the actual measurements of the
performance and availability of the service at that point in
time. SLIs are used to evaluate whether the service is meeting
the defined SLOs. By continuously tracking SLIs against the
target SLOs, teams can detect and resolve issues that impact
the performance and availability of their services while
ensuring that they continue to meet both external customer
expectations and internal performance standards.

Continuous improvement and periodic review of SLOs are
required to ensure they remain realistic and aligned with both
the system's capabilities and the business's objectives. Any
changes to the system that could affect its performance should
trigger a review of the associated SLOs.

**Related information:**

- [What
Is SLA (Service Level Agreement)?](https://aws.amazon.com/what-is/service-level-agreement/)
- [What
is the difference between SLA and KPI?](https://aws.amazon.com/what-is/service-level-agreement/#seo-faq-pairs#sla-kpi)
- [AWS Well-Architected Framework - Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- [Designed-For
Availability for Select AWS Services](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/appendix-a-designed-for-availability-for-select-aws-services.html)
- [Understanding
KPIs ("Golden Signals")](https://aws-observability.github.io/observability-best-practices/guides/operational/business/key-performance-indicators/#10-understanding-kpis-golden-signals)
- [The
Importance of Key Performance Indicators (KPIs) for
Large-Scale Cloud Migrations](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.5-set-and-monitor-service-level-objectives-against-performance-standards.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
