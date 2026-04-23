# Systems Performance — baseline statistics (2.5.16) (PDF pages 96–104)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-drilldown-latency-methodr-scout-p96-104.md

---

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
