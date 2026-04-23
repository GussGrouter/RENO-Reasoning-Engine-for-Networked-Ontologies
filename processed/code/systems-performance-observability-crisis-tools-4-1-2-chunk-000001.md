4.1.2

Crisis Tools

When you have a production performance crisis that requires various performance tools to
debug it, you might find that none of them are installed. Worse, since the server is suffering a
performance issue, installing the tools may take much longer than usual, prolonging the crisis.
For Linux, Table 4.1 lists the recommended installation packages or source repositories that provide these crisis tools. Package names for Ubuntu/Debian are shown in this table (these package
names may vary for different Linux distributions).

Table 4.1

Linux crisis tool packages

Package

Provides

procps

ps(1), vmstat(8), uptime(1), top(1)

util-linux

dmesg(1), lsblk(1), lscpu(1)

sysstat

iostat(1), mpstat(1), pidstat(1), sar(1)

131

132

Chapter 4 Observability Tools

Package

Provides

iproute2

ip(8), ss(8), nstat(8), tc(8)

numactl

numastat(8)

linux-tools-common linux-tools-$(uname -r)

perf(1), turbostat(8)

bcc-tools (aka bpfcc-tools)

opensnoop(8), execsnoop(8), runqlat(8),
runqlen(8), softirqs(8), hardirqs(8), ext4slower(8),
ext4dist(8), biotop(8), biosnoop(8), biolatency(8),
tcptop(8), tcplife(8), trace(8), argdist(8),
funccount(8), stackcount(8), profile(8), and
many more

bpftrace

bpftrace, basic versions of opensnoop(8),
execsnoop(8), runqlat(8), runqlen(8), biosnoop(8),
biolatency(8), and more

perf-tools-unstable

Ftrace versions of opensnoop(8), execsnoop(8),
iolatency(8), iosnoop(8), bitesize(8), funccount(8),
kprobe(8)

trace-cmd

trace-cmd(1)

nicstat

nicstat(1)

ethtool

ethtool(8)

tiptop

tiptop(1)

msr-tools

rdmsr(8), wrmsr(8)

github.com/brendangregg/msr-cloud-tools

showboost(8), cpuhot(8), cputemp(8)

github.com/brendangregg/pmc-cloud-tools

pmcarch(8), cpucache(8), icache(8), tlbstat(8),
resstalls(8)

Large companies, such as Netflix, have OS and performance teams who ensure that production
systems have all of these packages installed. A default Linux distribution may only have procps
and util-linux installed, so all the others must be added.
In container environments, it may be desirable to create a privileged debugging container that
has full access to the system2 and all tools installed. The image for this container can be installed
on container hosts and deployed when needed.
Adding tool packages is often not enough: kernel and user-space software may also need to be
configured to support these tools. Tracing tools typically require certain kernel CONFIG options
to be enabled, such as CONFIG_FTRACE and CONFIG_BPF. Profiling tools typically require software to be configured to support stack walking, either by using frame-pointer compiled versions
of all software (including system libraries: libc, libpthread, etc.) or debuginfo packages installed
2

It could also be configured to share namespaces with a target container to analyze.

4.2 Tool Types

to support dwarf stack walking. If your company has yet to do this, you should check that
each performance tool works and fix those that do not before they are urgently needed in
a crisis.
