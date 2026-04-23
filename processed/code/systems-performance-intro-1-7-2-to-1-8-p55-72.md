16   Chapter 1 Introduction


     Chapter 2, Methodologies, as well as later chapters, contain many more methodologies for perfor-
     mance analysis, including the USE method, workload characterization, latency analysis, and more.



     1.11 Case Studies
     If you are new to systems performance, case studies showing when and why various activities are
     performed can help you relate them to your current environment. Two hypothetical examples
     are summarized here; one is a performance issue involving disk I/O, and one is performance
     testing of a software change.

     These case studies describe activities that are explained in other chapters of this book. The
     approaches described here are also intended to show not the right way or the only way, but
     rather a way that these performance activities can be conducted, for your critical consideration.


     1.11.1       Slow Disks
     Sumit is a system administrator at a medium-size company. The database team has filed a
     support ticket complaining of “slow disks” on one of their database servers.

     Sumit’s first task is to learn more about the issue, gathering details to form a problem statement.
     The ticket claims that the disks are slow, but it doesn’t explain whether this is causing a database
     issue or not. Sumit responds by asking these questions:

         ■   Is there currently a database performance issue? How is it measured?
         ■   How long has this issue been present?
         ■   Has anything changed with the database recently?
         ■   Why were the disks suspected?

     The database team replies: “We have a log for queries slower than 1,000 milliseconds. These
     usually don’t happen, but during the past week they have been growing to dozens per hour.
     AcmeMon showed that the disks were busy.”

     This confirms that there is a real database issue, but it also shows that the disk hypothesis is
     likely a guess. Sumit wants to check the disks, but he also wants to check other resources quickly
     in case that guess was wrong.

     AcmeMon is the company’s basic server monitoring system, providing historical performance
     graphs based on standard operating system metrics, the same metrics printed by mpstat(1),
     iostat(1), and system utilities. Sumit logs in to AcmeMon to see for himself.

     Sumit begins with a methodology called the USE method (defined in Chapter 2, Methodologies,
     Section 2.5.9) to quickly check for resource bottlenecks. As the database team reported, utiliza-
     tion for the disks is high, around 80%, while for the other resources (CPU, network) utilization is
     much lower. The historical data shows that disk utilization has been steadily increasing during
     the past week, while CPU utilization has been steady. AcmeMon doesn’t provide saturation or
     error statistics for the disks, so to complete the USE method Sumit must log in to the server and
     run some commands.
                                                                                        1.11   Case Studies   17


He checks disk error counters from /sys; they are zero. He runs iostat(1) with an interval of one
second and watches utilization and saturation metrics over time. AcmeMon reported 80%
utilization but uses a one-minute interval. At one-second granularity, Sumit can see that disk
utilization fluctuates, often hitting 100% and causing levels of saturation and increased disk
I/O latency.

To further confirm that this is blocking the database—and isn’t asynchronous with respect to
the database queries—he uses a BCC/BPF tracing tool called offcputime(8) to capture stack traces
whenever the database was descheduled by the kernel, along with the time spent off-CPU. The
stack traces show that the database is often blocking during a file system read, during a query.
This is enough evidence for Sumit.

The next question is why. The disk performance statistics appear to be consistent with high load.
Sumit performs workload characterization to understand this further, using iostat(1) to measure
IOPS, throughput, average disk I/O latency, and the read/write ratio. For more details, Sumit can
use disk I/O tracing; however, he is satisfied that this already points to a case of high disk load,
and not a problem with the disks.

Sumit adds more details to the ticket, stating what he checked and including screenshots of the
commands used to study the disks. His summary so far is that the disks are under high load,
which increases I/O latency and is slowing the queries. However, the disks appear to be acting
normally for the load. He asks if there is a simple explanation: did the database load increase?

The database team responds that it did not, and that the rate of queries (which isn’t reported by
AcmeMon) has been steady. This sounds consistent with an earlier finding, that CPU utilization
was also steady.

