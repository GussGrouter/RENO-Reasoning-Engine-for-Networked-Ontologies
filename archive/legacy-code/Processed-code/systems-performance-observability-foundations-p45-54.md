6   Chapter 1 Introduction


    Bottlenecks can also be complex and related in unexpected ways; fixing one may simply move the
    bottleneck elsewhere in the system, with overall performance not improving as much as hoped.

    Apart from the complexity of the system, performance issues may also be caused by a complex
    characteristic of the production workload. These cases may never be reproducible in a lab envi-
    ronment, or only intermittently so.

    Solving complex performance issues often requires a holistic approach. The whole system—both
    its internals and its external interactions—may need to be investigated. This requires a wide
    range of skills, and can make performance engineering a varied and intellectually challenging
    line of work.

    Different methodologies can be used to guide us through these complexities, as introduced in
    Chapter 2; Chapters 6 to 10 include specific methodologies for specific system resources: CPUs,
    Memory, File Systems, Disks, and Network. (The analysis of complex systems in general, includ-
    ing oil spills and the collapse of financial systems, has been studied by [Dekker 18].)

    In some cases, a performance issue can be caused by the interaction of these resources.


    1.5.3     Multiple Causes
    Some performance issues do not have a single root cause, but instead have multiple contributing
    factors. Imagine a scenario where three normal events occur simultaneously and combine to
    cause a performance issue: each is a normal event that in isolation is not the root cause.

    Apart from multiple causes, there can also be multiple performance issues.


    1.5.4 Multiple Performance Issues
    Finding a performance issue is usually not the problem; in complex software there are often
    many. To illustrate this, try finding the bug database for your operating system or applications
    and search for the word performance. You might be surprised! Typically, there will be a number of
    performance issues that are known but not yet fixed, even in mature software that is considered
    to have high performance. This poses yet another difficulty when analyzing performance: the
    real task isn’t finding an issue; it’s identifying which issue or issues matter the most.

    To do this, the performance analyst must quantify the magnitude of issues. Some performance
    issues may not apply to your workload, or may apply only to a very small degree. Ideally, you
    will not just quantify the issues but also estimate the potential speedup to be gained for each
    one. This information can be valuable when management looks for justification for spending
    engineering or operations resources.

    A metric well suited to performance quantification, when available, is latency.



    1.6 Latency
    Latency is a measure of time spent waiting, and is an essential performance metric. Used
    broadly, it can mean the time for any operation to complete, such as an application request, a
    database query, a file system operation, and so forth. For example, latency can express the time
                                                                                      1.7   Observability   7


for a website to load completely, from link click to screen paint. This is an important metric for
both the customer and the website provider: high latency can cause frustration, and customers
may take their business elsewhere.

As a metric, latency can allow maximum speedup to be estimated. For example, Figure 1.3
depicts a database query that takes 100 ms (which is the latency) during which it spends 80 ms
blocked waiting for disk reads. The maximum performance improvement by eliminating disk
reads (e.g., by caching) can be calculated: from 100 ms to 20 ms (100 – 80) is five times (5x)
faster. This is the estimated speedup, and the calculation has also quantified the performance
issue: disk reads are causing the query to run up to 5x more slowly.




Figure 1.3 Disk I/O latency example

Such a calculation is not possible when using other metrics. I/O operations per second (IOPS),
for example, depend on the type of I/O and are often not directly comparable. If a change were
to reduce the IOPS rate by 80%, it is difficult to know what the performance impact would be.
There might be 5x fewer IOPS, but what if each of these I/O increased in size (bytes) by 10x?

Latency can also be ambiguous without qualifying terms. For example, in networking, latency
can mean the time for a connection to be established but not the data transfer time; or it can
mean the total duration of a connection, including the data transfer (e.g., DNS latency is com-
monly measured this way). Throughout this book I will use clarifying terms where possible:
those examples would be better described as connection latency and request latency. Latency
terminology is also summarized at the beginning of each chapter.

While latency is a useful metric, it hasn’t always been available when and where needed. Some
system areas provide average latency only; some provide no latency measurements at all. With
the availability of new BPF2 -based observability tools, latency can now be measured from cus-
tom arbitrary points of interest and can provide data showing the full distribution of latency.



1.7 Observability
Observability refers to understanding a system through observation, and classifies the tools that
accomplish this. This includes tools that use counters, profiling, and tracing. It does not include
benchmark tools, which modify the state of the system by performing a workload experiment.
For production environments, observability tools should be tried first wherever possible, as
experimental tools may perturb production workloads through resource contention. For test
environments that are idle, you may wish to begin with benchmarking tools to determine hard-
ware performance.


