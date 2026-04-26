# systems-performance-observability-1-7 (chunk 000001)

# Systems Performance — 1.7 Observability foundations (PDF pages 46–54)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction: pdftotext -f 46 -l 54 -layout
- Capture: Chapter 1.7 Observability + 1.7.1 counters/statistics/metrics + profiling/tracing overview

---

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
