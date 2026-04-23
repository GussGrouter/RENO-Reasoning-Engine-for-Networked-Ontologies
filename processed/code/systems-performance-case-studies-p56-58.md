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
