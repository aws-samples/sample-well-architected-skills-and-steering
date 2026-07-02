# MSFTCOST07 — Containers

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MSFTCOST07-BP01 Optimize AWS Fargate tasks with AWS Compute Optimizer

AWS Compute Optimizer can be used to help right size and optimize your workloads running on
AWS Fargate. If not reviewed, long running tasks can be overprovisioned and increase compute
costs.

**Desired outcome:** Aim to achieve optimal resource allocation and
cost efficiency. Right-size our Fargate tasks, avoiding overprovisioning and reducing
unnecessary compute costs. Through regular review and implementation of Compute Optimizer's recommendations,
we expect to maintain well-optimized workloads that balance performance and cost-effectiveness,
ultimately leading to improved resource utilization and significant cost savings in our AWS
environment.

**Common anti-patterns:**

- Deploying Fargate tasks with initial resource configurations and never reviewing or
adjusting them over time, ignoring Compute Optimizer's recommendations and missing significant cost
optimization opportunities.
- Deliberately configuring Fargate tasks with excessive CPU and memory as a
precautionary measure, leading to consistent overprovisioning and unnecessary costs despite
Compute Optimizer showing opportunities for right-sizing.

**Benefits of establishing this best practice:**

- Regular review and implementation of Compute Optimizer recommendations leads to right-sized
Fargate tasks, eliminating waste from overprovisioning and reducing monthly compute costs
while maintaining required performance levels.
- Leveraging Compute Optimizer's ML-powered analytics provides objective, metrics-based insights for
resource allocation decisions, replacing guesswork with actual usage patterns and ensuring
optimal task configurations across your workloads.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Enable AWS Compute Optimizer for your organization or account. Establish a monthly review process for
Fargate task recommendations. Implement changes gradually, starting with non-production
workloads. Monitor performance before and after optimizations. Create a feedback loop to
inform future deployments, and consider automating recommendation implementation through
Infrastructure as Code practices for consistency and efficiency.

### Implementation steps

- Enable AWS Compute Optimizer in your environment through the AWS Management Console and verify it begins
collecting task utilization data for analysis.
- Schedule monthly review meetings with relevant stakeholders to assess Compute Optimizer's
Fargate task recommendations and prioritize which optimizations to implement.
- Create a change management process that includes testing optimizations in
non-production environments first, with clear rollback procedures if needed.
- Implement approved recommendations through your existing Infrastructure as Code
(IaC) framework, ensuring changes are tracked and reproducible.
- Set up CloudWatch dashboards or alerts to monitor performance metrics post-optimization,
ensuring the changes maintain desired service levels while achieving cost savings.

## Resources

**Related documents:**

- [Optimize costs for AWS Fargate tasks on Amazon ECS](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/optimizer-ecs-fargate.html)

**Related tools:**

