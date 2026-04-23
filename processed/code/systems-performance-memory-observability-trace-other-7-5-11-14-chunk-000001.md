7.5.11

drsnoop
10

drsnoop(8) is a BCC tool for tracing the direct reclaim approach to freeing memory, showing
the process affected and the latency: the time taken for the reclaim. It can be used to quantify the
application performance impact of a memory-constrained system. For example:
# drsnoop -T
TIME(s)

COMM

PID

0.000000000

java

11266

LAT(ms) PAGES
1.72

57

0.004007000

java

11266

3.21

57

0.011856000

java

11266

2.02

43

0.018315000

java

11266

3.09

55

0.024647000

acpid

1209

6.46

73

[...]

This output shows some direct reclaims for Java, taking between one and seven milliseconds.
The rates of these reclaims and their duration in milliseconds (LAT(ms)) can be considered in
quantifying the application impact.
This tool works by tracing the vmscan mm_vmscan_direct_reclaim_begin and mm_vmscan_
direct_reclaim_end tracepoints. These are expected to be low-frequency events (usually happening in bursts), so the overhead should be negligible.
drsnoop(8) supports a -T option to include timestamps, and -p PID to match a single process.

7.5.12

wss

wss(8) is an experimental tool I developed to show how a process working set size (WSS) can be
measured using the page table entry (PTE) “accessed” bit. This was part of a longer study to summarize different ways working set size can be determined [Gregg 18c]. I’ve included wss(8) here
because working set size (the amount of frequently accessed memory) is an important metric for
understanding memory usage, and having an experimental tool with warnings is better than
no tool.
The following output shows wss(8) measuring the WSS of a MySQL database server (mysqld),
printing the cumulative WSS every one second:
# ./wss.pl $(pgrep -n mysqld) 1
Watching PID 423 page references grow, output every 1 seconds...
Est(s)

RSS(MB)

PSS(MB)

Ref(MB)

1.014

403.66

400.59

86.00

2.034

403.66

400.59

90.75

10

Origin: This was created by Wenbo Zhang on 10-Feb-2019.

7.5 Observability Tools

3.054

403.66

400.59

94.29

4.074

403.66

400.59

97.53

5.094

403.66

400.59

100.33

6.114

403.66

400.59

102.44

7.134

403.66

400.59

104.58

8.154

403.66

400.59

106.31

9.174

403.66

400.59

107.76

10.194

403.66

400.59

109.14

The output shows that by the five-second mark, mysqld had touched around 100 Mbytes of
memory. The RSS for mysqld was 400 Mbytes. The output also includes the estimated time for
the interval, including the time taken to set and read the accessed bit (Est(s)), and the proportional set size (PSS), which accounts for sharing pages with other processes.
This tool works by resetting the PTE accessed bit for every page in a process, pausing for an interval, and then checking the bits to see which have been set. Since this is page-based, the resolution is the page size, typically 4 Kbytes. Consider the numbers it reports to have been rounded
up to the page size.
WARNINGS: This tool uses /proc/PID/clear_refs and /proc/PID/smaps, which can cause slightly
higher application latency (e.g., 10%) while the kernel walks page structures. For large processes
(> 100 Gbytes), this duration of higher latency can last over one second, during which this tool is
consuming system CPU time. Keep these overheads in mind. This tool also resets the referenced
flag, which might confuse the kernel as to which pages to reclaim, especially if swapping is
active. Further, it also activates some old kernel code that may not have been used in your environment before. Test first in a lab environment to make sure you understand the overheads.

7.5.13 bpftrace
bpftrace is a BPF-based tracer that provides a high-level programming language, allowing the
creation of powerful one-liners and short scripts. It is well suited for custom application analysis
based on clues from other tools. The bpftrace repository contains additional tools for memory
analysis, including oomkill.bt [Robertson 20].
bpftrace is explained in Chapter 15, BPF. This section shows some examples for memory analysis.

