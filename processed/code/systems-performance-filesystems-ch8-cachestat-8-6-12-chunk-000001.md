8.6.12

cachestat

cachestat(8) is a BCC tool that shows page cache hit and miss statistics. This can be used to
check the hit ratio and efficiency of the page cache, and run while investigating system and
application tuning for feedback on cache performance.

(Omitted in this processed extract: numeric time series grid — see PDF.)

This output shows a read workload that is entirely cached (HITS with a 100% HITRATIO) and a
higher write workload (DIRTIES). Ideally, the hit ratio is close to 100% so that application reads
are not blocking on disk I/O.
If you encounter a low hit ratio that may be hurting performance, you may be able to tune the
application’s memory size to be a little smaller, leaving more room for the page cache. If swap
devices are configured, there is also the swappiness tunable to prefer evicting from the page
cache versus swapping.
Options include -T to print a timestamp.
While this tool provides crucial insight for the page cache hit ratio, it is also an experimental
tool that uses kprobes to trace certain kernel functions, so it will need maintenance to work on
different kernel versions. Even better, if tracepoints or /proc statistics are added, this tool can be
rewritten to use them and become stable. Its best use today may be simply to show that such a
tool is possible.
