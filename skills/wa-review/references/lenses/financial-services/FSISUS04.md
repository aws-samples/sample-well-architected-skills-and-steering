**Pillar**: Sustainability

# FSISUS04: How do you prioritize business critical functions over non-critical functions?

Determine what is defined as a business-critical process and workload, and protect and
prioritize it. Model and prioritize individual functions and workloads by recording relevant
metadata, such as interdependencies, SLAs for particular flows, and nuances of user access.

## FSISUS04-BP01 Actively manage each business function and the allocation and configuration of resources

**Prescriptive guidance**

- Use [Amazon ECS Spot](https://aws.amazon.com/ec2/spot/) compute for
non-critical workloads such as end-of-month reconciliations.
- Use [Amazon EC2 Dedicated
Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) queues for priority jobs such as order initiation.
- Use [Amazon ECR Lifecycle
Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) for ephemeral ETL data such as ingestion ledgers.
- Develop architecture strategies that use built-in queueing and buffering to
offload non-critical tasks.

## FSISUS04-BP02 FSI workloads serve the highest common denominator of application demands

Systems in financial services are built to serve the highest level of performance for
retention, availability, and integrity. This leads to workloads that often exceed
performance expectations or might not be respectful of ancillary or critical jobs and
workflows. Breaking down a system into its component parts allows for a more fine-grained
view of resource consumption and the trade-offs possible to balance SLAs against your
sustainability goals.

### Prescriptive guidance

Provide prioritization advice to customers on the following topics:

- **Prioritize at the organizational level:** Determine
what is defined as a business-critical process and workload and protect and
prioritize it.
- **Prioritize at the SCP or OU level:** Restrict AWS
usage-based metrics on your Organizational Units' (OU) profiles and requirements.
Batch-running processes that have extended SLAs can have dedicated accounts and
permissions to restrict and reduce their carbon impact; for

example, select serverless preferences, choose specific instance types, or operate
during specific processing hours. Development and test instances should have enforced
central guardrails to limit Amazon EBS attachments or automatically pause and resume
resources as needed.

- **Prioritize at the account level:** Model and
prioritize individual functions and workloads by recording relevant metadata, such
as interdependencies, SLAs for particular flows, and nuances of user access. For
example, investigations and warm access commonly take longer at a bank than its
typical 35-day retention period.
- **Prioritize at the resource or tag level:** Use tags
to group and aggregate the management and reporting of resources. You may only have
one critical flow but you likely monitor dozens of processes and receive millions of
Event Notifications. Create a prioritization schema to determine which process
matter most to your workload operations.
- **Prioritize at the job or object level:** Not all jobs
are born equal. Use mechanisms such as graceful termination of non-critical jobs and
active workload management to help you prioritize at the job and object levels.
- **Prioritize resource allocation for critical generative AI
applications in financial services:** Implement right-sized generative AI
models for different business criticality levels - use smaller, efficient models for
non-critical functions. Evaluate if generative AI is necessary or if simpler
approaches can achieve the same outcome. FSISUS05: How do you define, review, and
optimize network access patterns for sustainability?

Assess and optimize network access patterns for sustainability. Pay attention to
redundant layers and redirects or patterns generating excessive and unnecessary data
movement.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus04.html*
