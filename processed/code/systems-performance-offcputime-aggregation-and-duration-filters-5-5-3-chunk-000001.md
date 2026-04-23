start_thread
-

mysqld (10106)
13

[...]

Only one stack trace is included in this output, showing that SELECT_LEX::prepare() was sampled on-CPU with that ancestry 13 times.
profile(8) is further discussed in Chapter 6, CPUs, Section 6.6.14, profile, which lists its various
options and includes instructions for generating CPU flame graphs from its output.

5.5.3 offcputime
offcputime(8)12 is a BCC and bpftrace tool (Chapter 15) to summarize time spent by threads
blocked and off-CPU, showing stack traces to explain why. It supports Off-CPU analysis
(Section 5.4.2, Off-CPU Analysis). offcputime(8) is the counterpart to profile(8): between them,
they show the entire time spent by threads on the system.
The following shows offcputime(8) from BCC, tracing for 5 seconds:
# offcputime 5
Tracing off-CPU time (us) of all threads by user + kernel stack for 5 secs.
[...]
finish_task_switch
schedule
jbd2_log_wait_commit
jbd2_complete_transaction
ext4_sync_file
vfs_fsync_range
do_fsync
__x64_sys_fdatasync
do_syscall_64
entry_SYSCALL_64_after_hwframe
fdatasync
IO_CACHE_ostream::sync()
MYSQL_BIN_LOG::sync_binlog_file(bool)
MYSQL_BIN_LOG::ordered_commit(THD*, bool, bool)
MYSQL_BIN_LOG::commit(THD*, bool)
ha_commit_trans(THD*, bool, bool)
trans_commit(THD*, bool)
12
Origin: I created off-CPU analysis as a methodology, along with tools for performing it, in 2005; I developed this
offcputime(8) BCC tool on 13-Jan-2016.


5.5 Observability Tools

mysql_execute_command(THD*, bool)
Prepared_statement::execute(String*, bool)
Prepared_statement::execute_loop(String*, bool)
mysqld_stmt_execute(THD*, Prepared_statement*, bool, unsigned long, PS_PARAM*)
dispatch_command(THD*, COM_DATA const*, enum_server_command)
do_command(THD*)
[unknown]
[unknown]
start_thread
-

mysqld (10441)
352107

[...]

The output shows unique stack traces and their time spent off-CPU in microseconds. This
particular stack shows ext4 file system sync operations via a code path through MYSQL_BIN_
LOG::sync_binlog_file(), totaling 352 milliseconds during this trace.
For efficiency, offcputime(8) aggregates these stacks in kernel context, and emits only unique
stacks to user space. It also only records stack traces for off-CPU durations that exceed a threshold, one microsecond by default, which can be tuned using the -m option.
There is also a -M option to set the maximum time for recording stacks. Why would we want
to exclude long-duration stacks? This can be an effective way to filter out uninteresting stacks:
threads waiting for work and blocking for one or more seconds in a loop. Try using -M 900000, to
exclude durations longer than 900 ms.
