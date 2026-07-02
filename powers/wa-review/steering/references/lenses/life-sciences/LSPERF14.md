# LSPERF14 — Network and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF14-BP01 Conduct performance benchmarking across geographic research hubs

Develop comprehensive performance testing across research hubs to
establish baselines and find regional bottlenecks. Monitor key
metrics like latency, throughput, packet loss, and jitter under
simulated research workloads. Create geographic heat maps showing
areas needing improved delivery capabilities. Test using actual
research data types including genomic files, high resolution images,
and complex models. Set up ongoing performance monitoring to track
improvements and detect new issues as global research collaboration
patterns change.

**Desired outcome:** You have a
comprehensive performance testing and monitoring system that
provides real-time visibility into research network performance
across geographic locations. This enables proactive optimization of
data transfers and provides consistent application performance for
global research collaboration.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Define key performance indicators including latency, throughput,
and response times. Create a framework specifying testing
frequencies and thresholds for research data types and
collaboration scenarios. Deploy test endpoints across research
hubs and implement automated testing scripts for continuous
evaluation of network performance, data transfers, and application
responsiveness.

Document region-specific performance metrics, including latency
patterns, bandwidth utilization, and inter-hub connectivity.
Create heat maps highlighting bottlenecks and areas needing
optimization. Establish monitoring systems with alerting
thresholds to quickly identify and address performance issues
across the research network.

Design testing scenarios reflecting real research workflows,
including genomic data transfers and collaboration sessions.
Implement testing for file operations and data synchronization.
Focus on measuring application performance across research tools
to provide a consistent user experience globally.

Deploy monitoring dashboards for real-time performance visibility.
Configure automated alerts for performance issues and system
health. Maintain regular review cycles including weekly
assessments and monthly trend analysis for continuous improvement.

### Implementation steps

- Implement comprehensive performance testing with Amazon CloudWatch Synthetics for synthetic monitoring, AWS X-Ray
for distributed tracing, and CloudWatch metrics for detailed
performance data collection.
- Optimize geographic performance using AWS Global Accelerator
for intelligent routing, Amazon CloudFront regional caches
for content delivery, and Amazon Route 53 geolocation
routing for regional traffic management.
- Accelerate research data transfers with Amazon S3 Transfer
Acceleration for global uploads, DataSync for automated
transfers, and enhanced networking for optimized throughput.
- Establish proactive monitoring using CloudWatch dashboards
for visualization, Amazon EventBridge for automated
alerting, and Amazon RDS Performance Insights for deep
analysis of performance bottlenecks.
- Configure performance baselines and thresholds to
automatically detect and respond to anomalies across global
infrastructure.
- Document performance requirements and implement regular
optimization reviews to continuously improve user
experience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf14-bp01.html*

---

# LSPERF14-BP02 Evaluate multi-CDN architectures with intelligent traffic routing capabilities

Evaluate content delivery network (CDN) providers focusing on their
performance in academic and research regions. Create a dynamic
multi-CDN system that routes content based on real-time performance,
content type, and destination. Test features like origin shields,
cache optimization for scientific data, and API configuration.
Assess providers' capability to handle specialized research needs
including HD microscopy streaming, large dataset syncing, and
real-time collaborative visualization. Consider combining commercial
CDNs with research networks like Internet2 or GÉANT for optimal
performance.

**Desired outcome:** You have a
multi-CDN architecture optimized for research content delivery, with
intelligent traffic routing and comprehensive performance
monitoring. This enables efficient distribution of specialized
research data while maintaining high performance across academic
networks and research locations.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Evaluate and select CDN providers based on their performance in
academic and research regions. Analyze capabilities for handling
specialized research content types and assess integration with
research networks. Create comprehensive provider profiles
documenting performance metrics, features, and integration
capabilities with academic networks like Internet2 or GÉANT.

Design dynamic routing mechanisms that direct content based on
real-time performance metrics, content type, and destination
requirements. Implement routing policies that consider factors
like latency, throughput, and regional performance patterns.
Establish automated failover mechanisms for continuous content
availability across multiple providers.