2
    BPF is now a name and no longer an acronym (originally Berkeley Packet Filter).
8   Chapter 1 Introduction


    In this section I’ll introduce counters, metrics, profiling, and tracing. I’ll explain observabil-
    ity in more detail in Chapter 4, covering system-wide versus per-process observability, Linux
    observability tools, and their internals. Chapters 5 to 11 include chapter-specific sections on
    observability, for example, Section 6.6 for CPU observability tools.


    1.7.1 Counters, Statistics, and Metrics
    Applications and the kernel typically provide data on their state and activity: operation counts,
    byte counts, latency measurements, resource utilization, and error rates. They are typically
    implemented as integer variables called counters that are hard-coded in the software, some of
    which are cumulative and always increment. These cumulative counters can be read at different
    times by performance tools for calculating statistics: the rate of change over time, the average,
    percentiles, etc.

    For example, the vmstat(8) utility prints a system-wide summary of virtual memory statistics
    and more, based on kernel counters in the /proc file system. This example vmstat(8) output is
    from a 48-CPU production API server:

    $ vmstat 1 5
    procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
     r   b   swpd    free     buff   cache     si       so       bi       bo       in     cs us sy id wa st
    19   0       0 6531592    42656 1672040         0        0        1        7     21     33 51   4 46   0   0
    26   0       0 6533412    42656 1672064         0        0        0        0 81262 188942 54       4 43    0   0
    62   0       0 6533856    42656 1672088         0        0        0        8 80865 180514 53       4 43    0   0
    34   0       0 6532972    42656 1672088         0        0        0        0 81250 180651 53       4 43    0   0
    31   0       0 6534876    42656 1672088         0        0        0        0 74389 168210 46       3 51    0   0

    This shows a system-wide CPU utilization of around 57% (cpu us + sy columns). The columns are
    explained in detail in Chapters 6 and 7.

    A metric is a statistic that has been selected to evaluate or monitor a target. Most companies use
    monitoring agents to record selected statistics (metrics) at regular intervals, and chart them in a
    graphical interface to see changes over time. Monitoring software can also support creating cus-
    tom alerts from these metrics, such as sending emails to notify staff when problems are detected.

    This hierarchy from counters to alerts is depicted in Figure 1.4. Figure 1.4 is provided as a guide
    to help you understand these terms, but their use in the industry is not rigid. The terms counters,
    statistics, and metrics are often used interchangeably. Also, alerts may be generated by any layer,
    and not just a dedicated alerting system.

    As an example of graphing metrics, Figure 1.5 is a screenshot of a Grafana-based tool observing
    the same server as the earlier vmstat(8) output.

    These line graphs are useful for capacity planning, helping you predict when resources will
    become exhausted.

    Your interpretation of performance statistics will improve with an understanding of how they
    are calculated. Statistics, including averages, distributions, modes, and outliers, are summarized
    in Chapter 2, Methodologies, Section 2.8, Statistics.
                                                                                     1.7   Observability     9




Figure 1.4 Performance instrumentation terminology




Figure 1.5 System metrics GUI (Grafana)

Sometimes, time-series metrics are all that is needed to resolve a performance issue. Knowing the
exact time a problem began may correlate with a known software or configuration change, which can
be reverted. Other times, metrics only point in a direction, suggesting that there is a CPU or disk issue,
but without explaining why. Profiling or tracing tools are necessary to dig deeper and find the cause.
10   Chapter 1 Introduction


     1.7.2     Profiling
     In systems performance, the term profiling usually refers to the use of tools that perform sam-
     pling: taking a subset (a sample) of measurements to paint a coarse picture of the target. CPUs
     are a common profiling target. The commonly used method to profile CPUs involves taking
     timed-interval samples of the on-CPU code paths.

     An effective visualization of CPU profiles is flame graphs. CPU flame graphs can help you find
     more performance wins than any other tool, after metrics. They reveal not only CPU issues,
     but other types of issues as well, found by the CPU footprints they leave behind. Issues of lock
     contention can be found by looking for CPU time in spin paths; memory issues can be analyzed
     by finding excessive CPU time in memory allocation functions (malloc()), along with the code
     paths that led to them; performance issues involving misconfigured networking may be discov-
     ered by seeing CPU time in slow or legacy codepaths; and so on.

     Figure 1.6 is an example CPU flame graph showing the CPU cycles spent by the iperf(1) network
     micro-benchmark tool.




     Figure 1.6 CPU profiling using flame graphs
                                                                                 1.7   Observability   11


