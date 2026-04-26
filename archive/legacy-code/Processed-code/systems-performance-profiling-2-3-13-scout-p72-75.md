                                                                                    2.3    Concepts    33



Overhead
Performance metrics are not free; at some point, CPU cycles must be spent to gather and store
them. This causes overhead, which can negatively affect the performance of the target of mea-
surement. This is called the observer effect. (It is often confused with Heisenberg’s Uncertainty
Principle, which describes the limit of precision at which pairs of physical properties, such as
position and momentum, may be known.)


Issues
You might assume that a software vendor has provided metrics that are well chosen, are bug-free,
and provide complete visibility. In reality, metrics can be confusing, complicated, unreliable,
inaccurate, and even plain wrong (due to bugs). Sometimes a metric was correct in one software
version but did not get updated to reflect the addition of new code and code paths.

For more about problems with metrics, see Chapter 4, Observability Tools, Section 4.6,
Observing Observability.


2.3.11 Utilization
The term utilization3 is often used for operating systems to describe device usage, such as for the
CPU and disk devices. Utilization can be time-based or capacity-based.


Time-Based
Time-based utilization is formally defined in queueing theory. For example [Gunther 97]:

        the average amount of time the server or resource was busy

along with the ratio

        U = B/T

where U = utilization, B = total time the system was busy during T, the observation period.

This is also the “utilization” most readily available from operating system performance tools.
The disk monitoring tool iostat(1) calls this metric %b for percent busy, a term that better conveys
the underlying metric: B/T.

This utilization metric tells us how busy a component is: when a component approaches 100%
utilization, performance can seriously degrade when there is contention for the resource. Other
metrics can be checked to confirm and to see if the component has therefore become a system
bottleneck.

Some components can service multiple operations in parallel. For them, performance may not
degrade much at 100% utilization as they can accept more work. To understand this, consider a


3
    Spelled utilisation in some parts of the world.
34   Chapter 2 Methodologies


     building elevator. It may be considered utilized when it is moving between floors, and not uti-
     lized when it is idle waiting. However, the elevator may be able to accept more passengers even
     when it is busy 100% of the time responding to calls—that is, it is at 100% utilization.

     A disk that is 100% busy may also be able to accept and process more work, for example, by buff-
     ering writes in the on-disk cache to be completed later. Storage arrays frequently run at 100%
     utilization because some disk is busy 100% of the time, but the array has plenty of idle disks and
     can accept more work.


     Capacity-Based
     The other definition of utilization is used by IT professionals in the context of capacity planning
     [Wong 97]:

         A system or component (such as a disk drive) is able to deliver a certain amount of
         throughput. At any level of performance, the system or component is working at some
         proportion of its capacity. That proportion is called the utilization.

     This defines utilization in terms of capacity instead of time. It implies that a disk at 100% utiliza-
     tion cannot accept any more work. With the time-based definition, 100% utilization only means
     it is busy 100% of the time.

         100% busy does not mean 100% capacity.

     For the elevator example, 100% capacity may mean the elevator is at its maximum payload
     capacity and cannot accept more passengers.

     In an ideal world, we would be able to measure both types of utilization for a device, so that, for
     example, you would know when a disk is 100% busy and performance begins to degrade due to
     contention, and also when it is at 100% capacity and cannot accept more work. Unfortunately,
     this usually isn’t possible. For a disk, it would require knowledge of what the disk’s on-board con-
     troller was doing and a prediction of capacity. Disks do not currently provide this information.

     In this book, utilization usually refers to the time-based version, which you could also call non-
     idle time. The capacity version is used for some volume-based metrics, such as memory usage.


     2.3.12      Saturation
     The degree to which more work is requested of a resource than it can process is saturation.
     Saturation begins to occur at 100% utilization (capacity-based), as extra work cannot be
     processed and begins to queue. This is pictured in Figure 2.8.

     The figure pictures saturation increasing linearly beyond the 100% capacity-based utilization
     mark as load continues to increase. Any degree of saturation is a performance issue, as time
     is spent waiting (latency). For time-based utilization (percent busy), queueing and therefore
     saturation may not begin at the 100% utilization mark, depending on the degree to which the
     resource can operate on work in parallel.
                                                                                     2.3    Concepts    35




Figure 2.8 Utilization versus saturation

2.3.13      Profiling
Profiling builds a picture of a target that can be studied and understood. In the field of comput-
ing performance, profiling is typically performed by sampling the state of the system at timed
intervals and then studying the set of samples.

Unlike the previous metrics covered, including IOPS and throughput, the use of sampling pro-
vides a coarse view of the target’s activity. How coarse depends on the rate of sampling.

As an example of profiling, CPU usage can be understood in reasonable detail by sampling the
CPU instruction pointer or stack trace at frequent intervals to gather statistics on the code paths
that are consuming CPU resources. This topic is covered in Chapter 6, CPUs.


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
