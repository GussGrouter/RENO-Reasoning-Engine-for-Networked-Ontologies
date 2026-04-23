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
                                                                                2.4 Perspectives       37


    ■   Warm: A warm cache is one that is populated with useful data but doesn’t have a high
        enough hit ratio to be considered hot.
    ■   Hot: A hot cache is populated with commonly requested data and has a high hit ratio, for
        example, over 99%.
    ■   Warmth: Cache warmth describes how hot or cold a cache is. An activity that improves
        cache warmth is one that aims to improve the cache hit ratio.

When caches are first initialized, they begin cold and then warm up over time. When the cache
is large or the next-level storage is slow (or both), the cache can take a long time to become popu-
lated and warm.

For example, I worked on a storage appliance that had 128 Gbytes of DRAM as a file system
cache, 600 Gbytes of flash memory as a second-level cache, and rotational disks for storage. With
a random read workload, the disks delivered around 2,000 reads/s. With an 8 Kbyte I/O size,
this meant that the caches could warm up at a rate of only 16 Mbytes/s (2,000 × 8 Kbytes). When
both caches began cold, it took more than 2 hours for the DRAM cache to warm up, and more
than 10 hours for the flash memory cache to warm up.


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



2.4        Perspectives
There are two common perspectives for performance analysis, each with different audiences,
metrics, and approaches. They are workload analysis and resource analysis. They can be thought
of as either top-down or bottom-up analysis of the operating system software stack, as shown in
Figure 2.10.
38   Chapter 2 Methodologies




     Figure 2.10 Analysis perspectives

     Section 2.5, Methodology, provides specific strategies to apply for each. These perspectives are
     introduced here in more detail.


     2.4.1      Resource Analysis
     Resource analysis begins with analysis of the system resources: CPUs, memory, disks, network
     interfaces, buses, and interconnects. It is most likely performed by system administrators—those
     responsible for the physical resources. Activities include
         ■   Performance issue investigations: To see if a particular type of resource is responsible
         ■   Capacity planning: For information to help size new systems, and to see when existing
             system resources may become exhausted

     This perspective focuses on utilization, to identify when resources are at or approaching their
     limit. Some resource types, such as CPUs, have utilization metrics readily available. Utilization
     for other resources can be estimated based on available metrics, for example, estimating network
     interface utilization by comparing the send and receive megabits per second (throughput) with
     the known or expected maximum bandwidth.

     Metrics best suited for resource analysis include:

         ■   IOPS
         ■   Throughput
         ■   Utilization
         ■   Saturation

     These measure what the resource is being asked to do, and how utilized or saturated it is for a
     given load. Other types of metrics, including latency, are also useful to see how well the resource
     is responding for the given workload.
                                                                                2.4 Perspectives       39


Resource analysis is a common approach to performance analysis, in part thanks to the widely
available documentation on the topic. Such documentation focuses on the operating system
“stat” tools: vmstat(8), iostat(1), mpstat(1). It’s important when you read such documentation to
understand that this is one perspective, but not the only perspective.


2.4.2      Workload Analysis
Workload analysis (see Figure 2.11) examines the performance of applications: the workload
applied and how the application is responding. It is most commonly used by application devel-
opers and support staff—those responsible for the application software and configuration.




Figure 2.11 Workload analysis

The targets for workload analysis are:

    ■   Requests: The workload applied
    ■   Latency: The response time of the application
    ■   Completion: Looking for errors

Studying workload requests typically involves checking and summarizing their attributes: this is
the process of workload characterization (described in more detail in Section 2.5, Methodology). For
databases, these attributes may include the client host, database name, tables, and query string.
This data may help identify unnecessary work, or unbalanced work. Even when a system is perform-
ing its current workload well (low latency), examining these attributes may identify ways to reduce
or eliminate the work applied. Keep in mind that the fastest query is the one you don’t do at all.

