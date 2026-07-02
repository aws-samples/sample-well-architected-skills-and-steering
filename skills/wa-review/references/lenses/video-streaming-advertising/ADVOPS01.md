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
