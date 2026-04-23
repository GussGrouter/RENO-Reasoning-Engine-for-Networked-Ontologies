# Systems Performance — observability tool types & fixed counters (PDF pages 170–185)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction: pdftotext -f 170 -l 185 -layout
- Capture: from start of '4.2 Tool Types' up to before 'System-Wide'

---

## PDF page 172

4.2      Tool Types
A useful categorization for observability tools is whether they provide system-wide or per-process
observability, and whether they are based on counters or events. These attributes are shown in
Figure 4.3, along with Linux tool examples.




Figure 4.3 Observability tool types

Some tools fit in more than one quadrant; for example, top(1) also has a system-wide summary,
and system-wide event tools can often filter for a particular process (-p PID).

Event-based tools include profilers and tracers. Profilers observe activity by taking a series of
snapshots on events, painting a coarse picture of the target. Tracers instrument every event
of interest, and may perform processing on them, for example to generate customized counters.
Counters, tracing, and profiling were introduced in Chapter 1.

The following sections describe Linux tools that use fixed counters, tracing, and profiling, as
well as those that perform monitoring (metrics).


4.2.1 Fixed Counters
Kernels maintain various counters for providing system statistics. They are usually implemented
as unsigned integers that are incremented when events occur. For example, there are counters
for the number of network packets received, disk I/O issued, and interrupts that occurred. These
are exposed by monitoring software as metrics (see Section 4.2.4, Monitoring).

A common kernel approach is to maintain a pair of cumulative counters: one to count events
and the other to record the total time in the event. These provide the count of events directly

---

## PDF page 173

134   Chapter 4 Observability Tools


      and the average time (or latency) in the event, by dividing the total time by the count. Since
      they are cumulative, by reading the pair at a time interval (e.g., one second) the delta can be
      calculated, and from that the per-second count and average latency. This is how many system
      statistics are calculated.

      Performance-wise, counters are considered “free” to use since they are enabled by default and
      maintained continually by the kernel. The only additional cost when using them is the act of
      reading their values from user-space (which should be negligible). The following example tools
      read these system-wide or per process.
