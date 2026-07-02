**Pillar**: Reliability

# FSIREL05: Is the resilience of the architecture addressing challenges for distributed workloads across AWS and an external entity?

## FSIREL05-BP01 Evaluate the resilience of cross-cloud application architectures

Understand the characteristics of your application components and how each component that is consumed across clouds may impact your system as a whole. Use failure mode and effects analysis (FMEA) to consider the severity and plausibility of possible failure modes, including application-level failures and service provider failures based on the provider's service event history. Consider if the added complexity of deployment across different types of environments adds to or reduces overall resilience.

## FSIREL05-BP02 Address hybrid resiliency

Use Direct Connect to provide a consistent network experience rather than
internet-based connections. Achieve highly resilient network connections between
Amazon Virtual Private Cloud (Amazon VPC) and your on-premises infrastructure by using multiple redundant
Direct Connect connections. Use AWS Direct Connect Resiliency Toolkit to help you choose
the right resiliency model. The AWS Direct Connect Failover Testing feature allows you to
test the resiliency of your AWS Direct Connect connection by disabling the Border Gateway
Protocol session between your on-premises networks and AWS.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel05.html*
