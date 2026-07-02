# LSPERF06 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF06-BP01 Run comprehensive, benchmark-driven assessments

Execute standardized application-specific benchmarks using
representative datasets across multiple hardware solutions (GPUs,
FPGAs, ASICs), measuring not only raw performance but also
performance-per-watt, scaling efficiency, and cost-effectiveness
with your actual production workloads in molecular dynamics
(GROMACS, NAMD, AMBER) and genomics (BWA-MEM, GATK, Minimap2).

**Desired outcome:** Conduct
comprehensive benchmarks of scientific applications across diverse
hardware solutions to measure performance, energy efficiency,
scaling, and cost-effectiveness for optimal computational research
infrastructure selection.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Establish Standardized Testing
Methodology:**Develop rigorously controlled benchmark
protocols specific to life sciences applications. Standardized
methodologies facilitate consistent, reproducible results that can
be compared across different hardware architectures and over time.

**Evaluate Comprehensive Performance
Metrics:**Measure multiple dimensions of hardware
performance beyond raw speed. Comprehensive metrics provide a
holistic view of hardware value, including energy efficiency, cost
factors, and scaling characteristics.

**Compare Across Hardware Accelerator
Types:**Conduct benchmarks across diverse specialized
computing architectures. Systematic comparison across acceleration
technologies reveals which hardware best matches specific
application characteristics.

**Validate with Production
Workloads:**Use actual production datasets and workflows
for benchmark validation. Real-world validations make sure
benchmark results translate to meaningful improvements in
day-to-day research operations.

**Create Decision Support
Framework:** Develop a structured approach to translate
benchmark data into procurement decisions. A formal framework
validates objective evaluation of hardware options based on
quantified performance metrics aligned with research priorities.

### Implementation steps

- Define benchmark frameworks with standardized tests for
molecular dynamics and genomics.
- Implement measurements for performance-per-watt metrics and
total cost calculations.
- Execute testing across GPU, FPGA, and ASIC solutions for
bioinformatics.
- Perform validation using actual simulations to verify
benchmark predictions.
- Establish hardware selection using scoring matrices and ROI
models.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf06-bp01.html*

---

# LSPERF06-BP02 Perform a total cost of ownership analysis

Calculate complete TCO incorporating hardware acquisition costs,
software licensing, power consumption, cooling requirements,
physical footprint, specialized expertise needs, and expected
hardware lifespan, while quantifying research productivity
improvements to determine true value beyond initial purchase price.

**Desired outcome:** Develop
comprehensive TCO analysis including direct and indirect costs while
quantifying research productivity gains to reveal true value and
inform strategic technology investments beyond purchase price alone.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Develop financial models that capture direct and indirect
infrastructure expenses. Complete cost visibility blocks
unexpected budget impacts and enables accurate comparison between
technology options.

Evaluate costs across the entire useful lifespan of research
infrastructure. Lifecycle analysis reveals the true long-term
financial impact of technology decisions beyond initial
acquisition costs.

Measure how infrastructure investments translate to research
output improvements. Productivity quantification enables
value-based decisions by connecting technology costs to scientific
outcomes.

Integrate cost and benefit data to calculate true return on
infrastructure investment. Holistic value analysis balances
financial considerations with research advancement to optimize
technology investment decisions.

Monitor ongoing value delivery from infrastructure investments
after deployment. Continuous tracking verifies that technologies
deliver expected benefits and informs future procurement decisions
with actual performance data.

### Implementation steps

- Document costs including direct expenses, operational costs,
and staffing requirements.
- Develop financial models with depreciation schedules and
projected maintenance costs.
- Establish research metrics with productivity indicators and
improvement forecasts.
- Create value assessments with cost-per-output calculations
and comparison frameworks.
- Implement value tracking with ongoing measurement and
periodic TCO reassessment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf06-bp02.html*

---

# LSPERF06-BP03 Perform an environment compatibility validation

Evaluate hardware accelerators within your existing computational
infrastructure, verifying integration with workload managers,
container technologies, data transfer mechanisms, and storage
systems while assessing software support maturity, driver stability,
and vendor commitment to the scientific computing community.

**Desired outcome:** Identify
hardware accelerators compatible with current systems, providing
support for workloads, containers, and data needs while evaluating
software maturity and vendor reliability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Assess how accelerators interact with existing infrastructure
components. Comprehensive compatibility testing blocks deployment
delays and verifies that accelerators function properly within the
broader technology environment.

Assess the development status of libraries and tools supporting
the accelerator. A mature software solution verifies that
researchers can effectively utilize accelerator capabilities
without extensive custom development.

Determine the reliability of driver implementations and vendor
support responsiveness. Stable operation is critical for
production research environments where downtime directly impacts
scientific progress.

Evaluate the accelerator provider's dedication to research and
scientific applications. Vendor commitment continues the
development of features relevant to computational life sciences.

Identify potential challenges and mitigations across technical,
operational, and strategic dimensions. Comprehensive risk
assessment provides for informed decision-making that accounts for
both opportunities and potential complications.

### Implementation steps

- Conduct testing to validate compatibility with existing
systems and technologies.
- Analyze software support through libraries, compiler
capabilities, and documentation.
- Evaluate readiness through load testing and peer institution
consultation.
- Assess vendor alignment by reviewing roadmaps and life
sciences investments.
- Develop risk framework with technical evaluations and
contingency plans.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf06-bp03.html*

---