This flame graph shows how much CPU time is spent copying bytes (the path that ends in
copy_user_enhanced_fast_string()) versus TCP transmission (the tower on the left that includes
tcp_write_xmit()). The widths are proportional to the CPU time spent, and the vertical axis
shows the code path.

Profilers are explained in Chapters 4, 5, and 6, and the flame graph visualization is explained in
Chapter 6, CPUs, Section 6.7.3, Flame Graphs.


1.7.3 Tracing
Tracing is event-based recording, where event data is captured and saved for later analysis or
consumed on-the-fly for custom summaries and other actions. There are special-purpose tracing
tools for system calls (e.g., Linux strace(1)) and network packets (e.g., Linux tcpdump(8)); and
general-purpose tracing tools that can analyze the execution of all software and hardware events
(e.g., Linux Ftrace, BCC, and bpftrace). These all-seeing tracers use a variety of event sources, in
particular, static and dynamic instrumentation, and BPF for programmability.


Static Instrumentation
Static instrumentation describes hard-coded software instrumentation points added to the
source code. There are hundreds of these points in the Linux kernel that instrument disk I/O,
scheduler events, system calls, and more. The Linux technology for kernel static instrumen-
tation is called tracepoints. There is also a static instrumentation technology for user-space
software called user statically defined tracing (USDT). USDT is used by libraries (e.g., libc) for
instrumenting library calls and by many applications for instrumenting service requests.

As an example tool that uses static instrumentation, execsnoop(8) prints new processes created
while it is tracing (running) by instrumenting a tracepoint for the execve(2) system call. The
following shows execsnoop(8) tracing an SSH login:

# execsnoop
PCOMM               PID     PPID    RET ARGS
ssh                 30656   20063      0 /usr/bin/ssh 0
sshd                30657   1401       0 /usr/sbin/sshd -D -R
sh                  30660   30657      0
env                 30661   30660      0 /usr/bin/env -i PATH=/usr/local/sbin:/usr/local...
run-parts           30661   30660      0 /bin/run-parts --lsbsysinit /etc/update-motd.d
00-header           30662   30661      0 /etc/update-motd.d/00-header
uname               30663   30662      0 /bin/uname -o
uname               30664   30662      0 /bin/uname -r
uname               30665   30662      0 /bin/uname -m
10-help-text        30666   30661      0 /etc/update-motd.d/10-help-text
50-motd-news        30667   30661      0 /etc/update-motd.d/50-motd-news
cat                 30668   30667      0 /bin/cat /var/cache/motd-news
cut                 30671   30667      0 /usr/bin/cut -c -80
tr                  30670   30667      0 /usr/bin/tr -d \000-\011\013\014\016-\037
head                30669   30667      0 /usr/bin/head -n 10
12   Chapter 1 Introduction


     80-esm                    30672     30661        0 /etc/update-motd.d/80-esm
     lsb_release               30673     30672        0 /usr/bin/lsb_release -cs
     [...]

     This is especially useful for revealing short-lived processes that may be missed by other observ-
     ability tools such as top(1). These short-lived processes can be a source of performance issues.

     See Chapter 4 for more information about tracepoints and USDT probes.


     Dynamic Instrumentation
     Dynamic instrumentation creates instrumentation points after the software is running, by
     modifying in-memory instructions to insert instrumentation routines. This is similar to
     how debuggers can insert a breakpoint on any function in running software. Debuggers pass
     execution flow to an interactive debugger when the breakpoint is hit, whereas dynamic instru-
     mentation runs a routine and then continues the target software. This capability allows custom
     performance statistics to be created from any running software. Issues that were previously
     impossible or prohibitively difficult to solve due to a lack of observability can now be fixed.

     Dynamic instrumentation is so different from traditional observation that it can be difficult,
     at first, to grasp its role. Consider an operating system kernel: analyzing kernel internals can be
     like venturing into a dark room, with candles (system counters) placed where the kernel engi-
     neers thought they were needed. Dynamic instrumentation is like having a flashlight that you
     can point anywhere.

     Dynamic instrumentation was first created in the 1990s [Hollingsworth 94], along with tools
     that use it called dynamic tracers (e.g., kerninst [Tamches 99]). For Linux, dynamic instrumen-
     tation was first developed in 2000 [Kleen 08] and began merging into the kernel in 2004
     (kprobes). However, these technologies were not well known and were difficult to use. This
     changed when Sun Microsystems launched their own version in 2005, DTrace, which was easy
     to use and production-safe. I developed many DTrace-based tools that showed how important
     it was for systems performance, tools that saw widespread use and helped make DTrace and
     dynamic instrumentation well-known.


     BPF
     BPF, which originally stood for Berkeley Packet Filter, is powering the latest dynamic tracing
     tools for Linux. BPF originated as a mini in-kernel virtual machine for speeding up the execu-
     tion of tcpdump(8) expressions. Since 2013 it has been extended (hence is sometimes called
     eBPF3) to become a generic in-kernel execution environment, one that provides safety and fast
     access to resources. Among its many new uses are tracing tools, where it provides programmabil-
     ity for the BPF Compiler Collection (BCC) and bpftrace front ends. execsnoop(8), shown earlier,
     is a BCC tool.4



     3
         eBPF was initially used to describe this extended BPF; however, the technology is now referred to as just BPF.
     4
         I first developed it for DTrace, and I have since developed it for other tracers including BCC and bpftrace.
                                                                            1.8   Experimentation   13


