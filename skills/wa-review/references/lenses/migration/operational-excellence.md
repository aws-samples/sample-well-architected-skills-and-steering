# Operational excellence

**Pages**: 3

---

# Assess

The assess phase of AWS migration is a crucial step that lays the
foundation for a successful migration journey. In this phase, you
delve into various aspects of your migration plan, aligning it
with your organization's goals. To achieve this, you must consider
the scope, technology, and processes involved. Your migration plan
should be based on up-to-date data obtained through a
comprehensive discovery exercise, particularly vital for
long-running migrations. This data informs your migration patterns
and helps in refining your plans regularly.

MIG-OPS-01: Does your migration planning consider scope, technology, and process?

Your migration planning is the key to a successful migration to
AWS, and needs to cover many aspects. These include ensuring you
have the right skills at the points when they are needed and the
capacity required to meet your timeline, scope, and budget. The
requirements on your staff are driven by what you are migrating,
so your plan has to be based on up-to-date data from your
environment, obtained through a discovery exercise early on in
the migration process. For long running migrations spanning over
a year, this data needs to be refreshed and used to refine the
plans on a regular basis. The gathered discovery data may inform
which migration patterns can be adopted.

## MIG-OPS-BP-1.1 Your migration plan must be informed by and reflect technology, processes and business

This BP applies to the following best practice areas:
Organization

### Implementation guidance

**Suggestion 1.1.1**: Define the scope. What are you migrating?

In large migrations, the scope of the program can often remain undefined, even when you're halfway through the migration process. This uncertainty arises because certain factors may only surface in later stages. For instance, you might discover pockets of shadow IT or overlooked network and security requirements essential for your applications to function correctly. To address this, it's advisable to invest time in clearly defining the scope, starting from your desired business outcomes and potentially using discovery tools to uncover assets, as discussed later in this guide.

Furthermore, it's important to acknowledge that the scope is likely to evolve as large migrations frequently encompass unexpected elements. These surprises may include unidentified systems or unforeseen production incidents that can disrupt your plans. Therefore, it's crucial to remain adaptable and have contingency plans in place to ensure the smooth progress of your migration program. For more detail, see [Strategy and best practices for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/scope-strategy-time.html).

**Suggestion 1.1.2:** Understand your current on-premise inventory. Identify the missing details you need to collect and select the right discovery tool to do so.

Begin by identifying the information you have available regarding the environment you intend to migrate and the format in which it exists. Determine what additional information is missing, which is crucial for the workloads you plan to migrate. For instance, you may need insights into your on-premises database systems, networking metrics, application dependencies, visualization requirements, or other resource utilization profiles. Based on these requirements, you should select a discovery tool that can provide this information while adhering to your organization's operational and security standards (for example, whether the tool should be agent-based or agent-less).

Once you've pinpointed the discovery requirements, use a [comparison matrix](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools/) to filter out some of the available options. This results in a list of discovery tools that meet your specific requirements. Following this initial filtration, it is advisable to apply [this three-step technique](https://aws.amazon.com/blogs/architecture/selecting-the-appropriate-discovery-tool-for-your-cloud-migration/) to further narrow down and prioritize the list of discovery tools based on the essential features required for your business.

**Suggestion 1.1.3:** Perform a comprehensive portfolio discovery exercise to understand dependencies and complexity.

Completing a portfolio and discovery exercise is a requirement for a successful migration. In rehost migrations, this discovery exercise needs to be focused on capturing inventory, server to application mapping, and dependencies between systems in order to understand the affinities to drive migration waves and planning. It also provides validation of the scope and approach. For further guidance, see [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/welcome.html).

**Suggestion 1.1.4**: Familiarize yourself with recommended strategies and best practices for large migrations.

