26   Chapter 2 Methodologies


     Table 2.2     Example time scale of system latencies
     Event                                                  Latency                 Scaled
     1 CPU cycle                                              0.3 ns                1s
     Level 1 cache access                                     0.9 ns                3s
     Level 2 cache access                                       3 ns              10 s
     Level 3 cache access                                      10 ns              33 s
     Main memory access (DRAM, from CPU)                     100 ns                 6 min
     Solid-state disk I/O (flash memory)                 10–100 μs             9–90 hours
     Rotational disk I/O                                    1–10 ms             1–12 months
     Internet: San Francisco to New York                       40 ms                4 years
     Internet: San Francisco to United Kingdom                 81 ms                8 years
     Lightweight hardware virtualization boot                100 ms               11 years
     Internet: San Francisco to Australia                    183 ms               19 years
     OS virtualization system boot                            <1s                105 years
     TCP timer-based retransmit                              1–3 s         105–317 years
     SCSI command time-out                                     30 s                 3 millennia
     Hardware (HW) virtualization system boot                  40 s                 4 millennia
     Physical system reboot                                     5m                32 millennia



     As you can see, the time scale for CPU cycles is tiny. The time it takes light to travel 0.5 m, per-
     haps the distance from your eyes to this page, is about 1.7 ns. During the same time, a modern
     CPU may have executed five CPU cycles and processed several instructions.

     For more about CPU cycles and latency, see Chapter 6, CPUs, and for disk I/O latency, Chapter 9,
     Disks. The Internet latencies included are from Chapter 10, Network, which has more examples.


     2.3.3       Trade-Offs
     You should be aware of some common performance trade-offs. The good/fast/cheap “pick two”
     trade-off is shown in Figure 2.4, alongside the terminology adjusted for IT projects.




     Figure 2.4 Trade-offs: pick two
                                                                                   2.3    Concepts   27


Many IT projects choose on-time and inexpensive, leaving performance to be fixed later. This
choice can become problematic when earlier decisions inhibit improving performance, such as
choosing and populating a suboptimal storage architecture, using a programming language or
operating system that is implemented inefficiently, or selecting a component that lacks compre-
hensive performance analysis tools.

A common trade-off in performance tuning is the one between CPU and memory, as memory
can be used to cache results, reducing CPU usage. On modern systems with an abundance of
CPU, the trade may work the other way: CPU time may be spent compressing data to reduce
memory usage.

Tunable parameters often come with trade-offs. Here are a couple of examples:

   ■    File system record size (or block size): Small record sizes, close to the application I/O
        size, will perform better for random I/O workloads and make more efficient use of the file
        system cache while the application is running. Large record sizes will improve streaming
        workloads, including file system backups.
   ■    Network buffer size: Small buffer sizes will reduce the memory overhead per connection,
        helping the system scale. Large sizes will improve network throughput.

Look for such trade-offs when making changes to the system.


2.3.4 Tuning Efforts
Performance tuning is most effective when done closest to where the work is performed. For
workloads driven by applications, this means within the application itself. Table 2.3 shows an
example software stack with tuning possibilities.

By tuning at the application level, you may be able to eliminate or reduce database queries and
improve performance by a large factor (e.g., 20x). Tuning down to the storage device level may
eliminate or improve storage I/O, but a tax has already been paid in executing higher-level OS
stack code, so this may improve resulting application performance only by percentages (e.g., 20%).


Table 2.3      Example targets of tuning
Layer                Example Tuning Targets
Application          Application logic, request queue sizes, database queries performed
Database             Database table layout, indexes, buffering
System calls         Memory-mapped or read/write, sync or async I/O flags
File system          Record size, cache size, file system tunables, journaling
Storage              RAID level, number and type of disks, storage tunables



There is another reason for finding large performance wins at the application level. Many of
today’s environments target rapid deployment for features and functionality, pushing software
28   Chapter 2 Methodologies


     changes into production weekly or daily.2 Application development and testing therefore tend
     to focus on correctness, leaving little or no time for performance measurement or optimization
     before production deployment. These activities are conducted later, when performance becomes
     a problem.

     While the application can be the most effective level at which to tune, it isn’t necessarily the
     most effective level from which to base observation. Slow queries may be best understood from
     their time spent on-CPU, or from the file system and disk I/O that they perform. These are
     observable from operating system tools.

     In many environments (especially cloud computing) the application level is under constant
     development, pushing software changes into production weekly or daily. Large performance
     wins, including fixes for regressions, are frequently found as the application code changes. In
     these environments, tuning for the operating system and observability from the operating
     system can be easy to overlook. Remember that operating system performance analysis can also
     identify application-level issues, not just OS-level issues, in some cases more easily than from the
     application alone.


     2.3.5 Level of Appropriateness
     Different organizations and environments have different requirements for performance. You
     may have joined an organization where it is the norm to analyze much deeper than you’ve seen
     before, or even knew was possible. Or you may find that, in your new workplace, what you
     consider basic analysis is considered advanced and has never before been performed (good news:
     low-hanging fruit!).

     This doesn’t necessarily mean that some organizations are doing it right and some wrong. It
     depends on the return on investment (ROI) for performance expertise. Organizations with
     large data centers or large cloud environments may employ a team of performance engineers
     who analyze everything, including kernel internals and CPU performance counters, and make
     frequent use of a variety of tracing tools. They may also formally model performance and
     develop accurate predictions for future growth. For environments spending millions per year
     on computing, it can be easy to justify hiring such a performance team, as the wins they find
     are the ROI. Small startups with modest computing spend may only perform superficial checks,
     trusting third-party monitoring solutions to check their performance and provide alerts.

     However, as introduced in Chapter 1, systems performance is not just about cost: it is also about
     the end-user experience. A startup may find it necessary to invest in performance engineering
     to improve website or application latency. The ROI here is not necessarily a reduction in cost, but
     happier customers instead of ex-customers.

     The most extreme environments include stock exchanges and high-frequency traders, where
     performance and latency are critical and can justify intense effort and expense. As an example
     of this, a transatlantic cable between the New York and London exchanges was planned with a
     cost of $300 million, to reduce transmission latency by 6 ms [Williams 11].


     2
      Examples of environments that change rapidly include the Netflix cloud and Shopify, which push multiple changes
     per day.
                                                                                   2.3   Concepts     29


