**Pillar**: Reliability

# FSIREL07: How do you monitor your resilience objectives to achieve your strategic objectives and business plan?

## FSIREL07-BP01 Monitor and validate your RPO

RPO is the maximum amount of data loss allowed as the result of a system failure
expressed in units of time. Online Transaction Processing (OLTP) systems within
financial services institutions typically leverage continuous data replication to a
failover environment, where the RPO is a function of the latency of the data
replication. AWS database services such as Amazon RDS and Amazon DynamoDB offer continuous data
replication and also provide replication latency metrics that can be continuously
monitored. RPO can be further verified by continuously adding synthetic records into
the transaction stream and validating that each synthetic record was received,
processed, and replicated within the RPO target limit. Furthermore CloudWatch alarms should
be configured to alert whenever replication delays are routinely exceeding the system
RPO limits.

## FSIREL07-BP02 Monitor and validate your RTO

RTO is often defined as the maximum amount of time allowed for a system to resume
its normal operations after a failure. RTO is measured and validated by testing system
recovery processes and directly measuring the time it takes to recover. To be able to
provide audit evidence for proof of DR and recovery exercises, you have to understand
your workload's dependency chains to prove that if any of its dependencies fail, your
service can stay within the boundary of the defined RTO.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel07.html*