Chapter 3 explains BPF, and Chapter 15 introduces the BPF tracing front ends: BCC and bpf-
trace. Other chapters introduce many BPF-based tracing tools in their observability sections; for
example, CPU tracing tools are included in Chapter 6, CPUs, Section 6.6, Observability Tools. I
have also published prior books on tracing tools (for DTrace [Gregg 11a] and BPF [Gregg 19]).

Both perf(1) and Ftrace are also tracers with some similar capabilities to the BPF front ends.
perf(1) and Ftrace are covered in Chapters 13 and 14.



1.8 Experimentation
Apart from observability tools there are also experimentation tools, most of which are bench-
marking tools. These perform an experiment by applying a synthetic workload to the system
and measuring its performance. This must be done carefully, because experimental tools can
perturb the performance of systems under test.

There are macro-benchmark tools that simulate a real-world workload such as clients making
application requests; and there are micro-benchmark tools that test a specific component, such
as CPUs, disks, or networks. As an analogy: a car’s lap time at Laguna Seca Raceway could be
considered a macro-benchmark, whereas its top speed and 0 to 60mph time could be considered
micro-benchmarks. Both benchmark types are important, although micro-benchmarks are
typically easier to debug, repeat, and understand, and are more stable.

The following example uses iperf(1) on an idle server to perform a TCP network throughput
micro-benchmark with a remote idle server. This benchmark ran for ten seconds (-t 10) and
produces per-second averages (-i 1):

