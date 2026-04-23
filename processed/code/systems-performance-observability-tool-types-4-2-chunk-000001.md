The following sections explain performance observability tools in more detail.

4.2

Tool Types

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
