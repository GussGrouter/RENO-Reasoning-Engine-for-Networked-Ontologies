9.6.9

biostacks

biostacks(8)14 is a bpftrace tool that traces the block I/O request time (from OS enqueue to device
completion) with the I/O initialization stack trace. For example:
# biostacks.bt
Attaching 5 probes...
Tracing block I/O with init stacks. Hit Ctrl-C to end.
^C
[...]

14

Origin: I created it on 19-Mar-2019 for [Gregg 19].

9.6 Observability Tools

@usecs[
blk_account_io_start+1
blk_mq_make_request+1069
generic_make_request+292
submit_bio+115
submit_bh_wbc+384
ll_rw_block+173
ext4_bread+102
__ext4_read_dirblock+52
ext4_dx_find_entry+145
ext4_find_entry+365
ext4_lookup+129
lookup_slow+171
walk_component+451
path_lookupat+132
filename_lookup+182
user_path_at_empty+54
sys_access+175
do_syscall_64+115
entry_SYSCALL_64_after_hwframe+61
]:
[2K, 4K)

2 |@@

[4K, 8K)

37 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

|

[8K, 16K)

15 |@@@@@@@@@@@@@@@@@@@@@

|

[16K, 32K)

9 |@@@@@@@@@@@@

|

[32K, 64K)

1 |@

|

The output shows a latency histogram (in microseconds) for disk I/O, along with the requesting
I/O stack: via the access(2) syscall, filename_lookup(), and ext4_lookup(). This I/O was caused
by looking up pathnames during file permission checks. The output included many such stacks,
and these show that I/O are caused by activity other than reads and writes.
I have seen cases where there was mysterious disk I/O without any application causing it. The
reason turned out to be background file system tasks. (In one case it was ZFS’s background scrubber, which periodically verifies checksums.) biostacks(8) can identify the real reason for disk I/O
by showing the kernel stack trace.

