<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->

13050

0 /usr/lib/sysstat/sadc -F -L -S DISK 1 1 -S XALL

[...]

I ran this on my database system in case it would find anything interesting, and it did: the first
two lines show that a read/write microbenchmark was still running, launching oltp_read_write
commands in a loop—I had accidentally left this running for days! Since the database is handling a different workload, it wasn’t obvious from other system metrics that showed CPU and
disk load. The lines after oltp_read_write show sar(1) collecting system metrics.
execsnoop(8) works by tracing the execve(2) system call, and prints a one-line summary for
each. The tool supports some options, including -t for timestamps.
Chapter 1 shows another example of execsnoop(8). I have also published a threadsnoop(8) tool
for bpftrace to trace the creation of threads via libpthread pthread_create().

5.5.6 syscount
syscount(8)15 is a BCC and bpftrace tool to count system calls system-wide.
Example output from the BCC version:
# syscount
Tracing syscalls, printing top 10... Ctrl+C to quit.
^C[05:01:28]
SYSCALL

COUNT

recvfrom

114746

sendto

57395

ppoll

28654

futex

953

io_getevents

55

bpf

33

15
Origin: I first created this using Ftrace and perf(1) for the perf-tools collection on 07-Jul-2014, and Sasha
Goldshtein developed the BCC version on 15-Feb-2017.


5.5 Observability Tools

rt_sigprocmask

12

epoll_wait

11

select

7

nanosleep

6

Detaching...

This shows the most frequent syscall was recvfrom(2), which was called 114,746 times while
tracing. You can explore further using other tracing tools to examine the syscall arguments,
latency, and calling stack trace. For example, you can use perf(1) trace with a -e recvfrom filter,
or use bpftrace to instrument the syscalls:sys_enter_recvfrom tracepoint. See the tracers in
Chapters 13 to 15.
syscount(8) can also count by process using -P:
# syscount -P
Tracing syscalls, printing top 10... Ctrl+C to quit.
^C[05:03:49]
PID

COMM

COUNT

10106

mysqld

155463

13202

oltp_read_only.

61779

9618

sshd

36

344

multipathd
