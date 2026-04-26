                                                                                  2.5 Methodology       59



2.5.16       Baseline Statistics
Environments commonly use monitoring solutions to record server performance metrics and
to visualize them as line charts, with time on the x-axis (see Section 2.9, Monitoring). These
line charts can show whether a metric has changed recently, and if so, how it is now different,
simply by examining changes in the line. Sometimes additional lines are added to include more
histor ical data, such as historical averages or simply historical time ranges for comparison with
the current range. Many Netflix dashboards, for example, draw an extra line to show the same
time range but for the previous week, so that behavior at 3 p.m. on a Tuesday can be directly
compared with 3 p.m. on the previous Tuesday.

These approaches work well with already-monitored metrics and a GUI to visualize them.
However, there are many more system metrics and details available at the command line that
may not be monitored. You may be faced with unfamiliar system statistics and wonder if they
are “normal” for the server, or if they are evidence of an issue.

This is not a new problem, and there is a methodology to solve it that predates the widespread
use of monitoring solutions using line charts. It is the collection of baseline statistics. This can
involve collecting all the system metrics when the system is under “normal” load and recording
them in a text file or database for later reference. The baseline software can be a shell script that
runs observability tools and gathers other sources (cat(1) of /proc files). Profilers and tracing
tools can be included in the baseline, providing far more detail than is typically recorded by
monitoring products (but be careful with the overhead of those tools, so as not to perturb pro-
duction). These baselines may be collected at regular intervals (daily), as well as before and after
system or application changes, so that performance differences can be analyzed.

If baselines have not been collected and monitoring is not available, some observability tools
(those based on kernel counters) can show summary-since-boot averages, for comparison with
current activity. This is coarse, but better than nothing.


2.5.17       Static Performance Tuning
Static performance tuning focuses on issues of the configured architecture. Other methodol-
ogies focus on the performance of the applied load: the dynamic performance [Elling 00]. Static
performance analysis can be performed when the system is at rest and no load is applied.

For static performance analysis and tuning, step through all the components of the system and
check the following:

    ■   Does the component make sense? (outdated, underpowered, etc.)
    ■   Does the configuration make sense for the intended workload?
    ■   Was the component autoconfigured in the best state for the intended workload?
    ■   Has the component experienced an error such that it is now in a degraded state?

Here are some examples of issues that may be found using static performance tuning:

    ■   Network interface negotiation: selecting 1 Gbits/s instead of 10 Gbit/s
    ■   Failed disk in a RAID pool
    ■   Older version of the operating system, applications, or firmware used
60   Chapter 2 Methodologies


         ■   File system nearly full (can cause performance issues)
         ■   Mismatched file system record size compared to workload I/O size
         ■   Application running with a costly debug mode accidentally left enabled
         ■   Server accidentally configured as a network router (IP forwarding enabled)
         ■   Server configured to use resources, such as authentication, from a remote data center
             instead of locally

     Fortunately, these types of issues are easy to check for; the hard part is remembering to do it!


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


     2.5.19 Micro-Benchmarking
     Micro-benchmarking tests the performance of simple and artificial workloads. This differs from
     macro-benchmarking (or industry benchmarking), which typically aims to test a real-world and
     natural workload. Macro-benchmarking is performed by running workload simulations and can
     become complex to conduct and understand.

     With fewer factors in play, micro-benchmarking is less complicated to conduct and understand.
     A commonly used micro-benchmark is Linux iperf(1), which performs a TCP throughput test:
     this can identify external network bottlenecks (which would otherwise be difficult to spot) by
     examining TCP counters during a production workload.
                                                                             2.5 Methodology       61


Micro-benchmarking can be performed by a micro-benchmark tool that applies the workload and
measures its performance, or you can use a load generator tool that just applies the workload,
leaving measurements of performance to other observability tools (example load generators are
in Chapter 12, Benchmarking, Section 12.2.2, Simulation). Either approach is fine, but it can be
safest to use a micro-benchmark tool and to double-check performance using other tools.

Some example targets of micro-benchmarks, including a second dimension for the tests, are:
   ■   Syscall time: For fork(2), execve(2), open(2), read(2), close(2)
   ■   File system reads: From a cached file, varying the read size from one byte to one Mbyte
   ■   Network throughput: Transferring data between TCP endpoints, for varying socket
       buffer sizes

Micro-benchmarking typically conducts the target operation as quickly as possible and measures
the time for a large number of these operations to complete. The average time can then be calcu-
lated (average time = runtime/operation count).

Later chapters include specific micro-benchmarking methodologies, listing the targets and attri-
butes to test. The topic of benchmarking is covered in more detail in Chapter 12, Benchmarking.


2.5.20       Performance Mantras
This is a tuning methodology that shows how best to improve performance, listing actionable
items in order from most to least effective. It is:

   1. Don’t do it.

  2. Do it, but don’t do it again.

  3. Do it less.

  4. Do it later.

  5. Do it when they’re not looking.
  6. Do it concurrently.

   7. Do it more cheaply.

