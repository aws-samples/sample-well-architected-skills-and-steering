**Saga**: Quality assurance
**Capability**: QA.NT — Non-functional testing

---

# [QA.NT.3] Prioritize user experience with UX testing

**Category:** RECOMMENDED

User experience (UX) testing provides insight into the
system's user interface and overall user experience, ensuring
that they align with the diverse requirements of its user
base. Adopting UX testing ensures that as the system evolves,
its design remains intuitive, functional, and inclusive for
end users.

Recognize that UX is subjective and can vary based on
demographics, tech proficiency, and individual preferences.
Segment your tests to understand the diverse needs and
preferences of your user base. This means creating different
user profiles and scenarios, ensuring that the software is
tested from multiple perspectives. There are various forms of
non-functional UX tests which should be utilized to target
specific improvements:

- **Usability testing:** UX tests determines the ease with
which users can perform tasks using the application and evaluates if the interface is
intuitive and user-friendly. Usability testing helps identify issues related to the
application's design, navigation, and overall ease of use, ultimately leading to
building a better product. Conduct usability testing by recruiting a diverse group of
testing participants that represent the broader user base. Provide these users with
typical tasks they would perform when using the application. Observe the testing
participants and their interactions, note areas where they encounter challenges,
confusion, or get frustrated. During observation, encourage the participants to
verbalize their thought process as they perform the tasks. After the tasks are
completed, conduct a brief feedback session to gather additional perspective on their
use of the application. Use this data to drive user experience improvements and to fix
any bugs that were discovered. To continuously gather feedback over time, ensure that
there are mechanisms for users to provide feedback as they interact with the system.
- **Accessibility testing:** UX tests that evaluate the
application to ensure that it can be accessed and used by everyone. Regularly review
web content accessibility guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) to ensure
compliance with the latest standards. To get started quickly, consider adopting an
existing design system which incorporates accessibility best practices and a framework
to create accessible applications, such as the [Cloudscape Design System](https://cloudscape.design/). Automate accessibility tests as a part of the
development lifecycle using tools like [Axe](https://www.deque.com/axe/) or [WAVE](https://wave.webaim.org/). Adopt tools that
evaluate specific accessibility standards, such as color contrast analyzing tools like
[WebAim](https://webaim.org/resources/contrastchecker/). Consider
regularly conducting manual exploratory tests using assistive technologies to capture
issues that automated tools might miss.

**Related information:**

- [Usability
Evaluation Methods](https://www.usability.gov/how-to-and-tools/methods/usability-evaluation/index.html)
- [W3C
standards](https://www.w3.org/WAI/fundamentals/accessibility-principles/)
- [WCAG
2.1 AA](https://www.w3.org/WAI/WCAG21/Understanding/conformance#levels)
- [Web
Accessibility Initiative (WAI)](https://www.w3.org/WAI/design-develop/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.3-prioritize-user-experience-with-ux-testing.html*
