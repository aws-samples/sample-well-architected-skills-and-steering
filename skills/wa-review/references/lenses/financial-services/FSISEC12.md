**Pillar**: Security

# FSISEC12: How are you meeting your obligations for incident reporting to regulators?

Various regulations require that the banking organizations and
managed service providers notify the regulators as soon as a
cyber security incident has been discovered, such as the
[Final
Issuances](https://www.occ.treas.gov/topics/laws-and-regulations/occ-regulations/final-issuances/index-final-issuances.html) published by the Office of the
Comptroller of the Currency (OCC), Security and Exchanges
Commision (SEC)
[Cybersecurity
Disclosure](https://www.sec.gov/news/statement/gerding-cybersecurity-disclosure-20231214) or the Network and Information
Systems (NIS) regulation. Incident reporting now includes
AI-specific events such as harmful model responses or
unauthorized model access, model manipulation and poisoning
attacks.

## FSISEC12-BP01 Regularly review your incident response plan for regulatory compliance

Organizations that are operating in multiple Regions need to
be aware the
[regulatory
requirements](https://aws.amazon.com/financial-services/security-compliance/compliance-center/) of the regions they are
operating in and any local data residency requirements (such
as
[GDPR](https://aws.amazon.com/compliance/gdpr-center/)).
With local data residency requirements, you cannot copy the
data to a different Region for analysis purposes. In this
case, you may need to consider the latency aspects if you
have a global team that needs to access and analyze data
from a different Region. Consider setting up a local incident
response team that can act on the incident in a timely
manner and report to local regulators as necessary.

As mentioned before, as part of your incident response plan,
you should
[develop
playbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) to standardize response process
for cybersecurity incidents. With the ever-changing
regulatory requirements of the financial industry and the
dynamic nature of cloud environments, it is important to
establish a process that reviews the playbooks in use to
perform incident or recovery communications as required.

### Prescriptive guidance

- Create your own playbooks to facilitate responses during
cybersecurity incidents. Refer to
[building
incident response playbooks for AWS](https://github.com/aws-samples/aws-incident-response-playbooks-workshop)
for sample playbooks.
- Use
[AWS Compliance Center](https://aws.amazon.com/financial-services/security-compliance/compliance-center/?country-compliance-center-cards.sort-by=item.additionalFields.headline&country-compliance-center-cards.sort-order=asc&awsf.country-compliance-center-master-filter=%2Aall) for information on
regulatory responsibilities that can be related to
incident responses.
- For AI systems:

Include AI-specific incidents in response
procedures.
- Develop playbooks for model misuse.
- Establish reporting procedures for AI incidents.
- Include AI events in regulatory reporting
requirements.

## Resources

**Related documents:**

- [General
Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/)

**Related videos:**

- [Introduction
to AWS Compliance Center](https://www.youtube.com/watch?v=lp-Yn-xkhM8&ab_channel=AmazonWebServices)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec12.html*