Sumit thinks about what else could cause higher disk I/O load without a noticeable increase in
CPU and has a quick talk with his colleagues about it. One of them suggests file system fragmen-
tation, which is expected when the file system approaches 100% capacity. Sumit finds that it is
only at 30%.

Sumit knows he can perform drill-down analysis7 to understand the exact causes of disk I/O,
but this can be time-consuming. He tries to think of other easy explanations that he can check
quickly first, based on his knowledge of the kernel I/O stack. He remembers that this disk I/O is
largely caused by file system cache (page cache) misses.

Sumit checks the file system cache hit ratio using cachestat(8)8 and finds it is currently at 91%.
This sounds high (good), but he has no historical data to compare it to. He logs in to other data-
base servers that serve similar workloads and finds their cache hit ratio to be over 98%. He also
finds that the file system cache size is much larger on the other servers.

Turning his attention to the file system cache size and server memory usage, he finds something
that had been overlooked: a development project has a prototype application that is consuming
a growing amount of memory, even though it isn’t under production load yet. This memory is
taken from what is available for the file system cache, reducing its hit rate and causing more file
system reads to become disk reads.


7
    This is covered in Chapter 2, Methodologies, Section 2.5.12, Drill-Down Analysis.
8
    A BCC tracing tool covered in Chapter 8, File Systems, Section 8.6.12, cachestat.
18   Chapter 1 Introduction


     Sumit contacts the application development team and asks them to shut down the applica-
     tion and move it to a different server, referring to the database issue. After they do this, Sumit
     watches disk utilization creep downward in AcmeMon as the file system cache recovers to its
     original size. The slow queries return to zero, and he closes the ticket as resolved.


     1.11.2         Software Change
     Pamela is a performance and scalability engineer at a small company where she works on all
     performance-related activities. The application developers have developed a new core feature
     and are unsure whether its introduction could hurt performance. Pamela decides to perform
     non-regression testing 9 of the new application version, before it is deployed in production.

     Pamela acquires an idle server for the purpose of testing and searches for a client workload simu-
     lator. The application team had written one a while ago, although it has various limitations and
     known bugs. She decides to try it but wants to confirm that it adequately resembles the current
     production workload.

     She configures the server to match the current deployment configuration and runs the client
     workload simulator from a different system to the server. The client workload can be character-
     ized by studying an access log, and there is already a company tool to do this, which she uses.
     She also runs the tool on a production server log for different times of day and compares work-
     loads. It appears that the client simulator applies an average production workload but doesn’t
     account for variance. She notes this and continues her analysis.

     Pamela knows a number of approaches to use at this point. She picks the easiest: increasing load
     from the client simulator until a limit is reached (this is sometimes called stress testing). The cli-
     ent simulator can be configured to execute a target number of client requests per second, with a
     default of 1,000 that she had used earlier. She decides to increase load starting at 100 and adding
     increments of 100 until a limit is reached, each level being tested for one minute. She writes a
     shell script to perform the test, which collects results in a file for plotting by other tools.

     With the load running, she performs active benchmarking to determine what the limiting
     factors are. The server resources and server threads seem largely idle. The client simulator shows
     that the request throughput levels off at around 700 per second.

     She switches to the new software version and repeats the test. This also reaches the 700 mark
     and levels off. She also analyzes the server to look for limiting factors but again cannot see any.

     She plots the results, showing completed request rate versus load, to visually identify the scal-
     ability profile. Both appear to reach an abrupt ceiling.

     While it appears that the software versions have similar performance characteristics, Pamela is
     disappointed that she wasn’t able to identify the limiting factor causing the scalability ceiling.
     She knows she checked only server resources, and the limiter could instead be an application
     logic issue. It could also be elsewhere: the network or the client simulator.




     9
      Some call it regression testing, but it is an activity intended to confirm that a software or hardware change does
     not cause performance to regress, hence, non-regression testing.
                                                                                 1.12   References      19


