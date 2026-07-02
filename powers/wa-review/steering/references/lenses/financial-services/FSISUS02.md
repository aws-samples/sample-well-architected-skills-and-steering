**Pillar**: Sustainability

# FSISUS02: How do you address data sovereignty regulations for location of sustainable Region?

While selection of low-carbon Regions is generally recommended for processing of
financial data, sometimes data residency requirements stipulate the use of higher carbon
storage.

## FSISUS02-BP01 Run workloads and store restricted data in required country and unrestricted in sustainable Region selected by following SUS01 guidance

### Prescriptive guidance

The following guidance provides insights into data sovereignty regulations.

- Review data sovereignty regulations and identify workloads and data that can be
run in sustainable Regions. You may need to separate your data and processing to
take advantage of data and processes using lower carbon resources where data
residency is not required, while accessing higher carbon resources when data
residency is a requirement.
- Choose a sustainable Region following the guidance provided in FSISUS01.
- Run your workloads and store data whenever you are not restricted to specific
locations using more sustainable Regions.

- Balance data residency requirements with sustainable generative AI
infrastructure placement.
- Verify that generative AI training data and model artifacts adhere to regional
data sovereignty while optimizing for carbon footprint.
- Consider federated learning approaches for generative AI models when data
cannot cross jurisdictional boundaries.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus02.html*
