<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs) -->

6.5 Methodology

See Chapter 2, Methodologies, for more methodologies and the introduction to many of these.
You are not expected to use them all; treat this as a cookbook of recipes that may be followed
individually or used in combination.
My suggestion is to use the following, in this order: performance monitoring, the USE method,
profiling, micro-benchmarking, and static performance tuning.
Section 6.6, Observability Tools, and later sections, show the operating system tools for applying
these methodologies.

6.5.1 Tools Method
The tools method is a process of iterating over available tools, examining key metrics that they
provide. While this is a simple methodology, it can overlook issues for which the tools provide
poor or no visibility, and it can be time-consuming to perform.
For CPUs, the tools method can involve checking the following (Linux):
■

■

■

uptime/top: Check the load averages to see if load is increasing or decreasing over time. Bear
this in mind when using the following tools, as load may be changing during your analysis.
vmstat: Run vmstat(1) with a one-second interval and check the system-wide CPU utilization (“us” + “sy”). Utilization approaching 100% increases the likelihood of scheduler
latency.
mpstat: Examine statistics per-CPU and check for individual hot (busy) CPUs, identifying
a possible thread scalability problem.

■

top: See which processes and users are the top CPU consumers.

■

pidstat: Break down the top CPU consumers into user- and system-time.

■

perf/profile: Profile CPU usage stack traces for both user- or kernel-time, to identify why
the CPUs are in use.

■

perf: Measure IPC as an indicator of cycle-based inefficiencies.

■

showboost/turboboost: Check the current CPU clock rates, in case they are unusually low.

■

dmesg: Check for CPU temperature stall messages (“cpu clock throttled”).

If an issue is found, examine all fields from the available tools to learn more context. See
Section 6.6, Observability Tools, for more about each tool.