Pamela wonders if a different approach may be needed, such as running a fixed rate of oper-
ations and then characterizing resource usage (CPU, disk I/O, network I/O), so that it can be
expressed in terms of a single client request. She runs the simulator at a rate of 700 per second for
the current and new software and measures resource consumption. The current software drove
the 32 CPUs to an average of 20% utilization for the given load. The new software drove the
same CPUs to 30% utilization, for the same load. It would appear that this is indeed a regression,
one that consumes more CPU resources.

Curious to understand the 700 limit, Pamela launches a higher load and then investigates all
components in the data path, including the network, the client system, and the client workload
generator. She also performs drill-down analysis of the server and client software. She docu-
ments what she has checked, including screenshots, for reference.

To investigate the client software she performs thread state analysis and finds that it is single-
threaded! That one thread is spending 100% of its time executing on-CPU. This convinces her
that this is the limiter of the test.

As an experiment, she launches the client software in parallel on different client systems. In this
way, she drives the server to 100% CPU utilization for both the current and new software. The
current version reaches 3,500 requests/sec, and the new version 2,300 requests/sec, consistent
with earlier findings of resource consumption.

Pamela informs the application developers that there is a regression with the new software
version, and she begins to profile its CPU usage using a CPU flame graph to understand why:
what code paths are contributing. She notes that an average production workload was tested and
that varied workloads were not. She also files a bug to note that the client workload generator is
single-threaded, which can become a bottleneck.


1.11.3 More Reading
A more detailed case study is provided as Chapter 16, Case Study, which documents how I
resolved a particular cloud performance issue. The next chapter introduces the methodologies
used for performance analysis, and the remaining chapters cover the necessary background
and specifics.



1.12        References
   [Hollingsworth 94] Hollingsworth, J., Miller, B., and Cargille, J., “Dynamic Program
   Instrumentation for Scalable Performance Tools,” Scalable High-Performance Computing
   Conference (SHPCC), May 1994.

   [Tamches 99] Tamches, A., and Miller, B., “Fine-Grained Dynamic Instrumentation of
   Commodity Operating System Kernels,” Proceedings of the 3rd Symposium on Operating Systems
   Design and Implementation, February 1999.

   [Kleen 08] Kleen, A., “On Submitting Kernel Patches,” Intel Open Source Technology Center,
   http://halobates.de/on-submitting-patches.pdf, 2008.
20   Chapter 1 Introduction


       [Gregg 11a] Gregg, B., and Mauro, J., DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X and
       FreeBSD, Prentice Hall, 2011.

       [Gregg 15a] Gregg, B., “Linux Performance Analysis in 60,000 Milliseconds,” Netflix
       Technology Blog, http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.
       html, 2015.

       [Dekker 18] Dekker, S., Drift into Failure: From Hunting Broken Components to Understanding
       Complex Systems, CRC Press, 2018.

       [Gregg 19] Gregg, B., BPF Performance Tools: Linux System and Application Observability,
       Addison-Wesley, 2019.

       [Corry 20] Corry, A., Retrospectives Antipatterns, Addison-Wesley, 2020.
                                                         Chapter 2
                                                  Methodologies

                                                   Give a man a fish and you feed him for a day.
                                                   Teach a man to fish and you feed him for a lifetime.
                                                               Chinese proverb (English equivalent)



I began my tech career as a junior system administrator, and I thought I could learn performance
by studying command-line tools and metrics alone. I was wrong. I read man pages from top to
bottom and learned the definitions for page faults, context switches, and various other system
metrics, but I didn’t know what to do with them: how to move from signals to solutions.

I noticed that, whenever there was a performance issue, the senior system administrators had
their own mental procedures for moving quickly through tools and metrics to find the root
cause. They understood which metrics were important and when they pointed to an issue, and
how to use them to narrow down an investigation. It was this know-how that was missing from
the man pages—it was typically learned by watching over the shoulder of a senior admin or
engineer.

