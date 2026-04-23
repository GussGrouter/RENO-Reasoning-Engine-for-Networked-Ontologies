                                                                               2.5 Methodology        53



Microservices
A microservice architecture presents a similar problem to that of too many resource metrics:
there can be so many metrics for each service that it is laborious to check them all, and they can
overlook areas where metrics do not yet exist. The USE method can address these problems with
microservices as well. For example, for a typical Netflix microservice, the USE metrics are:
   ■   Utilization: The average CPU utilization across the entire instance cluster.
   ■   Saturation: An approximation is the difference between the 99th latency percentile and
       the average latency (assumes the 99th is saturation-driven).
   ■   Errors: Request errors.

These three metrics are already examined for each microservice at Netflix using the Atlas cloud-
wide monitoring tool [Harrington 14].

There is a similar methodology that has been designed specifically for services: the RED method.


2.5.10      The RED Method
The focus of this methodology is services, typically cloud services in a microservice architecture.
It identifies three metrics for monitoring health from a user perspective and can be summarized
as [Wilkie 18]:

    For every service, check the request rate, errors, and duration.

The metrics are:
   ■   Request rate: The number of service requests per second
   ■   Errors: The number of requests that failed
   ■   Duration: The time for requests to complete (consider distribution statistics such as per-
       centiles in addition to the average: see Section 2.8, Statistics)

Your task is to draw a diagram of your microservice architecture and ensure that these three
metrics are monitored for each service. (Distributed tracing tools may provide such diagrams for
you.) The advantages are similar to the USE method: the RED method is fast and easy to follow,
and comprehensive.

The RED method was created by Tom Wilkie, who has also developed implementations of the
USE and RED method metrics for Prometheus with dashboards using Grafana [Wilkie 18]. These
methodologies are complementary: the USE method for machine health, and the RED method
for user health.

The inclusion of the request rate provides an important early clue in an investigation: whether a
performance problem is one of load versus architecture (see Section 2.3.8, Load vs. Architecture).
If the request rate has been steady but the request duration has increased, it points to a problem
with the architecture: the service itself. If both the request rate and duration have increased,
then the problem may be one of the load applied. This can be further investigated using work-
load characterization.
54   Chapter 2 Methodologies


     2.5.11 Workload Characterization
     Workload characterization is a simple and effective method for identifying a class of issues:
     those due to the load applied. It focuses on the input to the system, rather than the resulting
     performance. Your system may have no architectural, implementation, or configuration issues
     present, but be experiencing more load than it can reasonably handle.

     Workloads can be characterized by answering the following questions:

         ■   Who is causing the load? Process ID, user ID, remote IP address?
         ■   Why is the load being called? Code path, stack trace?
         ■   What are the load characteristics? IOPS, throughput, direction (read/write), type? Include
             variance (standard deviation) where appropriate.
         ■   How is the load changing over time? Is there a daily pattern?

     It can be useful to check all of these, even when you have strong expectations about what the
     answers will be, because you may be surprised.

     Consider this scenario: You have a performance issue with a database whose clients are a pool of
     web servers. Should you check the IP addresses of who is using the database? You already expect
     them to be the web servers, as per the configuration. You check anyway and discover that the
     entire Internet appears to be throwing load at the databases, destroying their performance. You
     are actually under a denial-of-service (DoS) attack!

     The best performance wins are the result of eliminating unnecessary work. Sometimes unnec-
     essary work is caused by applications malfunctioning, for example, a thread stuck in a loop
     creating unnecessary CPU work. It can also be caused by bad configurations—for example,
     system-wide backups that run during peak hours—or even a DoS attack as described previously.
     Characterizing the workload can identify these issues, and with maintenance or reconfiguration
     they may be eliminated.

     If the identified workload cannot be eliminated, another approach may be to use system
     resource controls to throttle it. For example, a system backup task may be interfering with a
     production database by consuming CPU resources to compress the backup, and then network
     resources to transfer it. This CPU and network usage may be throttled using resource controls (if
     the system supports them) so that the backup runs more slowly without hurting the database.

     Apart from identifying issues, workload characterization can also be input for the design of
     simulation benchmarks. If the workload measurement is an average, ideally you will also collect
     details of the distribution and variation. This can be important for simulating the variety of
     workloads expected, rather than testing only an average workload. See Section 2.8, Statistics, for
     more about averages and variation (standard deviation), and Chapter 12, Benchmarking.

     Analysis of the workload also helps separate problems of load from problems of architecture,
     by identifying the former. Load versus architecture was introduced in Section 2.3.8, Load vs.
     Architecture.

     The specific tools and metrics for performing workload characterization depend on the target.
     Some applications record detailed logs of client activity, which can be the source for statistical
     analysis. They may also already provide daily or monthly reports of client usage, which can be
     mined for details.
                                                                               2.5 Methodology        55



