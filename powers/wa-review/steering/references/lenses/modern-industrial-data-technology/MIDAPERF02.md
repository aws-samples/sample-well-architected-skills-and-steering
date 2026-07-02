# MIDAPERF02 — Event-driven architecture

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MIDAPERF02-BP01 Implement event-driven architectures for manufacturing systems

In manufacturing environments, operational data is generated based on specific events
such as equipment state changes, threshold violations, or production milestones. Implementing
event-driven architectures allows systems to respond efficiently to these events rather than
constantly polling for changes, significantly improving resource utilization and system
responsiveness. This approach aligns perfectly with IoT communication patterns while enabling
scalable, loosely-coupled manufacturing systems.

**Desired outcome:** A responsive, efficient manufacturing data architecture that processes information only
when meaningful events occur, reducing unnecessary computation, minimizing latency for
critical operations, and enabling dynamic scaling based on actual processing demand rather
than peak capacity requirements.

**Common anti-patterns:**

- Transforming all incoming manufacturing data immediately instead of lazy evaluation when needed
- Making multiple small database calls per event instead of batching operations or using bulk APIs
- Processing all events and filtering in application code rather than using message-level filtering capabilities
- Routing all events from similar equipment to the same partition, creating processing bottlenecks
- Creating point-to-point integrations between manufacturing systems instead of using event mediators
- Making blocking calls between manufacturing subsystems instead of asynchronous event-driven communication
- Processing events without validating structure, leading to runtime failures and data corruption
- Building event consumers that depend on specific event producer implementations rather than standardized interfaces
- Allowing event processing failures to occur without proper logging, alerting, or dead letter handling
- Not implementing flow control when downstream systems cannot keep up with event volume
- Failing to implement end-to-end tracing for manufacturing processes spanning multiple event handlers
- Only monitoring for failures instead of proactively tracking performance metrics and trends

**Benefits of establishing this best practice:**

