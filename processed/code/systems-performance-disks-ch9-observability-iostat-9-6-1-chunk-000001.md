9.6.1

iostat

iostat(1) summarizes per-disk I/O statistics, providing metrics for workload characterization, utilization, and saturation. It can be executed by any user and is typically the first command used
to investigate disk I/O issues at the command line. The statistics it provides are also typically
shown by monitoring software, so it can be worthwhile to learn iostat(1) in detail to deepen your
understanding of monitoring statistics. These statistics are enabled by default by the kernel,9 so
the overhead of this tool is considered negligible.
The name “iostat” is short for “I/O statistics,” although it might have been better to call it
“diskiostat” to reflect the type of I/O it reports. This has led to occasional confusion when a user
knows that an application is performing I/O (to the file system) but wonders why it can’t be seen
via iostat(1) (the disks).
iostat(1) was written in the early 1980s for Unix, and different versions are available on the
different operating systems. It can be added to Linux-based systems via the sysstat package.
The following describes the Linux version.

iostat Default Output
Without any arguments or options, a summary-since-boot for CPU and disk statistics is printed.
It’s covered here as an introduction to this tool; however, you are not expected to use this mode,
as the extended mode covered later is more useful.
$ iostat
Linux 5.3.0-1010-aws (ip-10-1-239-218)

02/12/20

_x86_64_

avg-cpu:

%steal

%idle

0.21

99.28

(2 CPU)

%user

%nice %system %iowait

0.29

0.01

0.18

Device

tps

kB_read/s

kB_wrtn/s

kB_read

kB_wrtn

loop0

0.00

0.05

0.00

1232

0

3.40

17.11

36.03

409902

863344

0.03

[...]
nvme0n1

The first output line is a summary of the system, including the kernel version, host name, date,
architecture, and CPU count. Subsequent lines show summary-since-boot statistics for the CPUs
(avg-cpu; these statistics were covered in Chapter 6, CPUs) and disk devices (under Device:).
9

Statistics can be disabled via the /sys/block/<dev>/queue/iostats file. I don’t know of anyone ever doing so.

459

460

Chapter 9 Disks

Each disk device is shown as a row, with basic details in the columns. I’ve highlighted the column headers in bold; they are:
■

tps: Transactions per second (IOPS)

■

kB_read/s, kB_wrtn/s: Kilobytes read per second, and written per second

■

kB_read, kB_wrtn: Total kilobytes read and written

Some SCSI devices, including CD-ROMs, may not be shown by iostat(1). SCSI tape drives can be
examined using tapestat(1) instead, also in the sysstat package. Also note that, while iostat(1)
reports block device reads and writes, it may exclude some other types of disk device commands
depending on the kernel (see the logic in the kernel function blk_do_io_stat()). The iostat(1)
extended mode includes extra fields for these device commands.

iostat Options
iostat(1) can be executed with various options, followed by an optional interval and count. For
example:
# iostat 1 10

will print one-second summaries ten times. And:
# iostat 1

will print one-second summaries without end (until Ctrl-C is typed).
Commonly used options are:
■

-c: Display CPU report

■

-d: Display disk report

■

-k: Use kilobytes instead of (512-byte) blocks

■

-m: Use megabytes instead of (512-byte) blocks

■

-p: Include per-partition statistics

■

-t: Timestamp output

■

-x: Extended statistics

■

-s: Short (narrow) output

■

-z: Skip displaying zero-activity summaries

There is also an environment variable, POSIXLY_CORRECT=1, to output blocks (512 bytes each)
instead of Kbytes. Some older versions included an option for NFS statistics, -n. Since sysstat
version 9.1.3, this was moved to the separate nfsiostat command.

iostat Extended Short Output
Extended output (-x) provides extra columns that are useful for the methodologies covered earlier. These extra columns include IOPS and throughput metrics for workload characterization,

9.6 Observability Tools

utilization and queue lengths for the USE method, and disk response times for performance
characterization and latency analysis.
Over the years, the extended output has gained more and more fields, and the latest release
(12.3.1, Dec. 2019) produces output that is 197 characters wide. This not only does not fit in this
book, it does not fit in many wide terminals either, making the output difficult to read due to
line wraps. A solution was added in 2017, the -s option, to provide a “short” or narrow output
that is intended to fit within an 80-character width.
Here is an example of short (-s) extended (-x) statistics, and skipping zero-activity devices (-z):
$ iostat -sxz 1
[...]
avg-cpu:

%user

%nice %system %iowait

15.82

0.00

10.71

%steal

%idle

1.53

40.31

31.63

Device

tps

kB/s

rqm/s

await aqu-sz

nvme0n1

1642.00

9064.00

664.00

0.44

0.00

areq-sz

%util

5.52 100.00

[...]

