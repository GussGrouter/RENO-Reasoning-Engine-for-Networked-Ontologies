7.5.10

perf

perf(1) is the official Linux profiler, a multi-tool with many capabilities. Chapter 13 provides as
a summary of perf(1). This section covers its usage for memory analysis. Also see Chapter 6 for
perf(1) analysis of memory PMCs.

One-Liners
The following one-liners are both useful and demonstrate different perf(1) capabilities for memory analysis.
Sample page faults (RSS growth) with stack traces system wide, until Ctrl-C:
perf record -e page-faults -a -g

Record all page faults with stack traces for PID 1843, for 60 seconds:
perf record -e page-faults -c 1 -p 1843 -g -- sleep 60

Record heap growth via brk(2), until Ctrl-C:
perf record -e syscalls:sys_enter_brk -a -g

Record page migrations on NUMA systems:
perf record -e migrate:mm_migrate_pages -a

7.5 Observability Tools

Count all kmem events, printing a report every second:
perf stat -e 'kmem:*' -a -I 1000

Count all vmscan events, printing a report every second:
perf stat -e 'vmscan:*' -a -I 1000

Count all memory compaction events, printing a report every second:
perf stat -e 'compaction:*' -a -I 1000

Trace kswapd wakeup events with stack traces, until Ctrl-C:
perf record -e vmscan:mm_vmscan_wakeup_kswapd -ag

Profile memory accesses for the given command:
perf mem record command

Summarize a memory profile:
perf mem report

For commands that record or sample events, use perf report to summarize the profile or perf
script --header to print them all.
See Chapter 13, perf, Section 13.2, One-Liners, for more perf(1) one-liners, and Section 7.5.13,
bpftrace, which builds observability programs on many of the same events.

Page Fault Sampling
perf(1) can record the stack trace on page faults, showing the code path that triggered this event.
Since page faults occur as a process increases its resident set size (RSS), analyzing them can
explain why the main memory of a process is growing. See Figure 7.2 for the role of page faults
during memory usage.
In the following example, the page-fault software event is traced across all CPUs (-a9) with stack
traces (-g) for 60 seconds, and then the stacks are printed:
# perf record -e page-faults -a -g -- sleep 60
[ perf record: Woken up 4 times to write data ]
[ perf record: Captured and wrote 1.164 MB perf.data (2584 samples) ]
# perf script
[...]
sleep

4910 [001] 813638.716924:

1 page-faults:

ffffffff9303f31e __clear_user+0x1e ([kernel.kallsyms])
ffffffff9303f37b clear_user+0x2b ([kernel.kallsyms])

9

The -a option became the default in Linux 4.11.

339

340

Chapter 7 Memory

ffffffff92941683 load_elf_binary+0xf33 ([kernel.kallsyms])
ffffffff928d25cb search_binary_handler+0x8b ([kernel.kallsyms])
ffffffff928d38ae __do_execve_file.isra.0+0x4fe ([kernel.kallsyms])
ffffffff928d3e09 __x64_sys_execve+0x39 ([kernel.kallsyms])
ffffffff926044ca do_syscall_64+0x5a ([kernel.kallsyms])
ffffffff9320008c entry_SYSCALL_64_after_hwframe+0x44 ([kernel.kallsyms])
7fb53524401b execve+0xb (/usr/lib/x86_64-linux-gnu/libc-2.30.so)
[...]
mysqld

4918 [000] 813641.075298:

1 page-faults:

7fc6252d7001 [unknown] (/usr/lib/x86_64-linux-gnu/libc-2.30.so)
562cacaeb282 pfs_malloc_array+0x42 (/usr/sbin/mysqld)
562cacafd582 PFS_buffer_scalable_container<PFS_prepared_stmt, 1024, 1024,
PFS_buffer_default_array<PFS_prepared_stmt>,
PFS_buffer_default_allocator<PFS_prepared_stmt> >::allocate+0x262 (/usr/sbin/mysqld)
562cacafd820 create_prepared_stmt+0x50 (/usr/sbin/mysqld)
562cacadbbef [unknown] (/usr/sbin/mysqld)
562cab3719ff mysqld_stmt_prepare+0x9f (/usr/sbin/mysqld)
562cab3479c8 dispatch_command+0x16f8 (/usr/sbin/mysqld)
562cab348d74 do_command+0x1a4 (/usr/sbin/mysqld)
562cab464fe0 [unknown] (/usr/sbin/mysqld)
562cacad873a [unknown] (/usr/sbin/mysqld)
7fc625ceb669 start_thread+0xd9 (/usr/lib/x86_64-linux-gnu/libpthread2.30.so)
[...]

Only two stacks have been included here. The first is from the dummy sleep(1) command that
perf(1) invoked, and the second is a MySQL server. When tracing system-wide, you may see
many stacks from short-lived processes that briefly grew in memory, triggering page faults,
before exiting. You can use -p PID instead of -a to match on a process.
The full output is 222,582 lines; perf report summarizes code paths as a hierarchy, but the output is still 7,592 lines. Flame graphs can be used to visualize the entire profile more effectively.

Page Fault Flame Graphs
Figure 7.12 shows a page fault flame graph generated from the previous profile.
The Figure 7.12 flame graph shows that more than half of the memory growth in MySQL server
was from the JOIN::optimize() code path (left large tower). A mouse-over of JOIN::optimize()
shows that it and its child calls were responsible for 3,226 page faults; with 4 Kbyte pages, this
amounts to around 12 Mbytes of main memory growth.

7.5 Observability Tools

Figure 7.12 Page fault flame graph
The commands used to generate this flame graph, including the perf(1) command to record page
faults, are:
# perf record -e page-faults -a -g -- sleep 60
# perf script --header > out.stacks
$ git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
$ ./stackcollapse-perf.pl < ../out.stacks | ./flamegraph.pl --hash \
--bgcolor=green --count=pages --title="Page Fault Flame Graph" > out.svg

341

342

Chapter 7 Memory

I set the background color to green as a visual reminder that this is not a typical CPU flame
graph (yellow background) but is a memory flame graph (green background).