2.5.12      Drill-Down Analysis
Drill-down analysis starts with examining an issue at a high level, then narrowing the focus
based on the previous findings, discarding areas that seem uninteresting, and digging deeper
into the interesting ones. The process can involve digging down through deeper layers of the
software stack, to hardware if necessary, to find the root cause of the issue.

The following is a three-stage drill-down analysis methodology for system performance
[McDougall 06a]:

   1. Monitoring: This is used for continually recording high-level statistics over time, and
      identifying or alerting if a problem may be present.

  2. Identification: Given a suspected problem, this narrows the investigation to particular
     resources or areas of interest, identifying possible bottlenecks.

   3. Analysis: Further examination of particular system areas is done to attempt to root-cause
      and quantify the issue.

Monitoring may be performed company-wide and the results of all servers or cloud instances
aggregated. A historical technology to do this is the Simple Network Monitoring Protocol
(SNMP), which can be used to monitor any network-attached device that supports it. Modern
monitoring systems use exporters: software agents that run on each system to collect and publish
metrics. The resulting data is recorded by a monitoring system and visualized by front-end GUIs.
This may reveal long-term patterns that can be missed when using command-line tools over
short durations. Many monitoring solutions provide alerts if a problem is suspected, prompting
analysis to move to the next stage.

Identification is performed by analyzing a server directly and checking system components:
CPUs, disks, memory, and so on. It has historically been performed using command-line tools
such as vmstat(8), iostat(1), and mpstat(1). Today there are many GUI dashboards that expose
the same metrics to allow faster analysis.

Analysis tools include those based on tracing or profiling, for deeper inspection of suspect areas.
Such deeper analysis may involve the creation of custom tools and inspection of source code
(if available). Here is where most of the drilling down takes place, peeling away layers of the
software stack as necessary to find the root cause. Tools for performing this on Linux include
strace(1), perf(1), BCC tools, bpftrace, and Ftrace.

As an example implementation of this three-stage methodology, the following are the technolo-
gies used for the Netflix cloud:

   1. Monitoring: Netflix Atlas: an open-source cloud-wide monitoring platform [Harrington 14].

  2. Identification: Netflix perfdash (formally Netflix Vector): a GUI for analyzing a single
     instance with dashboards, including USE method metrics.

   3. Analysis: Netflix FlameCommander, for generating different types of flame graphs; and
      command-line tools over an SSH session, including Ftrace-based tools, BCC tools, and
      bpftrace.

