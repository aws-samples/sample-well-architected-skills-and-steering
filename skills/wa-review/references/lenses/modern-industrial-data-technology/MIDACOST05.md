# MIDACOST05 — Balancing resources

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# MIDACOST05-BP01 Implement a buffering or throttling approach

Implement balanced resource utilization that handles varying workload demands while
maintaining cost efficiency for manufacturing systems. This includes prioritizing critical
processes while queuing less time-sensitive tasks and implementing appropriate scaling
triggers aligned with production cycles.

**Desired outcome:** Balanced resource utilization that handles
varying workload demands while maintaining cost efficiency.

**Common anti-patterns:**

- Implementing throttling on time-critical manufacturing processes
- Using the same buffering strategy for all types of industrial data
- Overlooking real-time requirements of production monitoring systems
- Setting queue limits without considering production batch sizes
- Implementing aggressive throttling that impacts quality data collection
- Not accounting for upstream and downstream dependencies in manufacturing processes
- Using standard IT buffering patterns without adapting to manufacturing needs

**Benefits of establishing this best practice:**

- Controlled resource consumption
- Avoided system overload
- Optimized costs during peak periods
- Improved system stability

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- Documented critical and non-critical manufacturing processes
- Peak resource utilization patterns for different production phases
- Response time requirements for various manufacturing systems

Key decisions needed:

- Resource allocation priorities for critical vs. non-critical processes
- Throttling thresholds for different types of manufacturing workloads
- Queue configurations for deferrable processes
- Scaling triggers aligned with production cycles and peaks

Implement buffering and throttling mechanisms to manage cloud resource utilization
during manufacturing peaks. Design a system that prioritizes critical processes (for
example, real-time monitoring, quality control) for immediate resource access, while queuing
less time-sensitive tasks (for example, batch analytics, report generation). Use
auto-scaling for baseline capacity but implement throttling to help prevent non-critical
tasks from consuming resources needed for production-critical operations.

Consider the following:

- Using Spot Instances for interruptible, non-critical workloads
- Implementing reserved capacity for predictable, critical processes
- Using serverless technologies for sporadic, scalable tasks

Regularly review and adjust your buffering and throttling strategies based on changing
production patterns and business needs.

### Implementation steps

- Identify and categorize manufacturing workloads:

Critical real-time processes (for example, process control, safety systems)
- Time-sensitive operations (for example, quality inspections, inventory
updates)
- Deferrable tasks (for example, long-term analytics, reporting)

- Design resource allocation strategies:

Priority-based access for critical systems
- Queueing mechanisms for non-critical operations
- Load balancing across production lines or facilities

- Implement OT-aware monitoring:

Set up real-time monitoring for critical production KPIs
- Configure alerts based on manufacturing thresholds
- Integrate with SCADA or MES for comprehensive visibility

- Establish OT-IT integrated scaling mechanisms:

Automatic scaling triggered by production volumes
- Resource reservation for planned production increases
- Gradual scale-down aligned with shift changes or maintenance windows

- Conduct regular performance and cost reviews:

Analyze resource utilization against production output
- Identify opportunities for optimization without impacting OT
- Adjust strategies based on changing manufacturing requirements

- Implement feedback loops with shop floor:

Gather input from operators on system performance
- Align IT resource adjustments with production schedules
- Continuously refine based on real-world manufacturing impact

## Key AWS services

- Amazon SQS
- Amazon Kinesis
- AWS Auto Scaling
- Amazon API Gateway

## Resources

**Related documents:**

- [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [Amazon Kinesis Data Streams Developer Guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)
- [Throttle requests to your REST APIs for better throughput in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost05-bp01.html*

---

# MIDACOST05-BP02 Implement dynamic resource provisioning

Enable automated resource scaling that matches manufacturing workload demands while
optimizing costs. This includes implementing warm pools for faster scaling, considering
application warm-up times, and aligning scaling policies with production schedules and peak
processing times.

**Desired outcome:** Automated resource scaling that matches
manufacturing workload demands while optimizing costs.

**Common anti-patterns:**

- Implementing automatic scaling without considering production schedule requirements
- Setting scaling thresholds without consulting manufacturing operations teams
- Using the same scaling policies for both production and non-production workloads
- Neglecting warm-up times for manufacturing applications when scaling
- Implementing aggressive scale-in policies that could impact production monitoring
- Not accounting for data retention requirements when scaling storage resources
- Ignoring the impact of scaling on integrated manufacturing systems
- Setting up dynamic provisioning without consideration for compliance requirements

**Benefits of establishing this best practice:**

- Optimized resource utilization
- Reduced manual intervention
- Cost-efficient scaling
- Improved responsiveness

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- Detailed production schedules and patterns
- Peak resource usage data by workload type
- System warm-up and response time requirements

Key decisions needed:

- Scaling thresholds for different manufacturing workloads
- Resource retention periods based on production needs
- Performance impact limits for critical systems
- Cost optimization targets by workload type

Design your manufacturing workloads to automatically adjust resource provisioning
based on current demand and production schedules. Implement a data-driven approach that
correlates IT resource needs with manufacturing operations, providing appropriate safeguards
for critical production systems and consideration for startup times and warm pools.

### Implementation steps

- Define scaling metrics:

Production demand indicators
- Resource utilization thresholds
- Cost constraints

- Configure auto scaling policies:

Scale-out conditions
- Scale-in conditions
- Cool-down periods

- Implement monitoring.
- Set up cost tracking.
- Perform regular policy review and optimization.

## Key AWS services

- AWS Auto Scaling
- Amazon EC2 Auto Scaling
- AWS Lambda
- Amazon CloudWatch

## Resources

**Related documents:**

- [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)
- [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [AWS Lambda: Configuring reserved concurrency for a function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html)
- [AWS Lambda: Configuring provisioned concurrency for a function PDF RSS](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)
- [Amazon CloudWatch: Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost05-bp02.html*

---
