9.6.7

biosnoop

biosnoop(8)12 is a BCC and bpftrace tool that prints a one-line summary for each disk I/O. For
example:
# biosnoop
TIME(s)

COMM

T

SECTOR

BYTES

LAT(ms)

0.009165000

jbd2/nvme0n1p1 174

PID

nvme0n1 W

2116272

8192

0.43

0.009612000

jbd2/nvme0n1p1 174

nvme0n1 W

2116288

4096

0.39

0.011836000

mysqld

1948

nvme0n1 W

10434672

4096

0.45

0.012363000

jbd2/nvme0n1p1 174

nvme0n1 W

2116296

8192

0.49

0.012844000

jbd2/nvme0n1p1 174

nvme0n1 W

2116312

4096

0.43

0.016809000

mysqld

1948

nvme0n1 W

10227712

262144

1.82

0.017184000

mysqld

1948

nvme0n1 W

10228224

262144

2.19

0.017679000

mysqld

1948

nvme0n1 W

10228736

262144

2.68

0.018056000

mysqld

1948

nvme0n1 W

10229248

262144

3.05

0.018264000

mysqld

1948

nvme0n1 W

10229760

262144

3.25

0.018657000

mysqld

1948

nvme0n1 W

10230272

262144

3.64

0.018954000

mysqld

1948

nvme0n1 W

10230784

262144

3.93

0.019053000

mysqld

1948

nvme0n1 W

10231296

131072

4.03

0.019731000

jbd2/nvme0n1p1 174

nvme0n1 W

2116320

8192

0.49

0.020243000

jbd2/nvme0n1p1 174

nvme0n1 W

2116336

4096

0.46

0.020593000

mysqld

nvme0n1 R

4495352

4096

0.26

1948

DISK

[...]

12
Origin: I created the BCC version on 16-Sep-2015, and the bpftrace version on 15-Nov-2017, based on an earlier
tool of mine from 2003. The full origin is described in [Gregg 19].

9.6 Observability Tools

This output shows a write workload to disk nvme0n1, mostly from mysqld, PID 174, with varying
I/O sizes. The columns are:
■

TIME(s): I/O completion time in seconds

■

COMM: Process name (if known by this tool)

■

PID: Process ID (if known by this tool)

■

DISK: Storage device name

■

T: Type: R == reads, W == writes

■

SECTOR: Address on disk in units of 512-byte sectors

■

BYTES: Size of the I/O request

■

LAT(ms): Duration of the I/O from device issue to device completion (disk request time)

Around the middle of the example output is a series of 262,144 byte writes, beginning with a
latency of 1.82 ms and increasing in latency for each subsequent I/O, ending with 4.03 ms. This
is a pattern I commonly see, and the likely reason can be calculated from another column in
the output: TIME(s). If you subtract the LAT(ms) column from the TIME(s) column, you have the
starting time of the I/O, and these started around the same time. This appears to be a group of
writes that were sent at the same time, queued on the device, and then completed in turn, with
increasing latency for each.
By careful examination of the start and end times, reordering on the device can also be identified.
Since the output can many thousands of lines, I have often used the R statistical software to plot
the output as a scatter plot, to help in identifying these patterns (see Section 9.7, Visualizations).

Outlier Analysis
Here is a method for finding and analyzing latency outliers using biosnoop(8).
1. Write the output to a file:
# biosnoop > out.biosnoop01.txt

2. Sort the output by the latency column, and print the last five entries (those with the highest latency):
# sort -n -k 8,8 out.biosnoop01.txt | tail -5
31.344175

logger

10994

nvme0n1 W 15218056

262144

30.92

31.344401

logger

10994

nvme0n1 W 15217544

262144

31.15

31.344757

logger

10994

nvme0n1 W 15219080

262144

31.49

31.345260

logger

10994

nvme0n1 W 15218568

262144

32.00

46.059274

logger

10994

nvme0n1 W 15198896

4096

64.86

3. Open the output in a text editor (e.g., vi(1) or vim(1)):
# vi out.biosnoop01.txt

471

472

Chapter 9 Disks

4. Work through the outliers from slowest to fastest, searching for the time in the first column.
The slowest was 64.86 milliseconds, with the completion time of 46.059274 (seconds).
Searching for 46.059274:
[...]
45.992419

jbd2/nvme0n1p1 174

nvme0n1 W 2107232

8192

45.992988

jbd2/nvme0n1p1 174

nvme0n1 W 2107248

4096

0.50

46.059274

logger

nvme0n1 W 15198896

4096

64.86

10994

0.45

[...]

5. Look at events that occurred prior to the outlier, to see whether they had similar latency
and therefore this was the result of queueing (similar to the 1.82 to 4.03 ms ramp seen in
the first biosnoop(8) example output), or for any other clues. That’s not the case here: the
previous event was around 6 ms earlier, with a latency of 0.5 ms. The device may have
reordered events and completed the others first. If the previous completion event was
around 64 ms ago, then the gap in completions from the device may be explained by other
factors: e.g., this system is a VM instance, and can be de-scheduled by the hyper visor
during I/O, adding that time to the I/O time.

Queued Time
A -Q option to BCC biosnoop(8) can be used to show the time spent between the creation of the
I/O and the issue to the device (previously called the block I/O wait time or OS wait time). This time
is mostly spent on OS queues, but could also include memory allocation and lock acquisition.
For example:
# biosnoop -Q
TIME(s)

COMM

PID

DISK

T SECTOR

BYTES

0.000000

kworker/u4:0

9491

nvme0n1 W 5726504

4096

QUE(ms) LAT(ms)
0.06

0.60

0.000039

kworker/u4:0

9491

nvme0n1 W 8128536

4096

0.05

0.64

0.000084

kworker/u4:0

9491

nvme0n1 W 8128584

4096

0.05

0.68

0.000138

kworker/u4:0

9491

nvme0n1 W 8128632

4096

0.05

0.74

0.000231

kworker/u4:0

9491

nvme0n1 W 8128664

4096

0.05

0.83

[...]

The queued time is shown in the QUE(ms) column.

9.6.8
