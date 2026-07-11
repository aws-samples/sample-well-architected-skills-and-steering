# Well-Architected Framework — Best Practice Manifest

This is a lightweight index of every WA Framework question and best practice.
**Load this file first for any full review** — it gives you the complete catalog
of BP IDs (in canonical `PILLAR##-BP##` format) so you know what to cite from.

For detailed BP guidance (implementation, anti-patterns, resources), load the
corresponding per-pillar file at `references/pillars/{pillar-slug}.md`.

---

## Operational Excellence (OPS)

### OPS1 — How do you determine what your priorities are? (6 BPs)
- `OPS01-BP01` — Evaluate external customer needs
- `OPS01-BP02` — Evaluate internal customer needs
- `OPS01-BP03` — Evaluate governance requirements
- `OPS01-BP04` — Evaluate compliance requirements
- `OPS01-BP05` — Evaluate threat landscape
- `OPS01-BP06` — Evaluate tradeoffs while managing benefits and risks

### OPS2 — How do you structure your organization to support your business outcomes? (6 BPs)
- `OPS02-BP01` — Resources have identified owners
- `OPS02-BP02` — Processes and procedures have identified owners
- `OPS02-BP03` — Operations activities have identified owners responsible for their performance
- `OPS02-BP04` — Mechanisms exist to manage responsibilities and ownership
- `OPS02-BP05` — Mechanisms exist to request additions, changes, and exceptions
- `OPS02-BP06` — Responsibilities between teams are predefined or negotiated

### OPS3 — How does your organizational culture support your business outcomes? (7 BPs)
- `OPS03-BP01` — Provide executive sponsorship
- `OPS03-BP02` — Team members are empowered to take action when outcomes are at risk
- `OPS03-BP03` — Escalation is encouraged
- `OPS03-BP04` — Communications are timely, clear, and actionable
- `OPS03-BP05` — Experimentation is encouraged
- `OPS03-BP06` — Team members are encouraged to maintain and grow their skill sets
- `OPS03-BP07` — Resource teams appropriately

### OPS4 — How do you implement observability in your workload? (5 BPs)
- `OPS04-BP01` — Identify key performance indicators
- `OPS04-BP02` — Implement application telemetry
- `OPS04-BP03` — Implement user experience telemetry
- `OPS04-BP04` — Implement dependency telemetry
- `OPS04-BP05` — Implement distributed tracing

### OPS5 — How do you reduce defects, ease remediation, and improve flow into production? (10 BPs)
- `OPS05-BP01` — Use version control
- `OPS05-BP02` — Test and validate changes
- `OPS05-BP03` — Use configuration management systems
- `OPS05-BP04` — Use build and deployment management systems
- `OPS05-BP05` — Perform patch management
- `OPS05-BP06` — Share design standards
- `OPS05-BP07` — Implement practices to improve code quality
- `OPS05-BP08` — Use multiple environments
- `OPS05-BP09` — Make frequent, small, reversible changes
- `OPS05-BP10` — Fully automate integration and deployment

### OPS6 — How do you mitigate deployment risks? (4 BPs)
- `OPS06-BP01` — Plan for unsuccessful changes
- `OPS06-BP02` — Test deployments
- `OPS06-BP03` — Employ safe deployment strategies
- `OPS06-BP04` — Automate testing and rollback

### OPS7 — How do you know that you are ready to support a workload? (6 BPs)
- `OPS07-BP01` — Ensure personnel capability
- `OPS07-BP02` — Ensure a consistent review of operational readiness
- `OPS07-BP03` — Use runbooks to perform procedures
- `OPS07-BP04` — Use playbooks to investigate issues
- `OPS07-BP05` — Make informed decisions to deploy systems and changes
- `OPS07-BP06` — Create support plans for production workloads

### OPS8 — How do you utilize workload observability in your organization? (5 BPs)
- `OPS08-BP01` — Analyze workload metrics
- `OPS08-BP02` — Analyze workload logs
- `OPS08-BP03` — Analyze workload traces
- `OPS08-BP04` — Create actionable alerts
- `OPS08-BP05` — Create dashboards

