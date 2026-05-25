# CloudWatch Metrics Reference for Investigations

## Compute

### EC2 / Auto Scaling
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| CPUUtilization | AWS/EC2 | < 70% | > 80% | > 95% |
| StatusCheckFailed | AWS/EC2 | 0 | — | > 0 |
| NetworkIn/Out | AWS/EC2 | Baseline ±20% | > 2x baseline | > 5x baseline |
| EBSIOBalance% | AWS/EC2 | > 50% | < 30% | < 10% |

### ECS
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| CPUUtilization | AWS/ECS | < 70% | > 80% | > 95% |
| MemoryUtilization | AWS/ECS | < 75% | > 85% | > 95% |
| RunningTaskCount | AWS/ECS | ≥ desired | < desired | 0 |
| ServiceCount (DRAINING) | AWS/ECS | 0 | — | > 0 for extended period |

### Lambda
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| Errors | AWS/Lambda | < 1% | > 1% | > 5% |
| Throttles | AWS/Lambda | 0 | > 0 | > 10/min |
| Duration (p99) | AWS/Lambda | < 60% timeout | > 80% timeout | > 95% timeout |
| ConcurrentExecutions | AWS/Lambda | < 80% limit | > 80% limit | > 95% limit |
| IteratorAge | AWS/Lambda | < 1 min | > 5 min | > 30 min |

## Networking

### ALB / NLB
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| TargetResponseTime (p99) | AWS/ApplicationELB | < 1s | > 2s | > 5s |
| HTTPCode_ELB_5XX_Count | AWS/ApplicationELB | 0 | > 0.1% requests | > 1% requests |
| HTTPCode_Target_5XX_Count | AWS/ApplicationELB | < 0.1% | > 0.5% | > 2% |
| UnHealthyHostCount | AWS/ApplicationELB | 0 | > 0 | > 50% targets |
| RejectedConnectionCount | AWS/ApplicationELB | 0 | > 0 | > 100/min |
| ActiveConnectionCount | AWS/ApplicationELB | < 80% limit | > 80% limit | > 95% limit |

### API Gateway
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| 5XXError | AWS/ApiGateway | < 0.1% | > 0.5% | > 2% |
| 4XXError | AWS/ApiGateway | < 5% | > 10% | > 25% |
| Latency (p99) | AWS/ApiGateway | < 1s | > 3s | > 10s |
| Count (throttled) | AWS/ApiGateway | 0 | > 0 | > 1% requests |

## Database

### RDS
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| DatabaseConnections | AWS/RDS | < 70% max | > 80% max | > 95% max |
| CPUUtilization | AWS/RDS | < 70% | > 80% | > 95% |
| FreeableMemory | AWS/RDS | > 30% total | < 20% total | < 10% total |
| ReadLatency | AWS/RDS | < 5ms | > 10ms | > 50ms |
| WriteLatency | AWS/RDS | < 5ms | > 10ms | > 50ms |
| FreeStorageSpace | AWS/RDS | > 30% | < 20% | < 10% |
| ReplicaLag | AWS/RDS | < 5s | > 30s | > 120s |
| DiskQueueDepth | AWS/RDS | < 5 | > 10 | > 50 |

### DynamoDB
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| ThrottledRequests | AWS/DynamoDB | 0 | > 0 | > 100/min |
| ReadThrottleEvents | AWS/DynamoDB | 0 | > 0 | > 50/min |
| WriteThrottleEvents | AWS/DynamoDB | 0 | > 0 | > 50/min |
| SuccessfulRequestLatency (p99) | AWS/DynamoDB | < 10ms | > 25ms | > 100ms |
| SystemErrors | AWS/DynamoDB | 0 | > 0 | > 10/min |
| ConsumedReadCapacityUnits | AWS/DynamoDB | < 80% provisioned | > 80% | > 95% |

### ElastiCache (Redis)
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| CPUUtilization | AWS/ElastiCache | < 65% | > 75% | > 90% |
| DatabaseMemoryUsagePercentage | AWS/ElastiCache | < 70% | > 80% | > 90% |
| CurrConnections | AWS/ElastiCache | < 80% max | > 80% max | > 95% max |
| CacheHitRate | AWS/ElastiCache | > 90% | < 80% | < 60% |
| ReplicationLag | AWS/ElastiCache | < 1s | > 5s | > 30s |
| EngineCPUUtilization | AWS/ElastiCache | < 65% | > 75% | > 90% |

## Storage

### S3
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| 5xxErrors | AWS/S3 | 0 | > 0 | > 1% requests |
| 4xxErrors | AWS/S3 | < 1% | > 5% | > 15% |
| FirstByteLatency (p99) | AWS/S3 | < 100ms | > 200ms | > 1s |
| TotalRequestLatency (p99) | AWS/S3 | < 500ms | > 1s | > 5s |

### EBS
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| VolumeReadLatency | AWS/EBS | < 2ms | > 5ms | > 20ms |
| VolumeWriteLatency | AWS/EBS | < 2ms | > 5ms | > 20ms |
| VolumeQueueLength | AWS/EBS | < 1 | > 5 | > 20 |
| BurstBalance | AWS/EBS | > 50% | < 30% | < 10% |

## Messaging

### SQS
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| ApproximateAgeOfOldestMessage | AWS/SQS | < 60s | > 300s | > 1800s |
| ApproximateNumberOfMessagesVisible | AWS/SQS | < 1000 | > 10000 | > 100000 |
| NumberOfMessagesSent vs Received | AWS/SQS | Ratio ~1 | Ratio > 2 | Ratio > 10 |
| ApproximateNumberOfMessagesNotVisible | AWS/SQS | < DLQ threshold | Growing | > DLQ threshold |

### SNS
| Metric | Namespace | Normal | Warning | Critical |
|--------|-----------|--------|---------|----------|
| NumberOfNotificationsFailed | AWS/SNS | 0 | > 0 | > 1% published |
| NumberOfNotificationsFilteredOut-InvalidAttributes | AWS/SNS | Stable | Growing | Spike |

## Composite Alarm Patterns

### Service Health (recommended structure)
```
Service Health Alarm (AND)
├── Error Rate Alarm (metric: 5XX / total > threshold)
├── Latency Alarm (metric: p99 > threshold for 3 of 5 datapoints)
└── Availability Alarm (metric: healthy hosts < minimum)
```

### Deployment Safety (recommended structure)
```
Deployment Rollback Alarm (OR)
├── Error Rate Spike (metric: 5XX rate > 2x pre-deploy baseline)
├── Latency Spike (metric: p99 > 2x pre-deploy baseline)
└── Health Check Failures (metric: unhealthy targets > 0 for 2 min)
```

### Capacity Warning (recommended structure)
```
Capacity Warning Alarm (OR)
├── CPU Near Limit (metric: CPUUtilization > 80% for 5 min)
├── Memory Near Limit (metric: MemoryUtilization > 85% for 5 min)
└── Connections Near Limit (metric: connections > 80% max for 5 min)
```
