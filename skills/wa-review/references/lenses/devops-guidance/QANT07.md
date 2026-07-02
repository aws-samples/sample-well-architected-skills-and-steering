**Saga**: Quality assurance
**Capability**: QA.NT — Non-functional testing

---

# [QA.NT.7] Verify service integrations through contract testing

**Category:** RECOMMENDED

Contract testing helps ensure that different system components
or services can seamlessly communicate and are compatible with
each other. This involves creating contracts that detail
interactions between services, capturing everything from
request structures to expected responses. As changes are made,
these contracts can be used by producing (teams that expose
the API) and consuming (teams that use the API) services to
ensure they remain compatible. Contract testing provides a
safety net for both producers and consumers by ensuring
changes in one do not adversely impact the other. This creates
a culture of collaboration between teams while providing
faster feedback for identifying integration issues earlier in
the development lifecycle.

There are different types of contract testing. In
consumer-driven contract testing, the consumer of a service
dictates the expected behaviors of the producer. This is
contrasted with provider-driven approaches, where the producer
service determines its behaviors without explicit input from
its consumers. Consumer-driven contract testing is the type we
generally recommend, as designing contracts with the consumer
in mind ensures that APIs are tailored to the customer's
actual needs, making integrations more intuitive.

Begin by clearly defining contracts between your services. Use
purpose-built contract testing tools, such
as [Pact](http://Pact.io)
or [Spring
Cloud Contract](https://spring.io/projects/spring-cloud-contract/), to simplify managing and validating
contracts. When any modification is made in a producer
service, run contract tests to assess the contracts'
validity. Similarly, before a consumer service integrates with
a producer, run the relevant contract tests to guarantee
they'll interact correctly. This process allows producers to
maintain backwards compatibility, while allowing consumers to
identify and fix potential integration issues early in the
development lifecycle. Embed contract testing into your
deployment pipeline. This ensures continuous validation of
contracts as changes are made to services, promoting a
continuous and consistent integration process.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL03-BP03 Provide
service contracts per API](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_service_architecture_api_contracts.html)
- [Introduction
To Contract Testing With Examples](https://www.softwaretestinghelp.com/contract-testing/)
- [CloudFormation
Command Line Interface: Testing resource types using
contract tests](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.7-verify-service-integrations-through-contract-testing.html*
