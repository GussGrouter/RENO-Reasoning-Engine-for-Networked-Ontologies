# Systems Performance — Section 4.3.1 /proc (proc-observability-4-3-1)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch4-scout-p171-220.txt
- PDF pages (approx): 171–220

---

4.3.1 /proc
This is a file system interface for kernel statistics. /proc contains a number of directories, where
each directory is named after the process ID for the process it represents. In each of these directories is a number of files containing information and statistics about each process, mapped
from kernel data structures. There are additional files in /proc for system-wide statistics.
/proc is dynamically created by the kernel and is not backed by storage devices (it runs inmemory). It is mostly read-only, providing statistics for observability tools. Some files are
writeable, for controlling process and kernel behavior.
The file system interface is convenient: it’s an intuitive framework for exposing kernel statistics
to user-land via the directory tree, and has a well-known programming interface via the POSIX
file system calls: open(), read(), close(). You can also explore it at the command line using cd,
cat(1), grep(1), and awk(1). The file system also provides user-level security through use of file
access permissions. In rare cases where the typical process observability tools (ps(1), top(1), etc.)
cannot be executed, some process debugging can still be performed by shell built-ins from the
/proc directory.
The overhead of reading most /proc files is negligible; exceptions include some memory-map
related files that walk page tables.

Per-Process Statistics
Various files are provided in /proc for per-process statistics. Here is an example of what may be
available (Linux 5.4), here looking at PID 187333:
$ ls -F /proc/18733
arch_status

environ

mountinfo

personality

statm

attr/

exe@

mounts

projid_map

status

autogroup

fd/

mountstats

root@

syscall

auxv

fdinfo/

net/

sched

task/

cgroup

gid_map

ns/

schedstat

timers

clear_refs

io

numa_maps

sessionid

timerslack_ns

cmdline

limits

oom_adj

setgroups

uid_map

comm

loginuid

oom_score

smaps

wchan

coredump_filter

map_files/

oom_score_adj

smaps_rollup

cpuset

maps

pagemap

stack

cwd@

mem

patch_state

stat

3

You can also examine /proc/self for your current process (shell).

4.3 Observability Sources

The exact list of files available depends on the kernel version and CONFIG options.
Those related to per-process performance observability include:
■

limits: In-effect resource limits

■

maps: Mapped memory regions

■

sched: Various CPU scheduler statistics

■

schedstat: CPU runtime, latency, and time slices

■

smaps: Mapped memory regions with usage statistics

■

stat: Process status and statistics, including total CPU and memory usage

■

statm: Memory usage summary in units of pages

■

status: stat and statm information, labeled

■

fd: Directory of file descriptor symlinks (also see fdinfo)

■

cgroup: Cgroup membership information

■

task: Directory of per-task (thread) statistics

The following shows how per-process statistics are read by top(1), traced using strace(1):
stat("/proc/14704", {st_mode=S_IFDIR|0555, st_size=0, ...}) = 0
open("/proc/14704/stat", O_RDONLY)

= 4

read(4, "14704 (sshd) S 1 14704 14704 0 -"..., 1023) = 232
close(4)

This has opened a file called “stat” in a directory named after the process ID (14704), and then
read the file contents.
top(1) repeats this for all active processes on the system. On some systems, especially those with
many processes, the overhead from performing these can become noticeable, especially for versions of top(1) that repeat this sequence for every process on every screen update. This can lead
to situations where top(1) reports that top itself is the highest CPU consumer!

System-Wide Statistics
Linux has also extended /proc to include system-wide statistics, contained in these additional
files and directories:
$ cd /proc; ls -Fd [a-z]*
acpi/

dma

kallsyms

mdstat

schedstat

thread-self@

buddyinfo

driver/

kcore

meminfo

scsi/

timer_list

bus/

execdomains

keys

misc

self@

tty/

cgroups

fb

key-users

modules

slabinfo

uptime

cmdline

filesystems

kmsg

mounts@

softirqs

version

consoles

fs/

kpagecgroup

mtrr

stat

vmallocinfo

cpuinfo

interrupts

