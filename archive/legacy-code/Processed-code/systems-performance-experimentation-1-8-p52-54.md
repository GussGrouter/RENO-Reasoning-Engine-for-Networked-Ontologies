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