As an example of how we use this sequence at Netflix: Atlas may identify a problem micro-
service, perfdash may then narrow the problem to a resource, and then FlameCommander
56   Chapter 2 Methodologies


     shows the code paths consuming that resource, which can then be instrumented using BCC
     tools and custom bpftrace tools.


     Five Whys
     An additional methodology you can use during the drill-down analysis stage is the Five Whys
     technique [Wikipedia 20]: ask yourself “why?” then answer the question, and repeat five times
     in total (or more). Here is an example procedure:

        1. A database has begun to perform poorly for many queries. Why?

        2. It is delayed by disk I/O due to memory paging. Why?

        3. Database memory usage has grown too large. Why?

        4. The allocator is consuming more memory than it should. Why?

        5. The allocator has a memory fragmentation issue.

     This is a real-world example that unexpectedly led to a fix in a system memory allocation
     library. It was the persistent questioning and drilling down to the core issue that led to the fix.


     2.5.13      Latency Analysis
     Latency analysis examines the time taken to complete an operation and then breaks it into
     smaller components, continuing to subdivide the components with the highest latency so that
     the root cause can be identified and quantified. Similarly to drill-down analysis, latency analysis
     may drill down through layers of the software stack to find the origin of latency issues.

     Analysis can begin with the workload applied, examining how that workload was processed in
     the application, and then drill down into the operating system libraries, system calls, the kernel,
     and device drivers.

     For example, analysis of MySQL query latency could involve answering the following questions
     (example answers are given here):

        1. Is there a query latency issue? (yes)

        2. Is the query time largely spent on-CPU or waiting off-CPU? (off-CPU)

        3. What is the off-CPU time spent waiting for? (file system I/O)

        4. Is the file system I/O time due to disk I/O or lock contention? (disk I/O)

        5. Is the disk I/O time mostly spent queueing or servicing the I/O? (servicing)

        6. Is the disk service time mostly I/O initialization or data transfer? (data transfer)

     For this example, each step of the process posed a question that divided the latency into two
     parts and then proceeded to analyze the larger part: a binary search of latency, if you will. The
     process is pictured in Figure 2.14.

     As the slower of A or B is identified, it is then further split into A or B, analyzed, and so on.

     Latency analysis of database queries is the target of method R.
                                                                               2.5 Methodology        57




Figure 2.14 Latency analysis procedure

2.5.14      Method R
Method R is a performance analysis methodology developed for Oracle databases that focuses
on finding the origin of latency, based on Oracle trace events [Millsap 03]. It is described as
“a response time-based performance improvement method that yields maximum economic
value to your business” and focuses on identifying and quantifying where time is spent during
queries. While this is used for the study of databases, its approach could be applied to any system
and is worth mentioning here as an avenue of possible study.


2.5.15 Event Tracing
Systems operate by processing discrete events. These include CPU instructions, disk I/O and
other disk commands, network packets, system calls, library calls, application transactions,
database queries, and so on. Performance analysis usually studies summaries of these events,
such as operations per second, bytes per second, or average latency. Sometimes important detail
is lost in the summary, and the events are best understood when inspected individually.

Network troubleshooting often requires packet-by-packet inspection, with tools such as
tcpdump(8). This example summarizes packets as single lines of text:

# tcpdump -ni eth4 -ttt
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth4, link-type EN10MB (Ethernet), capture size 65535 bytes
00:00:00.000000 IP 10.2.203.2.22 > 10.2.0.2.33986: Flags [P.], seq
1182098726:1182098918, ack 4234203806, win 132, options [nop,nop,TS val 1751498743
ecr 1751639660], length 192
58   Chapter 2 Methodologies


     00:00:00.000392 IP 10.2.0.2.33986 > 10.2.203.2.22: Flags [.], ack 192, win 501,
     options [nop,nop,TS val 1751639684 ecr 1751498743], length 0
     00:00:00.009561 IP 10.2.203.2.22 > 10.2.0.2.33986: Flags [P.], seq 192:560, ack 1,
     win 132, options [nop,nop,TS val 1751498744 ecr 1751639684], length 368
     00:00:00.000351 IP 10.2.0.2.33986 > 10.2.203.2.22: Flags [.], ack 560, win 501,
     options [nop,nop,TS val 1751639685 ecr 1751498744], length 0
     00:00:00.010489 IP 10.2.203.2.22 > 10.2.0.2.33986: Flags [P.], seq 560:896, ack 1,
     win 132, options [nop,nop,TS val 1751498745 ecr 1751639685], length 336
     00:00:00.000369 IP 10.2.0.2.33986 > 10.2.203.2.22: Flags [.], ack 896, win 501,
     options [nop,nop,TS val 1751639686 ecr 1751498745], length 0
     [...]

     Varying amounts of information can be printed by tcpdump(8) as needed (see Chapter 10,
     Network).

     Storage device I/O at the block device layer can be traced using biosnoop(8) (BCC/BPF-based):

     # biosnoop
     TIME(s)         COMM              PID      DISK      T SECTOR        BYTES       LAT(ms)
     0.000004        supervise         1950     xvda1     W 13092560      4096           0.74
     0.000178        supervise         1950     xvda1     W 13092432      4096           0.61
     0.001469        supervise         1956     xvda1     W 13092440      4096           1.24
     0.001588        supervise         1956     xvda1     W 13115128      4096           1.09
     1.022346        supervise         1950     xvda1     W 13115272      4096           0.98
     [...]

     This biosnoop(8) output includes the I/O completion time (TIME(s)), initiating process details
     (COMM, PID), disk device (DISK), type of I/O (T), size (BYTES), and I/O duration (LAT(ms)). See
     Chapter 9, Disks, for more information about this tool.

     The system call layer is another common location for tracing. On Linux, it can be traced using
     strace(1) and perf(1)’s trace subcommand (see Chapter 5, Applications). These tools also have
     options to print timestamps.

     When performing event tracing, look for the following information:

         ■   Input: All attributes of an event request: type, direction, size, and so on
         ■   Times: Start time, end time, latency (difference)
         ■   Result: Error status, result of event (e.g., successful transfer size)

     Sometimes performance issues can be understood by examining attributes of the event, for
     either the request or the result. Event timestamps are particularly useful for analyzing latency
     and can often be included by using event tracing tools. The preceding tcpdump(8) output
     included delta timestamps, measuring the time between packets, using -ttt.

     The study of prior events provides more information. An uncommonly high latency event,
     known as a latency outlier, may be caused by previous events rather than the event itself. For
     example, the event at the tail of a queue may have high latency but be caused by the previously
     queued events, not its own properties. This case can be identified from the traced events.
                                                                                  2.5 Methodology       59