Migrating to AWS can be driven by various reasons, such as moving away from aging data centers, improving operational resilience and security posture, or reducing costs. Regardless of the motive, it's crucial to identify and prioritize these drivers, as they can impact migration in terms of time, cost, scope, and risk. Alignment of requirements across different teams, including Infrastructure, security, application, and operations, is key to a successful migration. This alignment aligns everyone towards a common goal and timeline. It's essential to explore how desired business outcomes can harmonize with various team objectives. In large migrations, it's advisable to adopt a *migrate first, then modernize* mindset to manage technical debt efficiently and leverage AWS scalability for long-term benefits in infrastructure deployment and feature release cycles. For detail on setting up and running a migration project at scale, see [Strategy and best practices for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/welcome.html).

**Suggestion 1.1.5**: Familiarize yourself with the technology available to you to expedite the migration.

Technology provides a great foundation for accelerating large migrations. For example, the [Cloud Migration Factory solution](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/) is focused on how to provide end-to-end automation for migrations. For more detail, review the Technology Perspective in [Strategy and best practices for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/technology.html). Check this guidance to explore some of the best practices for using technology to achieve the scale and velocity required, aligned with the scope, strategy, and timelines.

**Suggestion 1.1.6**: Define your process.

Having a well-defined process is a key for a successful
migration. Things like clear escalation path to remove
blocker, communication plan, and change request process are
examples of processes that need to be defined and refined as
the migration occurs. For a more comprehensive list of
example processes to define, see
[Process
perspective](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/process.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/assess-ops.html*

---

# Mobilize

The mobilize phase of migration is a critical step in a smooth
transition to the cloud. It involves comprehensive planning and
preparation, guided by best practices to maximize success. During
this phase, it's essential to establish mechanisms for tracking
planned versus actual business benefits and assess your team's
skills, implementing training plans where required. Acquire the
necessary bandwidth to operate workloads while migrating to the
cloud in parallel. Establish a Cloud Center of Excellence (CCoE)
responsible for cloud operations, and define a comprehensive Cloud
Operations Strategy, covering resource allocation, security, cost
management, and governance to streamline the migration process
effectively.

MIG-OPS-02: How do you report on planned versus actual business benefits throughout your migration?

We see customers with many drivers for migrating their workloads
to AWS, including consolidating or vacating data centers,
achieving cost savings, improving security and operational
resilience, increasing business agility, and improving staff
productivity. Throughout the migration, a wide range of
decisions need to be made, such as the target
[Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instance type or what type of
Amazon Elastic Block Store (Amazon EBS) to use. These micro
decisions may have a large impact on achieving the expected
business benefits at an organizational level. Defining and
measuring KPIs helps make sure that the program remains on track
to achieve the target business outcomes, and influences the
behavior of stakeholders who are making the decisions throughout
a migration. Furthermore, it helps identify when the program is
trending negatively against a KPI so that remediating actions
can be applied following a deep-dive review.

## MIG-OPS-BP-2.1 Define and measure key performance indicators (KPIs) which can be shared with all teams involved in the migration

This BP applies to the following best practice areas:
Organization

### Implementation guidance

**Suggestion 2.1.1**: Establish KPIs that support your target business outcomes.

When determining the KPIs, it's crucial to work backwards from your target business outcome. There might be more than one target business outcome for your migration, so you usually need multiple KPIs. It's recommended to socialize the KPIs with your organization's leaders to create alignment towards the goals. For example, if you're migrating to AWS to increase your operational stability, start by determining specific KPIs that measure operational capability. This could include comparing service availability with the agreed service level agreements (SLAs), the number of unplanned outages per quarter, and mean time to resolve issues. Once this is understood, you can define how it is measured in AWS so that comparisons can be made.

For more detail, see [The Importance of Key Performance Indicators (KPIs) for Large-Scale Cloud Migrations](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/).

MIG-OPS-03: Have you assessed your team's skills, identified any gaps, and implemented a training plan while tracking progress?

There's no denying that migration entails additional work for
your teams. For those responsible for operating and managing the
current environment, it necessitates acquiring new skills for
migrating, operating, and managing applications effectively in
the AWS Cloud. This can result in hesitation or resistance.
However, training your teams not only fosters familiarity with
the AWS Cloud, but also offers clarity on their roles in this
new environment, ultimately boosting their self-confidence in
their capabilities.

## MIG-OPS-BP-3.1 Invest time and effort to ensure the required migration and operations skills are captured, skills gaps identified, and training plans are implemented and managed

This BP applies to the following best practice areas:
Organization

### Implementation guidance

**Suggestion 3.1.1**: Assess your team's current skill level and
training needs.

Before embarking on your migration journey, we strongly recommend conducting an [AWS Learning Needs Analysis](https://aws.amazon.com/training/teams/learning-needs-analysis/) to evaluate the current roles and develop tailored training plans for each individual, aligning their skills with the requirements post-migration to AWS. Once the plan is established, you can identify knowledge gaps and begin preparing your teams. Depending on your team's existing knowledge level of migration, it's advisable to structure your training plan into three tiers: prerequisites, fundamentals, and advanced.

For a large migration project, it is essential that every team member completes the prerequisite-level training, which covers fundamental information about the AWS Cloud and migration concepts. As for the fundamentals and advanced levels, you can use a training plan to assign each workstream a suitable training tier. We recommend structuring training by workstreams rather than job roles and titles, as these can vary significantly across organizations. For more detailed information on training plans, see the following:

- [Large
migration training – Prerequisites](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/training-skills.html#training-pre)
- [Large
migration training – Fundamentals](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/training-skills.html#training-fundamentals)
- [Large
migration training – Advanced](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/training-skills.html#training-advanced)

**Suggestion 3.1.2**: Include references to requirements for
on-premises or legacy systems.

Having the requisite skills from day one is paramount to the successful migration of workloads, especially when dealing with the transition from on-premises or legacy estate. This is essential for maintaining and improving the level of service provided post-migration.

**Suggestion 3.1.3**: Consider engaging with AWS ProServe or a
certified AWS Migration Competency Partner to accelerate your migration readiness.

Education is not something that happens overnight in many cases, and if there is a requirement to move faster, engaging with an [AWS Migration Competency Partner](https://aws.amazon.com/migration/partner-solutions/) or [AWS Professional Services](https://aws.amazon.com/professional-services/) could be a worthwhile option. For more detail, contact your AWS account manager. Another great way to find individuals with the specific AWS skills you need is through [AWS IQ for Experts](https://aws.amazon.com/iq/experts/).

**Suggestion 3.1.4**: Run an AWS Experience Based Accelerator
(EBA).

Running an [AWS Experience Based Accelerator (EBA)](https://aws.amazon.com/blogs/mt/level-up-your-cloud-transformation-with-experience-based-acceleration-eba/), more specifically a Migration EBA, is another great way to improve your team's experience through migrating non-production or pilot applications, with the comfort of having AWS migration experts working alongside you. For more information, contact your AWS account team.

**Suggestion 3.1.5**: Leverage other available training resources
available.

There are other training resources that you can leverage to improve your team's migration skills. For example, the [AWS Migration Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/a033522c-f256-40f9-9ecb-5b76a71589bc/en-US) is a one day workshop that emulates an on-premise migration and allows customers to run a migration to AWS. The migration flow is aligned with [Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/) (MAP) best practices and includes steps from the assess, mobilize, and migrate phases.

MIG-OPS-04: Do you have the bandwidth required to operate your workloads while delivering the cloud migration in parallel?

Migration initiatives require involvement and input from various
teams in order to be successful. For example, input is required
from application owners to determine the move groups (like which
servers and applications must be migrated at the same time), as
well as shaping the target architecture. This extends to
operational teams who are required to support pre-migration,
migration, and cutover activities. At the same time, they need
to perform the roles they carried out before the migration
initiative (like maintaining workloads) and training on the AWS Cloud, so that they are prepared to support workloads once they
are migrated. This makes it important to understand if your
teams have the bandwidth required to operate your workloads
while delivering the cloud migration in parallel.

## MIG-OPS-BP-4.1 Build a comprehensive resource model for your migration that reflects the demands of the migration as well as the regular activities

This BP applies to the following best practice areas:
Organization

### Implementation guidance

**Suggestion 4.1.1**: Identify a cloud sponsor.

This sponsor serves as a driving force behind the migration, linking key performance indicators (KPIs) and objectives to the organization's overarching business goals. In essence, a migration sponsor helps navigate the complexities of migration, making critical decisions, and ultimately propelling the organization towards realizing the full benefits of the AWS Cloud.

**Suggestion 4.1.2**: Consider the workstreams, roles and team
composition required for your migration.

Review [People foundation](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/people-foundation.html) for guidance on workstreams, roles, and team composition before you start constructing your migration workstreams and teams. When assigning resources to roles from your existing teams, be sure to assess their current utilization and where that demand comes from (like normal business operation or other business initiatives and projects).

**Suggestion 4.1.3**: Consider augmenting your existing teams
with skilled resources from other parts of your organization or from a trusted
partner.

You cannot expect to run a large-scale time-bound migration without increasing your teams' workload. If you are not time-bound, and the migration can be spread over a longer period of time, then it may be possible to use the teams you have. However, the higher the migration velocity, the sooner you realize the full benefits of being in the cloud, so it could make sense to engage additional migration resources, such as [AWS Professional Services](https://aws.amazon.com/professional-services/) or [AWS Migration Competency Partners](https://aws.amazon.com/migration/partner-solutions/) to assist without impacting your business operations.

Alternatively, you may decide to leverage [AWS Managed Services](https://aws.amazon.com/managed-services/) to extend your team with operational capabilities, including monitoring, incident management, [AWS Incident Detection and Response](https://aws.amazon.com/premiumsupport/aws-incident-detection-response/), security, patch, backup, and cost optimization for migrated workloads.

MIG-OPS-05: Have you established a Cloud Enablement Engine (CEE) responsible for operating your cloud environment?

A key focus of the Cloud Enablement Engine (CEE) is transforming the information technology (IT) organization from an on-premises operating model to a Cloud Operating Model (COM). These components include the operations, security and control, platform architecture and governance, and infrastructure provisioning and configuration management functions. The target state architecture, as defined by your migration strategies and patterns, dictates the services and platforms that need to be catered for.

The Cloud Enablement Engine (CEE), sometimes referred to as [Cloud Center of Excellence (CCoE)](https://aws.amazon.com/blogs/enterprise-strategy/challenging-conventional-wisdom-about-how-to-build-a-cloud-center-of-excellence/), is defined as a multi-disciplinary team that is assembled to implement the governance, best practices, training, and architecture needed for cloud adoption in a manner that provides repeatable patterns for the larger enterprise to follow.

## MIG-OPS-BP-5.1 Build a Cloud Center of Excellence (CCoE) team within your organization as part of your migration planning

This BP applies to the following best practice areas:
Organization

### Implementation guidance

**Suggestion 5.1.1**: Review the [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/welcome.html).

Familiarize yourself with [People foundation](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/people-foundation.html), which focuses on preparing the people and processes involved in your project for the activities in each stage of the large migration. To build the people foundation, you need to define the workstreams in your project, organize individuals into functional teams, confirm that roles and responsibilities are well understood, and complete training.

**Suggestion 5.1.2**: Establish a cross-functional CCOE in your
organization.

One of the foundational steps that enterprises take as part of their journey to the cloud is establishing a Cloud Center of Excellence (CCoE). The CCoE is a multi-disciplinary team that is assembled to implement the governance, best practices, training, and architecture needed for cloud adoption in a manner that provides repeatable patterns for the larger enterprise to follow. Many companies have found that CCOE can accelerate their migrations to the cloud and broader digital transformations. More details on best practices to creating CCOE be found in [Designing a Cloud Center of Excellence (CCOE)](https://aws.amazon.com/blogs/enterprise-strategy/designing-a-cloud-center-of-excellence-ccoe/) blog post.

**Suggestion 5.1.3**: Define the operational support model during
migration.

In a migration to cloud scenario, it is likely you need to maintain a capability to provide operational support to your on-premises environment, as well as your new cloud environment, at least while you exit your on-premises estate. Operational support for the cloud environment may come from the team that currently provides on-premises support, but frequently a new team is created with skills and experience in the cloud services to be consumed to provide operational support in the cloud. For more detail, see [Building your Cloud Operating Model](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/welcome.html).

**Suggestion 5.1.4**: Define a RACI matrix (responsible,
accountable, consulted, and informed).

A clear shared understanding of where the operational support
delineation lines are to ensure a consistent and reliable
operational support service. A RACI matrix can be used to
capture each domain and activity and identify who is
responsible, accountable, consulted, and informed in each
case. For guidance on creating a cloud operations RACI matrix,
see
[Create
a RACI or RASCI matrix for a cloud operating model](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-raci-or-rasci-matrix-for-a-cloud-operating-model.html).

MIG-OPS-06: What is your cloud operations strategy?

When migrating to AWS, you most likely have people, tools, and
processes already in place to manage your current on-premises
architecture. However, what you have now may not be aligned or
best suited to the environment you are migrating to. Before
migrating workloads to cloud, you should establish an
operational capability in terms of people, tools, and process
that provides all the required operational capabilities expected
by the business. Initially this may be a minimum viable product
(MVP) capability aligned with supporting non-production or pilot
migrations, but prior to migrating production or
business-critical applications, it is strongly recommended to
have a full operational capability in place, serving all
necessary operational requirements.

## MIG-OPS-BP-6.1 Define Cloud Operations Strategy: understand your current operating model, processes and tools, and explore how to implement them efficiently, securely and reliably in the cloud to create your cloud operations strategy

This BP applies to the following best practice areas:
Organization

### Implementation guidance

**Suggestion 6.1.1**:
Prepare the people and process involved in your project for
the activities in each stage of the large
migration.

You need to define the workstreams in your project, organize individuals into functional teams, confirm that the roles and responsibilities are well understood, and complete the necessary training. For more detail, see [People foundation](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/people-foundation.html).

**Suggestion 6.1.2**: Check the operations perspective in Cloud Adoption Framework.

The operations perspective focuses on delivering cloud services at an agreed-upon level with your business stakeholders. Automating and optimizing operations allows you to effectively scale while improving the reliability of your workload. For more detail, see [Operations perspective: health and availability](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/operations-perspective.html).

**Suggestion 6.1.3**: Create your cloud operating strategy and model.

The process of modernizing operations in the cloud involves readiness, automation, and integration. To be operationally ready for your migrated workloads, incorporate tools, people, and process to deliver the various activities that together create a cloud operating model. For guidance on creating a cloud operations strategy and model, see [Modernizing operations in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/welcome.html).

**Suggestion 6.1.4**: Train operational teams on operational AWS services.

Cloud native tools and services for operational capabilities are built for the cloud, and exhibit increased scalability, reliability, and availability. In many cases, cloud-based tools can be used to manage on-premises environments, so a transition to cloud-hosted operational tools may be a sensible approach to avoid duplication of tooling. However, your operations teams need to be trained on these new tools prior to migration. Complete an [AWS Learning Needs Analysis](https://aws.amazon.com/training/teams/learning-needs-analysis/) for each member of your team to provide them an education plan to meet their role specific requirements.

**Suggestion 6.1.5**: Consider using managed service providers or AWS Managed Services (AMS).

If your organization doesn't have enough operational capability to fully cover your cloud operational strategy, consider using managed service providers (MSPs) or AWS Managed Services (AMS) offerings as an initial step. AMS helps you accelerate your adoption of AWS at scale and operate more efficiently and securely. AMS leverages standard AWS services and offers guidance and execution of operational best practices using specialized automation, skills, and experience that are contextual to your environment and application. For a selection of AWS-certified cloud operations managed service providers, see [Find an AWS Partner](https://partners.amazonaws.com/). For more detail on AMS offerings, see

[AWS Managed Services](https://aws.amazon.com/managed-services/).

## MIG-OPS-BP-6.2 Align AWS operational requirements with your existing tools and identify any gaps

This BP applies to the following best practice areas: Prepare

### Implementation guidance

**Suggestion 6.2.1**: Define your AWS operational requirements and identify operational tools.****
Mapping your AWS operational capability requirements to your existing operational tools and processes helps identify where there are gaps, allowing you to build an action plan to fill them. For example, you might decide to use [AWS Backup](https://aws.amazon.com/backup/) to centrally manage and automate your backups on AWS. We recommend reviewing the

[AWS Well Architected Framework Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) for guidance on developing your operational requirements specification and the aligned AWS tools.

## MIG-OPS-BP-6.3 Regularly test your operations in the cloud

This BP applies to the following best practice areas: Operate

### Implementation guidance

**Suggestion 6.3.1**: Simulate operational events.

One way to test operational capability is to simulate life-like system failures. An effective way to do this is by running events in your organization, also known as game days. Game days test systems, processes, and team responses, and help evaluate your readiness to react and recover from operational issues. The purpose is to actually perform the actions the team would perform as if an exceptional event had happened. The [Build Your Own Game Day to Support Operational Resilience](https://aws.amazon.com/blogs/architecture/build-your-own-game-day-to-support-operational-resilience/) blog from AWS guides you through this process and provides links to further information.

MIG-OPS-07: How many servers do you plan to replicate and migrate in each wave, and what factors have you considered when arriving at this number?

The number of servers that can be included in a migration wave, and the duration required to perform the migration, is generally dictated by the people you have to perform the migration, the applications you are migrating, the migration approach used, and the network bandwidth available between the source location and AWS.

For example, let's assume a customer has 1,000 servers to migrate in order to vacate their source data center. They're planning to rehost all of their servers using the AWS Application Migration Service (MGN) and have calculated it'll take approximately five weeks to complete a migration wave from an end-to-end perspective (including change control, governance, migrating the data, and acceptance testing). On average, their migration waves include 50 servers, so with one migration team it could take approximately two years to complete (100 weeks). However, they have sufficient network bandwidth and people to increase this to four migration teams working in parallel, so their migration could take approximately 25 weeks to complete. During the 25-week window, there's a two week change freeze where all migrations are impacted, which means their total estimated migration duration is 27 weeks, with an average velocity of 200 servers every five weeks.

## MIG-OPS-BP-7.1 Calculate your potential migration velocity using both technical and non-technical perspectives (like network bandwidth, team availability, volume of changes, and change freezes)

This BP applies to the following best practice areas: Prepare

### Implementation guidance

**Suggestion 7.1.1**: Determine how many migration waves you need.

When calculating how long your entire migration may take, we recommend first determining how many migration waves you need to perform based on the size of the in-scope estate and how they are migrated.

**Suggestion 7.1.2**: Assess available non-technical resources.

Assess your human resources to determine how many waves you can run in parallel to achieve the target outcomes, and validate it aligns with the business goals.

**Suggestion 7.1.3**: Determine technical limitations like bandwidth.

Assess your network bandwidth to estimate how many waves you can run in parallel to achieve target outcomes, and validate it aligns with the business goals. For more detail, see [AWS Application Migration Service best practices](https://aws.amazon.com/blogs/mt/aws-application-migration-service-best-practices/).

**Suggestion 7.1.4**: Include process estimations such as change management, testing strategy, and outage and maintenance windows.

Don't forget to include aspects like change freezes, which impact the migration.

**Suggestion 7.1.5**: Understand the volume of change necessary for each application in-scope for migration.

Your migration velocity is heavily influenced by how well you know your applications. When using rehost to lift and shift your applications to the cloud, there may still be configuration changes required for the application to work as expected after migration. You need to know what configuration changes are required, who can perform them, how long they will take to perform, and if the changes can be automated. This information should be gathered in a discovery exercise during the migration planning phase and should influence the applications that are assigned to each migration wave. You should have the people required to make these changes (ideally with automation) during the migration event so that the cut over can be performed within the expected time frame. For more detail, see [Application portfolio assessment guide for AWS Cloud migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/introduction.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/mobilize-ops.html*

---

# Migrate

The migrate phase is a pivotal stage in any migration process, and
effective strategies are key to success. It's essential to have a
well-defined testing phase strategy that covers thorough testing
of workloads in the AWS cloud environment. Rigorous and
appropriate testing helps identify and rectify issues before they
impact operations. Additionally, it's crucial to review your
application lifecycle management, such as the CI/CD pipeline, and
make necessary adjustments once your workloads are in the AWS Cloud. Aligning your application deployment and management
processes with the cloud environment can enhance efficiency and
maximize the benefits of AWS migration.

MIG-OPS-08: What is your testing phase strategy?

Every application migration has a testing phase, and you have to
plan how the tests are done, what to test, and what are the test
criteria. Functional testing ensures the seamless integration of
your application with the new environment, requiring the
development of comprehensive unit tests to validate application
workflows. Meanwhile, performance testing evaluates system
response times, identifies bottlenecks, and facilitates
optimization efforts, with cycles of testing and optimization as
needed.

## MIG-OPS-BP-8.1 Ensure you have a testing strategy in place

This BP applies to the following best practice areas: Prepare

With a rehost migration strategy, there is generally no need to perform a full regression functional test, like what you might perform with a major update to an application's code base. Logically, the application architecture and code base are unchanged in AWS, but there have been changes in the infrastructure and it's important to focus the testing on those areas.

When using a rehost migration pattern, your source workloads are cloned into AWS, and when they launch on the Amazon EC2 platform, they may attempt to speak to the services and applications which are still hosted on-premises. This could cause outages to your live systems and corrupt application data, so any testing with cloned workloads must be performed within an isolated network environment, or while the source systems are powered off. Even with source systems powered off, there can still be complications with shared user authentication systems (like Microsoft Active Directory) being updated by test systems.

This need for isolation makes meaningful application testing challenging. Technically, you could provision an isolated network in AWS for testing, but this would also need to permit safe and secure access to a number of shared infrastructure services, perhaps interface with other business critical applications still on-premises, and end users would need to be able to connect to the test application to run the tests. This generally requires significant effort, without really providing the assurance sought, as so much needs to be implemented to protect or replicate the source environment that it becomes questionable if you are actually performing representative testing.

### Implementation guidance

**Suggestion 8.1.1**: Use a risk-based, *points of change* testing strategy with your applications.

The primary change point is in the network, as the application's servers would be hosted in the AWS Cloud, which may have changed the prevailing network latency and could negatively impact end-user performance or interfaces with other applications. Additionally, there may be new controls implemented in the network, with additional firewall rules or network security groups which could impact connectivity to internal or external users, other applications, or external systems. You should create a series of test cases that perform transactions most likely to be impacted by increased network latency, or new network controls, and this may need to be performed from a variety of different user types (for example, internal browser user, fat-client desktop internal user, external browser user, or cloud-hosted virtual desktop user). Have a minimal set of functional test cases that validate the basic application capabilities (for example, user login, navigation around the application, and access to interfacing systems), and create a baseline set of test results from the applications before migration. Finally create a set of test cases that validate operational integration with the cloud operating strategy and model to verify the operational readiness to run the applications in AWS Cloud.

**Suggestion 8.1.2**: Test potential network latencies before moving workloads to the AWS Cloud.

Understand the network latency variance between the source and target environment. Measure the network latency between your users and your on-premises application servers, then deploy test servers on your target AWS networks and measure network latency between your users and the test workloads. If you have multiple source and target geographies, sites, or campuses and user locations (such as virtual desktop on-premises, fat-client on corporate network, or remote laptop on internet and VPN), document and baseline each scenario, then provide the network latency baselines to the migration planning team. It's a common scenario to migrate some of your workloads while keeping identity and access management systems on-premises (for example, Microsoft Active Directory). In this case, you need to consider the extra latency required to authenticate user and application activity. One best practice to minimize potential impact is to extend and configure your on-premises Active Directory domain into AWS, so that workloads running in AWS can communicate with Microsoft AD services hosted there. To explore the options for Microsoft Active Directory in AWS, see [Active Directory Domain Services on AWS](https://aws.amazon.com/solutions/partners/active-directory-ds/).

**Suggestion 8.1.3**: Test application performance before and after migration.

If application transaction performance is important, procure up-to-date performance tests results for the applications before migration, and repeat the same performance tests using the same test suite in the AWS Cloud. Attempting to compare test results from different test tools won't give you the assurance you want. Restrict performance testing to only what is needed to validate acceptable performance, with tests that focus on the points of change in the migrated application instance. If performance testing is not within an acceptable range, a rollback decision should be taken immediately to avoid impacting your business. Consider using automated test tools to minimize the time and effort required.

**Suggestion 8.1.4**: Perform a test cutover in AWS Transform MGN.

The server test cutover is essential for confirming MGN is able to successfully create a clone of the source server which can boot up on the Amazon EC2 platform. The test cutover should be performed within an isolated subnet in AWS, especially for Active Directory connected Windows workloads, to protect live systems and data hosted on-premises. MGN provides the ability to specify which AWS subnet to use for test cutovers.

MIG-OPS-09: Have you reviewed your application lifecycle management (like your CI/CD pipeline) and verified if it needs any adjustment once your workloads are in the AWS Cloud?

CI/CD pipelines or software development lifecycles (SDLC) can
vary in complexity between applications and businesses. Many
contain deployment steps that interact with the underlying
infrastructure in order to provision and de-provision resources,
while others may just need connectivity to code repositories and
tools. When migrating these applications to AWS, take these
processes into consideration, as it requires multiple stages to
migrate both the running application and the associated
deployment pipelines if present.

## MIG-OPS-BP-9.1 Determine if your current CI/CD pipeline works on AWS

This BP applies to the following best practice areas: Prepare

### Implementation guidance

**Suggestion 9.1.1**:
Assess your existing pipeline tools.

An assessment of each tool in the pipeline is required to
verify that it has capabilities to work with the AWS
services required. This assessment drives the requirement to
either build the migration plan and updates required to
support the new target AWS landing zone, or the selection of
new tools to achieve the desired outcome.

## MIG-OPS-BP-9.2 Provision resources through infrastructure as code (IaC) templates

This BP applies to the following best practice areas: Prepare

### Implementation guidance

**Suggestion 9.2.1**: Consider using AWS CloudFormation.

It is recommended that all resources required for each application are provisioned through IaC templates. These templates could be written in [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or another IaC tool. This approach keeps configuration with the application code so it can be managed centrally. With the rehost migration pattern, AWS MGN takes care of the source workload migrations, including all application data and configuration present on the source systems. However, the infrastructure components and configuration around the migrated application server on the Amazon EC2 platform still need to be deployed (for example, VPCs, subnets, network security groups, network access control lists, and load balancers).

**Suggestion 9.2.2**: Consider using a configuration management tool.

Maintain an accurate and complete record of all your cloud workloads, their relationships, and configuration changes over time. For more detail, see [Configuration management](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/configuration-management.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migrate-ops.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
