# Operational excellence

**Pillar**: Operational Excellence  
**Pages**: 3

---

# MD_OPS 1: How do you incorporate Māori views into your technology governance and operations?

Where appropriate, the Māori world view (te ao Māori) and Māori knowledge and
understanding (mātauranga Māori) could be incorporated into an organisation's way of operating
its technology in support of Māori customers. Sometimes this cannot be done as easily as
performing operations as code, instead it may require active and ongoing collaboration with Māori.
Understanding Māori interests and considerations relating to data collection, processing, and
storage, as well as how those interests are evolving, helps you make informed technology
decisions both in the interim and the long-term.

- **MD_OPS01-BP01:**
**Incorporate mātauranga Māori into your operational processes when it
relates to Māori data.** There are several ways of doing this. Work directly
with your Māori customer or accessible internal and external Māori advisers to help
develop your organisation's understanding of te ao Māori.
- **MD_OPS01-BP02:**
**Consider governance and accountability over Māori data.**
Consider incorporating specific accountabilities for Māori data into pre-existing roles in
your organisation, such as Chief Information Officer (CIO), Chief Information Security
Officer, or Chief Data Officer (CDO). Formalising these accountabilities and
responsibilities into position descriptions can prioritise Māori data considerations at
the executive level.
- **MD_OPS01-BP03:**
**Consider how you can incorporate international data management
principles into your data governance framework**. Some examples of
international data management principles include Findability, Accessibility,
Interoperability, Reuse (FAIR), which were developed for scientific data management and
stewardship.
- **MD_OPS01-BP04:**
**Consider how to supplement your knowledge for example through using
Māori cultural advisers at the appropriate time**. Build your network of Māori
advisers externally to your organisation, which you can engage with on particular
technology projects. AWS has a growing list of advisers in the Amazon Partner Network.
Working with external advisers also helps you develop your internal capabilities.
- **MD_OPS01-BP05:**
**Develop longer-term policies and procedures.** Consider how
to gradually develop the internal competencies and capabilities in your organisation as
you continue to work with Māori customers. This can help you set your organisation's or
your customer's overall data policies and processes with respect to collecting, storing,
processing, and handling Māori data. Raising awareness and understanding of this across
your technology staff and suppliers can help inform design decisions for handling Māori
data, but this may be a long-term process.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_ops-1-how-do-you-incorporate-māori-views-into-your-technology-governance-and-operations.html*

---

# MD_OPS 2: How can you design data collection with your Māori customer(s) in mind?

Organisations collect and process data to support the delivery of products and services
to customers, stakeholders, and citizens. Data collection occurs in many ways, including
filling in a digital form on a website, sensors capturing environmental data like temperature
or water flow rates, or a research team capturing data from participants in a university
study. Organisations need to consider what data they are collecting, the purpose for
collecting the data, and, in the case of personal information, to adhere to the New Zealand
Privacy Act 2020. For additional considerations around the collection of personal information,
see [Using AWS in the Context of New Zealand Privacy Considerations](https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_New_Zealand_Privacy_Considerations.pdf).

- **MD_OPS02-BP01:**
**Consider adopting a privacy by design approach by designing and
implementing mechanisms and processes that simplify compliance with the New Zealand
Privacy Act 2020.** When collecting and handling personal information, make
sure you comply with all applicable laws, such as the New Zealand Privacy Act 2020. You
can design continuous and informed consent mechanisms that provide clear information to
users about what personal information is being collected and for what purpose. Consider
incorporating mechanisms that make it easier for users to revoke consent and to request
access to, or correction of, their personal information. Maintain consent management over
how you capture, store, and preserve personal information.
- **MD_OPS02-BP02: Consider how you're communicating why you are
collecting this data.** Make it clear to users why the data is being collected,
how it is used, and how privacy is maintained on an ongoing basis. Customers can interact
with your organisation multiple times, so communicating what data is collected, why it is
collected, and how it is collected in the context of the interaction may help. Also
consider when to communicate this. Some examples include:

At the time a user registers or signs up to an organisation (for example, they
sign up to a new bank, a new medical centre, or subscribe to a music streaming
service).
- At the time a user applies for a service from your organisation (for example,
they apply for a home loan, book a medical exam, request a quote for home
improvements, or apply for a government entitlement like a student loan).
- At the time a user interacts with your organisation (for example, they lodge a
complaint with a local council, submit an insurance claim, or request a change to a
home loan).

