# RAIER01 — System evaluation

**Best Practices**: 3

---

# RAIER01-BP01 Validate that release criteria still align with current industry standards

At the start of a release evaluation, check that the release
criteria and associated evaluation tests are still aligned with the
current version of the AI system. Research and confirm that there
are no new and relevant benchmarks or expectations that need to be
included in the evaluation.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

- Compare your current release criteria against the actual
system features and capabilities you plan to release, looking
for gaps or mismatches. If your system includes capabilities
that were not considered when you last updated your criteria,
consider adding appropriate evaluation tests to cover these
new features. This includes revisiting your risk and benefit
assessment if necessary.
- Stay up to date with new benchmarks, evaluation methods, or
industry standards to see if there are new ways to test your
system against your release criteria.
- Consider new guidelines, updated regulations, or emerging
compliance-aligned frameworks that might affect what you need
to test before release. Consult with your legal team to assess
relevant regulatory considerations.
- Cross-check your evaluation datasets and test cases to make
sure they still match the real-world scenarios where your
system will be used. If your intended use cases have changed
or expanded, you may need to update your evaluation approach
to reflect these new applications.

## Resources

**Related documents**

- [ISO/IEC
42001:2023 A.6.2.4 AI system verification and
validation](https://www.iso.org/standard/42001)

**Related videos:**

- [AWS re:Invent 2024 - Responsible generative AI: Evaluation best
practices and tools (AIM342)](https://www.youtube.com/watch?v=wuVpCc5a81Y)

**Related examples:**

- [awslabs](https://github.com/awslabs)/[agent-evaluation](https://github.com/awslabs/agent-evaluation)
- [aws-samples](https://github.com/aws-samples)/[rag-evaluation](https://github.com/aws-samples/rag-evaluation)

**Related tools**

- [Amazon
Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/)
- [Amazon SageMaker AI AI](https://aws.amazon.com/sagemaker/ai/?trk=bba24a8e-fec0-4c35-b7c7-d2e5e6b67eeb&sc_channel=ps&ef_id=CjwKCAjw2vTFBhAuEiwAFaScwgLGwsaX0LbsbBiFc16GhqyAGMIK79BPAbk_Bnl_-rlJVFq23-H2KRoCz5cQAvD_BwE:G:s&s_kwcid=AL!4422!3!724106169285!e!!g!!amazon%20sagemaker%20ai!19090032234!170269930766&gad_campaignid=19090032234&gbraid=0AAAAADjHtp97_-1psrdUeBS9kWnK-_Zmt&gclid=CjwKCAjw2vTFBhAuEiwAFaScwgLGwsaX0LbsbBiFc16GhqyAGMIK79BPAbk_Bnl_-rlJVFq23-H2KRoCz5cQAvD_BwE)
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raier01-bp01.html*

---

# RAIER01-BP02 Independently corroborate more critical and subjective evaluations

Consider getting second opinions on release criteria that are highly
critical or more subjective. Such opinions can come from internal or
external parties. To maximize independence, consider asking the
independent party to build or acquire their own evaluation datasets,
using the same information about the intended use case(s) of the AI
solution that you intend to communicate to downstream users.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

- Identify which evaluations are most critical or subjective and
would benefit from independent review, such as safety
assessments, unwanted bias evaluations, or user experience
judgments. Include evaluations where your team is more likely
to have blind spots that could affect its assessment.
- Identify independent evaluation teams with the capability of
building or acquiring independent datasets, such as quality
assurance teams, product groups, or other research teams
within your organization.
- Run parallel evaluations where both the development team and
the independent team assess the same aspects of your system
using the same criteria and datasets. This gives you two
perspectives on the same issues and assists you to spot areas
where evaluations might be influenced by external factors.
- For high-risk systems or particularly subjective evaluations,
consider bringing in independent evaluators who have no stake
in your project's success, but who can build their own
evaluations datasets using only the information that you plan
to disclose to downstream deployers and users.
- Compare the results from different evaluation teams and
investigate significant disagreements before making release
decisions. When independent evaluations contradict internal
assessments, dig deeper to understand why before reconsidering
your evaluation approach.

## Resources

**Related documents**

- [ISO/IEC
42001:2023 A.6.2.4 AI system verification and
validation](https://www.iso.org/standard/42001)
- [Thorn
and All Tech Is Human Forge Generative AI Principles with AI Leaders to Enact Strong Child Safety Commitments July 16,
2024](https://www.thorn.org/blog/generative-ai-principles/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raier01-bp02.html*

---

# RAIER01-BP03 For each system update, re-run the evaluation and update the system registry

Record evaluation activities in logs that capture test conditions,
system configurations, data inputs, raw results, and methodological
notes with sufficient detail to make the entire process
reproducible. Establish version control for evaluation artifacts to
assist builders to trace unique system builds and their
corresponding evaluation results.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Log your evaluation runs, including information on which
datasets you used, what system version you tested, what
hardware and software configuration you ran on, and raw and
intermediate outputs. Your logs should be detailed enough that
someone else could reproduce your exact evaluation months
later.
- Set up version control for your evaluation materials,
including test scripts, configuration files, and result
outputs.
- Link your evaluation materials to both your system and your
dataset registry so that it is clear which data and system
versions led to the evaluation results. This allows you to
link each system build and dataset pair to its specific
evaluation artifacts.

## Resources

**Related documents**

- [ISO/IEC
42001:2023 A.6.2.4 AI system verification and
validation](https://www.iso.org/standard/42001)
- [ISO/IEC
42001:2023 A.7.2 Data for development and enhancement of AI
system](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raier01-bp03.html*

---
