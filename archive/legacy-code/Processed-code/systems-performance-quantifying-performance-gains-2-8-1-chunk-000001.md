# systems-performance-quantifying-performance-gains-2-8-1 (chunk 000001)

# Systems Performance — quantifying performance gains (2.8.1) (quantifying-performance-gains-2-8-1) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

2.8.1 Quantifying Performance Gains
Quantifying issues and the potential performance improvement for fixing them allows them to
be compared and prioritized. This task may be performed using observation or experiments.


Observation-Based
To quantify performance issues using observation:

   1. Choose a reliable metric.

   2. Estimate the performance gain from resolving the issue.

For example:

    ■   Observed: Application request takes 10 ms.
    ■   Observed: Of that, 9 ms is disk I/O.
    ■   Suggestion: Configure the application to cache I/O in memory, with expected DRAM
        latency around ~10 μs.
    ■   Estimated gain: 10 ms → 1.01 ms (10 ms - 9 ms + 10 μs) = ~9x gain.

As introduced in Section 2.3, Concepts, latency (time) is well suited for this, as it can be directly
compared between components, which makes calculations like this possible.

When using latency, ensure that it is measured as a synchronous component of the application
request. Some events occur asynchronously, such as background disk I/O (write flush to disk),
and do not directly affect application performance.


Experimentation-Based
To quantify performance issues experimentally:

   1. Apply the fix.

   2. Quantify before versus after using a reliable metric.
74   Chapter 2 Methodologies


     For example:

         ■   Observed: Application transaction latency averages 10 ms.
         ■   Experiment: Increase the application thread count to allow more concurrency instead of
             queueing.
         ■   Observed: Application transaction latency averages 2 ms.
         ■   Gain: 10 ms → 2 ms = 5x.

     This approach may not be appropriate if the fix is expensive to attempt in the production
     environment! For that case, observation-based should be used.
