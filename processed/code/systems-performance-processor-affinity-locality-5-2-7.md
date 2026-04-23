<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (combined extract; Chapter 5 Applications §5.2.5–5.2.7) -->
5.2

Application Performance Techniques

With an array of adjacent locks in memory, a performance problem can arise when locks fall
within the same cache line. Two CPUs updating different locks in the same cache line will
encounter cache coherency overhead, with each CPU invalidating the cache line in the other’s
cache. This situation is called false sharing and is commonly solved by padding locks with unused
bytes so that only one lock exists in each cache line in memory.

5.2.6

Non-Blocking I/O

The Unix process life cycle, pictured in Chapter 3, Operating Systems, shows processes blocking
