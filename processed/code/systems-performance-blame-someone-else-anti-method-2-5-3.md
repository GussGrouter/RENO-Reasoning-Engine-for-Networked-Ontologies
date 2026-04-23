# Systems Performance — blame-someone-else anti-method (2.5.3) (blame-someone-else-anti-method-2-5-3) (PDF pages 78–84)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-methodology-2-5-scout-p78-84.md

---

2.5.3     Blame-Someone-Else Anti-Method
This anti-methodology follows these steps:

   1. Find a system or environment component for which you are not responsible.

   2. Hypothesize that the issue is with that component.

   3. Redirect the issue to the team responsible for that component.

   4. When proven wrong, go back to step 1.

    “Maybe it’s the network. Can you check with the network team if they’ve had dropped
    packets or something?”

Instead of investigating performance issues, the user of this methodology makes them someone
else’s problem, which can be wasteful of other teams’ resources when it turns out not to be
their problem after all. This anti-methodology can be identified by a lack of data leading to the
hypothesis.

To avoid becoming a victim of blame-someone-else, ask the accuser for screenshots showing
which tools were run and how the output was interpreted. You can take these screenshots and
interpretations to someone else for a second opinion.
