# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 4

---

# ADVOPS01 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# ADVOPS01-BP01 Assess trade-offs between ad serving architecture options and associated risks

When designing the ad serving infrastructure, evaluate the trade-offs between different
architectural approaches and their associated risks. This includes considering factors such
as performance, scalability, availability, security, and cost to determine the optimal
solution.

## Implementation guidance

- Assess the performance and scalability requirements of your
ad serving workload, including peak traffic patterns and
seasonal fluctuations. Evaluate architectures that can
dynamically scale, such as serverless or containerized
approaches.
- Analyze the availability and reliability needs of your ad
serving infrastructure, ensuring that your architecture
includes redundancy and fault tolerance mechanisms to
maintain high uptime.
- Evaluate the security risks associated with your ad serving
workload, such as bot attacks and ad fraud, and implement
appropriate controls like web application firewalls and rate
limiting.

## Key AWS services

### Key AWS services

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Fargate](https://aws.amazon.com/fargate/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon EKS](https://aws.amazon.com/eks/)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [Amazon Route 53](https://aws.amazon.com/route53/)
- [AWS WAF](https://aws.amazon.com/waf/)
- [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
- [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/)

### Resources

- [Building
Applications with Serverless Architectures](https://aws.amazon.com/lambda/serverless-architectures-learn-more/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops01-bp01.html*

---

# ADVOPS01-BP02 Create RACI matrices that define the roles and responsibilities for each key advertising process like infrastructure monitoring

When designing advertising workloads, define roles and set clear
expectations for each stakeholder for seamless key advertising
processes. By implementing this best practice, organizations can
leverage RACI (responsible, accountable, consulted, and informed)
matrices to establish a robust framework for accountability and
decision-making.

## Implementation guidance

By creating comprehensive RACI matrices, organizations can
establish accountability, decision-making authority, and
communication requirements for each step of the ad-serving
workflow. This level of clarity assists in blocking confusion,
gaps, or overlaps in responsibilities. This clarity also
verifies that stakeholders understand their roles and how they
contribute to the overall success of the advertising
operations.

For data management specifically, implement the following
approach:

- Establish data classification and handling processes:

Classify advertising data based on criticality and
latency requirements (real-time bidding data, campaign
configuration data, historical analytics data)
- Define data retention policies for each classification
(for example, bid data retained for 30 days, campaign data
for one year)
- Implement data lineage tracking using AWS Glue Data
Catalog to document data origins, transformations, and
dependencies across the advertising pipeline

- Structure teams around data criticality:

**Real-time data operations team:** Responsible for
sub-100ms data like bidding, user profiles, and fraud
detection
- **Campaign data management team:** Handles near real-time
data for configurations, targeting, and budgets
- **Analytics and reporting team:** Manages batch processing
for historical data and business intelligence

- Define data ownership with specific domains:

Assign data stewards for specific advertising domains
such as:

Bid management domain (bid requests, responses,
auction data)
- User profile domain (demographic data, behavioral
signals, privacy preferences)
- Campaign domain (creative assets, targeting
parameters, budget configurations)
- Analytics domain (performance metrics, attribution
data, reporting datasets)

- Document domain-specific quality standards and
governance responsibilities in the RACI matrix

- Implement data governance using AWS services:

Use AWS Organizations with service control policies
(SCPs) to enforce data residency requirements for
different Regions
- Configure IAM roles with least-privilege permissions
aligned to team responsibilities (for example, real-time team
with write access to bidding data, read-only for
analytics)
- Deploy AWS Control Tower guardrails to help block
unauthorized cross-account or cross-Region data
transfers
- Implement AWS Config rules to continuously audit
compliance with data governance policies

- Establish data management processes:

Data cataloging: Use AWS AWS Glue Data Catalog to maintain
a comprehensive inventory of advertising datasets with
metadata, ownership, and classification
- Quality monitoring: Implement automated data quality
checks using AWS Glue DataBrew to validate incoming
data against defined schemas and business rules
- Workflow automation: Create AWS Step Functions
workflows for data handoffs between teams, with
validation checkpoints and approval gates for critical
data transitions

## Resources

- AWS Organizations for team boundaries: Implement
multi-account strategies with SCPs to enforce separation
of duties between data teams as described in
[AWS Organizations Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html)
- Data governance implementation: Follow the framework in
[AWS Data Governance Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-governance-aws/)
to establish controls specific to advertising data domains
- Team collaboration on data assets: Use
[Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/)
to create a data marketplace where teams can discover,
share, and collaborate on advertising datasets
- Automated operational procedures: Implement
[AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-best-practices.html)
runbooks for standardized data operations tasks across
teams
- Compliance monitoring: Deploy
[AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/best-practices.html)
to continuously validate that data handling practices meet
organizational and regulatory requirements
- [Create a RACI or RASCI matrix for a cloud operating model](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-raci-or-rasci-matrix-for-a-cloud-operating-model.html)

## Key AWS services

- AWS Organizations
- AWS IAM
- AWS Control Tower
- AWS AWS Glue Data Catalog
- AWS Glue DataBrew
- Amazon DataZone
- AWS Systems Manager
- AWS Config
- AWS Step Functions

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops01-bp02.html*

---

# ADVOPS01-BP03 Establish performance metrics by defining key performance indicators (KPIs) and service-level objectives (SLOs)

Establishing a comprehensive set of operational performance
metrics is critical in an advertising workload. It helps
organizations to measure, monitor, and validate the performance of
the advertising operations.

## Implementation guidance

Define operational KPIs and establish SLOs. For example,
consider the following example criteria:

- **Ad serving:** Ad serving
latency
- **Infrastructure
maintenance:** System uptime, maintenance task
completion rate, incident response time

## Key AWS services

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

## Resources

- [Improve
application reliability with effective SLOs](https://aws.amazon.com/blogs/mt/improve-application-reliability-with-effective-slos/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops01-bp03.html*

---

# ADVOPS01-BP04 Establish data governance and compliance operations

Advertising data management requires robust governance and
compliance procedures, especially in a multi-Region
environment. This best practice verifies adherence to
regional data privacy laws while maintaining operational
efficiency across global advertising operations.

## Implementation guidance

- For data residency compliance alignment:

Implement landing zone controls for different
geographical Regions
- Configure data boundary controls using AWS Control
Tower
- Set up guardrails for data movement between Regions
- Monitor and enforce data locality requirements

- For data governance:

Establish data classification policies for
advertising data types
- Implement data retention and archival procedures
- Set up access controls and encryption policies
- Configure audit logging and compliance reporting

- For regulatory compliance alignment:

Implement GDPR requirements for EU user data
- Set up consent management systems
- Monitor compliance with regional advertising laws

## Key AWS services

- AWS Control Tower
- AWS Organizations
- AWS Config
- AWS CloudTrail
- Amazon Macie
- AWS Local Zones
- AWS Identity and Access Management

## Resources

- [Best Practices for managing data residency in AWS Local Zones using landing zone controls](https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/)
- [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/)
- [Scale
across borders: build a multi-Region architecture while
maintaining data residency](https://community.aws/content/2dhVhtsciD5gVBlCKUlHoszrDzU/scale-beyond-borders?lang=en#aws-reference-architecture-for-multiregion-with-data-residency)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops01-bp04.html*

---

# ADVOPS02 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# ADVOPS02-BP01 Implement monitoring across each layer of your advertising stack including infrastructure, applications, and user experience

Ensuring operational excellence in advertising workloads requires
a holistic approach to monitoring. This best practice emphasizes
the importance of implementing comprehensive monitoring solutions
that span all layers of the advertising stack. The advertising
stack includes the ad-serving infrastructure, data pipelines,
application performance, and user experience. By monitoring these
various components, you can gain a complete understanding of the
overall health and performance of your advertising workload. This
understanding helps you identify and address issues, optimize
resource utilization, and deliver a seamless customer experience.
With a multi-layered monitoring approach, you can proactively
detect and resolve problems before they impact your business.

## Implementation guidance

Monitor and set KPIs and SLOs for infrastructure services using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for services like
[Amazon EC2](https://aws.amazon.com/ec2/)
and [Amazon EBS](https://aws.amazon.com/ebs/). Set up CloudWatch Alarms for resource utilization,
performance, and availability.

## Resources

- [Observability using native Amazon CloudWatch and AWS X-Ray for serverless modern applications](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/)
- [AWS Observability Maturity Model](https://aws-observability.github.io/observability-best-practices/guides/observability-maturity-model/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp01.html*

---

# ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns

Advertising workloads can experience significant spikes in traffic
and resource utilization, which can impact performance and
availability. To maintain observability across these dynamic
workloads, collect granular, one-second metrics with near
real-time latency. Use advanced analytics, machine learning, and
anomaly detection to continuously analyze this data and
proactively identify issues before they impact campaigns. This
level of observability and proactive issue detection improves the
reliability and responsiveness of your advertising infrastructure,
even during periods of high demand.

## Implementation guidance

Consider the following for collecting important ad-serving
metrics:

- **Granular metrics:** Collect
metrics at a one-second granularity to capture spikes and
fluctuations in advertising workloads. Key metrics to
monitor include:

**Bid requests per
second:** Number of bid requests received.
- **Bid response time:**
Time taken to respond to bid requests.
- **Successful bids:**
Number of successful bids placed.
- **Bid win rate:**
Percentage of bids won compared to total bids placed.
- **Latency metrics:**
Measure network latency, processing time, and database
query times.

For database metrics for RTB platforms:

- **Read and write latency:**
Measure the time taken for read and write operations in your
databases including
[DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html)
and
[Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html).
- **Throughput:** Monitor
[read
and write capacity units](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html) to verify that your database
can handle the load.
- **Error rates:** Track the
number of failed read/write operations.
- **Connection count:** Monitor
the number of
[active
connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html) to the database.

Consider the following for effective analysis of ad serving
insights:

- **Anomaly detection:** Use
Amazon CloudWatch anomaly detection to detect anomalies in
your metrics based on historical data patterns
automatically. This can help identify potential issues
before they impact campaigns.

Create useful alarms for monitoring and alerting. Configure
CloudWatch alarms for critical metrics such as:

- **High latency:** Set alarms
for when bid response times exceed a defined threshold (for
example, 100ms).
- **Low bid win rate:**
Initiate alerts if the bid win rate drops below a specific
percentage.
- **Database latency:** Create alarms for read or write
latency thresholds to ensure database performance.

Configure your notification mechanisms. Use Amazon Simple Notification Service (Amazon SNS) to send alerts to relevant
stakeholders using email or SMS when alarms go off. This makes
it possible for the appropriate teams to respond quickly to
potential issues.

Other important considerations for observability of advertising
workloads:

- **Impact on cost:**
CloudWatch has charges for custom metrics, alarms, and API
requests, which can add to the overall AWS costs. The cost
can vary based on the number of metrics, alarms, and API
calls configured. SNS has charges for the number of
notifications sent, which can also contribute to the overall
cost.
- **To reduce impact on cost:**
Analyze the expected usage patterns and configure CloudWatch
and SNS based on specific needs to optimize costs. Consider
cost-optimized approaches, such as using sampling or
aggregation for high-volume metrics, to reduce the number of
custom metrics and API calls.
- **Impact on latency:** The
monitoring and logging solutions recommended, when
implemented correctly, should have minimal impact on the
latency of your advertising workloads. CloudWatch provides
near real-time data ingestion and processing, which helps in
quickly detecting and diagnosing issues. However, it's
important to verify that the monitoring and logging
solutions are non-blocking and do not introduce additional
latency in your critical advertising workflows.
- **To reduce impact on
latency:** Implement monitoring and logging
solutions using asynchronous, non-blocking approaches to
minimize the impact on latency. Consider using sampling or
batching techniques to reduce the number of API calls and
optimize the performance of your monitoring and logging
solutions.
- **Ad fraud metrics:** Monitor
invalid traffic rates, bot detection rates, and suspicious
activity patterns.
- **Brand safety metrics:**
Track content classification accuracy, moderation response
times, and policy violation rates.
- **Measurement consistency:**
Monitor cross-system measurement discrepancies,
attribution model performance, and conversion path
integrity.

## Resources

- Set up
[custom
metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) in CloudWatch
- [Monitoring
metrics in an Amazon RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html)
- [Creating
cross-service dashboards](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-dashboards-visualizations.html)
- [Aggregating
metrics using CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#publishingDataPoints1)
- [Analyzing
performance anomalies with Amazon DevOps Guru for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/devops-guru-for-rds.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp02.html*

---

# ADVOPS02-BP03 Implement centralized logging to aggregate logs from all components of your advertising stack

To provide comprehensive visibility and operational efficiency
across your advertising stack, implement a centralized logging
solution. You can gain a holistic view of your system's
performance and behavior by aggregating logs from all components
of your advertising stack, including third-party integrations and
custom applications.

## Implementation guidance

Review
[centralized
logging with opensearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/) to aggregate logs from
all core components of the advertising workload.

**Amazon OpenSearch Service**

Use Amazon OpenSearch Service to aggregate logs from all core
components of the advertising workload, including ad serving
components like AWS Fargate tasks, Amazon EC2 instances, or AWS Lambda functions. OpenSearch provides a robust, scalable, and
highly-available log aggregation solution with powerful search
and analytics capabilities. Use this approach to have a
consolidated view of logs across your entire advertising
ecosystem, facilitating faster issue detection and resolution.

**Amazon CloudWatch Logs**

Alternatively, you can use Amazon CloudWatch Logs to capture and
aggregate logs specifically from your ad serving components.
CloudWatch Logs is a fully-managed service that makes it easy to
monitor, store, and access your log files from various AWS
services and on-premises sources. If your primary focus is on
monitoring and analyzing the logs related to your ad serving
components, CloudWatch Logs can be a suitable option.

The choice between OpenSearch and CloudWatch Logs for ad serving
logs depends on your specific requirements and the overall
complexity of your advertising workload. If you need a
comprehensive, cross-component log aggregation and analysis
solution, OpenSearch may be the preferred choice. However, if
your needs are more focused on the ad serving components,
CloudWatch Logs can be a simpler and more cost-effective option.

## Resources

- [Centralized
Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp03.html*

---

# ADVOPS02-BP04 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics

Instrument your advertising application code and infrastructure to
emit detailed, structured logs and metrics to achieve
comprehensive visibility into advertising workloads. Organizations
can monitor all components of their workloads, define KPIs, and
set up alerts for critical metrics by using observability services
like Amazon CloudWatch. This structured approach enables teams to
detect, diagnose, and resolve issues quickly. This approach also
optimizes performance and reliability of advertising campaigns.

## Implementation guidance

To gain comprehensive visibility into your advertising workload
and quickly detect, diagnose and resolve issues, use the
following logging strategy:

- Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and
[AWS X-Ray](https://aws.amazon.com/xray/) to capture key performance metrics,
error rates, latency data, and detailed logs from ad serving
infrastructure.
- Centralize all logs from the advertising stack, including third-party integrations
and partner platforms, using a log aggregation solution like Amazon CloudWatch Logs.
- Implement distributed tracing with AWS X-Ray to track user journeys and identify
performance bottlenecks across advertising applications and services.
- Integrate with ad tech platforms and partners to receive comprehensive event-level
data like bid requests, ad impressions, and conversions to power observability and
analytics.

## Resources

- [Observability
using native Amazon CloudWatch and AWS X-Ray for serverless
modern applications](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp04.html*

---

# ADVOPS03 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# ADVOPS03-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload

Develop structured procedures to manage operational events and
incidents in your advertising workloads. Runbooks provide
step-by-step procedures for well-understood, routine operations,
while playbooks guide your response to incidents with less
predictable outcomes. These documented procedures assist teams
to respond consistently and effectively, reducing human error
and improving operational resilience.

## Implementation guidance

- Use automation for predictable operational responses:

Implement auto scaling and load balancing using AWS services to handle common traffic patterns:

Configure Amazon EC2 Auto Scaling groups with appropriate
scaling policies based on advertising traffic patterns.
- Set up Elastic Load Balancing to distribute traffic across
healthy instances.
- Implement predictive scaling based on historical data for
cyclical advertising campaigns.
- Configure scheduled scaling for planned high-traffic
events like product launches or holiday promotions.

- For scenarios where auto scaling may not be sufficient:

Create runbooks for requesting additional EC2
capacity through ODCRs before anticipated
high-traffic events.
- Implement AWS Systems Manager automation documents
to execute common scaling procedures.
- Use AWS Auto Scaling for predictive scaling based
on historical data patterns.
- Configure CloudWatch alarms to trigger automated
responses for common capacity issues.

- Create purpose-built runbooks and playbooks for different
advertising scenarios:

Infrastructure capacity runbooks:

Document procedures for submitting on-demand
capacity requests (ODCRs) for anticipated
high-traffic events
- Create step-by-step guides for scaling resources
up or down based on traffic patterns
- Establish processes for capacity planning before
major advertising campaigns
- Define monitoring thresholds that trigger capacity
management procedures

- Ad fraud incident playbooks:

Document investigation procedures for detected
fraud patterns (bot traffic, click fraud,
impression fraud)
- Establish clear escalation paths for high-impact
fraud incidents with defined severity levels
- Create detailed workflows for fraud investigation
and mitigation, including evidence collection
- Define recovery procedures to restore normal
operations after fraud mitigation
- Document procedures for `ads.txt` and `sellers.json`
verification and maintenance
- Implement AWS Marketplace solutions like HUMAN for
automated fraud detection and prevention
- Create operational workflows for real-time fraud
detection using Amazon SageMaker AI ML models

- Brand safety incident playbooks:

Document procedures for content moderation
escalations and violations
- Establish workflows for emergency ad creative
approval and rejection
- Create processes for brand safety incident
response, including stakeholder communication
- Define procedures for implementing emergency
blocking rules in ad serving systems
- Implement content moderation workflows using
Amazon Rekognition for image/video analysis and
Amazon Comprehend for text analysis
- Create escalation procedures for high-risk content
identification with automated alerts via Amazon
EventBridge
- Document processes for regular updates to content
moderation models in SageMaker AI

- Measurement anomaly runbooks:

Document step-by-step procedures for investigating
common measurement discrepancies
- Establish workflows for cross- data reconciliation
and validation
- Create processes for measurement system
recalibration and data correction
- Define verification steps to confirm resolution of
measurement issues

- AI measurement system playbooks:

Document operational procedures for AI model
training, validation, and deployment
- Create monitoring workflows for detecting model
drift and performance degradation
- Establish human oversight processes for AI-based
measurement systems
- Document recovery procedures for AI system
failures
- Implement continuous improvement workflows using
AWS Step Functions to orchestrate model retraining
- Create operational procedures for managing model
versions and deployments

- Implement continuous improvement for runbooks and playbooks:

Review and update documentation after each incident or
significant operational event
- Conduct regular simulation exercises to validate
playbook effectiveness
- Incorporate lessons learned into revised procedures
- Track key metrics on playbook execution efficiency and
outcome effectiveness

## Key AWS services

- Amazon EC2 Auto Scaling
- Elastic Load Balancing
- AWS Systems Manager
- Amazon CloudWatch
- AWS Auto Scaling
- Amazon SageMaker AI
- Amazon Rekognition
- Amazon Comprehend
- AWS Lambda
- AWS Step Functions
- Amazon EventBridge
- Amazon Route 53
- AWS Marketplace solutions (like HUMAN)

## Resources

- [OPS07-BP03 Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html)
- [Use playbooks](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_playbooks.html)
- [AWS Marketplace: HUMAN Fraud Protection Solutions](https://aws.amazon.com/marketplace/seller-profile?id=22586a6c-27be-426c-b655-bb9783786286)
- [How HUMAN Advertising Intelligence Solutions Help Protect Against Ad Fraud in the Ad Tech Industry](https://aws.amazon.com/blogs/apn/how-human-advertising-intelligence-solutions-help-protect-against-ad-fraud-in-the-ad-tech-industry/)
- [Content Moderation Using Machine Learning on AWS](https://aws.amazon.com/blogs/machine-learning/utilize-aws-ai-services-to-automate-content-moderation-and-compliance/)
- [Guidance for Content Moderation on AWS](https://aws.amazon.com/solutions/guidance/content-moderation-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops03-bp01.html*

---

# ADVOPS03-BP02 Automate runbooks to gain operational efficiency

Document runbooks for failover procedures, capacity scaling, and incident response
workflows using AWS Systems Manager documents for automation.

## Implementation guidance

Consider the following example use case runbooks:

**Scaling runbook**

- Design step-by-step workflows for manually scaling up and down Amazon EC2 instances
and increasing or decreasing managed service capacities
- Create automation scripts to initiate auto scaling actions
based on predefined events
- Perform validation checks for successful scaling operations

**Third-party service
disruptions**

- Implement multi-provider redundancy and failover mechanisms
using AWS Lambda functions and Amazon API Gateway
- Use [AWS X-Ray](https://aws.amazon.com/xray/) for end-to-end tracing and troubleshooting of
distributed applications and third-party integrations
- Document playbooks for provider switching, data
synchronization, and incident escalation using
[AWS Step Functions](https://aws.amazon.com/step-functions/) and
[AWS Lambda](https://aws.amazon.com/lambda/)

**Infrastructure capacity
issues**

- Implement auto scaling and load balancing using Amazon EC2 Auto Scaling and
[Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/)
- Use
[AWS Auto Scaling](https://aws.amazon.com/autoscaling/) for predictive scaling based on
historical data and scheduled scaling for planned events
- Document runbooks for capacity planning, scaling procedures,
and cost optimization using
[AWS Systems Manager](https://aws.amazon.com/systems-manager/) Documents

**Cost optimization runbook**

- Procedures for reviewing resource utilization and
identifying opportunities for optimization using AWS Cost Explorer
- Guidelines for selecting the most cost-effective Amazon EC2 instance types and
purchasing models (like On-Demand, Reserved, or Spot) based on workload patterns
- Automation to right size Amazon EC2 instances, remove unused resources, and use AWS
Savings Plans
- Processes for periodic cost reviews and budget management

**Data management runbook**

- Create runbooks for:

Data pipeline failures
- Replication issues
- Storage capacity management
- Compliance violations

- Include Regional considerations.
- Document recovery procedures.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops03-bp02.html*

---

# ADVOPS04 — Manage operational processes

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# ADVOPS04-BP01 Implement operational procedures based on data classification and latency requirements

Managing advertising workloads requires different operational
approaches based on data latency needs. This best practice
focuses on establishing specific procedures for handling
low-latency data like bid requests, medium-latency data such as
campaign optimization, and high-latency data including
historical analytics.

## Implementation guidance

For low-latency data (bid data, user profiles, real-time
impressions):

- Implement multi-AZ deployments with automatic failover
mechanisms to facilitate continuous availability
- Configure monitoring with short evaluation periods
appropriate for detecting real-time issues
- Establish dedicated rapid-response procedures for critical
alerts affecting bidding operations
- Implement circuit breakers in API calls to help block
cascading failures during service degradation
- Create runbooks for emergency traffic management during
extreme load conditions
- Configure auto-scaling with aggressive scaling policies to
handle sudden traffic spikes
- Implement local caching strategies to reduce database load
for frequently accessed data
- Set up dedicated dashboards with high-frequency metric
collection for real-time monitoring

For medium-latency data (behavioral data, campaign
optimization):

- Configure batch processing jobs with appropriate completion
targets for campaign optimization
- Implement queue management with automated retry mechanisms
for failed operations
- Set up monitoring with balanced evaluation periods suitable
for near real-time operations
- Create standard incident response procedures with
appropriate escalation paths
- Implement data validation checks with error handling for
data quality issues
- Configure auto-scaling based on processing queue depth and
scheduled campaign activities
- Set up dashboards with appropriate refresh rates for
campaign management operations

For high-latency data (historical data, analytics):

- Schedule batch processing during off-peak hours to minimize
impact on real-time operations
- Implement cost-optimized storage strategies with appropriate
data lifecycle policies
- Configure monitoring with periodic health checks and summary
reporting
- Create standard support procedures with appropriate response
times for non-critical systems
- Implement automated data quality validation with
notification mechanisms
- Configure resource allocation with scheduled scaling based
on known processing windows
- Establish regular performance review processes with trend
analysis

For specialized advertising data types:

- Fraud detection data: Implement optimized processing
pipelines with appropriate monitoring and escalation
procedures designed for the critical nature of fraud
detection
- Content moderation data: Create workflows that balance
automated screening with human review processes, with
appropriate prioritization based on content risk assessment

## Key AWS services

- Amazon CloudWatch
- AWS Systems Manager
- Amazon EventBridge
- Amazon Kinesis Data Streams
- Amazon Managed Service for Apache Flink

## Resources

- [AWS for Advertising & Marketing](https://aws.amazon.com/advertising-marketing/adtech-real-time-bidding/)
- [Architectural patterns for real-time analytics using Amazon Kinesis Data Streams, part 1](https://aws.amazon.com/blogs/big-data/architectural-patterns-for-real-time-analytics-using-amazon-kinesis-data-streams-part-1/)
- [Streaming architecture patterns using a modern data architecture](https://docs.aws.amazon.com/whitepapers/latest/build-modern-data-streaming-analytics-architectures/streaming-analytics-architecture-patterns-using-a-modern-data-architecture.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops04-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