- **MD_OPS02-BP03: Consider important lineage and provenance of data
that could be captured as additional data.** It may be helpful to capture and
store lineage and provenance data, which could be included as metadata or a tag. This kind
of additional data can provide additional context to the data, such as when it was
collected, how it was collected and who was involved in the collection. Maintaining
careful records of the data provenance can build trust in the integrity and authenticity
of the data and from whom the data was derived. An example of this is a hapū's cultural
archive which captures which whānau provided which cultural record. It could also apply to
organisations conducting surveys of specific populations for the purpose of creating data
sets or performing data analysis.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_ops-2-how-can-you-design-data-collection-with-your-māori-customers-in-mind.html*

---

# MD_OPS 3: How do you use or share Māori data back with Māori?

Organisations use data in many different ways to design and deliver products and
services. They can use it to gain insight and understanding of their organisation, their
industry, and the wider world around them. Organisations should assess any legal and ethical
implications when making decisions relating to how data will be used and shared.

- **MD_OPS03-BP01: Collecting and separating Māori data
appropriately**. Organisations can consider how to collect and separate data
along different dimensions such as iwi and hapū or a Māori organisation. This may make data more relevant or
useful to different groups or communities. This needs to be considered when designing your
initial data collection plan to verify that the right data is collected and organised
early. For example, a government agency may want to report on specific agency outcomes for
Māori populations. If they captured an individual's hapū affiliations, they could report
information at a hapū level. However, if they only captured an individual's record, then
they can only report this at an individual level.
- **MD_OPS03-BP02: Consider how your organisation could share Māori data
back to Māori**. Data that your organisation holds could be used to better
understand Māori communities and realise individual and collective benefits. Consider how
you could identify useful data, and design ways to make data more accessible. Open data
initiatives are one approach, but also remember the importance of complying with the
Privacy Act 2020.
- **MD_OPS03-BP03: Use tools to effectively and securely share data
where there is a specific and appropriate purpose.** There are many approaches
to sharing data. Consider tools to share data both publicly and privately, which fits the
purpose for why that data is being shared and how it needs to be used. Share this data in culturally-appropriate ways, and avoid misappropriating that data or trying to create explanation around that data that isn't culturally-sensitive or informed. Seek advice from your Māori advisers if you are unsure how to do this. This includes open
data portals or exchanges such as the AWS Open Data Registry, AWS Data Exchange, or private data
portals hosted by your organisation. Consider solutions that allow data to be shared using
different formats such as flat files, application programming interfaces (APIs), or
interactive dashboards and visualisations to meet the needs of data consumers.
- **MD_OPS03-BP04: Share data in ways that can be easily used by your
various stakeholders**. Understand your Māori stakeholders, their interests in
accessing and using the data you are sharing back with them, and how they use the data.
This should drive your choice of format for that data. For example, graphs or
visualisations published on your website can make data easy to find and understand, while
data files such as comma-separated values files (CSV) or parquet are better for data
analytics users. An API supports application-to-application integration. For example, a
government agency may provide interactive graphs on their website so that anyone with a
web browser can see graphs relating to key agency objectives. They may provide the data
that sits behind the graphs in a CSV format so that people can download it and load it
into a spreadsheet tool or analytics programme to build their own graphs or perform
additional queries. They may also provide an open API so members of the public can
retrieve the data and load into their own databases or analytics systems.
- **MD_OPS03-BP05: Consider how your organisation could use federated
data access methods.** Organisations often need to access data from other
organisations to support a business process. Federated data approaches can allow
organisations to access data from other organisations without the need to replicate or
copy the data into your own systems. Federated data access models require appropriate
mechanisms for making your organisations data discoverable and for securely sharing data.
- **MD_OPS03-BP06: Define and implement appropriate authorisation
mechanisms.** Design data access mechanisms that support both internal access
and access for external third parties (for example, through federated data access or data
sharing mechanism). Consider authorisation mechanisms including role-based access control
(RBAC), attribute-based access control (ABAC), or policy-based access control (PBAC). The
authorisation mechanism should provide ways to manage, grant, and revoke access and
provide visibility into data access through auditing and logging. Establish appropriate
governance processes to effectively manage the process for requesting, granting, and
revoking access to data by verified, trusted, and approved external third parties.

