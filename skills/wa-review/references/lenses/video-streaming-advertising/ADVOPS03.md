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
