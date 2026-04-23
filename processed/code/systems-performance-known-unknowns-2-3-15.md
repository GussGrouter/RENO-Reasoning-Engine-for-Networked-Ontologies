# Systems Performance — known-unknowns (2.3.15) (PDF pages 75–82)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-profiling-caching-scout-p75-82.md
- Slice: from `2.3.15 Known-Unknowns` up to before `2.4 Perspectives`

---

2.3.15       Known-Unknowns
Introduced in the Preface, the notion of known-knowns, known-unknowns, and unknown-unknowns
is important for the field of performance. The breakdown is as follows, with examples for
systems performance analysis:
    ■   Known-knowns: These are things you know. You know you should be checking a per-
        formance metric, and you know its current value. For example, you know you should be
        checking CPU utilization, and you also know that the value is 10% on average.
    ■   Known-unknowns: These are things you know that you do not know. You know you
        can check a metric or the existence of a subsystem, but you haven’t yet observed it. For
        example, you know you could use profiling to check what is making the CPUs busy, but
        have yet to do so.
    ■   Unknown-unknowns: These are things you do not know that you do not know. For
        example, you may not know that device interrupts can become heavy CPU consumers, so
        you are not checking them.

Performance is a field where “the more you know, the more you don’t know.” The more you
learn about systems, the more unknown-unknowns you become aware of, which are then
known-unknowns that you can check on.
