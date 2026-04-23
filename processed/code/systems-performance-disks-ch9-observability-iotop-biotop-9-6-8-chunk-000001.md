9.6.8

iotop, biotop

I wrote the first iotop in 2005 for Solaris-based systems [McDougall 06a]. There are now many
versions, including a Linux iotop(1) tool based on kernel accounting statistics13 [Chazarain 13],
and my own biotop(8) based on BPF.

13

iotop(1) requires CONFIG_TASK_DELAY_ACCT, CONFIG_TASK_IO_ACCOUNTING, CONFIG_TASKSTATS, and
CONFIG_VM_EVENT_COUNTERS.

9.6 Observability Tools

iotop
iotop can typically be installed via an iotop package. When run without arguments, it refreshes
the screen every second, showing the top disk I/O processes. Batch mode (-b) can be used to
provide a rolling output (no screen clear); it is demonstrated here with I/O processes only (-o)
and an interval of 5 s (-d5):
# iotop -bod5
Total DISK READ:
TID

PRIO

USER

22400 be/4 root
279 be/3 root

4.78 K/s | Total DISK WRITE:

15.04 M/s

DISK READ

DISK WRITE

IO

4.78 K/s

0.00 B/s

SWAPIN

COMMAND

0.00 % 13.76 % [flush-252:0]

0.00 B/s 1657.27 K/s

0.00 %

9.25 % [jbd2/vda2-8]

22446 be/4 root

0.00 B/s

0.00 %

0.00 % beam.smp -K true ...

Total DISK READ:

0.00 B/s | Total DISK WRITE:

TID

PRIO

USER

10.16 M/s

10.75 M/s

DISK READ

DISK WRITE

SWAPIN

279 be/3 root

0.00 B/s

9.55 M/s

0.00 %

0.01 % [jbd2/vda2-8]

IO

COMMAND

22446 be/4 root

0.00 B/s

10.37 M/s

0.00 %

0.00 % beam.smp -K true ...

646 be/4 root

0.00 B/s

272.71 B/s

0.00 %

0.00 % rsyslogd -n -c 5

[...]

The output shows the beam.smp process (Riak) performing a disk write workload of around 10
Mbytes/s. The columns include:
■

DISK READ: Read Kbytes/s

■

DISK WRITE: Write Kbytes/s

■

SWAPIN: Percent of time the thread spent waiting for swap-in I/O

■

IO: Percent of time the thread spent waiting for I/O

iotop(8) supports various other options, including -a for accumulated statistics (instead of
per-interval), -p PID to match a process, and -d SEC to set the interval.
I recommend that you test iotop(8) with a known workload and check that the numbers match.
I just tried (iotop version 0.6) and found that it greatly undercounts write workloads. You can also
use biotop(8), which uses a different instrumentation source and does match my test workload.

biotop
biotop(8) is a BCC tool, and is another top(1) for disks. Example output:
# biotop
Tracing... Output every 1 secs. Hit Ctrl-C to end
08:04:11 loadavg: 1.48 0.87 0.45 1/287 14547
PID

COMM

D MAJ MIN DISK

I/O

Kbytes

AVGms

14501

cksum

R 202 1

361

28832

3.39

xvda1

473

474

Chapter 9 Disks

6961

dd

R 202 1

xvda1

1628

13024

0.59

13855

dd

R 202 1

xvda1

1627

13016

0.59

326

jbd2/xvda1-8

W 202 1

xvda1

3

168

3.00

1880

supervise

W 202 1

xvda1

2

8

6.71

1873

supervise

W 202 1

xvda1

2

8

2.51

1871

supervise

W 202 1

xvda1

2

8

1.57

1876

supervise

W 202 1

xvda1

2

8

1.22

[...]

This shows cksum(1) and dd(1) commands performing reads, and supervise processes performing
some writes. This is a quick way to identify who is performing disk I/O, and by how much. The
columns are:
■

PID: Cached process ID (best effort)

■

COMM: Cached process name (best effort)

■

D: Direction (R == read, W == write)

■

MAJ MIN: Disk major and minor numbers (a kernel identifier)

■

DISK: Disk name

■

I/O: Number of disk I/O during interval

■

Kbytes: Total disk throughput during interval (Kbytes)

■

AVGms: Average time for the I/O (latency) from the issue to the device, to its completion
(milliseconds)

By the time disk I/O is issued to the device, the requesting process may no longer be on CPU, and
identifying it can be difficult. biotop(8) uses a best-effort approach: the PID and COMM columns
will usually match the correct process, but this is not guaranteed.
biotop(8) supports optional interval and count columns (the default interval is one second), -C
to not clear the screen, and -r MAXROWS to specify the top number of processes to display.

