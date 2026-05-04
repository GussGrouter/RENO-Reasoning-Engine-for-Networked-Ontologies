<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs §6.5 continued) -->

6.5.5

Cycle Analysis

You can use Performance Monitoring Counters (PMCs) to understand CPU utilization at the
cycle level. This may reveal that cycles are spent stalled on Level 1, 2, or 3 cache misses, memory
or resource I/O, or spent on floating-point operations or other activity. This information may
show performance wins you can achieve by adjusting compiler options or changing the code.
Begin cycle analysis by measuring IPC (inverse of CPI). If IPC is low, continue to investigate
types of stall cycles. If IPC is high, look for ways in the code to reduce instructions performed.
The values for “high” or “low” IPC depend on your processor: low could be less than 0.2, and
high could be greater than 1. You can get a sense of these values by performing known workloads that are either memory I/O-intensive or instruction-intensive, and measuring the resulting
IPC for each.
Apart from measuring counter values, PMCs can be configured to interrupt the kernel on the
overflow of a given value. For example, at every 10,000 Level 3 cache misses, the kernel could be
interrupted to gather a stack backtrace. Over time, the kernel builds a profile of the code paths
that are causing Level 3 cache misses, without the prohibitive overhead of measuring every single miss. This is typically used by integrated developer environment (IDE) software, to annotate
code with the locations that are causing memory I/O and stall cycles.
As described in Chapter 4, Observability Tools, Section 4.3.9 under PMC Challenges, overflow
sampling can miss recording the correct instruction due to skid and out-of-order execution. On
Intel the solution is PEBS, which is supported by the Linux perf(1) tool.
Cycle analysis is an advanced activity that can take days to perform with command-line tools, as
demonstrated in Section 6.6, Observability Tools. You should also expect to spend some quality
time with your CPU vendor’s processor manuals. Performance analyzers such as Intel vTune
[Intel 20b] and AMD uprof [AMD 20] can save time as they are programmed to find the PMCs of
interest to you.

6.5.6 Performance Monitoring
Performance monitoring can identify active issues and patterns of behavior over time. Key
metrics for CPUs are:
■

Utilization: Percent busy

■

Saturation: Either run-queue length or scheduler latency

Utilization should be monitored on a per-CPU basis to identify thread scalability issues. For
environments that implement CPU limits or quotas (resource controls), such as cloud computing
environments, CPU usage compared to these limits should also be recorded.
Choosing the right interval to measure and archive is a challenge in monitoring CPU usage.
Some monitoring tools use five-minute intervals, which can hide the existence of shorter bursts
of CPU utilization. Per-second measurements are preferable, but you should be aware that there
can be bursts even within one second. These can be identified from saturation, and examined
using FlameScope (Section 6.7.4), which was created for subsecond analysis.

251

252

Chapter 6 CPUs

