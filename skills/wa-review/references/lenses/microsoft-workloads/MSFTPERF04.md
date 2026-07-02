# MSFTPERF04 — Performance measurement

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MSFTPERF04-BP01 Use historical data to evaluate performance

Effective assessment of Microsoft workload performance requires
comprehensive data collection across key system components: compute,
memory, storage, and networking. This approach aligns with the
Well-Architected Framework's Performance Excellence guidelines,
specifically the best practice PERF02-BP03, which focuses on
gathering compute-related metrics. By monitoring these critical
areas, organizations can identify suboptimal performance and
implement timely corrective measures. This holistic monitoring
strategy enables proactive management of Microsoft workloads,
ensuring they meet performance expectations and allowing for swift
intervention when performance falls below desired thresholds.

**Desired outcome:** Establish
comprehensive performance data collection and analysis capabilities
for Microsoft workloads that enable data-driven optimization
decisions, proactive issue identification, and continuous
performance improvement through historical trend analysis and
performance pattern recognition.

**Common anti-patterns:**

- Collecting performance data without systematic analysis or
historical comparison, missing opportunities to identify
performance trends and optimization opportunities over time.
- Monitoring only basic system metrics without collecting
Microsoft-specific performance indicators, limiting visibility
into application-level performance issues and optimization
potential.
- Implementing reactive performance monitoring that only triggers
during incidents, rather than proactive analysis that can
prevent performance degradation before it impacts users.

**Benefits of establishing this best
practice:**

- Data-driven optimization decisions through comprehensive
historical performance analysis that identifies trends,
patterns, and optimization opportunities across Microsoft
workload components.
- Proactive issue identification and prevention through continuous
monitoring and analysis that can detect performance degradation
before it impacts business operations.
- Improved capacity planning and resource allocation through
historical data analysis that enables accurate forecasting of
future performance and scaling requirements.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing comprehensive performance data collection and
analysis requires establishing systematic monitoring across all
Microsoft workload components and creating processes for regular
performance evaluation and optimization.

### Implementation steps

- Identify key performance metrics for Microsoft workload
components including compute, memory, storage, and network
performance indicators.
- Configure comprehensive monitoring using Amazon CloudWatch,
Performance Counters, and application-specific monitoring
tools to collect historical performance data.
- Establish data retention policies that maintain sufficient
historical data for trend analysis and performance
comparison over time.
- Implement automated data analysis and reporting processes
that regularly evaluate performance trends and identify
optimization opportunities.
- Create performance dashboards and visualization tools that
enable easy analysis of historical performance data and
trend identification.
- Establish regular performance review processes that analyze
historical data to identify patterns, anomalies, and
optimization opportunities.
- Document performance baselines and thresholds based on
historical analysis to enable effective anomaly detection
and alerting.
- Integrate historical performance analysis into capacity
planning and architectural decision-making processes for
continuous improvement.

## Resources

**Related documents:**

- [Monitoring
Windows services with Amazon CloudWatch](https://aws.amazon.com/blogs/mt/monitoring-windows-services-with-amazon-cloudwatch-2/)
- [How
do I use the CloudWatch agent on a Windows Server to view
metrics for Performance Monitor?](https://repost.aws/knowledge-center/cloudwatch-performance-monitor-windows)
- [How
to monitor Windows and Linux servers and get internal
performance metrics](https://aws.amazon.com/blogs/compute/how-to-monitor-windows-and-linux-servers-and-get-internal-performance-metrics/)
- [Run
ADOTCollector on AWS Windows Ec2 Host](https://aws-otel.github.io/docs/setup/build-collector-on-windows)

**Related tools:**

- [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/)
- [OpenTelemetry](https://opentelemetry.io/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf04-bp01.html*

---

# MSFTPERF04-BP02 Define baseline performance requirements

Microsoft workloads vary in their performance needs, making
historical data analysis crucial for establishing baseline
performance metrics. This approach allows organizations to detect
and quantify performance fluctuations effectively. By implementing
targeted alerts, IT teams can quickly identify anomalies, such as
unexpected CPU usage spikes, changes in storage throughput,
increased memory consumption, or more intricate performance issues.
The collected monitoring data serves a dual purpose: it not only
helps in detecting problems, but also provides valuable insights for
ongoing performance optimization.

**Desired outcome:** Establish clear,
measurable performance baselines for Microsoft workloads that enable
effective anomaly detection, performance optimization, and capacity
planning while providing objective criteria for evaluating system
health and performance improvements over time.

**Common anti-patterns:**

- Operating Microsoft workloads without defined performance
baselines, making it difficult to identify when performance
degrades or to measure the effectiveness of optimization
efforts.
- Setting performance baselines based on assumptions rather than
actual historical data analysis, leading to inappropriate
thresholds that generate false alerts or miss genuine
performance issues.
- Creating static baselines that does not account for normal
performance variations or business cycles, resulting in alert
fatigue or missed performance degradation during expected usage
patterns.

**Benefits of establishing this best
practice:**

- Effective anomaly detection through well-defined baselines that
enable accurate identification of performance deviations and
potential issues before they impact business operations.
- Improved performance optimization through objective measurement
criteria that enable evaluation of optimization efforts and
identification of areas requiring attention.
- Enhanced capacity planning and resource allocation through
baseline-driven analysis that supports data-driven decisions
about scaling and infrastructure investments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing performance baselines requires systematic analysis of
historical performance data and establishment of meaningful
thresholds that account for normal variations while detecting
genuine performance issues.

### Implementation steps

- Collect sufficient historical performance data across all
Microsoft workload components to establish statistically
meaningful baselines.
- Analyze performance patterns including daily, weekly, and
seasonal variations to understand normal performance
fluctuations.
- Define performance baseline metrics for key indicators
including CPU utilization, memory consumption, storage I/O,
network throughput, and application response times.
- Establish performance thresholds and alert criteria based on
statistical analysis of historical data and business
requirements.
- Configure monitoring and alerting systems to detect
deviations from established baselines and notify appropriate
teams of performance anomalies.
- Implement regular baseline review and adjustment processes
to account for changing workload patterns and business
requirements.
- Document baseline definitions, measurement criteria, and
alert thresholds for consistent application across
environments and teams.
- Integrate baseline monitoring into operational procedures
and incident response processes to enable rapid performance
issue identification and resolution.

## Resources

**Related documents:**

- [Using
CloudWatch outlier detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
- [Best
practices for monitoring Microsoft SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/monitoring.html)
- [Windows
Server - Power and performance tuning](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/hardware/power/power-performance-tuning)
- [Select
the right instance type for Windows workloads](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/right-size-selection.html)
- [FSx for Windows File Server performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
- [Windows
container memory requirements](https://docs.aws.amazon.com/eks/latest/best-practices/windows-oom.html#_windows_container_memory_requirements)

**Related tools:**

- [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/)
- [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf04-bp02.html*

---
