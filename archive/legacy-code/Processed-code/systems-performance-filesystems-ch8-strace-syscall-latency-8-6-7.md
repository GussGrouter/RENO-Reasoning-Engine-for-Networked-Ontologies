8.6.7

strace

File system latency can be measured at the syscall interface using tracing tools including strace(1)
for Linux. However, the current ptrace(2)-based implementation of strace(1) can severely hurt
performance and may be suitable for use only when the performance overhead is acceptable and
other methods to analyze latency are not possible. See Chapter 5, Section 5.5.4, strace, for more
on strace(1).

This example shows strace(1) timing reads on an ext4 file system:
$ strace -ttT -p 845
[...]
18:41:01.513110 read(9, ... 65536) = 65536 <0.018225>
18:41:01.531646 read(9, ... 65536) = 65536 <0.000056>
18:41:01.531984 read(9, ... 65536) = 65536 <0.005760>

The -tt option prints the relative timestamps on the left, and -T prints the syscall times on the
right. Each read(2) was for 64 Kbytes, the first taking 18 ms, followed by 56 μs (likely cached),
then 5 ms. The reads were to file descriptor 9. To check that this is to a file system (and isn’t a
socket), either the open(2) syscall will be visible in earlier strace(1) output, or another tool such
as lsof(8) can be used. You can also find information on FD 9 in the /proc file system: /proc/845/
fd{,info}/9.
Given the current overheads of strace(1), the measured latency can be skewed by observer effect.
See newer tracing tools, including ext4slower(8), which use per-CPU buffered tracing and BPF to
greatly reduce overhead, providing more accurate latency measurements.