Here are some examples for each of these:

   1. Don’t do it: Eliminate unnecessary work.

  2. Do it, but don’t do it again: Caching.

  3. Do it less: Tune refreshes, polling, or updates to be less frequent.

  4. Do it later: Write-back caching.

  5. Do it when they’re not looking: Schedule work to run during off-peak hours.

  6. Do it concurrently: Switch from single-threaded to multi-threaded.

   7. Do it more cheaply: Buy faster hardware.

This is one of my favorite methodologies, which I learned from Scott Emmons at Netflix. He
attributes it to Craig Hanson and Pat Crain (though I’ve yet to find a published reference).
62   Chapter 2 Methodologies



     2.6      Modeling
     Analytical modeling of a system can be used for various purposes, in particular scalability analysis:
     studying how performance scales as load or resources increase. Resources may be hardware (such
     as CPU cores) or software (processes or threads).

     Analytical modeling can be considered the third type of performance evaluation activity, along
     with observability of a production system (“measurement”) and experimental testing (“simula-
     tion”) [Jain 91]. Performance is best understood when at least two of these activities are performed:
     analytical modeling and simulation, or simulation and measurement.

     If the analysis is for an existing system, you can begin with measurement: characterizing the
     load and resulting performance. Experimental analysis, by testing a workload simulation, can be
     used if the system does not yet have production load, or in order to test workloads beyond what
     is seen in production. Analytical modeling can be used to predict performance and can be based
     on the results of measurement or simulation.

     Scalability analysis may reveal that performance stops scaling linearly at a particular point
     due to a resource constraint. This is referred to as a knee point: when one function switches to
     another, in this case, from linear scaling to contention. Finding whether these points exist, and
     where, can direct an investigation to performance issues that inhibit scalability so that they can
     be fixed before they are encountered in production.

     See Section 2.5.11, Workload Characterization, and Section 2.5.19, Micro-Benchmarking, for
     more on those steps.


     2.6.1 Enterprise vs. Cloud
     While modeling allows us to simulate large-scale enterprise systems without the expense of
     owning one, the performance of large-scale environments is often complex and difficult to
     model accurately.

     With cloud computing, environments of any scale can be rented for short durations—the length
     of a benchmark test. Instead of creating a mathematical model from which to predict perfor-
     mance, the workload can be characterized, simulated, and then tested on clouds of different
     scales. Some of the findings, such as knee points, may be the same but will now be based on
     measured data rather than theoretical models, and by testing a real environment you may dis-
     cover limiters that were not included in your model.


     2.6.2     Visual Identification
     When enough results can be collected experimentally, plotting them as delivered performance
     versus a scaling parameter may reveal a pattern.

     Figure 2.15 shows the throughput of an application as the number of threads is scaled. There
     appears to be a knee point around eight threads, where the slope changes. This can now be
     investigated, for example by looking at the application and system configuration for any setting
     around the value of eight.
                                                                                      2.6   Modeling   63




Figure 2.15 Scalability test results

In this case, the system was an eight-core system, each core having two hardware threads. To
further confirm that this is related to the CPU core count, the CPU effects at fewer than and
more than eight threads can be investigated and compared (e.g., IPC; see Chapter 6, CPUs). Or,
this can be investigated experimentally by repeating the scaling test on a system with a different
core count and confirming that the knee point moves as expected.

There are a number of scalability profiles to look for that may be identified visually, without
using a formal model. These are shown in Figure 2.16.

For each of these, the x-axis is the scalability dimension, and the y-axis is the resulting perfor-
mance (throughput, transactions per second, etc.). The patterns are:

    ■   Linear scalability: Performance increases proportionally as the resource is scaled. This
        may not continue forever and may instead be the early stages of another scalability
        pattern.
    ■   Contention: Some components of the architecture are shared and can be used only
        serially, and contention for these shared resources begins to reduce the effectiveness of
        scaling.
    ■   Coherence: The tax to maintain data coherency including propagation of changes begins
        to outweigh the benefits of scaling.
64   Chapter 2 Methodologies


         ■   Knee point: A factor is encountered at a scalability point that changes the scalability
             profile.
         ■   Scalability ceiling: A hard limit is reached. This may be a device bottleneck, such as a
             bus or interconnect reaching maximum throughput, or a software-imposed limit (system
             resource control).




     Figure 2.16 Scalability profiles

     While visual identification can be easy and effective, you can learn more about system scalabil-
     ity by using a mathematical model. The model may deviate from the data in an unexpected way,
     which can be useful to investigate: either there is a problem with the model, and hence with
     your understanding of the system, or the problem is in the real scalability of the system. The next
     sections introduce Amdahl’s Law of Scalability, the Universal Scalability Law, and queueing
     theory.


     2.6.3      Amdahl’s Law of Scalability
     Named after computer architect Gene Amdahl [Amdahl 67], this law models system scalability,
     accounting for serial components of workloads that do not scale in parallel. It can be used to
     study the scaling of CPUs, threads, workloads, and more.

     Amdahl’s Law of Scalability was shown in the earlier scalability profiles as contention, which
     describes contention for the serial resource or workload component. It can be defined as
     [Gunther 97]:

         C(N) = N/(1 + α(N – 1))
                                                                                    2.6   Modeling     65