### OPS9 — How do you understand the health of your operations? (3 BPs)
- `OPS09-BP01` — Measure operations goals and KPIs with metrics
- `OPS09-BP02` — Communicate status and trends to ensure visibility into operation
- `OPS09-BP03` — Review operations metrics and prioritize improvement

### OPS10 — How do you manage workload and operations events? (7 BPs)
- `OPS10-BP01` — Use a process for event, incident, and problem management
- `OPS10-BP02` — Have a process per alert
- `OPS10-BP03` — Prioritize operational events based on business impact
- `OPS10-BP04` — Define escalation paths
- `OPS10-BP05` — Define a customer communication plan for service-impacting events
- `OPS10-BP06` — Communicate status through dashboards
- `OPS10-BP07` — Automate responses to events

### OPS11 — How do you evolve operations? (9 BPs)
- `OPS11-BP01` — Have a process for continuous improvement
- `OPS11-BP02` — Perform post-incident analysis
- `OPS11-BP03` — Implement feedback loops
- `OPS11-BP04` — Perform knowledge management
- `OPS11-BP05` — Define drivers for improvement
- `OPS11-BP06` — Validate insights
- `OPS11-BP07` — Perform operations metrics reviews
- `OPS11-BP08` — Document and share lessons learned
- `OPS11-BP09` — Allocate time to make improvements

## Security (SEC)

### SEC1 — How do you securely operate your workload? (8 BPs)
- `SEC01-BP01` — Separate workloads using accounts
- `SEC01-BP02` — Secure account root user and properties
- `SEC01-BP03` — Identify and validate control objectives
- `SEC01-BP04` — Stay up to date with security threats and recommendations
- `SEC01-BP05` — Reduce security management scope
- `SEC01-BP06` — Automate deployment of standard security controls
- `SEC01-BP07` — Identify threats and prioritize mitigations using a threat model
- `SEC01-BP08` — Evaluate and implement new security services and features regularly

### SEC2 — How do you manage identities for people and machines? (6 BPs)
- `SEC02-BP01` — Use strong sign-in mechanisms
- `SEC02-BP02` — Use temporary credentials
- `SEC02-BP03` — Store and use secrets securely
- `SEC02-BP04` — Rely on a centralized identity provider
- `SEC02-BP05` — Audit and rotate credentials periodically
- `SEC02-BP06` — Employ user groups and attributes

### SEC3 — How do you manage permissions for people and machines? (9 BPs)
- `SEC03-BP01` — Define access requirements
- `SEC03-BP02` — Grant least privilege access
- `SEC03-BP03` — Establish emergency access process
- `SEC03-BP04` — Reduce permissions continuously
- `SEC03-BP05` — Define permission guardrails for your organization
- `SEC03-BP06` — Manage access based on lifecycle
- `SEC03-BP07` — Analyze public and cross-account access
- `SEC03-BP08` — Share resources securely within your organization
- `SEC03-BP09` — Share resources securely with a third party

### SEC4 — How do you detect and investigate security events? (4 BPs)
- `SEC04-BP01` — Configure service and application logging
- `SEC04-BP02` — Capture logs, findings, and metrics in standardized locations
- `SEC04-BP03` — Correlate and enrich security alerts
- `SEC04-BP04` — Initiate remediation for non-compliant resources

### SEC5 — How do you protect your network resources? (4 BPs)
- `SEC05-BP01` — Create network layers
- `SEC05-BP02` — Control traffic flow within your network layers
- `SEC05-BP03` — Implement inspection-based protection
- `SEC05-BP04` — Automate network protection

### SEC6 — How do you protect your compute resources? (5 BPs)
- `SEC06-BP01` — Perform vulnerability management
- `SEC06-BP02` — Provision compute from hardened images
- `SEC06-BP03` — Reduce manual management and interactive access
- `SEC06-BP04` — Validate software integrity
- `SEC06-BP05` — Automate compute protection