- **MD_OPS03-BP07: Incorporate responsible and ethical use of machine
learning (ML) and artificial intelligence (AI) as a core part of your governance
framework and development lifecycle.** ML and AI have transformational
potential. It is already widely used for tasks such as transcription, translation, fraud
detection, information security, search, and recommendation engines. At Amazon, we believe
the design, development, and deployment of AI must respect the rule of law, human rights,
and values of equity, privacy, and fairness. We are committed to developing fair and
accurate AI services and providing customers with the tools and guidance needed to build
applications responsibly. Developers and deployers of AI systems should ensure such
systems are built based on principles of safety and responsibility by design. AWS builds
AI with responsibility in mind at each stage of our comprehensive development process.
Throughout design, development, deployment, and operations, we consider a range of factors
including accuracy, fairness, appropriate usage, toxicity, security, safety, and privacy. Ask your Māori customers what particular ethical questions and principles they may want you to adopt as a part of your governance framework and development lifecycle. Regularly revisit and refine your AI ethics practices through ongoing dialogue and partnerships with Māori communities.
- **MD_OPS03-BP08: Leverage vendor tools to provide AI
transparency.** For example, AWS AI Service Cards deliver a form of
transparency documentation that provide customers with a single place to find information
on the intended use cases and limitations, responsible AI design choices, and deployment
and performance optimisation best practices for our AI services. Amazon SageMaker AI Clarify detects
and measures potential bias using a variety of metrics so developers can address potential
bias and explain model predictions. Amazon's Responsible Use of Machine Learning Guide highlights key best practices and
tooling that AI developers and deployers can use to mitigate risks across the lifecycle of
an AI system.
- **Other considerations:**

**Discuss AI with stakeholders.** Artificial intelligence
including generative AI and machine learning is a rapidly evolving area. Discuss the
benefits and risks with your stakeholders. Your stakeholders may be internal to your
organisation, external customers, or members of the public. Cross-functional expertise from technologists, ethicists, lawyers, domain experts, and external resources provides a holistic understanding and consideration of ethical, legal, and domain-specific factors. Customers should engage with Māori stakeholders early and continuously to understand their perspectives, concerns, and preferences regarding the use of certain data in AI/ML deployment and development. Employ Māori expertise in the design, development, and testing phases to verify cultural competence and alignment with tikanga.
- **Consider potential inaccuracies.** Customers should consider potential inaccuracies in ML system results (especially concerning te reo Māori and Māori cultural concepts) and prepare a plan to address them, such as narrowing scope, introducing human oversight, or altering dependencies on the AI system. Customers should also consider incorporating appropriate testing of model outputs into the AI application creation process when model inputs or outputs are dealing with te reo Māori or Māori cultural concepts. Evaluation of outputs should be made by appropriately skilled people. To assess if an AI system operates as intended, it is important to use accurate and representative training data. AWS encourages specific policies and provides safeguards such as [Guardrails for Amazon Bedrock](https://aws.amazon.com/bedrock/guardrails/) to block harmful user inputs.
- **Use case evaluation and testing.** Testing should
include not just the AI system itself but also the overall process it is a part of,
including decisions or actions that might be taken based on system output. Customers should consider evaluating models thoroughly on safety characteristics such as prompt stereotyping (like encoded biases for gender or socioeconomic status), factual knowledge, and toxicity. [FMEval](https://aws.amazon.com/blogs/machine-learning/evaluate-large-language-models-for-quality-and-responsibility/), an open source library is available in [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) for developing these insights. [Model evaluation is also available in Amazon Bedrock](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/) for large language models (LLMs). Model outputs can be evaluated by a pool of human evaluators, or through an automated process. Customers can test performance through techniques like [red teaming](https://www-cdn.anthropic.com/82564d4ec2451b2eed2e0796b7c658fc989f0c1a/Anthropic_RedTeaming.pdf) and reinforcement learning from human feedback (RLHF). Customers should also consider continually evaluating performance and responsibility metrics before deployment and use tools like [SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to detect data drift and prompt retraining if needed.
- **Continuous improvement and validation.** Monitoring for
potential bias and accuracy, and for models performing as expected across different
segments, is an important part of this process.
- **Ongoing education.** AI is a constantly-evolving
landscape, and new techniques, technologies, laws, and social norms continue to be
developed and refined over time. It is essential that all parties involved with
building and using AI systems stay educated on these issues and account for them in
the design, deployment, and operation of their systems. Successful AI adoption requires significant cultural and organisational changes, including defining the roles and responsibilities required for accountability, and customers should verify that they are allowing Māori to make informed decisions about participation.

For further reading, refer to the [AWS Machine
Learning lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html).

AWS continues to update this information and share additional guidance to customers on
the use of AI/ML. Please reach out to the team at AWS for further updates.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_ops-3-how-do-you-use-or-share-māori-data.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
