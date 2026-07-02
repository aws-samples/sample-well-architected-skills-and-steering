# SCPERF01 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# SCPERF01-BP01 Use internal and external risk to determine performance requirements

External regulatory or supplier systems, as well as internal risk
requirements, are often a good place to start for performance
requirements. For certain systems, regulators release sector-wide
guidance and data residency rules and regulators require that
system have the capability to deliver on the operational
resilience and the performance targets they have set for
themselves.

**Desired**
**outcome:** You can achieve best
end-user performance irrespective of the data residency rules due
to the regulatory requirements.

**Benefits of establishing this best
practice:** Low latency, best end-user experience, and
low risk of violating data regulations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

External regulatory or supplier systems, as well as internal
risk requirements, are often a good place to start for
performance requirements. For certain systems, regulators
release sector-wide guidance and data residency rules and
regulators require that system have the capability to deliver on
the operational resilience and the performance targets they have
set for themselves. If the systems update the supplier database
or connected to their network to pull data, the performance
targets should be taken into consideration.

### Implementation steps

- Identify all relevant regulatory requirements and data
residency rules that apply to your supply chain systems.
- Analyze supplier system performance requirements and
integration points that may impact overall system
performance.
- Establish performance baselines based on regulatory
guidance and internal risk assessments.
- Define performance targets that balance compliance
requirements with operational efficiency.
- Implement monitoring and alerting systems to track
performance against established targets.
- Regularly review and update performance requirements as
regulations and business needs evolve.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf01-bp01.html*

---

# SCPERF01-BP02 Factor in rate of increase in load, traffic, and scale-out intervals

Identify the upper bounds of the peak load against a system, as
well as the amount of time needed to reach peak load. Load tests
often overlook the rate of increase in traffic and create tests
that scale up too quickly or too slowly.

**Desired**
**outcome:** You mimic the traffic
and load situation of the system and see how the user experience
in such situations, this will help to fine-tune the underlying
resources of the architecture to achieve better results.

**Benefits of establishing this best
practice:** System resiliency prediction, and system
behavior during peak hours/loads.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Identify the upper bounds of the peak load against a system, as
well as the amount of time needed to reach peak load. Load tests
often overlook the rate of increase in traffic and create tests
that scale up too quickly or too slowly. If the load test ramps
up too quickly, the system may not be able to add capacity
rapidly enough to meet the demand, which degrades performance
and introduces errors. Load tests need to be run periodically
and with every major release of the system or when new systems
or architecture is introduced in the supply chain eco-system.

### Implementation steps

- Analyze historical traffic patterns to identify peak load
periods and growth rates specific to supply chain
operations.
- Design load tests that accurately simulate realistic
traffic ramp-up patterns based on actual usage scenarios.
- Establish automated scaling policies that can respond
appropriately to gradual and sudden load increases.
- Implement comprehensive monitoring during load tests to
identify performance bottlenecks and capacity constraints.
- Create regular load testing schedules that coincide with
major system releases and supply chain system
integrations.
- Document and analyze load test results to continuously
improve system performance and scaling capabilities.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf01-bp02.html*

---
