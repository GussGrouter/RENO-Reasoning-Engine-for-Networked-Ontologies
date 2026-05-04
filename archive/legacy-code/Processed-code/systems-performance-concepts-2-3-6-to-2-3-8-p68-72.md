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
32   Chapter 2 Methodologies




     Figure 2.7 Performance degradation

     Higher response time is, of course, bad. The “fast” degradation profile may occur for memory
     load, when the system begins moving memory pages to disk to free main memory. The “slow”
     degradation profile may occur for CPU load.

     Another “fast” profile example is disk I/O. As load (and the resulting disk utilization) increases,
     I/O becomes more likely to queue behind other I/O. An idle rotational (not solid state) disk may
     serve I/O with a response time of about 1 ms, but when load increases, this can approach 10 ms.
     This is modeled in Section 2.6.5, Queueing Theory, under M/D/1 and 60% Utilization, and disk
     performance is covered in Chapter 9, Disks.

     Linear scalability of response time could occur if the application begins to return errors when
     resources are unavailable, instead of queueing work. For example, a web server may return 503
     “Service Unavailable” instead of adding requests to a queue, so that those requests that are
     served can be performed with a consistent response time.


     2.3.10       Metrics
     Performance metrics are selected statistics generated by the system, applications, or additional
     tools that measure activity of interest. They are studied for performance analysis and monitor-
     ing, either numerically at the command line or graphically using visualizations.

     Common types of system performance metrics include:

         ■   Throughput: Either operations or data volume per second
         ■   IOPS: I/O operations per second
         ■   Utilization: How busy a resource is, as a percentage
         ■   Latency: Operation time, as an average or percentile

     The usage of throughput depends on its context. Database throughput is usually a measure of
     queries or requests (operations) per second. Network throughput is a measure of bits or bytes
     (volume) per second.

     IOPS is a throughput measurement for I/O operations only (reads and writes). Again, context
     matters, and definitions can vary.
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
