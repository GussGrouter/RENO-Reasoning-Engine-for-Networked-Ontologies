9.6.5

perf

The Linux perf(1) tool (Chapter 13) can record block tracepoints. Listing them:
# perf list 'block:*'
List of pre-defined events (to be used in -e):
block:block_bio_backmerge

[Tracepoint event]

block:block_bio_bounce

[Tracepoint event]

block:block_bio_complete

[Tracepoint event]

block:block_bio_frontmerge

[Tracepoint event]

block:block_bio_queue

[Tracepoint event]

block:block_bio_remap

[Tracepoint event]

block:block_dirty_buffer

[Tracepoint event]

block:block_getrq

[Tracepoint event]

block:block_plug

[Tracepoint event]

block:block_rq_complete

[Tracepoint event]

block:block_rq_insert

[Tracepoint event]

block:block_rq_issue

[Tracepoint event]

block:block_rq_remap

[Tracepoint event]

block:block_rq_requeue

[Tracepoint event]

block:block_sleeprq

[Tracepoint event]

block:block_split

[Tracepoint event]

block:block_touch_buffer

[Tracepoint event]

block:block_unplug

[Tracepoint event]

465

466

Chapter 9 Disks

For example, the following records block device issues with stack traces. A sleep 10 command is
provided as the duration of tracing.
# perf record -e block:block_rq_issue -a -g sleep 10
[ perf record: Woken up 22 times to write data ]
[ perf record: Captured and wrote 5.701 MB perf.data (19267 samples) ]
# perf script --header
[...]
mysqld 1965 [001] 160501.158573: block:block_rq_issue: 259,0 WS 12288 () 10329704 +
24 [mysqld]
ffffffffb12d5040 blk_mq_start_request+0xa0 ([kernel.kallsyms])
ffffffffb12d5040 blk_mq_start_request+0xa0 ([kernel.kallsyms])
ffffffffb1532b4c nvme_queue_rq+0x16c ([kernel.kallsyms])
ffffffffb12d7b46 __blk_mq_try_issue_directly+0x116 ([kernel.kallsyms])
ffffffffb12d87bb blk_mq_request_issue_directly+0x4b ([kernel.kallsyms])
ffffffffb12d8896 blk_mq_try_issue_list_directly+0x46 ([kernel.kallsyms])
ffffffffb12dce7e blk_mq_sched_insert_requests+0xae ([kernel.kallsyms])
ffffffffb12d86c8 blk_mq_flush_plug_list+0x1e8 ([kernel.kallsyms])
ffffffffb12cd623 blk_flush_plug_list+0xe3 ([kernel.kallsyms])
ffffffffb12cd676 blk_finish_plug+0x26 ([kernel.kallsyms])
ffffffffb119771c ext4_writepages+0x77c ([kernel.kallsyms])
ffffffffb10209c3 do_writepages+0x43 ([kernel.kallsyms])
ffffffffb1017ed5 __filemap_fdatawrite_range+0xd5 ([kernel.kallsyms])
ffffffffb10186ca file_write_and_wait_range+0x5a ([kernel.kallsyms])
ffffffffb118637f ext4_sync_file+0x8f ([kernel.kallsyms])
ffffffffb1105869 vfs_fsync_range+0x49 ([kernel.kallsyms])
ffffffffb11058fd do_fsync+0x3d ([kernel.kallsyms])
ffffffffb1105944 __x64_sys_fsync+0x14 ([kernel.kallsyms])
ffffffffb0e044ca do_syscall_64+0x5a ([kernel.kallsyms])
ffffffffb1a0008c entry_SYSCALL_64_after_hwframe+0x44 ([kernel.kallsyms])
7f2285d1988b fsync+0x3b (/usr/lib/x86_64-linux-gnu/libpthread-2.30.so)
55ac10a05ebe Fil_shard::redo_space_flush+0x44e (/usr/sbin/mysqld)
55ac10a06179 Fil_shard::flush_file_redo+0x99 (/usr/sbin/mysqld)
55ac1076ff1c [unknown] (/usr/sbin/mysqld)
55ac10777030 log_flusher+0x520 (/usr/sbin/mysqld)
55ac10748d61
std::thread::_State_impl<std::thread::_Invoker<std::tuple<Runnable, void (*)(log_t*),
log_t*> > >::_M_run+0xc1 (/usr/sbin/mysql
7f228559df74 [unknown] (/usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.28)
7f226c3652c0 [unknown] ([unknown])
55ac107499f0
std::thread::_State_impl<std::thread::_Invoker<std::tuple<Runnable, void (*)(log_t*),
log_t*> > >::~_State_impl+0x0 (/usr/sbin/
5441554156415741 [unknown] ([unknown])
[...]

9.6 Observability Tools

The output is a one-line summary for each event, followed by the stack trace that led to it. The
one-line summary begins with default fields from perf(1): the process name, thread ID, CPU
ID, timestamp, and event name (see Chapter 13, perf, Section 13.11, perf script). The remaining
fields are specific to the tracepoint: for this block:block_rq_issue tracepoint, they are, along with
the field contents:
■

Disk major and minor numbers: 259,0

■

I/O type: WS (synchronous writes)

■

I/O size: 12288 (bytes)

■

I/O command string: ()

■

Sector address: 10329704

■

Number of sectors: 24

■

Process: mysqld

These fields are from the format string of the tracepoint (see Chapter 4, Observability Tools,
Section 4.3.5, Tracepoints, under Tracepoints Arguments and Format String).
The stack trace can help explain the nature of the disk I/O. In this case, it is from the mysqld
log_flusher() routine that called fsync(2). The kernel code path shows it was handled by the ext4
file system, and became a disk I/O issue via blk_mq_try_issue_list_directly().
Often I/O will be queued and then issued later by a kernel thread, and tracing the block:block_
rq_issue tracepoint will not show the originating process or user-level stack trace. In those cases
you can try tracing block:block_rq_insert instead, which is for queue insertion. Note that it
misses I/O that did not queue.

One-Liners
The following one-liners demonstrate using filters with the block tracepoints.
Trace all block completions, of size at least 100 Kbytes, until Ctrl-C10:
perf record -e block:block_rq_complete --filter 'nr_sector > 200'

Trace all block completions, synchronous writes only, until Ctrl-C:
perf record -e block:block_rq_complete --filter 'rwbs == "WS"

Trace all block completions, all types of writes, until Ctrl-C:
perf record -e block:block_rq_complete --filter 'rwbs ~ "*W*"'

Disk I/O Latency
Disk I/O latency (described earlier as disk request time) can also be determined by recording both
the disk issue and completion events for later analysis. The following records them for 60 seconds then writes the events to a out.disk01.txt file:

10

With a sector size of 512 bytes, 100 Kbytes means 200 sectors.

467

468

Chapter 9 Disks

perf record -e block:block_rq_issue,block:block_rq_complete -a sleep 60
perf script --header > out.disk01.txt

You can post-process the output file using whatever is convenient: awk(1), Perl, Python, R,
Google Spreadsheets, etc. Associate issues with completions and use the recorded timestamps to
calculate the latency.
The following tools, biolatency(8) and biosnoop(8), calculate disk I/O latency efficiently in kernel
space using a BPF program, and include the latency directly in the output.

