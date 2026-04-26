# systems-performance-tools-method-2-5-8 (chunk 000001)

# Systems Performance — tools method (2.5.8) (tools-method-2-5-8) (PDF pages 82–92)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-methodology-2-5-scout-p82-92.md

---

2.5.8 Tools Method
     A tools-oriented approach is as follows:

        1. List available performance tools (optionally, install or purchase more).

        2. For each tool, list useful metrics it provides.

        3. For each metric, list possible ways to interpret it.

     The result of this is a prescriptive checklist showing which tool to run, which metrics to read,
     and how to interpret them. While this can be fairly effective, it relies exclusively on available
     (or known) tools, which can provide an incomplete view of the system, similar to the streetlight
     anti-method. Worse, the user is unaware that they have an incomplete view—and may remain
     unaware. Issues that require custom tooling (e.g., dynamic tracing) may never be identified
     and solved.

     In practice, the tools method does identify certain resource bottlenecks, errors, and other types
     of problems, though it may not do this efficiently.

     When a large number of tools and metrics are available, it can be time-consuming to iterate
     through them. The situation gets worse when multiple tools appear to have the same functional-
     ity and you spend additional time trying to understand the pros and cons of each. In some cases,
     such as file system micro-benchmark tools, there are over a dozen tools to choose from, when
     you may need only one.4


     4
       As an aside, an argument I’ve encountered to support multiple overlapping tools is that “competition is good.”
     I would be cautious about this: while it can be helpful to have overlapping tools for cross-checking results (and I fre-
     quently cross-check BPF tools using Ftrace), multiple overlapping tools can become a waste of developer time that
     could be more effectively used elsewhere, as well as a waste of time for end users who must evaluate each choice.
                                                                                 2.5 Methodology        47
