<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs) -->

6.6.5 ps
The process status command, ps(1), can list details on all processes, including CPU usage statistics.
For example:
$ ps aux
USER

RSS TTY

STAT START

TIME COMMAND

root

PID %CPU %MEM
1

0.0

0.0

23772

VSZ

1948 ?

Ss

2012

0:04 /sbin/init

root

2

0.0

0.0

0

0 ?

S

2012

0:00 [kthreadd]

root

3

0.0

0.0

0

0 ?

S

2012

0:26 [ksoftirqd/0]

root

4

0.0

0.0

0

0 ?

S

2012

0:00 [migration/0]

root

5

0.0

0.0

0

0 ?

S

2012

0:00 [watchdog/0]

[...]
web

11715 11.3

0.0 632700 11540 pts/0

Sl

01:36

0:27 node indexer.js

web

11721 96.5

0.1 638116 52108 pts/1

Rl+

01:37

3:33 node proxy.js

[...]

This style of operation originated from BSD, as can be recognized by the lack of a dash before the
aux options. These list all users (a), with extended user details (u), and include processes without
a terminal (x). The terminal is shown in the teletype (TTY) column.
A different style, from SVR4, uses options preceded by a dash:
$ ps -ef
PID

PPID

root

1

0

0 Nov13 ?

00:00:04 /sbin/init

root

2

0

0 Nov13 ?

00:00:00 [kthreadd]

root

3

2

0 Nov13 ?

00:00:00 [ksoftirqd/0]

root

4

2

0 Nov13 ?

00:00:00 [migration/0]

root

5

2

0 Nov13 ?

00:00:00 [watchdog/0]

[...]

C STIME TTY

TIME CMD

UID

6.6 Observability Tools

This lists every process (-e) with full details (-f). Various other options are available for ps(1)
including -o to customize the output and columns shown.
Key columns for CPU usage are TIME and %CPU (earlier example).
The TIME column shows the total CPU time consumed by the process (user + system) since it was
created, in hours:minutes:seconds.
On Linux, the %CPU column from the first example shows the average CPU utilization over the
lifetime of the process, summed across all CPUs. A single-threaded process that has always been
CPU-bound will report 100%. A two-thread CPU-bound process will report 200%. Other operating systems may normalize %CPU to the CPU count so that its maximum is 100%, and they may
only show recent or current CPU usage rather than the average over the lifetime. On Linux, to
see the current CPU usage of processes, you can use top(1).

6.6.6 top
top(1) was created by William LeFebvre in 1984 for BSD. He was inspired by the VMS command
MONITOR PROCESS/TOPCPU, which showed the top CPU-consuming jobs with CPU percentages and
an ASCII bar chart histogram (but not columns of data).
The top(1) command monitors top running processes, updating the screen at regular intervals.
For example, on Linux:
$ top
top - 01:38:11 up 63 days,
Tasks: 256 total,
Cpu(s):
Mem:

1:17,

2 users,

load average: 1.57, 1.81, 1.77

2.0%us,

2 running, 254 sleeping,
3.6%sy,

0 stopped,

0.0%ni, 94.2%id,

0.0%wa,

0.0%hi,

49548744k total, 16746572k used, 32802172k free,

Swap: 100663292k total,

0 zombie
0.2%si,

0.0%st

182900k buffers

0k used, 100663292k free, 14925240k cached

PID USER

PR

NI

VIRT

RES

11721 web

20

0

623m

50m 4984 R

SHR S %CPU %MEM
93

0.1

0:59.50 node

TIME+

COMMAND

11715 web

20

0

619m

20m 4916 S

0:07.52 node

10 root

20

0

0

0

0

25

0.0

0 S

1

0.0 248:52.56 ksoftirqd/2

51 root

20

0

0

0 S

0

0.0

0:35.66 events/0

11724 admin

20

0 19412 1444

960 R

0

0.0

0:00.07 top

1 root

20

0 23772 1948 1296 S

0

0.0

0:04.35 init

A system-wide summary is at the top and a process/task listing at the bottom, sorted by the top
CPU consumer by default. The system-wide summary includes the load averages and CPU states:
%us, %sy, %ni, %id, %wa, %hi, %si, %st. These states are equivalent to those printed by mpstat(1), as
described earlier, and are averaged across all CPUs.
CPU usage is shown by the TIME and %CPU columns. TIME is the total CPU time consumed by the
process at a resolution of hundredths of a second. For example, “1:36.53” means 1 minute and
36.53 seconds of on-CPU time in total. Some versions of top(1) provide an optional “cumulative
time” mode, which includes the CPU time from child processes that have exited.

