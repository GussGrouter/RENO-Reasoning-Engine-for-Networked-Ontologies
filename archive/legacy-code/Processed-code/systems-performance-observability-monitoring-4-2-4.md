# Systems Performance — Section 4.2.4 Monitoring (observability-monitoring-4-2-4)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch4-scout-p171-220.txt
- PDF pages (approx): 171–220

---

4.2.4

Monitoring

Monitoring was introduced in Chapter 2, Methodologies. Unlike the tool types covered previously,
monitoring records statistics continuously in case they are later needed.

sar(1)
A traditional tool for monitoring a single operating system host is the System Activity Reporter,
sar(1), originating from AT&T Unix. sar(1) is counter-based and has an agent that executes at
scheduled times (via cron) to record the state of system-wide counters. The sar(1) tool allows
these to be viewed at the command line, for example:
# sar
Linux 4.15.0-66-generic (bgregg)

12/21/2019

_x86_64_

(8 CPU)

12:00:01 AM

CPU

%user

%nice

%system

%iowait

%steal

%idle

12:05:01 AM

all

3.34

0.00

0.95

0.04

0.00

95.66

12:10:01 AM

all

2.93

0.00

0.87

0.04

0.00

96.16

12:15:01 AM

all

3.05

0.00

1.38

0.18

0.00

95.40

12:20:01 AM

all

3.02

0.00

0.88

0.03

0.00

96.06

all

0.00

0.00

0.00

0.00

0.00

0.00

[...]
Average:

By default, sar(1) reads its statistics archive (if enabled) to print recent historical statistics. You
can specify an optional interval and count for it to examine current activity at the rate specified.
sar(1) can record dozens of different statistics to provide insight into CPU, memory, disks, networking, interrupts, power usage, and more. It is covered in more detail in Section 4.4, sar.
Third-party monitoring products are often built on sar(1) or the same observability statistics it
uses, and expose these metrics over the network.

SNMP
The traditional technology for network monitoring is the Simple Network Management Protocol
(SNMP). Devices and operating systems can support SNMP and in some cases provide it by
default, avoiding the need to install third-party agents or exporters. SNMP includes many basic
OS metrics, although it has not been extended to cover modern applications. Most environments
have been switching to custom agent-based monitoring instead.

Agents
Modern monitoring software runs agents (also known as exporters or plugins) on each system to
record kernel and application metrics. These can include agents for specific applications and
targets, for example, the MySQL database server, the Apache Web Server, and the Memcached
caching system. Such agents can provide detailed application request metrics that are not available from system counters alone.

137

138

Chapter 4 Observability Tools

Monitoring software and agents for Linux include:
■

■

■

Performance Co-Pilot (PCP): PCP supports dozens of different agents (called
Performance Metric Domain Agents: PMDAs), including for BPF-based metrics [PCP 20].
Prometheus: The Prometheus monitoring software supports dozens of different exporters,
for databases, hardware, messaging, storage, HTTP, APIs, and logging [Prometheus 20].
collectd: Supports dozens of different plugins.

An example monitoring architecture is pictured in Figure 4.4 involving a monitoring database
server for archiving metrics, and a monitoring web server for providing a client UI. The metrics
are sent (or made available) by agents to the database server and then made available to client
UIs for display in as line graphs and in dashboards. For example, Graphite Carbon is a monitoring database server, and Grafana is a monitoring web server/dashboard.

Figure 4.4 Example monitoring architecture
There are dozens of monitoring products, and hundreds of different agents for different target
types. Covering them is beyond the scope of this book. There is, however, one common denominator that is covered here: system statistics (based on kernel counters). The system statistics
shown by monitoring products are typically the same as those shown by system tools: vmstat(8),
iostat(1), etc. Learning these will help you understand monitoring products, even if you never
use the command-line tools. These tools are covered in later chapters.
Some monitoring products read their system metrics by running the system tools and parsing
the text output, which is inefficient. Better monitoring products use library and kernel interfaces to read the metrics directly—the same interfaces as used by the command-line tools. These
sources are covered in the next section, focusing on the most common denominator: the kernel
interfaces.