- [Reduces processing overhead by 40-60% compared to polling-based systems](https://arxiv.org/html/2510.04404v1)
- Improves response time to critical manufacturing events by removing processing queues
- Enhances system scalability by allocating resources only when needed for event
processing
- Simplifies integration between manufacturing subsystems through standardized event
interfaces
- Enables more granular cost allocation by associating resource usage with specific
event types

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Implement a publish or subscribe
messaging architecture where manufacturing devices and systems publish events to
centralized topics. Configure consumers to process only relevant event types using message
filtering capabilities to reduce unnecessary processing.
- Deploy durable message queues between producers and
consumers to handle throughput spikes and provide reliable event delivery even during
processing backlogs or temporary downstream system outages common in manufacturing
environments. AWS SQS and Amazon EventBridge services are tools that can accomplish these
goals.
- Design event handlers with idempotency in mind to help
prevent duplicate processing when events are retried. Implement deduplication mechanisms
using event IDs or processing timestamps to maintain data integrity during retries. A
- Establish dead-letter queues to capture events that
cannot be processed successfully after multiple attempts. Implement automated monitoring
and alerting for these queues to quickly identify and resolve processing issues that could
impact manufacturing operations. AWS Step functions, Amazon EventBridge, and AWS IoT core
are example services to help accomplish these tasks.
- For multi-step manufacturing processes, implement
state machines to coordinate event sequences and manage process state. Design workflows
that can handle long-running operations while maintaining visibility into process status.
AWS Step functions, Amazon EventBridge, and AWS IoT core are example services to help
accomplish these tasks.

## Key AWS services

- Amazon EventBridge for event routing and filtering
- Amazon SQS for reliable message queueing
- AWS Lambda for serverless event processing
- Amazon SNS for event notifications
- AWS Step Functions for manufacturing process orchestration
- AWS IoT Core for device-generated events

## Resources

**Related documents:**

- [Building Event-Driven Architectures on AWS](https://aws.amazon.com/event-driven-architecture/)
- [Serverless Patterns for Event-Driven Architectures](https://serverlessland.com/patterns)
- [Implementing Idempotency Patterns with AWS Lambda](https://aws.amazon.com/blogs/compute/implementing-idempotent-aws-lambda-functions-with-powertools-for-aws-lambda-typescript/)
- [Handling Failure Scenarios with Amazon SQS Dead-Letter
Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- [Build a serverless Amazon Bedrock batch job orchestration workflow using AWS Step Functions](https://aws.amazon.com/blogs/machine-learning/build-a-serverless-amazon-bedrock-batch-job-orchestration-workflow-using-aws-step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf02-bp01.html*

---

# MIDAPERF02-BP02 Use historical cloud usage data aligned with production schedules and business forecasts

Aligning cloud resource allocation with production schedules and business forecasts
enables organizations to optimize system performance during critical periods while helping
prevent resource constraints that could impact throughput and quality. By analyzing patterns
in historical cloud usage alongside manufacturing cycles, plant managers can anticipate
processing requirements for data-intensive operations like quality inspection systems,
predictive maintenance algorithms, and real-time production monitoring, providing optimal
performance when manufacturing demands are highest.

**Desired outcome:** A predictive resource management approach that provides manufacturing systems with
precisely calibrated computing capacity, removing performance bottlenecks during peak
production periods while maintaining processing responsiveness for time-sensitive
manufacturing analytics and control systems.

Common anti-patterns:

- Using static capacity planning without considering manufacturing cycles, seasonal demands, or planned maintenance windows
- Analyzing cloud usage data in isolation without correlating with production schedules, quality metrics, or business forecasts
- Applying uniform auto-scaling rules across all manufacturing workloads regardless of their specific performance characteristics
- Triggering resource scaling exactly when demand increases without accounting for provisioning and initialization delays
- Using only basic CPU/memory metrics for scaling decisions without considering manufacturing-specific performance indicators
- Running large ETL jobs or analytics workloads during active production periods, competing for resources with real-time systems
- Processing all manufacturing data synchronously, even for non-time-sensitive analytics
- Retaining all historical data at the same performance tier regardless of access patterns
- Setting static performance thresholds that don't account for normal variations in manufacturing operations
- Monitoring individual components without understanding overall system performance impact on manufacturing processes
- Failing to establish and maintain performance baselines for different production scenarios
- Running development, testing, and production workloads on shared infrastructure during critical manufacturing periods
- Not considering latency between cloud resources and manufacturing equipment locations when designing system architecture
- Failing to properly tag resources to correlate performance investments with specific manufacturing outcomes and ROI

**Benefits of establishing this best practice:**

- [Improves production system responsiveness by up to 40% during peak manufacturing
periods](https://www.researchgate.net/publication/393472445_A_Cloud-Native_Framework_for_Cross-Industry_Demand_Forecasting_Transferring_Retail_Intelligence_to_Manufacturing_with_Empirical_Validation)
- Removes data processing bottlenecks that can cause manufacturing quality or
throughput issues
- Enables higher-fidelity monitoring and analytics during critical production runs
- Accelerates time-to-insight for manufacturing intelligence during complex production
sequences
- Facilitates seamless integration between production scheduling and infrastructure
provisioning teams

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Analyze cloud resource utilization patterns during different manufacturing operations to identify performance-critical periods requiring enhanced computing capacity, especially for vision systems, complex analytics, or high-frequency data collection. Analysis and alerting can be implanted through using Amazon CloudWatch, AWS X-Ray, and Amazon CloudWatch insights.
- Establish relationships between specific manufacturing activities (high-precision runs, quality inspections, material changeovers) and corresponding infrastructure performance requirements to develop predictive capacity models.
- Develop automated scaling mechanisms that proactively adjust computing resources based on upcoming production schedules, which verifies that critical systems have sufficient processing power before high-demand manufacturing phases begin. Using services such as Amazon SageMaker AI for predictive modeling, auto scaling with AWS Auto Scaling, and Amazon CloudWatch for monitoring metrics can help with implementation.
- Refine ETL processes and analytics workflows based on historical performance data to maximize throughput during peak production periods when real-time insights are most valuable. AWS services such as Amazon Kinesis Data Streams, Amazon MSK, and AWS IoT Core can help with implementing optimized data processing pipelines. Real time processing can be implemented through Lambda, and Amazon Kinesis Data Analytics. AWS X-Ray can help with end to end pipeline tracking and anomaly detection.
- Implement continuous performance monitoring that compares actual versus expected response times and processing capabilities, refining resource allocation models to improve manufacturing system responsiveness over time. AWS services that can help with implementation are Amazon CloudWatch, AWS X-Ray, and Application Load Balancer.

## Key AWS services

- Amazon CloudWatch for performance monitoring and metrics collection
- AWS Auto Scaling for automatically adjusting capacity based on production needs
- AWS Forecast for predicting resource requirements based on historical patterns
- Amazon Kinesis for managing high-throughput data streams from manufacturing
equipment
- AWS Lambda for dynamic processing of production event data
- Amazon RDS Performance Insights for database performance optimization

## Resources

- [Performance Efficiency Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
- [Implementing Predictive Scaling with AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
- [Real-time Analytics with Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [Optimizing AWS Lambda Performance for Manufacturing Workloads](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf02-bp0.html*

---
