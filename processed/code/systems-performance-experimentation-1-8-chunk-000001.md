# systems-performance-experimentation-1-8 (chunk 000001)

# Systems Performance — 1.8 Experimentation (without 1.9) (PDF pages 52–54)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-experimentation-1-8-p52-54.md
- Slice: 1.8 Experimentation (without 1.9)

---

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