Since then I’ve collected, documented, shared, and developed performance methodologies of my
own. This chapter includes these methodologies and other essential background for systems
performance: concepts, terminology, statistics, and visualizations. This covers theory before
later chapters dive into implementation.

The learning objectives of this chapter are:
    ■   Understand key performance metrics: latency, utilization, and saturation.
    ■   Develop a sense for the scale of measured time, down to nanoseconds.
    ■   Learn tuning trade-offs, targets, and when to stop analysis.
    ■   Identify problems of workload versus architecture.
    ■   Consider resource versus workload analysis.
    ■   Follow different performance methodologies, including: the USE method, workload
        characterization, latency analysis, static performance tuning, and performance mantras.
    ■   Understand the basics of statistics and queueing theory.
22   Chapter 2 Methodologies


     Of all the chapters in this book, this one has changed the least since the first edition. Software,
     hardware, performance tools, and performance tunables have all changed over the course of
     my career. What have remained the same are the theory and methodologies: the durable skills
     covered in this chapter.

     This chapter has three parts:

         ■   Background introduces terminology, basic models, key performance concepts, and
             perspectives. Much of this will be assumed knowledge for the rest of this book.
         ■   Methodology discusses performance analysis methodologies, both observational and
             experimental; modeling; and capacity planning.
         ■   Metrics introduces performance statistics, monitoring, and visualizations.

     Many of the methodologies introduced here are explored in more detail in later chapters,
     including the methodology sections in Chapters 5 through 10.



     2.1        Terminology
     The following are key terms for systems performance. Later chapters provide additional terms
     and describe some of these in different contexts.
         ■   IOPS: Input/output operations per second is a measure of the rate of data transfer opera-
             tions. For disk I/O, IOPS refers to reads and writes per second.
         ■   Throughput: The rate of work performed. Especially in communications, the term is
             used to refer to the data rate (bytes per second or bits per second). In some contexts (e.g.,
             databases) throughput can refer to the operation rate (operations per second or transactions
             per second).
         ■   Response time: The time for an operation to complete. This includes any time spent
             waiting and time spent being serviced (service time), including the time to transfer the
             result.
         ■   Latency: A measure of time an operation spends waiting to be serviced. In some contexts
             it can refer to the entire time for an operation, equivalent to response time. See Section 2.3,
             Concepts, for examples.
         ■   Utilization: For resources that service requests, utilization is a measure of how busy a
             resource is, based on how much time in a given interval it was actively performing work.
             For resources that provide storage, utilization may refer to the capacity that is consumed
             (e.g., memory utilization).
         ■   Saturation: The degree to which a resource has queued work it cannot service.
         ■   Bottleneck: In systems performance, a bottleneck is a resource that limits the perfor-
             mance of the system. Identifying and removing systemic bottlenecks is a key activity of
             systems performance.
         ■   Workload: The input to the system or the load applied is the workload. For a database, the
             workload consists of the database queries and commands sent by the clients.
                                                                                    2.2 Models       23


   ■   Cache: A fast storage area that can duplicate or buffer a limited amount of data, to avoid
       communicating directly with a slower tier of storage, thereby improving performance. For
       economic reasons, a cache is often smaller than the slower tier.

The Glossary includes more terminology for reference if needed.



2.2       Models
The following simple models illustrate some basic principles of system performance.


2.2.1 System Under Test
The performance of a system under test (SUT) is shown in Figure 2.1.




Figure 2.1 Block diagram of system under test

It is important to be aware that perturbations (interference) can affect results, including those
caused by scheduled system activity, other users of the system, and other workloads. The origin
of the perturbations may not be obvious, and careful study of system performance may be
required to determine it. This can be particularly difficult in some cloud environments, where
other activity (by guest tenants) on the physical host system may not be observable from within
a guest SUT.

Another difficulty with modern environments is that they may be composed of several net-
worked components servicing the input workload, including load balancers, proxy servers, web
servers, caching servers, application servers, database servers, and storage systems. The mere act
of mapping the environment may help to reveal previously overlooked sources of perturbations.
The environment may also be modeled as a network of queueing systems, for analytical study.


