# RAIER03 — Address unmet release criteria

**Best Practices**: 2

---

# RAIER03-BP01 For each failed release criterion, re-assess the implementation strategy

Re-evaluate the original implementation strategy assigned to each
release criteria. Either improve the execution of the implementation
strategy or design a new approach based of baking techniques (for
example, additional fine-tuning, new training approaches or
component choices), blocking techniques (for example, adding
additional guardrails or filtering strategies) or a user steering
strategy (for example, publishing user guidance).

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Analyze why your current implementation strategy failed to
meet the release criteria by looking at the specific test
results, edge cases where it did not work, and patterns in the
failures. Understanding the root cause assists you to decide
whether you need to alter your existing approach or add
completely new implementation techniques.
- Add new or enhance existing baking solutions by building
additional implementations directly into your model through
extra training rounds, refined fine-tuning approaches, or
different model component choices. These approaches modify the
model's core behavior rather than trying to catch problems
afterward, which can be more effective for persistent issues
that keep appearing.
- Implement new or strengthen existing filtering techniques by
adding more sophisticated content filters, better output
classifiers, or additional input validation rules that catch
harmful content before it reaches users. You might need to
layer multiple blocking approaches or make your existing
filters more sensitive to handle the specific failure cases
you discovered.
- Create new or improve existing guiding approaches that assist
users to avoid harmful interactions through redesigned
interfaces, clearer guidance, better warnings about
limitations, or more comprehensive educational content about
appropriate use cases. This works particularly well for
criteria that depend on how people choose to interact with
your system.
- Test your new or modified implementation approaches against
the same evaluation criteria that your original strategy
failed on. Document what you added or changed and what you can
learn from this experience for future implementations.

## Resources

**Related documents:**

- [Build
responsible AI applications with Amazon Bedrock
Guardrails](https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raier03-bp01.html*

---

# RAIER03-BP02 Identify release criteria that cannot be met and narrow your use case

Assess which of your release criteria you cannot meet with your
current system design and implementation strategies, no matter how
you refine them. When you find gaps that can't be closed through
technical solutions alone, consider whether you are trying to solve
too broad of a problem with your current approach. Rather than
compromising on safety or performance standards, narrow your use
case to focus on scenarios where you can meet your release criteria.
Go back to your original risk and benefit assessment with this more
focused scope, identifying new opportunities and constraints that
come with the narrower application. Update your release criteria to
reflect this refined use case, verifying they capture the specific
harms you need to block and benefits you want to deliver within your
new boundaries. This iterative process assists you to build a system
that performs appropriately in its intended domain rather than
struggling to meet unrealistic expectations or risk releasing with
unmet criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- List out which release criteria your system consistently fails
to meet despite multiple implementation attempts and assess
whether these failures are fundamental limitations of your
current approach rather than problems that more
implementations can solve. Look for patterns like specific
types of content your system can't handle safely or
performance gaps that persist across different model
architectures.
- Map these persistent failures to specific parts of your use
case to understand which scenarios are causing the problems.

For example, if your chatbot struggles with medical advice but
works well for general conversation, or if your content
moderation system fails on certain languages but works fine for
English, you can see where to draw new boundaries.

- Define a narrower use case that avoids the scenarios where you
cannot meet your release criteria, focusing on areas where
your system can genuinely excel and deliver value. This might
mean limiting the types of queries you handle, the domains you
operate in, or the user populations you serve, but it lets you
build something that performs appropriately.
- Redo your risk and benefit analysis using this more focused
scope, since narrowing your use case may change both the
potential harms and the benefits you can deliver. You might
discover new risks in your focused area that you had not
considered or find that some broad risks no longer apply.
- Rewrite your release criteria to match your refined use case,
making sure they capture the specific standards that matter
for your new boundaries. Your updated criteria may be
achievable with your current system design while still
maintaining the quality standards that protect users and
deliver real value.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raier03-bp02.html*

---