### SEC7 — How do you classify your data? (4 BPs)
- `SEC07-BP01` — Understand your data classification scheme
- `SEC07-BP02` — Apply data protection controls based on data sensitivity
- `SEC07-BP03` — Automate identification and classification
- `SEC07-BP04` — Define scalable data lifecycle management

### SEC8 — How do you protect your data at rest? (4 BPs)
- `SEC08-BP01` — Implement secure key management
- `SEC08-BP02` — Enforce encryption at rest
- `SEC08-BP03` — Automate data at rest protection
- `SEC08-BP04` — Enforce access control

### SEC9 — How do you protect your data in transit? (3 BPs)
- `SEC09-BP01` — Implement secure key and certificate management
- `SEC09-BP02` — Enforce encryption in transit
- `SEC09-BP03` — Authenticate network communications

### SEC10 — How do you anticipate, respond to, and recover from incidents? (8 BPs)
- `SEC10-BP01` — Identify key personnel and external resources
- `SEC10-BP02` — Develop incident management plans
- `SEC10-BP03` — Prepare forensic capabilities
- `SEC10-BP04` — Develop and test security incident response playbooks
- `SEC10-BP05` — Pre-provision access
- `SEC10-BP06` — Pre-deploy tools
- `SEC10-BP07` — Run simulations
- `SEC10-BP08` — Establish a framework for learning from incidents

### SEC11 — How do you incorporate and validate the security properties of applications? (8 BPs)
- `SEC11-BP01` — Train for application security
- `SEC11-BP02` — Automate testing throughout the development and release lifecycle
- `SEC11-BP03` — Perform regular penetration testing
- `SEC11-BP04` — Conduct code reviews
- `SEC11-BP05` — Centralize services for packages and dependencies
- `SEC11-BP06` — Deploy software programmatically
- `SEC11-BP07` — Regularly assess security properties of the pipelines
- `SEC11-BP08` — Build a program that embeds security ownership in workload teams

## Reliability (REL)

### REL1 — How do you manage Service Quotas and constraints? (6 BPs)
- `REL01-BP01` — Aware of service quotas and constraints
- `REL01-BP02` — Manage service quotas across accounts and regions
- `REL01-BP03` — Accommodate fixed service quotas and constraints through architecture
- `REL01-BP04` — Monitor and manage quotas
- `REL01-BP05` — Automate quota management
- `REL01-BP06` — Ensure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover

### REL2 — How do you plan your network topology? (5 BPs)
- `REL02-BP01` — Use highly available network connectivity for your workload public endpoints
- `REL02-BP02` — Provision redundant connectivity between private networks in the cloud and on-premises environments
- `REL02-BP03` — Ensure IP subnet allocation accounts for expansion and availability
- `REL02-BP04` — Prefer hub-and-spoke topologies over many-to-many mesh
- `REL02-BP05` — Enforce non-overlapping private IP address ranges in all private address spaces where they are connected

### REL3 — How do you design your workload service architecture? (3 BPs)
- `REL03-BP01` — Choose how to segment your workload
- `REL03-BP02` — Build services focused on specific business domains and functionality
- `REL03-BP03` — Provide service contracts per API

### REL4 — How do you design interactions in a distributed system to prevent failures? (4 BPs)
- `REL04-BP01` — Identify the kind of distributed systems you depend on
- `REL04-BP02` — Implement loosely coupled dependencies
- `REL04-BP03` — Do constant work
- `REL04-BP04` — Make mutating operations idempotent

### REL5 — How do you design interactions in a distributed system to mitigate or withstand failures? (7 BPs)
- `REL05-BP01` — Implement graceful degradation to transform applicable hard dependencies into soft dependencies
- `REL05-BP02` — Throttle requests
- `REL05-BP03` — Control and limit retry calls
- `REL05-BP04` — Fail fast and limit queues
- `REL05-BP05` — Set client timeouts
- `REL05-BP06` — Make systems stateless where possible
- `REL05-BP07` — Implement emergency levers

