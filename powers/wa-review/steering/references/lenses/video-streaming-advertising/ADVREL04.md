# ADVREL04 — Change management

**Pillar**: Reliability  
**Best Practices**: 2

---

# ADVREL04-BP01 Through your CI/CD pipeline, employ end-to-end regression, performance, and canary testing

Integrate comprehensive testing methodologies into CI/CD pipelines
for advertising workloads. Monitor key metrics like 5xx errors and
latency, especially in RTB systems, and respond quickly to issues
through immediate engagement and fast rollbacks.

## Implementation guidance

For RTB at scale, the primary reliability metrics for
availability are 5xx internal errors and elevated latency. If
these metrics are breached, do not wait for impacts to ad
effectiveness. Instead, fail fast and revert changes until the
root cause of the issue can be identified and addressed.

## Key AWS services

- [AWS CodePipeline](https://aws.amazon.com/codepipeline/) is a fully-managed continuous
delivery service
- [AWS Fault Injection Service](https://aws.amazon.com/fis/) is a
fully-managed service that simulates real-world failures
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

## Resources

- [Deployment
strategies](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html)
- [Canary
deployments](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/canary-deployments.html)
- [Use
CloudWatch Synthetics to Monitor Sites, API Endpoints, Web Workflows, and More](https://aws.amazon.com/blogs/aws/new-use-cloudwatch-synthetics-to-monitor-sites-api-endpoints-web-workflows-and-more/)
- [Performing
canary deployments and metrics-driven rollback with Amazon managed Service for Prometheus and Flagger](https://aws.amazon.com/blogs/opensource/performing-canary-deployments-and-metrics-driven-rollback-with-amazon-managed-service-for-prometheus-and-flagger/index.html)
- [Testing
and creating CI/CD pipelines for AWS Step Functions](https://aws.amazon.com/blogs/devops/testing-and-creating-ci-cd-pipelines-for-aws-step-functions-using-aws-codepipeline-and-aws-codebuild/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp01.html*

---

# ADVREL04-BP02 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful

Implement gradual, phased deployments to minimize risks and
service impacts when updating systems.

## Implementation guidance

When deploying new code or resources, it is possible for
unintended results to occur. Various deployment strategies can
be used to reduce frequency and service impact.

By making changes through a blue/green deployment methodology,
you can significantly reduce the impact of any potential issues
and avoid downtime.

When a blue/green deployment isn't possible, a rolling
deployment methodology should be used to reduce the number of
resources being modified simultaneously. With a rolling
deployment, changes are made in small batches, with a
pre-determined amount of buffer time between batches. If an
issue occurs with the deployment, the unchanged resources can
continue handling traffic, avoiding downtime.

## Key AWS services

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)

## Resources

- [Blue/Green
Deployments on AWS](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html)
- [Rolling
deployments](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/rolling-deployments.html)
- [Deployment
methods](Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp02.html*

---
