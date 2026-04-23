# Systems Performance — cache tuning (2.5.18) (cache-tuning-2-5-18) (PDF pages 98–106)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-cache-microbench-mantras-scout-p98-106.md

---

2.5.18       Cache Tuning
     Applications and operating systems may employ multiple caches to improve I/O performance,
     from the application down to the disks. See Chapter 3, Operating Systems, Section 3.2.11,
     Caching, for a full list. Here is a general strategy for tuning each cache level:

        1. Aim to cache as high in the stack as possible, closer to where the work is performed, reduc-
           ing the operational overhead of cache hits. This location should also have more metadata
           available, which can be used to improve the cache retention policy.

        2. Check that the cache is enabled and working.

        3. Check the cache hit/miss ratios and miss rate.

        4. If the cache size is dynamic, check its current size.

        5. Tune the cache for the workload. This task depends on available cache tunable parameters.

        6. Tune the workload for the cache. Doing this includes reducing unnecessary consumers of
           the cache, which frees up more space for the target workload.

     Look out for double caching—for example, two different caches that consume main memory
     and cache the same data twice.

     Also consider the overall performance gain of each level of cache tuning. Tuning the CPU Level 1
     cache may save nanoseconds, as cache misses may then be served by Level 2. But improving CPU
     Level 3 cache may avoid much slower DRAM accesses and result in a greater overall performance
     gain. (These CPU caches are described in Chapter 6, CPUs.)