261

262

Chapter 6 CPUs

The %CPU column shows the total CPU utilization for the current screen update interval. On
Linux, this is not normalized by the CPU count, and so a two-thread CPU-bound process will
report 200%; top(1) calls this “Irix mode,” after its behavior on IRIX. This can be switched to
“Solaris mode” (by pressing I to toggle the modes), which divides the CPU usage by the CPU
count. In that case, the two-thread process on a 16-CPU server would report CPU as 12.5%.
Though top(1) is often a tool for beginning performance analysts, you should be aware that the
CPU usage of top(1) itself can become significant and place top(1) as the top CPU-consuming
process! This has been due to the system calls it uses to read /proc—open(2), read(2), close(2)—
and calling these over many processes. Some versions of top(1) on other operating systems have
reduced the overhead by leaving file descriptors open and calling pread(2).
There is a variant of top(1) called htop(1), which provides more interactive features, customizations, and ASCII bar charts for CPU usage. It also calls four times as many syscalls, perturbing
the system even further. I rarely use it.
Since top(1) takes snapshots of /proc, it can miss short-lived processes that exit before a snapshot
is taken. This commonly happens during software builds, where the CPUs can be heavily loaded
by many short-lived tools from the build process. A variant of top(1) for Linux, called atop(1), uses
process accounting to catch the presence of short-lived processes, which it includes in its display.

6.6.7

pidstat

The Linux pidstat(1) tool prints CPU usage by process or thread, including user- and system-time
breakdowns. By default, a rolling output is printed of only active processes. For example:
$ pidstat 1
Linux 2.6.35-32-server (dev7)

11/12/12

_x86_64_

(16 CPU)

22:24:42

PID

%usr %system

%guest

%CPU

CPU

22:24:43

7814

0.00

1.98

0.00

1.98

3

Command
tar

22:24:43

7815

97.03

2.97

0.00

100.00

11

gzip

22:24:43

PID

%usr %system

%guest

%CPU

CPU

Command

22:24:44

448

0.00

1.00

0.00

1.00

0

kjournald

22:24:44

7814

0.00

2.00

0.00

2.00

3

tar

22:24:44

7815

97.00

3.00

0.00

100.00

11

gzip

22:24:44

7816

0.00

2.00

0.00

2.00

2

pidstat

[...]

This example captured a system backup, involving a tar(1) command to read files from the
file system, and the gzip(1) command to compress them. The user-time for gzip(1) is high, as
expected, as it becomes CPU-bound in compression code. The tar(1) command spends more
time in the kernel, reading from the file system.
The -p ALL option can be used to print all processes, including those that are idle. -t prints perthread statistics. Other pidstat(1) options are included in other chapters of this book.

6.6 Observability Tools

6.6.8 time, ptime
The time(1) command can be used to run programs and report CPU usage. It is provided in the
operating system under /usr/bin, and as a shell built-in.
This example runs time twice on a cksum(1) command, calculating the checksum of a large file:
$ time cksum ubuntu-19.10-live-server-amd64.iso
1044945083 883949568 ubuntu-19.10-live-server-amd64.iso
real

0m5.590s

user

0m2.776s

sys

0m0.359s

$ time cksum ubuntu-19.10-live-server-amd64.iso
1044945083 883949568 ubuntu-19.10-live-server-amd64.iso
real

0m2.857s

user

0m2.733s

sys

0m0.114s

The first run took 5.6 seconds, of which 2.8 seconds was in user mode, calculating the checksum.
There was 0.4 seconds in system-time, spanning the system calls required to read the file. There
is a missing 2.4 seconds (5.6 – 2.8 – 0.4), which is likely time spent blocked on disk I/O reads as
this file was only partially cached. The second run completed more quickly, in 2.9 seconds, with
almost no blocked time. This is expected, as the file may be fully cached in main memory for the
second run.
On Linux, the /usr/bin/time version supports verbose details. For example:
$ /usr/bin/time -v cp fileA fileB
Command being timed: "cp fileA fileB"
User time (seconds): 0.00
System time (seconds): 0.26
Percent of CPU this job got: 24%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:01.08
Average shared text size (kbytes): 0
Average unshared data size (kbytes): 0
Average stack size (kbytes): 0
Average total size (kbytes): 0
Maximum resident set size (kbytes): 3792
Average resident set size (kbytes): 0
Major (requiring I/O) page faults: 0
Minor (reclaiming a frame) page faults: 294
Voluntary context switches: 1082
Involuntary context switches: 1
Swaps: 0

