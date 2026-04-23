9.6.2 sar
The system activity reporter, sar(1), can be used to observe current activity and can be configured to archive and report historical statistics. It is introduced in Section 4.4, sar, and mentioned
in various other chapters in this book for the different statistics it provides.
The sar(1) disk summary is printed using the -d option, demonstrated in the following examples
with an interval of one second. The output is wide, so it is included here in two parts (sysstat
12.3.2):
$ sar -d 1
Linux 5.3.0-1010-aws (ip-10-0-239-218)

02/13/20

_x86_64_

(2 CPU)

09:10:22

DEV

tps

rkB/s

wkB/s

dkB/s

areq-sz \ ...

09:10:23

dev259-0

1509.00

11100.00

12776.00

0.00

15.82 / ...

[...]

Here are the remaining columns:
$ sar -d 1
09:10:22

\ ... \

aqu-sz

await

%util

09:10:23

/ ... /

0.02

0.60

94.00

[...]

These columns also appear in iostat(1) -x output, and were described in the previous section.
This output shows a mixed read/write workload with an await of 0.6 ms, driving the disk to 94%
utilization.

463

464

Chapter 9 Disks

Previous versions of sar(1) included a svctm (service time) column: the average (inferred) disk
response time, in milliseconds. See Section 9.3.1, Measuring Time, for background on service
time. Since its simplistic calculation was no longer accurate for modern disks that perform I/O in
parallel, svctm has been removed in later versions.