Latency (response time) is the most important metric for expressing application performance.
For a MySQL database, it’s query latency; for Apache, it’s HTTP request latency; and so on. In
these contexts, the term latency is used to mean the same as response time (refer to Section 2.3.1,
Latency, for more about context).

The tasks of workload analysis include identifying and confirming issues—for example, by
looking for latency beyond an acceptable threshold—then finding the source of the latency and
confirming that the latency is improved after applying a fix. Note that the starting point is the
application. Investigating latency usually involves drilling down deeper into the application,
libraries, and the operating system (kernel).

System issues may be identified by studying characteristics related to the completion of an
event, including its error status. While a request may complete quickly, it may do so with an
error status that causes the request to be retried, accumulating latency.
40   Chapter 2 Methodologies


     Metrics best suited for workload analysis include:

        ■    Throughput (transactions per second)
        ■    Latency

     These measure the rate of requests and the resulting performance.



     2.5        Methodology
     When faced with an underperforming and complicated system environment, the first challenge
     can be knowing where to begin your analysis and how to proceed. As I said in Chapter 1, perfor-
     mance issues can arise from anywhere, including software, hardware, and any component along
     the data path. Methodologies can help you approach these complex systems by showing where
     to start your analysis and suggesting an effective procedure to follow.

     This section describes many performance methodologies and procedures for system perfor-
     mance and tuning, some of which I developed. These methodologies help beginners get started
     and serve as reminders for experts. Some anti-methodologies have also been included.

     To help summarize their role, these methodologies have been categorized as different types,
     such as observational analysis and experimental analysis, as shown in Table 2.4.


     Table 2.4    Generic system performance methodologies
     Section     Methodology                              Type
     2.5.1       Streetlight anti-method                  Observational analysis
     2.5.2       Random change anti-method                Experimental analysis
     2.5.3       Blame-someone-else anti-method           Hypothetical analysis
     2.5.4       Ad hoc checklist method                  Observational and experimental analysis
     2.5.5       Problem statement                        Information gathering
     2.5.6       Scientific method                        Observational analysis
     2.5.7       Diagnosis cycle                          Analysis life cycle
     2.5.8       Tools method                             Observational analysis
     2.5.9       USE method                               Observational analysis
     2.5.10      RED method                               Observational analysis
     2.5.11      Workload characterization                Observational analysis, capacity planning
     2.5.12      Drill-down analysis                      Observational analysis
     2.5.13      Latency analysis                         Observational analysis
     2.5.14      Method R                                 Observational analysis
     2.5.15      Event tracing                            Observational analysis
     2.5.16      Baseline statistics                      Observational analysis
     2.5.17      Static performance tuning                Observational analysis, capacity planning
                                                                              2.5 Methodology       41



Section     Methodology                           Type
2.5.18      Cache tuning                          Observational analysis, tuning
2.5.19      Micro-benchmarking                    Experimental analysis
2.5.20      Performance mantras                   Tuning
2.6.5       Queueing theory                       Statistical analysis, capacity planning
2.7         Capacity planning                     Capacity planning, tuning
2.8.1       Quantifying performance gains         Statistical analysis
2.9         Performance monitoring                Observational analysis, capacity planning



Performance monitoring, queueing theory, and capacity planning are covered later in this chap-
ter. Other chapters also recast some of these methodologies in different contexts and provide
some additional methodologies for specific targets of performance analysis. Table 2.5 lists these
additional methodologies.