- [What is
AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost07-bp01.html*

---

# MSFTCOST07-BP02 Improve Amazon Elastic Kubernetes Service cost tracking with Kubecost

Kubecost improves the cost tracking for your Windows containers.
Kubecost helps right sizing cluster nodes, container requests, and
manages underutilized infrastructure.

**Desired outcome:** Aim to achieve
improved cost tracking for our Windows containers. The desired
outcome is to optimize cluster resource utilization through
right-sizing of nodes and container requests, while effectively
managing underutilized infrastructure. This implementation may
provide better visibility into EKS costs, enabling more informed
decision-making and ultimately leading to cost savings in Kubernetes
deployments.

**Common anti-patterns:**

- Lack of cost monitoring tools, leading to untracked spending and
no visibility into workload-specific costs across Amazon Elastic Kubernetes Service (EKS) clusters.
- Blindly overprovisioning Windows container resources without
usage data, resulting in unnecessary infrastructure costs and
resource waste.

**Benefits of establishing this best
practice:**

- Gain detailed insights into container-level expenses, enabling
accurate cost allocation across teams, projects, and workloads.
- Identify and right-size underutilized resources, leading to
significant cost savings and improved cluster efficiency for
Windows containers.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start by deploying Kubecost into your environment. Configure it to
integrate with your EKS cluster and AWS Cost and Usage Reports.
Set up proper tagging for resources to ensure accurate cost
allocation. Regularly review Kubecost dashboards to identify
cost-saving opportunities, such as right-sizing nodes and
optimizing container requests. Use Kubecost's recommendations to
adjust resource allocations and implement cost controls.
Continuously monitor and refine your cost optimization strategy
based on the insights provided by Kubecost.

### Implementation steps

- Deploy Kubecost to your EKS clusters, ensuring proper IAM
roles and permissions are configured
- Set up AWS Cost and Usage Report integration and configure
Kubecost to access your billing data
- Implement a comprehensive resource tagging strategy to
accurately track costs across teams and applications
- Configure alerts and thresholds for cost anomalies and
resource utilization metrics
- Review initial baseline metrics and identify immediate
optimization opportunities for Windows containers
- Establish regular review cycles to analyze Kubecost reports
and implement recommended optimizations

## Resources

**Related documents:**

- [Gain
visibility into your Amazon EKS costs](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/kubecost-main.html)
- [Learn
more about Kubecost](https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring-kubecost-bundles.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost07-bp02.html*

---

# MSFTCOST07-BP03 Change your scale strategy for Windows Containers on Kubernetes using Karpenter

Karpenter is a Kubernetes cluster autoscaler that dynamically
provisions EC2 instances based on your workload demands,
automatically launching right-sized instances in response to pending
pods and continuously evaluating the cluster to optimize costs by
consolidating workloads onto more efficient instance types. The tool
proactively replaces outdated nodes with newer ones to maintain
security compliance and supports diverse compute requirements by
selecting from a broad range of instance types and purchasing
options, including both On-Demand and Spot instances.

**Desired outcome:** Expect to
achieve improved resource utilization, reduced operational overhead,
and optimized cloud costs. EKS clusters will dynamically scale to
meet application demands, maintain up-to-date and secure
infrastructure, and efficiently manage diverse workloads without
manual intervention, ultimately leading to a more responsive,
cost-effective, and easily managed Kubernetes environment on AWS.

**Common anti-patterns:**

- Teams often configure Karpenter with unnecessarily specific
instance type constraints or narrow capacity requirements,
limiting its ability to efficiently provision nodes and
potentially increasing costs by forcing the use of suboptimal
instance types.
- Organizations frequently deploy Karpenter without properly
configuring Pod Disruption Budgets (PDBs), leading to unexpected
application downtime during node consolidation or replacement
operations, as Karpenter may terminate nodes without ensuring
proper workload migration.

**Benefits of establishing this best
practice:**

- By allowing Karpenter to intelligently select from a broad range
of instance types and automatically consolidate workloads,
organizations can significantly reduce their AWS compute costs
while maintaining optimal performance for their applications.
- Teams spend less time on manual cluster management and capacity
planning, as Karpenter automates node provisioning, scaling, and
replacement activities, enabling engineers to focus on
higher-value development tasks.
- With Karpenter's automated node replacement feature, clusters
maintain better security hygiene through regular updates and
patches, reducing the risk of vulnerabilities while ensuring
compliance with security standards without manual intervention.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement Karpenter effectively, define flexible provisioner
configurations that accommodate both Linux and Windows workloads,
ensuring appropriate instance types are available for each OS. Set
up distinct provisioners with OS-specific requirements, configure
Pod Disruption Budgets for critical applications, and establish
proper taints and tolerations to ensure workloads land on
compatible nodes. Regularly monitor cluster behavior and costs to
optimize your configuration.

### Implementation steps

- Install and configure Karpenter in your EKS cluster,
ensuring proper IAM permissions and VPC settings
- Create flexible provisioner configurations for both Linux
and Windows workloads, specifying appropriate instance types
and purchasing options
- Set up Pod Disruption Budgets for critical applications to
maintain availability during node consolidation
- Configure monitoring and alerting to track Karpenter's
performance and cluster resource utilization
- Regularly review and adjust Karpenter settings based on
observed cluster behavior and cost metrics

## Resources

**Related documents:**

- [Karpenter](https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html)
- [Getting
Started with Karpenter](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost07-bp03.html*

---
