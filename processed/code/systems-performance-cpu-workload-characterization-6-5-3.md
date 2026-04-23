<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs) -->

6.5.3 Workload Characterization
Characterizing the load applied is important in capacity planning, benchmarking, and simulating
workloads. It can also lead to some of the largest performance gains by identifying unnecessary
work that can be eliminated.
Basic attributes for characterizing CPU workload are:
■

CPU load averages (utilization + saturation)

■

User-time to system-time ratio

■

Syscall rate

■

Voluntary context switch rate

■

Interrupt rate

The intent is to characterize the applied load, not the delivered performance. The load averages
on some operating systems (e.g., Solaris) show CPU demand only, making them a primary metric
for CPU workload characterization. On Linux, however, load averages include other load types.
See the example and further explanation in Section 6.6.1, uptime.
The rate metrics are a little harder to interpret, as they reflect both the applied load and to some
degree the delivered performance, which can throttle their rate.6
The user-time to system-time ratio shows the type of load applied, as introduced earlier in
Section 6.3.9, User Time/Kernel Time. High user time rates are due to applications spending time
6

E.g., imagine finding that a given batch computing workload has higher syscall rates when run on faster CPUs, even
though the workload is the same. It completes sooner!


<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs §6.5 continued) -->

6.5 Methodology

performing their own compute. High system time shows time spent in the kernel instead, which
may be further understood by the syscall and interrupt rate. I/O-bound workloads have higher
system time, syscalls, and higher voluntary context switches than CPU-bound workloads as
threads block waiting for I/O.
Here is an example workload description, designed to show how these attributes can be
expressed together:
On an average 48-CPU application server, the load average varies between 30 and 40
during the day. The user/system ratio is 95/5, as this is a CPU-intensive workload. There
are around 325 K syscalls/s, and around 80 K voluntary context switches/s.
These characteristics can vary over time as different load is encountered.

Advanced Workload Characterization/Checklist
Additional details may be included to characterize the workload. These are listed here as
questions for consideration, which may also serve as a checklist when studying CPU issues
thoroughly:
■

What is the CPU utilization system-wide? Per CPU? Per core?

■

How parallel is the CPU load? Is it single-threaded? How many threads?

■

Which applications or users are using the CPUs? How much?

■

Which kernel threads are using the CPUs? How much?

■

What is the CPU usage of interrupts?

■

What is the CPU interconnect utilization?

■

Why are the CPUs being used (user- and kernel-level call paths)?

■

What types of stall cycles are encountered?

See Chapter 2, Methodologies, for a higher-level summary of this methodology and the characteristics to measure (who, why, what, how). The sections that follow expand upon the last two
questions in this list: how call paths can be analyzed using profiling, and stall cycles using cycle
analysis.
