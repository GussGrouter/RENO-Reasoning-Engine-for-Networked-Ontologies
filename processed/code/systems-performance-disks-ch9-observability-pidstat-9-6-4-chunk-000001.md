9.6.4

pidstat

The Linux pidstat(1) tool prints CPU usage by default and includes a -d option for disk I/O statistics. This is available on kernels 2.6.20 and later. For example:
$ pidstat -d 1
Linux 5.3.0-1010-aws (ip-10-0-239-218)

02/13/20

_x86_64_

(2 CPU)

kB_wr/s kB_ccwr/s iodelay

Command

09:47:41

UID

PID

kB_rd/s

09:47:42

0

2705

32468.00

0.00

0.00

5

tar

09:47:42

0

2706

0.00

8192.00

0.00

0

gzip

09:47:56

UID

PID

kB_rd/s

09:47:57

0

229

0.00

72.00

0.00

0

systemd-journal

09:47:57

0

380

0.00

4.00

0.00

0

auditd

09:47:57
0
u4:1-flush-259:0

2699

4.00

0.00

0.00

10

kworker/

09:47:57

0

2705

15104.00

0.00

0.00

0

tar

09:47:57

0

2706

0.00

6912.00

0.00

0

gzip

[...]
kB_wr/s kB_ccwr/s iodelay

Command

9.6 Observability Tools

Columns include:
■

kB_rd/s: Kilobytes read per second

■

kB_wd/s: Kilobytes issued for write per second

■

■

kB_ccwr/s: Kilobytes canceled for write per second (e.g., overwritten or deleted
before flush)
iodelay: The time the process was blocked on disk I/O (clock ticks), including swapping

The workload seen in the output was a tar command reading the file system to a pipe, and
gzip reading the pipe and writing a compressed archive file. The tar reads caused iodelay
(5 clock ticks), whereas the gzip writes did not, due to write-back caching in the page cache.
Some time later the page cache was flushed, as can be seen in the second interval output by the
kworker/u4:1-flush-259:0 process, which experienced iodelay.
iodelay is a recent addition and shows the magnitude of performance issues: how much the
application waited. The other columns show the workload applied.
Note that only superusers (root) can access disk statistics for processes that they do not own.
These are read via /proc/PID/io.