Configure CDN settings specifically for research and academic
content types, including cache optimization for scientific
datasets and streaming configurations for HD microscopy. Implement
specialized handling for large dataset synchronization and
real-time collaborative visualization tools. Create
content-specific delivery rules that optimize performance for
different research workflows.

Deploy comprehensive monitoring systems to track CDN performance
across academic regions and research networks. Establish real-time
performance dashboards and automated alerting systems for quick
issue identification. Implement regular performance analysis
cycles to continuously optimize content delivery across the
multi-CDN architecture.

### Implementation steps

- Deploy Amazon CloudFront as primary CDN with origin shields
and cache optimization for research data, while implementing
additional CDN providers with Internet2 connections and
configuring origin failover for continuous availability.
- Set up Amazon Route 53 traffic flow policies for intelligent
performance-based routing, deploy health checks for endpoint
monitoring across academic regions, and implement
latency-based routing to optimize delivery paths.
- Configure specialized cache policies for scientific
datasets, API configurations for efficient research
application requests, and streaming optimizations to support
HD microscopy and real-time visualization needs.
- Establish comprehensive monitoring with performance tracking
across academic regions, cost analysis for usage pattern
optimization, and customized dashboards for content delivery
efficiency visibility.
- Implement automated testing to regularly validate CDN
performance across different research data types and
geographic locations.
- Document CDN architecture with failover procedures and
optimization strategies for different content categories and
research applications.
- Conduct quarterly performance reviews to identify
improvement opportunities and adjust configurations based on
evolving research needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf14-bp02.html*

---

# LSPERF14-BP03 Assess edge computing integration for localized processing of research workloads

Assess edge computing solutions that enable research processing near
data sources and users. Review edge systems' compatibility with
research computing frameworks while improving version consistency.
Test edge-based collaboration tools including shared notebooks,
visualization systems, and model training. Compare performance and
resource efficiency between edge and centralized processing.
Evaluate edge solutions supporting secure multi-tenant environments
where researchers from different institutions can share computing
resources with proper data isolation.

**Desired outcome:** You have a
secure edge computing environment that enables localized processing
of research workloads with effective collaboration tools, optimized
performance, and strict multi-tenant isolation. This allows
researchers from different institutions to efficiently share
computing resources while maintaining data security and low-latency
access.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Assess edge computing systems for compatibility with research
workflows and computing frameworks. Document system capabilities
including processing power, memory requirements, and storage
options. Create comprehensive evaluation criteria focusing on
version management, framework support, and integration
capabilities with existing research infrastructure.

Evaluate edge-based collaboration tools and their effectiveness in
supporting research workflows. Test implementation of shared
notebooks, real-time visualization systems, and distributed model
training capabilities. Document performance metrics and user
experience factors across different edge locations and research
scenarios.

Conduct systematic comparison of edge versus centralized
processing for common research workloads. Measure resource
utilization, processing times, and data transfer requirements
across different deployment models. Create performance baselines
and optimization strategies for various research computing
scenarios.

Design secure multi-tenant environments that enable resource
sharing while maintaining strict data isolation. Implement access
controls and monitoring systems that foster secure collaboration
across institutions. Establish clear security protocols and
frameworks for edge deployments.

### Implementation steps

- Deploy comprehensive edge infrastructure with AWS Outposts
for local processing, AWS Wavelength for ultra-low latency
applications, and AWS Local Zones to reduce latency for
research tools and visualization.
- Establish collaborative research solutions using Amazon SageMaker AI for distributed model training, AWS IoT Greengrass
for edge device management, and container services for
consistent application deployment across locations.
- Implement robust monitoring and optimization with Amazon CloudWatch for edge performance tracking, AWS Systems Manager for infrastructure management, and AWS X-Ray for
distributed application tracing and analysis.
- Secure edge environments through AWS IAM for granular access
control, AWS Security Hub CSPM for centralized security posture
management, and AWS KMS for comprehensive data encryption
and key management.
- Document edge architecture with connectivity patterns, data
synchronization procedures, and failover mechanisms for
research continuity.
- Conduct regular performance testing to validate latency
requirements and optimize resource allocation for evolving
research workloads.
- Establish governance framework for edge deployments
including monitoring and automated security controls.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf14-bp03.html*

---
