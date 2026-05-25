# Well-Architected Framework — Best Practices Reference

## Operational Excellence

### Design Principles
- Perform operations as code
- Make frequent, small, reversible changes
- Refine operations procedures frequently
- Anticipate failure
- Learn from all operational failures

### Key Best Practices
| Practice | Implementation | AWS Services |
|----------|---------------|--------------|
| IaC for all environments | Version-controlled templates, no manual changes | CloudFormation, CDK, Terraform |
| Automated deployments | CI/CD pipelines with automated testing gates | CodePipeline, CodeBuild, CodeDeploy |
| Observability | Metrics, logs, and traces correlated across services | CloudWatch, X-Ray, OpenTelemetry |
| Runbooks and playbooks | Documented procedures for operational events | Systems Manager, DevOps Agent Skills |
| Deployment strategies | Canary, blue/green, rolling with automatic rollback | CodeDeploy, ECS, EKS |
| Operational reviews | Regular reviews of operational health | AWS Health, Trusted Advisor |

### Investigation Checklist
When investigating operational issues:
1. Check recent deployments — was anything changed in the last 24 hours?
2. Review CloudWatch alarms — which metrics are breaching?
3. Check service quotas — is the workload hitting limits?
4. Review Auto Scaling events — did scaling actions fail?
5. Check dependency health — are downstream services healthy?
6. Review error logs — are there new error patterns?

## Security

### Design Principles
- Implement a strong identity foundation
- Enable traceability
- Apply security at all layers
- Automate security best practices
- Protect data in transit and at rest
- Keep people away from data
- Prepare for security events

### Key Best Practices
| Practice | Implementation | AWS Services |
|----------|---------------|--------------|
| Least privilege | Scoped IAM policies, no wildcards in production | IAM, IAM Access Analyzer |
| MFA enforcement | Required for all human access, especially privileged | IAM, Identity Center |
| Encryption everywhere | At rest and in transit, using CMKs for sensitive data | KMS, ACM, CloudHSM |
| Detection and response | Automated threat detection with response workflows | GuardDuty, Security Hub, Detective |
| Network segmentation | Private subnets, security groups, NACLs | VPC, Network Firewall, WAF |
| Secrets management | No hardcoded credentials, automated rotation | Secrets Manager, Parameter Store |

### Investigation Checklist
When investigating security incidents:
1. Check GuardDuty findings — are there new HIGH/CRITICAL findings?
2. Review CloudTrail — what API calls were made by the affected identity?
3. Check Security Hub — are there compliance violations?
4. Review IAM Access Analyzer — are there external access findings?
5. Check VPC Flow Logs — is there unexpected network traffic?
6. Review Config rules — is there configuration drift?

## Reliability

### Design Principles
- Automatically recover from failure
- Test recovery procedures
- Scale horizontally to increase aggregate workload availability
- Stop guessing capacity
- Manage change in automation

### Key Best Practices
| Practice | Implementation | AWS Services |
|----------|---------------|--------------|
| Multi-AZ deployment | Active resources in 2+ AZs | ALB, RDS Multi-AZ, ECS |
| Auto-scaling | Dynamic scaling based on demand with appropriate limits | Auto Scaling, ECS, Lambda |
| Health checks | Deep health checks that verify actual functionality | ALB, Route 53, ECS |
| Backup and recovery | Automated backups with tested restore procedures | AWS Backup, RDS snapshots |
| Circuit breakers | Prevent cascade failures from dependency issues | App-level, Step Functions |
| Chaos engineering | Regular failure injection to validate resilience | FIS (Fault Injection Service) |

### Investigation Checklist
When investigating reliability issues:
1. Check health check status — which targets are unhealthy?
2. Review scaling events — did Auto Scaling trigger? Did it succeed?
3. Check AZ health — is the issue isolated to one AZ?
4. Review dependency health — are upstream/downstream services affected?
5. Check resource quotas — are limits being hit?
6. Review backup status — when was the last successful backup?