### REL6 — How do you monitor workload resources? (7 BPs)
- `REL06-BP01` — Monitor all components for the workload (Generation)
- `REL06-BP02` — Define and calculate metrics (Aggregation)
- `REL06-BP03` — Send notifications (Real-time processing and alarming)
- `REL06-BP04` — Automate responses (Real-time processing and alarming)
- `REL06-BP05` — Analyze logs
- `REL06-BP06` — Regularly review monitoring scope and metrics
- `REL06-BP07` — Monitor end-to-end tracing of requests through your system

### REL7 — How do you design your workload to adapt to changes in demand? (4 BPs)
- `REL07-BP01` — Use automation when obtaining or scaling resources
- `REL07-BP02` — Obtain resources upon detection of impairment to a workload
- `REL07-BP03` — Obtain resources upon detection that more resources are needed for a workload
- `REL07-BP04` — Load test your workload

### REL8 — How do you implement change? (5 BPs)
- `REL08-BP01` — Use runbooks for standard activities such as deployment
- `REL08-BP02` — Integrate functional testing as part of your deployment
- `REL08-BP03` — Integrate resiliency testing as part of your deployment
- `REL08-BP04` — Deploy using immutable infrastructure
- `REL08-BP05` — Deploy changes with automation

### REL9 — How do you back up data? (4 BPs)
- `REL09-BP01` — Identify and back up all data that needs to be backed up, or reproduce the data from sources
- `REL09-BP02` — Secure and encrypt backups
- `REL09-BP03` — Perform data backup automatically
- `REL09-BP04` — Perform periodic recovery of the data to verify backup integrity and processes

### REL10 — How do you use fault isolation to protect your workload? (3 BPs)
- `REL10-BP01` — Deploy the workload to multiple locations
- `REL10-BP02` — Automate recovery for components constrained to a single location
- `REL10-BP03` — Use bulkhead architectures to limit scope of impact

### REL11 — How do you design your workload to withstand component failures? (7 BPs)
- `REL11-BP01` — Monitor all components of the workload to detect failures
- `REL11-BP02` — Fail over to healthy resources
- `REL11-BP03` — Automate healing on all layers
- `REL11-BP04` — Rely on the data plane and not the control plane during recovery
- `REL11-BP05` — Use static stability to prevent bimodal behavior
- `REL11-BP06` — Send notifications when events impact availability
- `REL11-BP07` — Architect your product to meet availability targets and uptime service level agreements (SLAs)

### REL12 — How do you test reliability? (5 BPs)
- `REL12-BP01` — Use playbooks to investigate failures
- `REL12-BP02` — Perform post-incident analysis
- `REL12-BP03` — Test scalability and performance requirements
- `REL12-BP04` — Test resiliency using chaos engineering
- `REL12-BP05` — Conduct game days regularly

### REL13 — How do you plan for disaster recovery (DR)? (5 BPs)
- `REL13-BP01` — Define recovery objectives for downtime and data loss
- `REL13-BP02` — Use defined recovery strategies to meet the recovery objectives
- `REL13-BP03` — Test disaster recovery implementation to validate the implementation
- `REL13-BP04` — Manage configuration drift at the DR site or Region
- `REL13-BP05` — Automate recovery

## Performance Efficiency (PERF)

### PERF1 — How do you select appropriate cloud resources and architecture patterns? (7 BPs)
- `PERF01-BP01` — Learn about and understand available cloud services and features
- `PERF01-BP02` — Use guidance from your cloud provider or an appropriate partner to learn about architecture patterns and best practices
- `PERF01-BP03` — Factor cost into architectural decisions
- `PERF01-BP04` — Evaluate how trade-offs impact customers and architecture efficiency
- `PERF01-BP05` — Use policies and reference architectures
- `PERF01-BP06` — Use benchmarking to drive architectural decisions
- `PERF01-BP07` — Use a data-driven approach for architectural choices

### PERF2 — How do you select and use compute resources? (6 BPs)
- `PERF02-BP01` — Select the best compute options for your workload
- `PERF02-BP02` — Understand the available compute configuration and features
- `PERF02-BP03` — Collect compute-related metrics
- `PERF02-BP04` — Configure and right-size compute resources
- `PERF02-BP05` — Scale your compute resources dynamically
- `PERF02-BP06` — Use optimized hardware-based compute accelerators

