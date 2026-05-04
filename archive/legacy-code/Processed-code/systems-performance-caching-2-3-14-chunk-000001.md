# systems-performance-caching-2-3-14 (chunk 000001)

# Systems Performance — caching (2.3.14) (PDF pages 72–75)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-profiling-2-3-13-scout-p72-75.md
- Slice: from `2.3.14 Caching` up to before `2.3.15 Known-Unknowns`

---

2.3.14      Caching
Caching is frequently used to improve performance. A cache stores results from a slower storage
tier in a faster storage tier, for reference. An example is caching disk blocks in main memory (RAM).

Multiple tiers of caches may be used. CPUs commonly employ multiple hardware caches for
main memory (Levels 1, 2, and 3), beginning with a very fast but small cache (Level 1) and
increasing in both storage size and access latency. This is an economic trade-off between density
and latency; levels and sizes are chosen for the best performance for the on-chip space available.
These caches are covered in Chapter 6, CPUs.

There are many other caches present in a system, many of them implemented in software using
main memory for storage. See Chapter 3, Operating Systems, Section 3.2.11, Caching, for a list of
caching layers.

One metric for understanding cache performance is each cache’s hit ratio—the number of times
the needed data was found in the cache (hits) versus the total accesses (hits + misses):

    hit ratio = hits / (hits + misses)

The higher, the better, as a higher ratio reflects more data successfully accessed from faster
media. Figure 2.9 shows the expected performance improvement for increasing cache hit ratios.
36   Chapter 2 Methodologies




     Figure 2.9 Cache hit ratio and performance

     The performance difference between 98% and 99% is much greater than that between 10%
     and 11%. This is a nonlinear profile because of the difference in speed between cache hits and
     misses—the two storage tiers at play. The greater the difference, the steeper the slope becomes.

     Another metric for understanding cache performance is the cache miss rate, in terms of misses
     per second. This is proportional (linear) to the performance penalty of each miss and can be
     easier to interpret.

     For example, workloads A and B perform the same task using different algorithms and use a
     main memory cache to avoid reading from disk. Workload A has a cache hit ratio of 90%, and
     workload B has a cache hit ratio of 80%. This information alone suggests workload A performs
     better. What if workload A had a miss rate of 200/s and workload B, 20/s? In those terms, work-
     load B performs 10x fewer disk reads, which may complete the task much sooner than A. To be
     certain, the total runtime for each workload can be calculated as

         runtime = (hit rate × hit latency) + (miss rate × miss latency)

     This calculation uses the average hit and miss latencies and assumes the work is serialized.


     Algorithms
     Cache management algorithms and policies determine what to store in the limited space avail-
     able for a cache.

     Most recently used (MRU) refers to a cache retention policy, which decides what to favor keeping
     in the cache: the objects that have been used most recently. Least recently used (LRU) can refer to
     an equivalent cache eviction policy, deciding what objects to remove from the cache when more
     space is needed. There are also most frequently used (MFU) and least frequently used (LFU) policies.

     You may encounter not frequently used (NFU), which may be an inexpensive but less thorough
     version of LRU.


     Hot, Cold, and Warm Caches
     These words are commonly used to describe the state of the cache:

         ■   Cold: A cold cache is empty, or populated with unwanted data. The hit ratio for a cold
             cache is zero (or near zero as it begins to warm up).