## Performance Efficiency

### Design Principles
- Democratize advanced technologies
- Go global in minutes
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

### Key Best Practices
| Practice | Implementation | AWS Services |
|----------|---------------|--------------|
| Right-sizing | Match resource types to workload requirements | Compute Optimizer, Cost Explorer |
| Caching | Cache at multiple layers (CDN, app, database) | CloudFront, ElastiCache, DAX |
| Async processing | Decouple with queues for non-real-time work | SQS, SNS, EventBridge, Step Functions |
| Database optimization | Read replicas, connection pooling, query optimization | RDS Proxy, Aurora, DynamoDB |
| Content delivery | Edge caching for static and dynamic content | CloudFront, Global Accelerator |
| Load testing | Regular performance testing under expected peak load | Distributed Load Testing on AWS |

### Investigation Checklist
When investigating performance issues:
1. Check latency percentiles — p50, p99, p99.9 for the affected operation
2. Review CPU/memory utilization — is the workload resource-constrained?
3. Check database metrics — connection count, query latency, IOPS
4. Review network metrics — throughput, packet loss, latency
5. Check cache hit rates — are caches effective?
6. Review throttling — are API rate limits being hit?

## Cost Optimization

### Design Principles
- Implement cloud financial management
- Adopt a consumption model
- Measure overall efficiency
- Stop spending money on undifferentiated heavy lifting
- Analyze and attribute expenditure

### Key Best Practices
| Practice | Implementation | AWS Services |
|----------|---------------|--------------|
| Right-sizing | Continuous right-sizing based on utilization | Compute Optimizer, Cost Explorer |
| Pricing models | Savings Plans, Reserved Instances for steady-state | Savings Plans, RIs |
| Spot instances | Use for fault-tolerant, flexible workloads | EC2 Spot, ECS Spot |
| Serverless | Pay-per-use for variable workloads | Lambda, Fargate, Aurora Serverless |
| Data lifecycle | Tiering, expiration, compression | S3 Lifecycle, Glacier, EBS snapshots |
| Tagging and allocation | Tag all resources for cost attribution | Cost Allocation Tags, Organizations |

### Investigation Checklist
When investigating cost anomalies:
1. Check Cost Anomaly Detection — what triggered the alert?
2. Review Cost Explorer — which service/region/account spiked?
3. Check resource utilization — are there idle resources?
4. Review data transfer — are there unexpected cross-region or internet transfers?
5. Check for orphaned resources — unattached EBS volumes, unused EIPs, stale snapshots
6. Review scaling events — did unexpected scaling increase costs?

## Sustainability

### Design Principles
- Understand your impact
- Establish sustainability goals
- Maximize utilization
- Anticipate and adopt new, more efficient hardware and software offerings
- Use managed services
- Reduce the downstream impact of your cloud workloads

### Key Best Practices
| Practice | Implementation | AWS Services |
|----------|---------------|--------------|
| Maximize utilization | Right-size, scale to zero when idle | Auto Scaling, Lambda, Fargate |
| Managed services | Reduce undifferentiated operations | Aurora, DynamoDB, SQS, S3 |
| Data efficiency | Compress, deduplicate, tier, expire | S3 Intelligent-Tiering, Lifecycle |
| Region selection | Choose regions with lower carbon intensity | AWS Customer Carbon Footprint Tool |
| Efficient architectures | Event-driven, async, batch processing | EventBridge, Step Functions, Batch |
| Hardware efficiency | Use Graviton processors for better perf/watt | Graviton EC2, Graviton RDS |

### Investigation Checklist
When assessing sustainability impact:
1. Check resource utilization — are instances consistently under 40%?
2. Review scaling configuration — does the workload scale to zero?
3. Check storage efficiency — is data tiered and expired appropriately?
4. Review compute selection — are Graviton instances used where possible?
5. Check managed service usage — what could be replaced with serverless?
6. Review data transfer patterns — can processing be moved closer to data?
