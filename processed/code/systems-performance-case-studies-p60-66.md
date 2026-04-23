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