One-liners
The following one-liners are useful and demonstrate different bpftrace capabilities.
Sum libc malloc() request bytes by user stack and process (high overhead):
bpftrace -e 'uprobe:/lib/x86_64-linux-gnu/libc.so.6:malloc {
@[ustack, comm] = sum(arg0); }'

Sum libc malloc() request bytes by user stack for PID 181 (high overhead):
bpftrace -e 'uprobe:/lib/x86_64-linux-gnu/libc.so.6:malloc /pid == 181/ {
@[ustack] = sum(arg0); }'

343

344

Chapter 7 Memory

Show libc malloc() request bytes by user stack for PID 181 as a power-of-2 histogram (high
overhead):
bpftrace -e 'uprobe:/lib/x86_64-linux-gnu/libc.so.6:malloc /pid == 181/ {
@[ustack] = hist(arg0); }'

Sum kernel kmem cache allocation bytes by kernel stack trace:
bpftrace -e 't:kmem:kmem_cache_alloc { @bytes[kstack] = sum(args->bytes_alloc); }'

Count process heap expansion (brk(2)) by code path:
bpftrace -e 'tracepoint:syscalls:sys_enter_brk { @[ustack, comm] = count(); }'

Count page faults by process:
bpftrace -e 'software:page-fault:1 { @[comm, pid] = count(); }'

Count user page faults by user-level stack trace:
bpftrace -e 't:exceptions:page_fault_user { @[ustack, comm] = count(); }'

Count vmscan operations by tracepoint:
bpftrace -e 'tracepoint:vmscan:* { @[probe] = count(); }'

Count swapins by process:
bpftrace -e 'kprobe:swap_readpage { @[comm, pid] = count(); }'

Count page migrations:
bpftrace -e 'tracepoint:migrate:mm_migrate_pages { @ = count(); }'

Trace compaction events:
bpftrace -e 't:compaction:mm_compaction_begin { time(); }'

List USDT probes in libc:
bpftrace -l 'usdt:/lib/x86_64-linux-gnu/libc.so.6:*'

List kernel kmem tracepoints:
bpftrace -l 't:kmem:*'

List all memory subsystem (mm) tracepoints:
bpftrace -l 't:*:mm_*'

7.5 Observability Tools

User Allocation Stacks
User-level allocations can be traced from the allocation functions used. For this example, the
malloc(3) function from libc is traced for PID 4840, a MySQL database server. The allocation
requested size is recorded as a histogram keyed by user-level stack trace:
# bpftrace -e 'uprobe:/lib/x86_64-linux-gnu/libc.so.6:malloc /pid == 4840/ {
@[ustack] = hist(arg0); }'
Attaching 1 probe...
^C
[...]
__libc_malloc+0
Filesort_buffer::allocate_sized_block(unsigned long)+52
0x562cab572344
filesort(THD*, Filesort*, RowIterator*, Filesort_info*, Sort_result*, unsigned
long long*)+4017
SortingIterator::DoSort(QEP_TAB*)+184
SortingIterator::Init()+42
SELECT_LEX_UNIT::ExecuteIteratorQuery(THD*)+489
SELECT_LEX_UNIT::execute(THD*)+266
Sql_cmd_dml::execute_inner(THD*)+563
Sql_cmd_dml::execute(THD*)+1062
mysql_execute_command(THD*, bool)+2380
Prepared_statement::execute(String*, bool)+2345
Prepared_statement::execute_loop(String*, bool)+172
mysqld_stmt_execute(THD*, Prepared_statement*, bool, unsigned long, PS_PARAM*)
+385
dispatch_command(THD*, COM_DATA const*, enum_server_command)+5793
do_command(THD*)+420
0x562cab464fe0
0x562cacad873a
start_thread+217
]:
[32K, 64K)

676 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

[64K, 128K)

338 |@@@@@@@@@@@@@@@@@@@@@@@@@@

|

The output shows that, while tracing, this code path had 676 malloc() requests sized between 32
and 64 Kbytes, and 338 sized between 64 Kbytes and 128 Kbytes.

345

346

Chapter 7 Memory

