**Pillar**: Performance Efficiency

# FSIPERF01: How do you select the best performing architecture?

Performance objectives for workloads can vary depending on the criticality of the
workload. While more stringent performance requirements are expected for critical systems
such as core banking, payments processing, trade performance, and market data feeds, all
cloud workloads benefit from defining performance requirements.

## FSIPERF01-BP01 Use internal and external risk to determine performance requirements

External regulatory, as well as internal risk requirements, are often a good place to
start for performance requirements. For some systems, regulators release sector-wide
guidance including potential stress tests. For others, regulators require that financial
institutions have the capability to deliver on the operational resilience and the
performance targets they have set for themselves.

## FSIPERF01-BP02 Factor in rate of increase in load and scale-out intervals

Identify the upper bounds of the peak load against a system, as well as the amount of
time needed to reach peak load. Load tests often overlook the rate of increase in traffic
and create tests that scale up too quickly or too slowly. If the load test ramps up too
quickly, the system may not be able to add capacity rapidly enough to meet the demand,
which degrades performance and introduces errors. Load tests need to be run periodically
and with every major release of the system.

## FSIPERF01-BP03 Benchmark your solution

Benchmark your existing solution and its components in order to understand their
performance characteristics and capacity to exceed their current profiles. AWS services
like AWS Lambda and CloudWatch can be useful tools for building, running and monitoring a load
testing environment due to their low overhead for setup and extensive scaling
capabilities. For more information, see [AWS Prescriptive Guidance
for load testing](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/welcome.html) and [Distributed Performance
Testing](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf01.html*
