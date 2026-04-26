# Systems Performance — 1.10 Methodologies + 1.10.1 60-second checklist (PDF pages 54–54)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-experimentation-1-8-p52-54.md
- Slice: 1.10 Methodologies + 1.10.1 60-second checklist

---

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
