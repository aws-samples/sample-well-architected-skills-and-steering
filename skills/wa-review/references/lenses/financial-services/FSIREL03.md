**Pillar**: Reliability

# FSIREL03: How are your business and regulatory requirements driving the resilience of your workload?

## FSIREL03-BP01 Use business criticality to drive recovery objectives

Financial institutions scrutinize their most critical functions where a disruption
to the function could cause harm to consumers, policy holders, participants, or
industry integrity. This harm could mean that customers are unable to quickly recover
(for example, when a firm is unable to put a client back into the correct financial
position after a disruption or if they exceed the allowed disruption time). Resilience
requirements should guide the development and operation of workloads that deliver or
support these functions. Resilience requirements should be written to verify that the
workload implementing the requirements is able to meet impact tolerances. In capturing
resilience requirements, financial institutions must also consider any regulatory
requirements concerning resilience.

The resilience of a workload should be defined by the business sponsoring the
workload and is usually presented as RTO and RPOs plus a service-level objective
(SLO). The criticality of a workload should therefore drive the investment for
automated recovery of the workload. Example SLOs and mappings to resilience tiers are
shown in Table 1 and 2.

*Table 1 – Example resilience tiering for
SLO*

Availability SLO
Resilience tier
Acceptable downtime per year

99.99%
Platinum - Tier 1
52.60 minutes

99.90%
Gold - Tier 2
8.77 hours

98%
Silver - Tier 3
7.31 days

*Table 2 – Example resilience tiering for RTO and RPO*

Tier
Max RTO
Max RPO
Criteria
Cost

Platinum - Tier 1
15 minutes
30 seconds
Mission-critical workloads
$$$

Gold - Tier 2
15 minutes – 8 hours
2 hours
Important, but not mission-critical workloads
$$

Silver - Tier 3
6 hours – a few days
24 hours
Noncritical workloads
$

## FSIREL03-BP02 Apply fine grained workload resilience requirements

It's common to initially think of a workload's availability as a single target for
the workload as a whole. However, upon closer inspection, we frequently find that
certain functions of a workload have different availability requirements. For example,
some systems might prioritize the ability to receive and store new data ahead of
retrieving existing data. Other systems prioritize real-time operations over
operations that change a system's configuration or environment. The Well-Architected
reliability pillar outlines a few of the ways that you can decompose a single workload
into constituent parts-per-function and evaluate the availability requirements for
each. The benefit of decomposing is to focus efforts on availability according to the
specific needs of and the value delivered by the individual function, rather than
engineering the whole system to the strictest requirement.

Developing a system to the highest levels of availability can be expensive. Being
able to address the resilience of individual workload functions can allow you to
justify the investment based on the value of the function. With the functions measured
by their criticality, you can also make informed trade-offs such as degrading the
performance of less critical functions to maintain performance of the workload's most
critical functions.

## FSIREL03-BP03 Use past examples of market volatility in determining peak loads

In financial services workloads, even ones that do not directly provide services
for traders such as settlement and clearing, market volatility creates peak demand
requirements with a long-tail. The peak volume of an extreme event is much higher than
one would expect to model a normal distribution, and thus typical p95 and p99 metrics
are insufficient for estimating peak load. Determine if the workloads have
dependencies on market volatility, and adjust load testing scenarios based on
historical peaks, allowing you to determine how the workload performs in unexpected
situations. It is common that financial services workloads are subject to dramatic
increases in demand. The scaling response to the increase in demand must keep up with
the change in demand. For example, automatic scaling can take several minutes for a
workload to be ready to receive traffic, and may exceed the ability to respond to
customer requests in the expected timeframe, resulting in missed SLAs. For mission
critical workloads, consider concepts like [static
stability](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) and [graceful degradation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html) so that the workload continues to perform within
acceptable limits, even under extreme load.

## FSIREL03-BP04 Model failures to identify resilience requirements

Resilience requirements, like other system requirements, can
be tested and should be documented in response to a business
need. A resilience requirement must be met by the workload
in order

to achieve the RTO, RPO, and availability objective of the
business function the workload supports. The resilience
requirement does this by defining a control, which must be
designed and implemented to mitigate the impact of a failure
somewhere within the workload, with the

workload's dependencies, or in the workload's environment.

Use modeling techniques (for example, failure modes and
effects analysis (FMEA)), combined with Operational Readiness
Reviews (ORR), to anticipate the scenarios that could
disrupt the workload's ability to meet its objectives.
Create resilience requirements to mitigate any harm
anticipated by the failure modeling analysis.

As failures are modeled, implement appropriate tooling to
detect these failures in the future. Create runbooks for
documentation on resolving failures to minimize impact.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel03.html*
