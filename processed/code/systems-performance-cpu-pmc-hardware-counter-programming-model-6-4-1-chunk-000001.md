<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

Hardware Counters (PMCs)
Performance monitoring counters (PMCs) were summarized as a source of observability statistics in Chapter 4, Observability Tools, Section 4.3.9, Hardware Counters (PMCs). This section
describes their CPU implementation in more detail, and provides additional examples.
PMCs are processor registers implemented in hardware that can be programmed to count lowlevel CPU activity. They typically include counters for the following:

4

■

CPU cycles: Including stall cycles and types of stall cycles

■

CPU instructions: Retired (executed)

■

Level 1, 2, 3 cache accesses: Hits, misses

There is also quad-pumped, where data is transferred on the rising edge, peak, falling edge, and trough of the clock
cycle. Quad pumping is used by the Intel FSB.

237

238

Chapter 6 CPUs

■

Floating-point unit: Operations

■

Memory I/O: Reads, writes, stall cycles

■

Resource I/O: Reads, writes, stall cycles

Each CPU has a small number of registers, usually between two and eight, that can be programmed to record events like these. Those available depend on the processor type and model
and are documented in the processor manual.
As a relatively simple example, the Intel P6 family of processors provide performance counters
via four model-specific registers (MSRs). Two MSRs are the counters and are read-only. The other
two MSRs, called event-select MSRs, are used to program the counters and are read-write. The
performance counters are 40-bit registers, and the event-select MSRs are 32-bit. The format of
the event-select MSRs is shown in Figure 6.11.

Figure 6.11 Example Intel performance event-select MSR
The counter is identified by the event select and the UMASK. The event select identifies the type
of event to count, and the UMASK identifies subtypes or groups of subtypes. The OS and USR
bits can be set so that the counter is incremented only while in kernel mode (OS) or user mode
(USR), based on the processor protection rings. The CMASK can be set to a threshold of events
that must be reached before the counter is incremented.
The Intel processor manual (volume 3B [Intel 19b]) lists the dozens of events that can be counted
by their event-select and UMASK values. The selected examples in Table 6.5 provide an idea of
the different targets (processor functional units) that may be observable, including descriptions
from the manual. You will need to refer to your current processor manual to see what you actually have.