malloc() Bytes Flame Graph
The output from the previous one-liner was many pages long, so is more easily understood as a
flame graph. One can be generated using the following steps:
# bpftrace -e 'u:/lib/x86_64-linux-gnu/libc.so.6:malloc /pid == 4840/ {
@[ustack] = hist(arg0); }' > out.stacks
$ git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
$ ./stackcollapse-bpftrace.pl < ../out.stacks | ./flamegraph.pl --hash \
--bgcolor=green --count=bytes --title="malloc() Bytes Flame Graph" > out.svg

WARNING: user-level allocation requests can be a frequent activity, occurring many millions
of times per second. While the instrumentation cost is small, when multiplied by a high rate, it
can lead to significant CPU overhead while tracing, slowing down the target by a factor of two
or more—use sparingly. Because it is low-cost, I first use CPU profiling of stack traces to get a
handle on allocation paths, or page fault tracing shown in the next section.

Page Fault Flame Graphs
Tracing page faults shows when a process grows in memory size. The previous malloc() one-liner
traced the allocation path. Page fault tracing was performed earlier in Section 7.5.10, perf, and
from it a flame graph was generated. An advantage of using bpftrace instead is that the stack
traces can be aggregated in kernel space for efficiency, and only the unique stacks and counts
written to user space.
The following commands use bpftrace to collect page fault stack traces and then generate a
flame graph from them:
# bpftrace -e 't:exceptions:page_fault_user { @[ustack, comm] = count(); }
' > out.stacks
$ git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
$ ./stackcollapse-bpftrace.pl < ../out.stacks | ./flamegraph.pl --hash \
--bgcolor=green --count=pages --title="Page Fault Flame Graph" > out.svg

See Section 7.5.10, perf, for an example page fault stack trace and flame graph.

Memory Internals
If needed, you can develop custom tools to explore memory allocation and internals in more
depth. Start by trying tracepoints for the kernel memory events, and USDT probes for library
allocators such as libc. Listing tracepoints:
# bpftrace -l 'tracepoint:kmem:*'
tracepoint:kmem:kmalloc
tracepoint:kmem:kmem_cache_alloc
tracepoint:kmem:kmalloc_node
tracepoint:kmem:kmem_cache_alloc_node
tracepoint:kmem:kfree

7.5 Observability Tools

tracepoint:kmem:kmem_cache_free
[...]
# bpftrace -l 't:*:mm_*'
tracepoint:huge_memory:mm_khugepaged_scan_pmd
tracepoint:huge_memory:mm_collapse_huge_page
tracepoint:huge_memory:mm_collapse_huge_page_isolate
tracepoint:huge_memory:mm_collapse_huge_page_swapin
tracepoint:migrate:mm_migrate_pages
tracepoint:compaction:mm_compaction_isolate_migratepages
tracepoint:compaction:mm_compaction_isolate_freepages
[...]

Each of these tracepoints have arguments that can be listed using -lv. On this kernel (5.3) there
are 12 kmem tracepoints, and 47 tracepoints beginning with “mm_”.
Listing USDT probes for libc on Ubuntu:
# bpftrace -l 'usdt:/lib/x86_64-linux-gnu/libc.so.6'
usdt:/lib/x86_64-linux-gnu/libc.so.6:libc:setjmp
usdt:/lib/x86_64-linux-gnu/libc.so.6:libc:longjmp
usdt:/lib/x86_64-linux-gnu/libc.so.6:libc:longjmp_target
usdt:/lib/x86_64-linux-gnu/libc.so.6:libc:lll_lock_wait_private
usdt:/lib/x86_64-linux-gnu/libc.so.6:libc:memory_mallopt_arena_max
usdt:/lib/x86_64-linux-gnu/libc.so.6:libc:memory_mallopt_arena_test
usdt:/lib/x86_64-linux-gnu/libc.so.6:libc:memory_tunable_tcache_max_bytes
[...]

