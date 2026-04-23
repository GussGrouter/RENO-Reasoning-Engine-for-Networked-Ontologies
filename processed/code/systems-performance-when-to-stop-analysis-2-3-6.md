# Systems Performance — 2.3.6 When to Stop Analysis (PDF pages 68–72)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-concepts-2-3-6-to-2-3-8-p68-72.md
- Slice: 2.3.6 When to Stop Analysis

---

2.3.6 When to Stop Analysis
A challenge whenever doing performance analysis is knowing when to stop. There are so many
tools, and so many things to examine!

When I teach performance classes (as I’ve begun to do again recently), I can give my students a
performance issue that has three contributing reasons, and find that some students stop after
finding one reason, others two, and others all three. Some students keep going, trying to find
even more reasons for the performance issue. Who is doing it right? It might be easy to say you
should stop after finding all three reasons, but for real-life issues you don’t know the number
of causes.

Here are three scenarios where you may consider stopping analysis, with some personal
examples:

    ■   When you’ve explained the bulk of the performance problem. A Java application was
        consuming three times more CPU than it had been. The first issue I found was one of
        exception stacks consuming CPU. I then quantified time in those stacks and found that
        they accounted for only 12% of the overall CPU footprint. If that figure had been closer to
        66%, I could have stopped analysis—the 3x slowdown would have been accounted for. But
        in this case, at 12%, I needed to keep looking.
    ■   When the potential ROI is less than the cost of analysis. Some performance issues I
        work on can deliver wins measured in tens of millions of dollars per year. For these I can
        justify spending months of my own time (engineering cost) on analysis. Other performance
        wins, say for tiny microservices, may be measured in hundreds of dollars: it may not be
        worth even an hour of engineering time to analyze them. Exceptions might include when
        I have nothing better to do with company time (which never happens in practice) or if I
        suspected that this might be a canary for a bigger issue later on, and therefore worth
        debugging before the problem grows.
    ■   When there are bigger ROIs elsewhere. Even if the previous two scenarios have not been
        met, there may be larger ROIs elsewhere that take priority.

If you are working full-time as a performance engineer, prioritizing the analysis of different
issues based on their potential ROI is likely a daily task.
