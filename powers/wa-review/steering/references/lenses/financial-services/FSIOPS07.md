**Pillar**: Operational Excellence

# FSIOPS7: Have you developed a continuous improvement model?

Financial institutions should continually assess and optimize their operational
processes.

## FSIOPS07-BP01 Test, model, and simulate scenarios before rollout

One of the best practices to determine if you have addressed your risk with
appropriate controls is to actually run scenarios against your cloud control framework and
operational procedures. Once your risk and control program is established, financial
institutions should continually asses and optimize their operational processes. Regular
[game days](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_run_game_days.html) for workloads deployed on AWS can help build your team's muscle
memory and validate that all operational procedures are effective in supporting your
recovery objectives and compliance with notification requirements to regulatory bodies. We
recommend designing game days to test your risk appetite and include severe, but plausible
scenarios.

### Prescriptive guidance

Identify financial services compliance requirements first, and then structure your
game days to meet those requirements. Align the complexity of game days with the
resources available within your organization. For large organizations, game days are
often scoped to a specific business unit or product team. It's acceptable to presume
certain inputs from other teams during your initial game days, which can make scheduling
more practical. It's more important to complete simple game days regularly, and iterate
on the scope and complexity over time, than to try to run complex game days from the
beginning. The most critical piece of a game day is the retrospective review of lessons
learned and the iterative improvement over time. Sufficient time to accomplish this
should be set aside early in the planning process so that it can occur in the days
immediately following the game day.

## FSIOPS07-BP02 Conduct post-event operational reviews

Post-event operational reviews should be conducted after an incident. After
troubleshooting and performing repair procedures, follow-up documentation and actions
should be assigned. An effective post-event review results in a list of practical actions
that address each of the issues that allowed the threat actor to succeed. These actions
should minimize the impact of the event and teach the wider enterprise how to prevent,
detect, and respond to a similar event in the future. For significant events, a Correction
of Error (COE) document should be composed to capture the root cause and take preventative
actions for the future. Implementation of the preventative measures should be measured in
future operations meetings.

### Prescriptive guidance

Post-event operational reviews are comprised of two components: identification of
the problem (root cause analysis) and the identification of actions to help prevent a
reoccurrence of the event (corrective actions). Identify a mechanism, such as an ITSM
tool or ticketing system, to track root cause analysis efforts and associated corrective
actions. Ownership for each task should be assigned to an individual, and a periodic
review should be used to track status. In a large and complex environment, competing
priorities and urgent activities can supersede processes such as post-event reviews that
are important for long-term stability. Leaders should establish a culture which
prioritizes these reviews, and should encourage teams to set aside a recurring time to
spend on analysis and corrective actions.

## FSIOPS07-BP03 Implement feedback loops for model improvement

Establish mechanisms to capture user feedback on generative AI
outputs and use this data to improve prompt engineering, model
selection, bias detection, and operational procedures. Create
processes for incorporating lessons learned into model
governance and operational practices.

### Prescriptive guidance

Deploy feedback collection mechanisms using Amazon DynamoDB to
store user ratings and comments. Use Amazon Comprehend to
analyze feedback sentiment and identify improvement areas.
Implement A/B testing frameworks using AWS Lambda to compare
different models or prompts. Create monthly operational
reviews focused on generative AI metrics and improvement
opportunities. Use Amazon SageMaker AI Clarify for automated bias
detection and fairness analysis based on feedback patterns.
Implement Amazon Athena for advanced analytics on feedback
trends and correlation analysis.

## FSIOPS07-BP04 Conduct generative AI-specific chaos engineering

Test the
[resilience
of generative AI workloads](https://catalog.us-east-1.prod.workshops.aws/workshops/d56fd754-5e56-43c5-addc-d69ac130a099/en-US) through controlled experiments
including model API failures, rate limiting scenarios, quality
degradation simulations, and bias amplification scenarios.
Validate that fallback mechanisms and human oversight processes
function correctly under stress.

### Prescriptive guidance

Use
[AWS Fault Injection Service](https://builder.aws.com/content/2uSMnBJb3h7JxB9SkryFvXfQWk8/chaos-engineering-scenarios-for-genai-workloads) to test generative AI workload
resilience.

Simulate model API throttling, timeout scenarios, and complete
service or model unavailability to test failover mechanisms
and business continuity procedures.

Test fallback mechanisms when primary models are unavailable
including automated switching to backup models.

Validate that human review processes can handle increased load
during model failures.

Test system behavior when input data quality deteriorates to
ensure graceful degradation and appropriate human intervention
triggers.

Simulate bias amplification scenarios to test detection
mechanisms and response procedures for maintaining fair and
compliant AI outputs.

Test cross-system dependencies by simulating failures in
databases, APIs, and other generative AI services' dependent
systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops7.html*