For this libc version (6) there are 33 USDT probes.
If the tracepoints and USDT probes are insufficient, consider using dynamic instrumentation
with kprobes and uprobes.
There is also the watchpoint probe type for memory watchpoints: events when a specified memory address is read, written, or executed.
Since memory events can be very frequent, instrumenting them can consume significant overhead. malloc(3) functions from user space can be called millions of times per second, and with
the current uprobes overhead (see Chapter 4, Observability Tools, Section 4.3.7, uprobes), tracing
them can slow a target two-fold or more. Use caution and find ways to reduce this overhead,
such as using maps to summarize statistics instead of printing per-event details, and tracing the
fewest possible events.

7.5.14

Other Tools

Cross-chapter memory-related observability utilities appear as Table 7.6 in the book (**table omitted here — cross-reference catalog**).

Other Linux memory observability tools and sources include the following:
■

dmesg: Check for “Out of memory” messages from the OOM killer.

■

dmidecode: Shows BIOS information for memory banks.

■

tiptop: A version of top(1) that displays PMC statistics by process.

■

■

valgrind: A performance analysis suite, including memcheck, a wrapper for user-level
allocators for memory usage analysis including leak detection. This costs significant
overhead; the manual advises that it can cause the target to run 20 to 30 times slower
[Valgrind 20].
iostat: If the swap device is a physical disk or slice, device I/O may be observable using
iostat(1), which indicates that the system is paging.

■

/proc/zoneinfo: Statistics for memory zones (DMA, etc.).

■

/proc/buddyinfo: Statistics for the kernel buddy allocator for pages.

■

/proc/pagetypeinfo: Kernel free memory page statistics; can be used to help debug issues
of kernel memory fragmentation.

■

/sys/devices/system/node/node*/numastat: Statistics for NUMA nodes.

■

SysRq m: Magic SysRq has an “m” key to dump memory info to the console.

7.5 Observability Tools

Here is an example output from dmidecode(8), showing a bank of memory:
# dmidecode
[...]
Memory Device
Array Handle: 0x0003
Error Information Handle: Not Provided
Total Width: 64 bits
Data Width: 64 bits
Size: 8192 MB
Form Factor: SODIMM
Set: None
Locator: ChannelA-DIMM0
Bank Locator: BANK 0
Type: DDR4
Type Detail: Synchronous Unbuffered (Unregistered)
Speed: 2400 MT/s
Manufacturer: Micron
Serial Number: 00000000
Asset Tag: None
Part Number: 4ATS1G64HZ-2G3A1
Rank: 1
Configured Clock Speed: 2400 MT/s
Minimum Voltage: Unknown
Maximum Voltage: Unknown
Configured Voltage: 1.2 V
[...]

This output is useful information for static performance tuning (e.g., it shows the type is DDR4
and not DDR5). Unfortunately, this information is typically unavailable to cloud guests.
Here is some sample output from the SysRq “m” trigger:
# echo m > /proc/sysrq-trigger
# dmesg
[...]
[334849.389256] sysrq: Show Memory
[334849.391021] Mem-Info:
[334849.391025] active_anon:110405 inactive_anon:24 isolated_anon:0
active_file:152629 inactive_file:137395 isolated_file:0
unevictable:4572 dirty:311 writeback:0 unstable:0
slab_reclaimable:31943 slab_unreclaimable:14385
mapped:37490 shmem:186 pagetables:958 bounce:0
free:37403 free_pcp:478 free_cma:2289

349

350

Chapter 7 Memory

[334849.391028] Node 0 active_anon:441620kB inactive_anon:96kB active_file:610516kB
inactive_file:549580kB unevictable:18288kB isolated(anon):0kB isolated(file):0kB
mapped:149960kB dirty:1244kB writeback:0kB shmem:744kB shmem_thp: 0kB
shmem_pmdmapped: 0kB anon_thp: 2048kB writeback_tmp:0kB unstable:0kB
all_unreclaimable? no
[334849.391029] Node 0 DMA free:12192kB min:360kB low:448kB high:536kB ...
[...]

This can be useful if the system has locked up, as it may still be possible to request this information using the SysRq key sequence on the console keyboard, if available [Linux 20g].
Applications and virtual machines (e.g., the Java VM) may also provide their own memory
analysis tools. See Chapter 5, Applications.

