# Systems Performance — Section 4.3.3 Delay accounting (delay-accounting-4-3-3)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch4-scout-p171-220.txt
- PDF pages (approx): 171–220

---

4.3.3 Delay Accounting
Linux systems with the CONFIG_TASK_DELAY_ACCT option track time per task in the following
states:
■

Scheduler latency: Waiting for a turn on-CPU

■

Block I/O: Waiting for a block I/O to complete

■

Swapping: Waiting for paging (memory pressure)

■

Memory reclaim: Waiting for the memory reclaim routine

Technically, the scheduler latency statistic is sourced from schedstats (mentioned earlier, in
/proc) but is exposed with the other delay accounting states. (It is in struct sched_info, not struct
task_delay_info.)
These statistics can be read by user-level tools using taskstats, which is a netlink-based interface
for fetching per-task and process statistics. In the kernel source there is:
■

Documentation/accounting/delay-accounting.txt: the documentation

■

tools/accounting/getdelays.c: an example consumer

The following is some output from getdelays.c:
$ ./getdelays -dp 17451
print delayacct stats ON
PID
CPU

17451
count

real total

virtual total

delay total

386

3452475144

31387115236

1253300657

IO

count

delay total

delay average

302

1535758266

SWAP

count

delay total

0

0

count

delay total

0

0

RECLAIM

delay average
3.247ms

5ms
delay average
0ms
delay average
0ms

Times are given in nanoseconds unless otherwise specified. This example was taken from a
heavily CPU-loaded system, and the process inspected was suffering scheduler latency.

