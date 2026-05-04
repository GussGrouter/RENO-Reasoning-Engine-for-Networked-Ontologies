9.6.6 biolatency
biolatency(8)11 is a BCC and bpftrace tool to show disk I/O latency as a histogram. The term I/O
latency used here refers to the time from issuing a request to the device, to when it completes
(aka disk request time).
The following shows biolatency(8) from BCC tracing block I/O for 10 seconds:
# biolatency 10 1
Tracing block device I/O... Hit Ctrl-C to end.
usecs

: count

distribution

0 -> 1

: 0

|

|

2 -> 3

: 0

|

|

4 -> 7

: 0

|

|

8 -> 15

: 0

|

|

16 -> 31

: 2

|

|

32 -> 63

: 0

|

|

64 -> 127

: 0

|

|

128 -> 255

: 1065

|*****************

|

256 -> 511

: 2462

|****************************************|

512 -> 1023

: 1949

|*******************************

|

1024 -> 2047

: 373

|******

|

2048 -> 4095

: 1815

|*****************************

|

4096 -> 8191

: 591

|*********

|

8192 -> 16383

: 397

|******

|

16384 -> 32767

: 50

|

|

This output shows a bi-modal distribution, with one mode between 128 and 1023 microseconds,
and another between 2048 and 4095 microseconds (2.0 to 4.1 milliseconds.) Now that I know
that the device latency is bi-modal, understanding why may lead to tuning that moves more I/O
to the faster mode. For example, the slower I/O could be random I/O or larger-sized I/O (which

11

Origin: I created biolatency for BCC on 20-Sep-2015 and bpftrace on 13-Sep-2018, based on an earlier iolatency
tool I developed. I added the “b” to these tools to make it clear it refers to block I/O.

9.6 Observability Tools

can be determined using other BPF tools), or different I/O flags (shown using the -F option). The
slowest I/O in this output reached the 16- to 32-millisecond range: this sounds like queueing on
the device.
The BCC version of biolatency(8) supports options including:
■

-m: Output in milliseconds

■

-Q: Include OS queued I/O time (OS request time)

■

-F: Show a histogram for each I/O flag set

■

-D: Show a histogram for each disk device

Using -Q makes biolatency(8) report the full I/O time from creation and insertion on a kernel
queue to device completion, described earlier as the block I/O request time.
The BCC biolatency(8) also accepts optional interval and count arguments, in seconds.

Per-Flag
The -F option is especially useful, breaking down the distribution for each I/O flag. For example,
with -m for millisecond histograms:
# biolatency -Fm 10 1
Tracing block device I/O... Hit Ctrl-C to end.
flags = Sync-Write
msecs
0 -> 1

: count

distribution

: 2

|****************************************|

flags = Flush
msecs
0 -> 1

: count

distribution

: 1

|****************************************|

flags = Write
msecs

: count

distribution

0 -> 1

: 14

|****************************************|

2 -> 3

: 1

|**

|

4 -> 7

: 10

|****************************

|

8 -> 15

: 11

|*******************************

|

16 -> 31

: 11

|*******************************

|

flags = NoMerge-Write
msecs

: count

distribution

0 -> 1

: 95

|**********

|

2 -> 3

: 152

|*****************

|

4 -> 7

: 266

|******************************

|

8 -> 15

: 350

|****************************************|

16 -> 31

: 298

|**********************************

|

469

470

Chapter 9 Disks

flags = Read
msecs
0 -> 1

: count

distribution

: 11

|****************************************|

flags = ReadAhead-Read
msecs

: count

distribution

0 -> 1

: 5261

|****************************************|

2 -> 3

: 1238

|*********

|

4 -> 7

: 481

|***

|

8 -> 15

: 5

|

|

16 -> 31

: 2

|

|

These flags may be handled differently by the storage device; separating them allows us to
study them in isolation. The previous output shows that writes were slower than reads, and can
explain the earlier bi-modal distribution.
biolatency(8) summarizes disk I/O latency. To examine it for each I/O, use biosnoop(8).