### PERF3 — How do you store, manage, and access data? (5 BPs)
- `PERF03-BP01` — Use a purpose-built data store that best supports your data access and storage requirements
- `PERF03-BP02` — Evaluate available configuration options for data store
- `PERF03-BP03` — Collect and record data store performance metrics
- `PERF03-BP04` — Implement strategies to improve query performance in data store
- `PERF03-BP05` — Implement data access patterns that utilize caching

### PERF4 — How do you select and configure networking resources? (7 BPs)
- `PERF04-BP01` — Understand how networking impacts performance
- `PERF04-BP02` — Evaluate available networking features
- `PERF04-BP03` — Choose appropriate dedicated connectivity or VPN for your workload
- `PERF04-BP04` — Use load balancing to distribute traffic across multiple resources
- `PERF04-BP05` — Choose network protocols to improve performance
- `PERF04-BP06` — Choose your workload's location based on network requirements
- `PERF04-BP07` — Optimize network configuration based on metrics

### PERF5 — What process do you use to support more performance efficiency? (7 BPs)
- `PERF05-BP01` — Establish key performance indicators (KPIs) to measure workload health and performance
- `PERF05-BP02` — Use monitoring solutions to understand the areas where performance is most critical
- `PERF05-BP03` — Define a process to improve workload performance
- `PERF05-BP04` — Load test your workload
- `PERF05-BP05` — Use automation to proactively remediate performance-related issues
- `PERF05-BP06` — Keep your workload and services up-to-date
- `PERF05-BP07` — Review metrics at regular intervals

## Cost Optimization (COST)

### COST1 — How do you implement cloud financial management? (9 BPs)
- `COST01-BP01` — Establish ownership of cost optimization
- `COST01-BP02` — Establish a partnership between finance and technology
- `COST01-BP03` — Establish cloud budgets and forecasts
- `COST01-BP04` — Implement cost awareness in your organizational processes
- `COST01-BP05` — Report and notify on cost optimization
- `COST01-BP06` — Monitor cost proactively
- `COST01-BP07` — Keep up-to-date with new service releases
- `COST01-BP08` — Create a cost-aware culture
- `COST01-BP09` — Quantify business value from cost optimization

### COST2 — How do you govern usage? (6 BPs)
- `COST02-BP01` — Develop policies based on your organization requirements
- `COST02-BP02` — Implement goals and targets
- `COST02-BP03` — Implement an account structure
- `COST02-BP04` — Implement groups and roles
- `COST02-BP05` — Implement cost controls
- `COST02-BP06` — Track project lifecycle

### COST3 — How do you monitor usage and cost? (6 BPs)
- `COST03-BP01` — Configure detailed information sources
- `COST03-BP02` — Add organization information to cost and usage
- `COST03-BP03` — Identify cost attribution categories
- `COST03-BP04` — Establish organization metrics
- `COST03-BP05` — Configure billing and cost management tools
- `COST03-BP06` — Allocate costs based on workload metrics

### COST4 — How do you decommission resources? (5 BPs)
- `COST04-BP01` — Track resources over their lifetime
- `COST04-BP02` — Implement a decommissioning process
- `COST04-BP03` — Decommission resources
- `COST04-BP04` — Decommission resources automatically
- `COST04-BP05` — Enforce data retention policies

### COST5 — How do you evaluate cost when you select services? (6 BPs)
- `COST05-BP01` — Identify organization requirements for cost
- `COST05-BP02` — Analyze all components of the workload
- `COST05-BP03` — Perform a thorough analysis of each component
- `COST05-BP04` — Select software with cost-effective licensing
- `COST05-BP05` — Select components of this workload to optimize cost in line with organization priorities
- `COST05-BP06` — Perform cost analysis for different usage over time