2.5.16       Baseline Statistics
Environments commonly use monitoring solutions to record server performance metrics and
to visualize them as line charts, with time on the x-axis (see Section 2.9, Monitoring). These
line charts can show whether a metric has changed recently, and if so, how it is now different,
simply by examining changes in the line. Sometimes additional lines are added to include more
histor ical data, such as historical averages or simply historical time ranges for comparison with
the current range. Many Netflix dashboards, for example, draw an extra line to show the same
time range but for the previous week, so that behavior at 3 p.m. on a Tuesday can be directly
compared with 3 p.m. on the previous Tuesday.

These approaches work well with already-monitored metrics and a GUI to visualize them.
However, there are many more system metrics and details available at the command line that
may not be monitored. You may be faced with unfamiliar system statistics and wonder if they
are “normal” for the server, or if they are evidence of an issue.

This is not a new problem, and there is a methodology to solve it that predates the widespread
use of monitoring solutions using line charts. It is the collection of baseline statistics. This can
involve collecting all the system metrics when the system is under “normal” load and recording
them in a text file or database for later reference. The baseline software can be a shell script that
runs observability tools and gathers other sources (cat(1) of /proc files). Profilers and tracing
tools can be included in the baseline, providing far more detail than is typically recorded by
monitoring products (but be careful with the overhead of those tools, so as not to perturb pro-
duction). These baselines may be collected at regular intervals (daily), as well as before and after
system or application changes, so that performance differences can be analyzed.

If baselines have not been collected and monitoring is not available, some observability tools
(those based on kernel counters) can show summary-since-boot averages, for comparison with
current activity. This is coarse, but better than nothing.


2.5.17       Static Performance Tuning
Static performance tuning focuses on issues of the configured architecture. Other methodol-
ogies focus on the performance of the applied load: the dynamic performance [Elling 00]. Static
performance analysis can be performed when the system is at rest and no load is applied.

For static performance analysis and tuning, step through all the components of the system and
check the following:

    ■   Does the component make sense? (outdated, underpowered, etc.)
    ■   Does the configuration make sense for the intended workload?
    ■   Was the component autoconfigured in the best state for the intended workload?
    ■   Has the component experienced an error such that it is now in a degraded state?

Here are some examples of issues that may be found using static performance tuning:

    ■   Network interface negotiation: selecting 1 Gbits/s instead of 10 Gbit/s
    ■   Failed disk in a RAID pool
    ■   Older version of the operating system, applications, or firmware used
