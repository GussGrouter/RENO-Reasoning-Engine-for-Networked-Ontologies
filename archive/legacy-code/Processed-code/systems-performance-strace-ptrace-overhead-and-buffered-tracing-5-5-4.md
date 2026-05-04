<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->

Off-CPU Time Flame Graphs
Despite only showing unique stacks, the full output from the previous example was still over
200,000 lines. To make sense of it, it can be visualized as an off-CPU time flame graph. An
example was shown in Figure 5.4. The commands to generate these are similar to those with
profile(8):
# git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
# offcputime -f 5 | ./flamegraph.pl --bgcolors=blue \
--title="Off-CPU Time Flame Graph"> out.svg

This time I’ve set the background color to blue, as a visual reminder that this is an off-CPU flame
graph rather than the commonly-used CPU flame graphs.

5.5.4 strace
The strace(1) command is the Linux system call tracer.13 It can trace syscalls, printing a one-line
summary for each, and can also count syscalls and print a report.
13
Syscall tracers for other operating systems are: BSD has ktrace(1), Solaris has truss(1), OS X has dtruss(1) (a tool
I originally developed), and Windows has a number of options including logger.exe and ProcMon.

205


206

Chapter 5 Applications

For example, tracing syscalls by PID 1884:
$ strace -ttt -T -p 1884
1356982510.395542 close(3)

= 0 <0.000267>

1356982510.396064 close(4)

= 0 <0.000293>

1356982510.396617 ioctl(255, TIOCGPGRP, [1975]) = 0 <0.000019>
1356982510.396980 rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0 <0.000024>
1356982510.397288 rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0 <0.000014>
1356982510.397365 wait4(-1, [{WIFEXITED(s) && WEXITSTATUS(s) == 0}], WSTOPPED|
WCONTINUED, NULL) = 1975 <0.018187>
[...]

The options in this invocation were (see the strace(1) man page for all):
■

■

■

-ttt: Prints the first column of time-since-epoch, in units of seconds with microsecond
resolution.
-T: Prints the last field (<time>), which is the duration of the system call, in units of seconds
with microsecond resolution.
-p PID: Trace this process ID. A command can also be specified so that strace(1) launches
and traces it.

Other options not used here include -f to follow child threads, and -o filename to write the
strace(1) output to the given file name.
A feature of strace(1) can be seen in the output—translation of syscall arguments into a
human-readable form. This is especially useful for understanding ioctl(2) calls.
The -c option can be used to summarize system call activity. The following example also
invokes and traces a command (dd(1)) rather than attaching to a PID:
$ strace -c dd if=/dev/zero of=/dev/null bs=1k count=5000k
5120000+0 records in
5120000+0 records out
5242880000 bytes (5.2 GB) copied, 140.722 s, 37.3 MB/s
% time

seconds

usecs/call

calls

errors syscall

------ ----------- ----------- --------- --------- ---------------51.46

0.008030

0

5120005

48.54

0.007574

0

5120003

read
write

0.00

0.000000

0

20

13 open

[...]
------ ----------- ----------- --------- --------- ---------------100.00

0.015604

10240092

19 total


5.5 Observability Tools

The output begins with three lines from dd(1) followed by the strace(1) summary. The columns are:
■

time: Percentage showing where system CPU time was spent

■

seconds: Total system CPU time, in seconds

■

usecs/call: Average system CPU time per call, in microseconds

■

calls: Number of system calls

■

syscall: System call name

strace Overhead
WARNING: The current version of strace(1) employs breakpoint-based tracing via the Linux
ptrace(2) interface. This sets breakpoints for the entry and return of all syscalls (even if the -e
option is used to select only some). This is invasive, and applications with high syscall rates may
find their performance worsened by an order of magnitude. To illustrate this, here is the same
dd(1) command without strace(1):
$ dd if=/dev/zero of=/dev/null bs=1k count=5000k
5120000+0 records in
5120000+0 records out
5242880000 bytes (5.2 GB) copied, 1.91247 s, 2.7 GB/s
