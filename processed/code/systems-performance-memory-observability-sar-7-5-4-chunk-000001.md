7.5.4 sar
The system activity reporter, sar(1), can be used to observe current activity and can be configured to archive and report historical statistics. It is mentioned in various chapters in this book
for the different statistics it provides, and was introduced in Chapter 4, Observability Tools,
Section 4.4, sar.
The Linux version provides memory statistics via the following options:
■

-B: Paging statistics

■

-H: Huge pages statistics

■

-r: Memory utilization

■

-S: Swap space statistics

■

-W: Swapping statistics

These span memory usage, activity of the page-out daemon, and huge pages usage. See Section 7.3,
Architecture, for background on these topics.

331

332

Chapter 7 Memory

Statistics provided include those in Table 7.5.

Table 7.5

Linux sar memory statistics

Option

Statistic

Description

Units

-B

pgpgin/s

Page-ins

Kbytes/s

-B

pgpgout/s

Page-outs

Kbytes/s

-B

fault/s

Both major and minor faults

Count/s

-B

majflt/s

Major faults

Count/s

-B

pgfree/s

Pages added to free list

Count/s

-B

pgscank/s

Pages scanned by background page-out daemon
(kswapd)

Count/s

-B

pgscand/s

Direct page scans

Count/s

-B

pgsteal/s

Page and swap cache reclaims

Count/s

-B

%vmeff

Ratio of page steal/page scan, which shows page
reclaim efficiency

Percent

-H

hbhugfree

Free huge pages memory (large page size)

Kbytes

-H

hbhugused

Used huge pages memory

Kbytes

-H

%hugused

Huge page usage

Percent

-r

kbmemfree

Free memory (completely unused)

Kbytes

-r

kbavail

Available memory, including pages that can be readily
freed from the page cache

Kbytes

-r

kbmemused

Used memory (excluding the kernel)

Kbytes

-r

%memused

Memory usage

Percent

-r

kbbuffers

Buffer cache size

Kbytes

-r

kbcached

Page cache size

Kbytes

-r

kbcommit

Main memory committed: an estimate of the amount
needed to serve the current workload

Kbytes

-r

%commit

Main memory committed for current workload, estimate

Percent

-r

kbactive

Active list memory size

Kbytes

-r

kbinact

Inactive list memory size

Kbytes

-r

kbdirtyw

Modified memory to be written to disk

Kbytes

-r ALL

kbanonpg

Process anonymous memory

Kbytes

-r ALL

kbslab

Kernel slab cache size

Kbytes

-r ALL

kbkstack

Kernel stack space size

Kbytes

-r ALL

kbpgtbl

Lowest-level page table size

Kbytes

7.5 Observability Tools

Option

Statistic

Description

Units

-r ALL

kbvmused

Used virtual address space

Kbytes

-S

kbswpfree

Free swap space

Kbytes

-S

kbswpused

Used swap space

Kbytes

-S

%swpused

Used swap space

Percent

-S

kbswpcad

Cached swap space: this resides in both main memory
and the swap device and so can be paged out without
disk I/O

Kbytes

-S

%swpcad

Ratio of cached swap versus used swap

Percent

-W

pswpin/s

Page-ins (Linux “swap-ins”)

Pages/s

-W

pswpout/s

Page-outs (Linux “swap-outs”)

Pages/s

Many of the statistic names include the units measured: pg for pages, kb for kilobytes, % for a percentage, and /s for per second. See the man page for the full list, which includes some additional
percentage-based statistics.
It is important to remember that this much detail is available, when needed, on the usage and
operation of high-level memory subsystems. To understand these in deeper detail, you may
need to use tracers to instrument memory tracepoints and kernel functions, such as perf(1) and
bpftrace in the following sections. You can also browse the source code in mm, specifically
mm/vmscan.c. There are many posts to the linux-mm mailing list that provide further insight,
as the developers discuss what the statistics should be.
The %vmeff metric is a useful measure of page reclaim efficiency. High means pages are successfully stolen from the inactive list (healthy); low means the system is struggling. The man page
describes near 100% as high, and less than 30% as low.
Another useful metric is pgscand, which effectively shows the rate at which an application is
blocking on memory allocations and entering direct reclaim (higher is bad). To see the time spent
by applications during direct reclaim events, you can use tracing tools: see Section 7.5.11, drsnoop.

