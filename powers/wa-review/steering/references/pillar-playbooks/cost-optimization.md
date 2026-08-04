# Cost Optimization Pillar — Deep-Dive Discovery Playbook

When wa-review is scoped to the Cost Optimization pillar, apply these specialized discovery steps in addition to general infrastructure discovery.

## Compute Costs

Examine:
- EC2 instance types and sizes in ASG/launch templates
- ECS task definitions (CPU/memory allocations)
- Lambda memory and timeout configurations
- Fargate task sizes
- EKS node group configurations
- Batch compute environments

Flag HIGH RISK:
- Fixed-size compute (no auto-scaling) for variable workloads
- Over-provisioned Lambda (>1024MB for simple operations)
- x86 instance types where Graviton equivalents exist
- Large instances where horizontal scaling with smaller instances would work
- Dev/test environments with production-sized resources
- No scheduled scaling for environments with clear off-hours

## Storage and Data Costs

Examine:
- S3 bucket configs (storage class, lifecycle policies, versioning)
- EBS volume types and sizes
- RDS storage (type, allocated size, auto-scaling)
- DynamoDB capacity mode and provisioning
- ElastiCache node types and cluster sizes
- EFS configurations (throughput mode, lifecycle)
- Backup retention policies
- Log retention settings (CloudWatch log groups)

Flag HIGH RISK:
- S3 buckets without lifecycle policies (accumulating indefinitely)
- CloudWatch log groups with "never expire" retention
- DynamoDB provisioned capacity that should use on-demand (or vice versa)
- Over-provisioned IOPS on EBS/RDS
- EBS volumes not using gp3 (gp2 is more expensive for same performance)
- Backup retention > 35 days without justification
- S3 versioning without lifecycle rules for old versions

## Data Transfer Costs

Examine:
- NAT Gateway usage (VPC endpoints as alternative)
- Cross-region data transfer patterns
- VPC endpoint configurations (or absence for S3/DynamoDB)
- CloudFront distributions (or absence for static content)
- Cross-AZ traffic patterns
- API Gateway type (REST vs HTTP API — 70% price difference)

Flag HIGH RISK:
- S3/DynamoDB access going through NAT Gateway (VPC endpoint would be free)
- No CloudFront for static content delivery
- REST API Gateway where HTTP API would suffice
- Cross-region replication without business justification

## Pricing Model Alignment

Evaluate:
- Steady-state compute → Savings Plans or Reserved Instances opportunity
- Variable/batch compute → Spot Instance opportunity
- Serverless vs provisioned alignment
- DynamoDB on-demand vs provisioned
- Aurora Serverless v2 vs provisioned
- S3 Intelligent-Tiering for unknown access patterns

## Environment and Lifecycle Management

Examine:
- Dev/test/staging environment sizing vs production
- Scheduled scaling or shutdown for non-production
- Resource lifecycle policies (TTL on test resources)
- Cost allocation tags on resources
- Budget and anomaly detection configurations

Flag IMPROVEMENT OPPORTUNITY:
- Non-production running 24/7 at production scale
- No cost allocation tags
- No AWS Budget or Cost Anomaly Detection
- No lifecycle policies on temporary resources

## Cost-Specific Report Format

When producing a pillar-scoped cost report, include:
- **Cost Scorecard** with 6 domains: Compute Right-Sizing, Storage Lifecycle, Data Transfer, Pricing Models, Environment Management, Cost Visibility
- **Savings Summary** table: Category | Current Config | Optimized Config | Relative Savings | Effort
- Savings estimates as relative (%) when absolute spend is unknown

## Calibration

- Always assess trade-offs: cost optimization MUST NOT introduce reliability risks without acknowledgment
- "Cannot Determine" is valid for actual utilization (recommend Compute Optimizer, Cost Explorer)
- Savings estimates should be relative (%) when absolute spend is unknown