The disk columns are:
■

tps: Transactions issued per second (IOPS)

■

kB/s: Kbytes per second

■

rqm/s: Requests queued and merged per second

■

■

await: Average I/O response time, including time queued in the OS and the I/O response
time of the device (ms)
aqu-sz: Average number of requests both waiting in the driver request queue and active on
the device

■

areq-sz: Average request size in Kbytes

■

%util: Percent of time the device was busy processing I/O requests (utilization)

The most important metric for delivered performance is await, showing the average total wait
time for I/O. What constitutes “good” or “bad” depends on your needs. In the example output,
await was 0.44 ms, which is satisfactory for this database server. It can increase for a number of
reasons: queueing (load), larger I/O sizes, random I/O on rotational devices, and device errors.
For resource usage and capacity planning, %util is important, but bear in mind that it is only a
measure of busyness (non-idle time) and may mean little for virtual devices backed by multiple disks. Those devices may be better understood by the load applied: tps (IOPS) and kB/s
(throughput).
Nonzero counts in the rqm/s column show that contiguous requests were merged before delivery
to the device, to improve performance. This metric is also a sign of a sequential workload.
Since areq-sz is after merging, small sizes (8 Kbytes or less) are an indicator of a random I/O
workload that could not be merged. Large sizes may be either large I/O or a merged sequential
workload (indicated by earlier columns).

461

462

Chapter 9 Disks

iostat Extended Output
Without the -s option, -x prints many more columns. Here is the summary since boot (no interval or count) for sysstat version 12.3.2 (from Apr 2020):
$ iostat -x
[...]
Device
r/s
rkB/s
wrqm/s %wrqm w_await wareq-sz
f/s f_await aqu-sz %util
nvme0n1
0.92 22.91
0.00
0.00

0.23
0.89
0.00

rrqm/s
d/s

9.91
0.16
10.66
0.00
0.12

%rrqm r_await rareq-sz
w/s
wkB/s
dkB/s
drqm/s %drqm d_await dareq-sz
40.70
0.00

0.56
0.00

43.01
0.00

3.10
0.00

33.09
0.00

These break down many of the -sx metrics into read and write components, and also includes
discards and flushes.
The extra columns are:
■

■

■

■

■

r/s, w/s, d/s, f/s: Read, write, discard, and flush requests completed from the disk device
per second (after merges)
rkB/s, wkB/s, dkB/s: Read, write, and discard Kbytes from the disk device per second
%rrqm/s, %wrqm/s, %drqm/s: Read, write, and discard requests queued and merged as a percentage of the total requests for that type
r_await, w_await, d_await, f_await: Read, write, discard, and flush average response time,
including time queued in the OS and the response time from the device (ms)
rareq-sz, wareq-sz, dareq-sz: Read, write, and discard average size (Kbytes)

Examining reads and writes separately is important. Applications and file systems commonly
use techniques to mitigate write latency (e.g., write-back caching), so the application is less likely
to be blocked on disk writes. This means that any metrics that group reads and writes are skewed
by a component that may not directly matter (the writes). By splitting them, you can start examining r_wait, which shows average read latency, and is likely to be the most important metric for
application performance.
The reads and writes as IOPS (r/s, w/s) and throughput (rkB/s, wkB/s) are important for workload
characterization.
The discard and flush statistics are new additions to iostat(1). Discard operations free up blocks
on the drive (the ATA TRIM command), and their statistics were added in the Linux 4.19 kernel.
Flush statistics were added in Linux 5.5. These can help to narrow down the reason for disk
latency.
Here is another useful iostat(1) combination:
$ iostat -dmstxz -p ALL 1
Linux 5.3.0-1010-aws (ip-10-1-239-218)

02/12/20

_x86_64_

(2 CPU)

9.6 Observability Tools

02/12/20 17:39:29
Device

tps

MB/s

rqm/s

await

areq-sz

aqu-sz

%util

nvme0n1

3.33

0.04

1.09

0.87

12.84

0.00

0.12

nvme0n1p1

3.31

0.04

1.09

0.87

12.91

0.00

0.12

02/12/20 17:39:30
Device

tps

MB/s

rqm/s

await

areq-sz

aqu-sz

%util

nvme0n1

1730.00

14.97

709.00

0.54

8.86

0.02

99.60

nvme0n1p1

1538.00

14.97

709.00

0.61

9.97

0.02

99.60

[...]

The first output is the summary since boot, followed by one-second intervals. The -d focuses on
disk statistics only (no CPU), -m for Mbytes, and -t for the timestamp, which can be useful when
comparing the output to other timestamped sources, and-p ALL includes per-partition statistics.
Unfortunately, the current version of iostat(1) does not include disk errors; otherwise all USE
method metrics could be checked from one tool!