### COST6 — How do you meet cost targets when you select resource type, size and number? (4 BPs)
- `COST06-BP01` — Perform cost modeling
- `COST06-BP02` — Select resource type, size, and number based on data
- `COST06-BP03` — Select resource type, size, and number automatically based on metrics
- `COST06-BP04` — Consider using shared resources

### COST7 — How do you use pricing models to reduce cost? (5 BPs)
- `COST07-BP01` — Perform pricing model analysis
- `COST07-BP02` — Choose Regions based on cost
- `COST07-BP03` — Select third-party agreements with cost-efficient terms
- `COST07-BP04` — Implement pricing models for all components of this workload
- `COST07-BP05` — Perform pricing model analysis at the management account level

### COST8 — How do you plan for data transfer charges? (3 BPs)
- `COST08-BP01` — Perform data transfer modeling
- `COST08-BP02` — Select components to optimize data transfer cost
- `COST08-BP03` — Implement services to reduce data transfer costs

### COST9 — How do you manage demand, and supply resources? (3 BPs)
- `COST09-BP01` — Perform an analysis on the workload demand
- `COST09-BP02` — Implement a buffer or throttle to manage demand
- `COST09-BP03` — Supply resources dynamically

### COST10 — How do you evaluate new services? (2 BPs)
- `COST10-BP01` — Develop a workload review process
- `COST10-BP02` — Review and analyze this workload regularly

### COST11 — How do you evaluate the cost of effort? (1 BPs)
- `COST11-BP01` — Perform automation for operations

## Sustainability (SUS)

### SUS1 — How do you select Regions for your workload? (1 BPs)
- `SUS01-BP01` — Choose Region based on both business requirements and sustainability goals

### SUS2 — How do you align cloud resources to your demand? (6 BPs)
- `SUS02-BP01` — Scale workload infrastructure dynamically
- `SUS02-BP02` — Align SLAs with sustainability goals
- `SUS02-BP03` — Stop the creation and maintenance of unused assets
- `SUS02-BP04` — Optimize geographic placement of workloads based on their networking requirements
- `SUS02-BP05` — Optimize team member resources for activities performed
- `SUS02-BP06` — Implement buffering or throttling to flatten the demand curve

### SUS3 — How do you take advantage of software and architecture patterns to support your sustainability goals? (5 BPs)
- `SUS03-BP01` — Optimize software and architecture for asynchronous and scheduled jobs
- `SUS03-BP02` — Remove or refactor workload components with low or no use
- `SUS03-BP03` — Optimize areas of code that consume the most time or resources
- `SUS03-BP04` — Optimize impact on devices and equipment
- `SUS03-BP05` — Use software patterns and architectures that best support data access and storage patterns

### SUS4 — How do you take advantage of data management policies and patterns? (8 BPs)
- `SUS04-BP01` — Implement a data classification policy
- `SUS04-BP02` — Use technologies that support data access and storage patterns
- `SUS04-BP03` — Use policies to manage the lifecycle of your datasets
- `SUS04-BP04` — Use elasticity and automation to expand block storage or file system
- `SUS04-BP05` — Remove unneeded or redundant data
- `SUS04-BP06` — Use shared file systems or storage to access common data
- `SUS04-BP07` — Minimize data movement across networks
- `SUS04-BP08` — Back up data only when difficult to recreate

### SUS5 — How do you select and use cloud hardware and services to support your sustainability goals? (4 BPs)
- `SUS05-BP01` — Use the minimum amount of hardware to meet your needs
- `SUS05-BP02` — Use instance types with the least impact
- `SUS05-BP03` — Use managed services
- `SUS05-BP04` — Optimize your use of hardware-based compute accelerators

### SUS6 — How do your organizational processes support your sustainability goals? (5 BPs)
- `SUS06-BP01` — Communicate and cascade your sustainability goals
- `SUS06-BP02` — Adopt methods that can rapidly introduce sustainability improvements
- `SUS06-BP03` — Keep your workload up-to-date
- `SUS06-BP04` — Increase utilization of build environments
- `SUS06-BP05` — Use managed device farms for testing

---

**Total: 307 BPs across 57 questions in 6 pillars.**