kpagecount

net@

swaps

vmstat

141

142

Chapter 4 Observability Tools

crypto

iomem

kpageflags

pagetypeinfo

sys/

devices

ioports

loadavg

partitions

sysrq-trigger

diskstats

irq/

locks

sched_debug

sysvipc/

zoneinfo

System-wide files related to performance observability include:
■

cpuinfo: Physical processor information, including every virtual CPU, model name, clock
speed, and cache sizes.

■

diskstats: Disk I/O statistics for all disk devices

■

interrupts: Interrupt counters per CPU

■

loadavg: Load averages

■

meminfo: System memory usage breakdowns

■

net/dev: Network interface statistics

■

net/netstat: System-wide networking statistics

■

net/tcp: Active TCP socket information

■

pressure/: Pressure stall information (PSI) files

■

schedstat: System-wide CPU scheduler statistics

■

self: A symlink to the current process ID directory, for convenience

■

slabinfo: Kernel slab allocator cache statistics

■

■

stat: A summary of kernel and system resource statistics: CPUs, disks, paging, swap,
processes
zoneinfo: Memory zone information

These are read by system-wide tools. For example, here’s vmstat(8) reading /proc, as traced by
strace(1):
open("/proc/meminfo", O_RDONLY)

= 3

lseek(3, 0, SEEK_SET)

= 0

read(3, "MemTotal:

889484 kB\nMemF"..., 2047) = 1170

open("/proc/stat", O_RDONLY)
read(4, "cpu

= 4

14901 0 18094 102149804 131"..., 65535) = 804

open("/proc/vmstat", O_RDONLY)

= 5

lseek(5, 0, SEEK_SET)

= 0

read(5, "nr_free_pages 160568\nnr_inactive"..., 2047) = 1998

This output shows that vmstat(8) was reading meminfo, stat, and vmstat.

CPU Statistic Accuracy
The /proc/stat file provides system-wide CPU utilization statistics and is used by many tools
(vmstat(8), mpstat(1), sar(1), monitoring agents). The accuracy of these statistics depends on
the kernel configuration. The default configuration (CONFIG_TICK_CPU_ACCOUNTING)

4.3 Observability Sources

measures CPU utilization with a granularity of clock ticks [Weisbecker 13], which may be four
milliseconds (depending on CONFIG_HZ). This is generally sufficient. There are options to
improve accuracy by using higher-resolution counters, though with a small performance cost
(VIRT_CPU_ACCOUNTING_NATIVE and VIRT_CPU_ACCOUTING_GEN), as well an option
to for more accurate IRQ time (IRQ_TIME_ACCOUNTING). A different approach to obtaining
accurate CPU utilization measurements is to use MSRs or PMCs.

File Contents
/proc files are usually text formatted, allowing them to be read easily from the command line
and processed by shell scripting tools. For example:
$ cat /proc/meminfo
MemTotal:

15923672 kB

MemFree:

10919912 kB

MemAvailable:

15407564 kB

Buffers:

94536 kB

Cached:

2512040 kB

SwapCached:
Active:

0 kB
1671088 kB

[...]
$ grep Mem /proc/meminfo
MemTotal:

15923672 kB

MemFree:

10918292 kB

MemAvailable:

15405968 kB

While this is convenient, it does add a small amount of overhead for the kernel to encode the
statistics as text, and for any user-land tool that then parses the text. netlink, covered in
Section 4.3.4, netlink, is a more efficient binary interface.
The contents of /proc are documented in the proc(5) man page and in the Linux kernel documentation: Documentation/filesystems/proc.txt [Bowden 20]. Some parts have extended documentation, such as diskstats in Documentation/iostats.txt and scheduler stats in Documentation/
scheduler/sched-stats.txt. Apart from the documentation, you can also study the kernel source
code to understand the exact origin of all items in /proc. It can also be helpful to read the source to
the tools that consume them.
Some of the /proc entries depend on CONFIG options: schedstats is enabled with CONFIG_
SCHEDSTATS, sched with CONFIG_SCHED_DEBUG, and pressure with CONFIG_PSI.