The relative capacity is C(N), and N is the scaling dimension, such as the CPU count or user load.
The α parameter (where 0 <= α <= 1) represents the degree of seriality and is how this deviates
from linear scalability.

Amdahl’s Law of Scalability can be applied by taking the following steps:

   1. Collect data for a range of N, either by observation of an existing system or experimentally
      using micro-benchmarking or load generators.

   2. Perform regression analysis to determine the Amdahl parameter (α); this may be done
      using statistical software, such as gnuplot or R.

   3. Present the results for analysis. The collected data points can be plotted along with the
      model function to predict scaling and reveal differences between the data and the model.
      This may also be done using gnuplot or R.

The following is example gnuplot code for Amdahl’s Law of Scalability regression analysis, to
provide a sense of how this step can be performed:

inputN = 10                          # rows to include as model input
alpha = 0.1                          # starting point (seed)
amdahl(N) = N1 * N/(1 + alpha * (N - 1))
# regression analysis (non-linear least squares fitting)
fit amdahl(x) filename every ::1::inputN using 1:2 via alpha

A similar amount of code is required to process this in R, involving the nls() function for non-
linear least squares fitting to calculate the coefficients, which are then used during plotting. See
the Performance Scalability Models toolkit in the references at the end of this chapter for the full
code in both gnuplot and R [Gregg 14a].

An example Amdahl’s Law of Scalability function is shown in the next section.


2.6.4 Universal Scalability Law
The Universal Scalability Law (USL), previously called the super-serial model [Gunther 97], was
developed by Dr. Neil Gunther to include a parameter for coherency delay. This was pictured
earlier as the coherence scalability profile, which includes the effects of contention.

USL can be defined as:

    C(N) = N/(1 + α(N – 1) + βN(N – 1))

C(N), N, and α are as with Amdahl’s Law of Scalability. β is the coherence parameter. When
β == 0, this becomes Amdahl’s Law of Scalability.

Examples of both USL and Amdahl’s Law of Scalability analysis are graphed in Figure 2.17.
66   Chapter 2 Methodologies




     Figure 2.17 Scalability models

     The input dataset has a high degree of variance, making it difficult to visually determine the
     scalability profile. The first ten data points, drawn as circles, were provided to the models. An
     additional ten data points are also plotted, drawn as crosses, which check the model prediction
     against reality.

     For more on USL analysis, see [Gunther 97] and [Gunther 07].


     2.6.5     Queueing Theory
     Queueing theory is the mathematical study of systems with queues, providing ways to analyze
     their queue length, wait time (latency), and utilization (time-based). Many components in
     computing, both software and hardware, can be modeled as queueing systems. The modeling of
     multiple queueing systems is called queueing networks.

     This section summarizes the role of queueing theory and provides an example to help you under-
     stand that role. It is a large field of study, covered in detail in other texts [Jain 91][Gunther 97].

     Queueing theory builds upon various areas of mathematics and statistics, including probability
     distributions, stochastic processes, Erlang’s C formula (Agner Krarup Erlang invented queueing
     theory), and Little’s Law. Little’s Law can be expressed as

          L = λW

     which determines the average number of requests in a system, L, as the average arrival rate, λ,
     multiplied by the average request time in the system, W. This can be applied to a queue, such
     that L is the number of requests in the queue, and W is the average wait time on the queue.
                                                                                     2.6   Modeling    67


Queueing systems can be used to answer a variety of questions, including the following:

    ■   What will the mean response time be if the load doubles?
    ■   What will be the effect on mean response time after adding an additional processor?
    ■   Can the system provide a 90th percentile response time of under 100 ms when the load
        doubles?

Apart from response time, other factors, including utilization, queue lengths, and number of
resident jobs, can be studied.

A simple queueing system model is shown in Figure 2.18.




Figure 2.18 Queueing model

This has a single service center that processes jobs from the queue. Queueing systems can have
multiple service centers that process work in parallel. In queueing theory, the service centers are
often called servers.

Queueing systems can be categorized by three factors:

    ■   Arrival process: This describes the inter-arrival time for requests to the queueing system,
        which may be random, fixed-time, or a process such as Poisson (which uses an exponen-
        tial distribution for arrival time).
    ■   Service time distribution: This describes the service times for the service center. They
        may be fixed (deterministic), exponential, or of another distribution type.
    ■   Number of service centers: One or many.

These factors can be written in Kendall’s notation.


Kendall’s Notation
This notation assigns codes for each attribute. It has the form

    A/S/m

These are the arrival process (A), service time distribution (S), and number of service centers (m).
There is also an extended form of Kendall’s notation that includes more factors: number of buf-
fers in the system, population size, and service discipline.