# iperf -c 100.65.33.90 -i 1 -t 10
------------------------------------------------------------
Client connecting to 100.65.33.90, TCP port 5001
TCP window size: 12.0 MByte (default)
------------------------------------------------------------
[   3] local 100.65.170.28 port 39570 connected with 100.65.33.90 port 5001
[ ID] Interval          Transfer       Bandwidth
[   3]   0.0- 1.0 sec    582 MBytes    4.88 Gbits/sec
[   3]   1.0- 2.0 sec    568 MBytes    4.77 Gbits/sec
[   3]   2.0- 3.0 sec    574 MBytes    4.82 Gbits/sec
[   3]   3.0- 4.0 sec    571 MBytes    4.79 Gbits/sec
[   3]   4.0- 5.0 sec    571 MBytes    4.79 Gbits/sec
[   3]   5.0- 6.0 sec    432 MBytes    3.63 Gbits/sec
[   3]   6.0- 7.0 sec    383 MBytes    3.21 Gbits/sec
[   3]   7.0- 8.0 sec    388 MBytes    3.26 Gbits/sec
[   3]   8.0- 9.0 sec    390 MBytes    3.28 Gbits/sec
[   3]   9.0-10.0 sec    383 MBytes    3.22 Gbits/sec
[   3]   0.0-10.0 sec   4.73 GBytes    4.06 Gbits/sec
14   Chapter 1 Introduction


     The output shows a throughput5 of around 4.8 Gbits for the first five seconds, which drops to
     around 3.2 Gbits/sec. This is an interesting result that shows bi-modal throughput. To improve
     performance, one might focus on the 3.2 Gbits/sec mode, and search for other metrics that can
     explain it.

     Consider the drawbacks of debugging this performance issue on a production server using
     observability tools alone. Network throughput can vary from second to second because of natu-
     ral variance in the client workload, and the underlying bi-modal behavior of the network might
     not be apparent. By using iperf(1) with a fixed workload, you eliminate client variance, revealing
     the variance due to other factors (e.g., external network throttling, buffer utilization, and so on).

     As I recommended earlier, on production systems you should first try observability tools.
     However, there are so many observability tools that you might spend hours working through
     them when an experimental tool would lead to quicker results. An analogy taught to me by a
     senior performance engineer (Roch Bourbonnais) many years ago was this: you have two hands,
     observability and experimentation. Only using one type of tool is like trying to solve a problem
     one-handed.

     Chapters 6 to 10 include sections on experimental tools; for example, CPU experimental tools
     are covered in Chapter 6, CPUs, Section 6.8, Experimentation.



     1.9 Cloud Computing
     Cloud computing, a way to deploy computing resources on demand, has enabled rapid scaling
     of applications by supporting their deployment across an increasing number of small virtual
     systems called instances. This has decreased the need for rigorous capacity planning, as more
     capacity can be added from the cloud at short notice. In some cases it has also increased the
     desire for performance analysis, because using fewer resources can mean fewer systems. Since
     cloud usage is typically charged by the minute or hour, a performance win resulting in fewer
     systems can mean immediate cost savings. Compare this scenario to an enterprise data center,
     where you may be locked into a fixed support contract for years, unable to realize cost savings
     until the contract has ended.

     New difficulties caused by cloud computing and virtualization include the management of
     performance effects from other tenants (sometimes called performance isolation) and physical
     system observability from each tenant. For example, unless managed properly by the system,
     disk I/O performance may be poor due to contention with a neighbor. In some environments,
     the true usage of the physical disks may not be observable by each tenant, making identification
     of this issue difficult.

     These topics are covered in Chapter 11, Cloud Computing.




     5
      The output uses the term “Bandwidth,” a common misuse. Bandwidth refers to the maximum possible throughput,
     which iperf(1) is not measuring. iperf(1) is measuring the current rate of its network workload: its throughput.
                                                                                        1.10 Methodologies            15



1.10          Methodologies
Methodologies are a way to document the recommended steps for performing various tasks
in systems performance. Without a methodology, a performance investigation can turn into
a fishing expedition: trying random things in the hope of catching a win. This can be time-
consuming and ineffective, while allowing important areas to be overlooked. Chapter 2,
Methodologies, includes a library of methodologies for systems performance. The following is
the first I use for any performance issue: a tool-based checklist.


1.10.1        Linux Perf Analysis in 60 Seconds
This is a Linux tool-based checklist that can be executed in the first 60 seconds of a performance
issue investigation, using traditional tools that should be available for most Linux distributions
[Gregg 15a]. Table 1.1 shows the commands, what to check for, and the section in this book that
covers the command in more detail.


Table 1.1     Linux 60-second analysis checklist
#    Tool                        Check                                                                 Section
1    uptime                      Load averages to identify if load is increasing or                    6.6.1
                                 decreasing (compare 1-, 5-, and 15-minute averages).
2    dmesg -T | tail             Kernel errors including OOM events.                                   7.5.11
3    vmstat -SM 1                System-wide statistics: run queue length, swapping,                   7.5.1
                                 overall CPU usage.
4    mpstat -P ALL 1             Per-CPU balance: a single busy CPU can indicate poor                  6.6.3
                                 thread scaling.
5    pidstat 1                   Per-process CPU usage: identify unexpected CPU        6.6.7
                                 consumers, and user/system CPU time for each process.
6    iostat -sxz 1               Disk I/O statistics: IOPS and throughput, average wait                9.6.1
                                 time, percent busy.
7    free -m                     Memory usage including the file system cache.                         8.6.2
8    sar -n DEV 1                Network device I/O: packets and throughput.                           10.6.6
9    sar -n TCP,ETCP 1           TCP statistics: connection rates, retransmits.                        10.6.6
10 top                           Check overview.                                                       6.6.6



This checklist can also be followed using a monitoring GUI, provided the same metrics are
available.6



6
  You could even make a custom dashboard for this checklist; however, bear in mind that this checklist was designed
to make the most of readily available CLI tools, and monitoring products may have more (and better) metrics avail-
able. I’d be more inclined to make custom dashboards for the USE method and other methodologies.