Table 2.5    Additional performance methodologies
Section     Methodology                           Type
1.10.1      Linux performance analysis in 60s     Observational analysis
5.4.1       CPU profiling                         Observational analysis
5.4.2       Off-CPU analysis                      Observational analysis
6.5.5       Cycle analysis                        Observational analysis
6.5.8       Priority tuning                       Tuning
6.5.8       Resource controls                     Tuning
6.5.9       CPU binding                           Tuning
7.4.6       Leak detection                        Observational analysis
7.4.10      Memory shrinking                      Experimental analysis
8.5.1       Disk analysis                         Observational analysis
8.5.7       Workload separation                   Tuning
9.5.10      Scaling                               Capacity planning, tuning
10.5.6      Packet sniffing                       Observational analysis
10.5.7      TCP analysis                          Observational analysis
12.3.1      Passive benchmarking                  Experimental analysis
12.3.2      Active benchmarking                   Observational analysis
12.3.6      Custom benchmarks                     Software development
12.3.7      Ramping load                          Experimental analysis
12.3.8      Sanity check                          Observational analysis
42   Chapter 2 Methodologies


     The following sections begin with commonly used but weaker methodologies for comparison,
     including the anti-methodologies. For the analysis of performance issues, the first methodology
     you should attempt is the problem statement method, before moving on to others.


     2.5.1 Streetlight Anti-Method
     This method is actually the absence of a deliberate methodology. The user analyzes performance
     by choosing observability tools that are familiar, found on the Internet, or just at random to see if
     anything obvious shows up. This approach is hit or miss and can overlook many types of issues.

     Tuning performance may be attempted in a similar trial-and-error fashion, setting whatever
     tunable parameters are known and familiar to different values to see if that helps.

     Even when this method reveals an issue, it can be slow as tools or tunings unrelated to the issue
     are found and tried, just because they’re familiar. This methodology is therefore named after an
     observational bias called the streetlight effect, illustrated by this parable:

         One night a police officer sees a drunk searching the ground beneath a streetlight and
         asks what he is looking for. The drunk says he has lost his keys. The police officer can’t
         find them either and asks: “Are you sure you lost them here, under the streetlight?” The
         drunk replies: “No, but this is where the light is best.”

     The performance equivalent would be looking at top(1), not because it makes sense, but because
     the user doesn’t know how to read other tools.

     An issue that this methodology does find may be an issue but not the issue. Other methodolo-
     gies quantify findings, so that false positives can be ruled out more quickly, and bigger issues
     prioritized.


     2.5.2 Random Change Anti-Method
     This is an experimental anti-methodology. The user randomly guesses where the problem may
     be and then changes things until it goes away. To determine whether performance has improved
     or not as a result of each change, a metric is studied, such as application runtime, operation
     time, latency, operation rate (operations per second), or throughput (bytes per second). The
     approach is as follows:

        1. Pick a random item to change (e.g., a tunable parameter).

        2. Change it in one direction.

        3. Measure performance.

        4. Change it in the other direction.

        5. Measure performance.

        6. Were the results in step 3 or step 5 better than the baseline? If so, keep the change and go
           back to step 1.

     While this process may eventually unearth tuning that works for the tested workload, it is very
     time-consuming and can also result in tuning that doesn’t make sense in the long term. For
                                                                                 2.5 Methodology       43


example, an application change may improve performance because it works around a database
or operating system bug that is later fixed. But the application will still have that tuning that no
longer makes sense, and that no one understood properly in the first place.

Another risk is where a change that isn’t properly understood causes a worse problem during
peak production load, and a need to back out the change.


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


2.5.4     Ad Hoc Checklist Method
Stepping through a canned checklist is a common methodology used by support professionals
when asked to check and tune a system, often in a short time frame. A typical scenario involves
the deployment of a new server or application in production, and a support professional spending
half a day checking for common issues now that the system is under real load. These checklists
are ad hoc and are built from recent experience and issues for that system type.

Here is an example checklist entry:

    Run iostat –x 1 and check the r_await column. If this is consistently over 10 (ms)
    during load, then either disk reads are slow or the disk is overloaded.

A checklist may be composed of a dozen or so such checks.

While these checklists can provide the most value in the shortest time frame, they are point-in-
time recommendations (see Section 2.3, Concepts) and need to be frequently refreshed to stay
current. They also tend to focus on issues for which there are known fixes that can be easily
documented, such as the setting of tunable parameters, but not custom fixes to the source code
or environment.