263

264

Chapter 6 CPUs

File system inputs: 275432
File system outputs: 275432
Socket messages sent: 0
Socket messages received: 0
Signals delivered: 0
Page size (bytes): 4096
Exit status: 0

The -v option is not typically provided in the shell built-in version.

6.6.9 turbostat
turbostat(1) is a model-specific register (MSR)–based tool that shows the state of the CPUs,
and is often available in a linux-tools-common package. MSRs were mentioned in Chapter 4,
Observability Tools, Section 4.3.10, Other Observability Sources. Here is some sample output:
# turbostat
turbostat version 17.06.23 - Len Brown <lenb@kernel.org>
CPUID(0): GenuineIntel 22 CPUID levels; family:model:stepping 0x6:8e:a (6:142:10)
CPUID(1): SSE3 MONITOR SMX EIST TM2 TSC MSR ACPI-TM TM
CPUID(6): APERF, TURBO, DTS, PTM, HWP, HWPnotify, HWPwindow, HWPepp, No-HWPpkg, EPB
cpu0: MSR_IA32_MISC_ENABLE: 0x00850089 (TCC EIST No-MWAIT PREFETCH TURBO)
CPUID(7): SGX
cpu0: MSR_IA32_FEATURE_CONTROL: 0x00040005 (Locked SGX)
CPUID(0x15): eax_crystal: 2 ebx_tsc: 176 ecx_crystal_hz: 0
TSC: 2112 MHz (24000000 Hz * 176 / 2 / 1000000)
CPUID(0x16): base_mhz: 2100 max_mhz: 4200 bus_mhz: 100
[...]
Core

CPU

Avg_MHz

Busy%

Bzy_MHz

TSC_MHz

IRQ

SMI

C1

C1E

C3

C6

C7s

C8

C9

C10

C1%

C1E%

C3%

C6%

C7s%

C8%

C9%

C10%

CPU%c1

CPU%c3

CPU%c6

CPU%c7

GFX%C0

CPUGFX% Pkg%pc2

CoreTmp PkgTmp

GFX%rc6 GFXMHz

Totl%C0

Any%C0

Pkg%pc3 Pkg%pc6

Pkg%pc7 Pkg%pc8

Pkg%pc9

Pk%pc10 PkgWatt CorWatt GFXWatt

RAMWatt PKG_%

RAM_%

0

97

2.70

3609

2112

1370

0

41

293

41

453

0

693

0

311

0.24

1.23

0.15

5.35

0.00

39.33

0.00

50.97

7.50

0.18

6.26

83.37

52

75

91.41

300

118.58

100.38

8.47

8.30

0.00

0.00

0.00

0.00

0.00

0.00

0.00

17.69

14.84

0.65

1.23

0.00

0.00

[...]
0

[...]

6.6 Observability Tools

turbostat(8) begins by printing information about the CPU and MSRs, which can be over 50
lines of output, truncated here. It then prints interval summaries of metrics for all CPUs and
per-CPU, at a default five-second interval. This interval summary output is 389 characters wide
in this example, and the lines have wrapped five times, making it difficult to read. The columns
include the CPU number (CPU), average clock rate in MHz (Avg_MHz), C-state information,
temperatures (*Tmp), and power (*Watt).

6.6.10 showboost
Prior to the availability of turbostat(8) on the Netflix cloud, I developed showboost(1) to show
the CPU clock rate with a per-interval summary. showboost(1) is short for “show turbo boost”
and also uses MSRs. Some sample output:
# showboost
Base CPU MHz : 3000
Set CPU MHz

: 3000

Turbo MHz(s) : 3400 3500
Turbo Ratios : 113% 116%
CPU 0 summary every 1 seconds...
TIME

C0_MCYC

C0_ACYC

UTIL

RATIO

MHz

21:41:43

3021819807

3521745975

100%

116%

3496

21:41:44

3021682653

3521564103

100%

116%

3496

21:41:45

3021389796

3521576679

