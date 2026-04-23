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