2.2.2      Queueing System
Some components and resources can be modeled as a queueing system so that their performance
under different situations can be predicted based on the model. Disks are commonly modeled
as a queueing system, which can predict how response time degrades under load. Figure 2.2
shows a simple queueing system.
24   Chapter 2 Methodologies




     Figure 2.2 Simple queueing model

     The field of queueing theory, introduced in Section 2.6, Modeling, studies queueing systems and
     networks of queueing systems.



     2.3 Concepts
     The following are important concepts of systems performance and are assumed knowledge
     for the rest of this chapter and this book. The topics are described in a generic manner, before
     implementation-specific details are introduced in the Architecture sections of later chapters.


     2.3.1 Latency
     For some environments, latency is the sole focus of performance. For others, it is the top one or
     two key metrics for analysis, along with throughput.

     As an example of latency, Figure 2.3 shows a network transfer, such as an HTTP GET request,
     with the time split into latency and data transfer components.




     Figure 2.3 Network connection latency

     The latency is the time spent waiting before an operation is performed. In this example, the
     operation is a network service request to transfer data. Before this operation can take place,
     the system must wait for a network connection to be established, which is latency for this
     operation. The response time spans this latency and the operation time.

     Because latency can be measured from different locations, it is often expressed with the target of
     the measurement. For example, the load time for a website may be composed of three different
     times measured from different locations: DNS latency, TCP connection latency, and then TCP data
                                                                                    2.3    Concepts     25


transfer time. DNS latency refers to the entire DNS operation. TCP connection latency refers to
the initialization only (TCP handshake).

At a higher level, all of these, including the TCP data transfer time, may be treated as latency
of something else. For example, the time from when the user clicks a website link to when the
resulting page is fully loaded may be termed latency, which includes the time for the browser
to fetch a web page over a network and render it. Since the single word “latency” can be ambig-
uous, it is best to include qualifying terms to explain what it measures: request latency, TCP
connection latency, etc.

As latency is a time-based metric, various calculations are possible. Performance issues can
be quantified using latency and then ranked because they are expressed using the same units
(time). Predicted speedup can also be calculated, by considering when latency can be reduced or
removed. Neither of these can be accurately performed using an IOPS metric, for example.

For reference, time orders of magnitude and their abbreviations are listed in Table 2.1.


Table 2.1       Units of time
Unit                   Abbreviation     Fraction of 1 Second
Minute                 m                60
Second                 s                1
Millisecond            ms               0.001 or 1/1000 or 1 × 10 -3
Microsecond            μs               0.000001 or 1/1000000 or 1 × 10 -6
Nanosecond             ns               0.000000001 or 1/1000000000 or 1 × 10 -9
Picosecond             ps               0.000000000001 or 1/1000000000000 or 1 × 10 -12



When possible, converting other metric types to latency or time allows them to be compared. If
you had to choose between 100 network I/O or 50 disk I/O, how would you know which would
perform better? It’s a complicated question, involving many factors: network hops, rate of net-
work drops and retransmits, I/O size, random or sequential I/O, disk types, and so on. But if you
compare 100 ms of total network I/O and 50 ms of total disk I/O, the difference is clear.


2.3.2         Time Scales
While times can be compared numerically, it also helps to have an instinct about time, and rea-
sonable expectations for latency from different sources. System components operate over vastly
different time scales (orders of magnitude), to the extent that it can be difficult to grasp just how
big those differences are. In Table 2.2, example latencies are provided, starting with CPU register
access for a 3.5 GHz processor. To demonstrate the differences in time scales we’re working with,
the table shows an average time that each operation might take, scaled to an imaginary system
in which a CPU cycle—0.3 ns (about one-third of one-billionth1 of a second) in real life—takes
one full second.

1
    US billionth: 1/1000,000,000
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