When doing performance analysis, the level of appropriateness also comes in to play in deciding
when to stop analysis.


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


2.3.7 Point-in-Time Recommendations
The performance characteristics of environments change over time, due to the addition of more
users, newer hardware, and updated software or firmware. An environment currently limited by
a 10 Gbit/s network infrastructure may start to experience a bottleneck in disk or CPU perfor-
mance after an upgrade to 100 Gbits/s.

Performance recommendations, especially the values of tunable parameters, are valid only at a
specific point in time. What may have been the best advice from a performance expert one week
may become invalid a week later after a software or hardware upgrade, or after adding more users.
30   Chapter 2 Methodologies


     Tunable parameter values found by searching on the Internet can provide quick wins—in some
     cases. They can also cripple performance if they are not appropriate for your system or workload,
     were appropriate once but are not now, or are appropriate only as a temporary workaround for a
     software bug that is fixed properly in a later software upgrade. It is akin to raiding someone else’s
     medicine cabinet and taking drugs that may not be appropriate for you, may have expired, or
     were supposed to be taken only for a short duration.

     It can be useful to browse such recommendations just to see which tunable parameters exist and
     have needed changing in the past. Your task then becomes to see whether and how these should
     be tuned for your system and workload. But you may still miss an important parameter if others
     have not needed to tune that one before, or have tuned it but haven’t shared their experience
     anywhere.

     When changing tunable parameters, it can be helpful to store them in a version control system
     with a detailed history. (You may already do something similar when using configuration man-
     agement tools such as Puppet, Salt, Chef, etc.) That way the times and reasons that tunables were
     changed can be examined later on.


     2.3.8     Load vs. Architecture
     An application can perform badly due to an issue with the software configuration and hardware
     on which it is running: its architecture and implementation. However, an application can also
     perform badly simply due to too much load being applied, resulting in queueing and long laten-
     cies. Load and architecture are pictured in Figure 2.5.




     Figure 2.5 Load versus architecture

     If analysis of the architecture shows queueing of work but no problems with how the work is per-
     formed, the issue may be too much load applied. In a cloud computing environment, this is the
     point where more server instances can be introduced on demand to handle the work.

     For example, an issue of architecture may be a single-threaded application that is busy on-CPU,
     with requests queueing while other CPUs are available and idle. In this case, performance is
                                                                                   2.3   Concepts     31


limited by the application’s single-threaded architecture. Another issue of architecture may be
a multi-threaded program that contends for a single lock, such that only one thread can make
forward progress while others wait.

An issue of load may be a multithreaded application that is busy on all available CPUs, with
requests still queueing. In this case, performance is limited by the available CPU capacity, or put
differently, by there being more load than the CPUs can handle.


2.3.9     Scalability
The performance of the system under increasing load is its scalability. Figure 2.6 shows a typical
throughput profile as a system’s load increases.




Figure 2.6 Throughput versus load

For some period, linear scalability is observed. A point is then reached, marked with a dotted
line, where contention for a resource begins to degrade throughput. This point can be described
as a knee point, as it is the boundary between two functions. Beyond this point, the throughput
profile departs from linear scalability, as contention for the resource increases. Eventually the
overheads for increased contention and coherency cause less work to be completed and through-
put to decrease.

This point may occur when a component reaches 100% utilization: the saturation point. It may
also occur when a component approaches 100% utilization and queueing begins to be frequent
and significant.

An example system that may exhibit this profile is an application that performs heavy com-
putation, with more load added as additional threads. As the CPUs approach 100% utilization,
response time begins to degrade as CPU scheduler latency increases. After peak performance, at
100% utilization, throughput begins to decrease as more threads are added, causing more con-
text switches, which consume CPU resources and cause less actual work to be completed.

The same curve can be seen if you replace “load” on the x-axis with a resource such as CPU cores.
For more on this topic, see Section 2.6, Modeling.

The degradation of performance for nonlinear scalability, in terms of average response time or
latency, is graphed in Figure 2.7 [Cockcroft 95].
