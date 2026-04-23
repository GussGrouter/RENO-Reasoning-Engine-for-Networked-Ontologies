Analyze
The blktrace package includes btt(1) to analyze I/O traces. Here is an example invocation, now
using blktrace(8) on /dev/nvme0n1p1 to write trace files (a new directory is used since these
commands create several files):
# mkdir tracefiles; cd tracefiles
# blktrace -d /dev/nvme0n1p1 -o out -w 10
=== nvme0n1p1 ===
CPU

0:

20135 events,

944 KiB data

CPU

1:

38272 events,

1795 KiB data

Total:

58407 events (dropped 0),

2738 KiB data

# blkparse -i out.blktrace.* -d out.bin
259,0

1

1

0.000000000

7113

A

RM 161888 + 8 <- (259,1) 159840

259,0

1

1

0.000000000

7113

A

RM 161888 + 8 <- (259,1) 159840

[...]
# btt -i out.bin
==================== All Devices ====================
ALL

MIN

AVG

MAX

N

--------------- ------------- ------------- ------------- ----------Q2Q

0.000000001

0.000365336

2.186239507

Q2A

0.000037519

0.000476609

0.001628905

24625
1442

Q2G

0.000000247

0.000007117

0.006140020

15914

G2I

0.000001949

0.000027449

0.000081146

602

Q2M

0.000000139

0.000000198

0.000021066

8720

I2D

0.000002292

0.000008148

0.000030147

602

M2D

0.000001333

0.000188409

0.008407029

8720

9.6 Observability Tools

D2C

0.000195685

0.000885833

0.006083538

12308

Q2C

0.000198056

0.000964784

0.009578213

12308

[...]

These statistics are in units of seconds, and show times for each stage of I/O processing.
Interesting times include:
■

Q2C: The total time from the I/O request to completion (time in block layer)

■

D2C: The device issue to completion (disk I/O latency)

■

I2D: The time from device queue insertion to device issue (request queue time)

■

M2D: The time from I/O merge to issue

The output shows an average D2C time of 0.86 ms, and a max M2D of 8.4 ms. Maximums such
as these can cause I/O latency outliers.
For more information, see the btt User Guide [Brunelle 08].

Visualizations
The blktrace(8) tool can record events to trace files that can be visualized using iowatcher(1),
also provided in the blktrace package, and also visualized using Chris Mason’s seekwatcher
[Mason 08].

