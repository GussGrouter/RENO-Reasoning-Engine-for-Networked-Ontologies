# systems-performance-drill-down-analysis-2-5-12 (chunk 000001)

# Systems Performance — drill-down analysis (2.5.12) (drill-down-analysis-2-5-12) (PDF pages 92–98)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-drilldown-latency-scout-p92-98.md

---

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