100%

116%

3496

[...]

This output shows a clock rate of 3496 MHz on CPU0. The base CPU frequency is 3000 MHz: it is
reaching 3496 via Intel turbo boost. The possible turbo boost levels, or “steps,” are also listed in
the output: 3400 and 3500 MHz.
showboost(8) is in my msr-cloud-tools repository [Gregg 20d], so named as I developed these for
use in the cloud. Because I only keep it working for the Netflix environment, it may not work
elsewhere due to CPU differences, in which case try turboboost(1).

6.6.11 pmcarch
pmcarch(8) shows a high-level view of CPU cycle performance. It is a PMC-based tool based
on the Intel “architectural set” of PMCs, hence the name (PMCs were explained in Chapter 4,
Observability Tools, Section 4.3.9, Hardware Counters (PMCs)). In some cloud environments,
these architectural PMCs are the only ones available (e.g., some AWS EC2 instances). Some sample output:
# pmcarch
K_CYCLES

K_INSTR

IPC BR_RETIRED

BR_MISPRED

BMR% LLCREF

96163187

87166313

0.91 19730994925

679187299

3.44 656597454 174313799

LLCMISS

73.45

LLC%

93988372

87205023

0.93 19669256586

724072315

3.68 666041693 169603955

74.54

265

266

Chapter 6 CPUs

93863787

86981089

0.93 19548779510

669172769

3.42 649844207 176100680

72.90

93739565

86349653

0.92 19339320671

634063527

3.28 642506778 181385553

71.77

[...]

The tool prints raw counters as well as some ratios as percents. Columns include:
■

K_CYCLES: CPU Cycles x 1000

■

K_INSTR: CPU Instructions x 1000

■

IPC: Instructions-Per-Cycle

■

BMR%: Branch Misprediction Ratio, as a percentage

■

LLC%: Last Level Cache hit ratio, as a percentage

IPC was explained in Section 6.3.7, IPC, CPI, along with example values. The other ratios provided, BMR% and LLC%, provide some insight as to why IPC may be low and where the stall
cycles may be.
I developed pmcarch(8) for my pmc-cloud-tools repository, which also has cpucache(8) for
more CPU cache statistics [Gregg 20e]. These tools employ workarounds and use processor-specific PMCs so that they work on the AWS EC2 cloud, and may not work elsewhere. Even if this
never works for you, it provides examples of useful PMCs that you can instrument using perf(1)
directly (Section 6.6.13, perf).

6.6.12

tlbstat

tlbstat(8) is another tool from pmc-cloud-tools, which shows the TLB cache statistics. Example
output:
# tlbstat -C0 1
K_CYCLES

K_INSTR

IPC DTLB_WALKS ITLB_WALKS K_DTLBCYC

K_ITLBCYC

DTLB% ITLB%

2875793

276051

0.10 89709496

65862302

787913

650834

27.40 22.63

2860557

273767

0.10 88829158

65213248

780301

644292

27.28 22.52

2885138

276533

0.10 89683045

65813992

787391

650494

27.29 22.55

2532843

243104

0.10 79055465

58023221

693910

573168

27.40 22.63

[...]

This particular output showed a worst-case scenario for the KPTI patches that work around the
Meltdown CPU vulnerability (the KPTI performance impact was summarized in Chapter 3,
Operating Systems, Section 3.4.3, KPTI (Meltdown)). KPTI flushes the TLB caches on syscalls and
other events, causing stall cycles during TLB walks: this is shown in the last two columns. In this
output, the CPU is spending roughly half its time on TLB walks, and would be expected to run
the application workload roughly half as fast.
Columns include:
■

K_CYCLES: CPU Cycles × 1000

■

K_INSTR: CPU Instructions × 1000

6.6 Observability Tools

■

IPC: Instructions-Per-Cycle

■

DTLB_WALKS: Data TLB walks (count)

■

ITLB_WALKS: Instruction TLB walks (count)

■

K_DTLBCYC: Cycles at least one PMH is active with data TLB walks × 1000

■

K_ITLBCYC: Cycles at least one PMH is active with instr. TLB walks × 1000

■

DTLB%: Data TLB active cycles as a ratio of total cycles

■

ITLB%: Instruction TLB active cycles as a ratio of total cycles

As with pmcarch(8), this tool may not work for your environment due to processor differences. It
is nonetheless a useful source of ideas.

