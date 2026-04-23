Chapter 4
Observability Tools

Operating systems have historically provided many tools for observing system software and
hardware components. To the newcomer, the wide range of available tools and metrics suggested
that everything—or at least everything important—could be observed. In reality there were
many gaps, and systems performance experts became skilled in the art of inference and interpretation: figuring out activity from indirect tools and statistics. For example, network packets
could be examined individually (sniffing), but disk I/O could not (at least, not easily).
Observability has greatly improved in Linux thanks to the rise of dynamic tracing tools, including the BPF-based BCC and bpftrace. Dark corners are now illuminated, including individual
disk I/O using biosnoop(8). However, many companies and commercial monitoring products
have not yet adopted system tracing, and are missing out on the insight it brings. I have led
the way by developing, publishing, and explaining new tracing tools, tools already in use by
companies such as Netflix and Facebook.
The learning objectives of this chapter are:
■

Identify static performance tools and crisis tools.

■

Understand tool types and their overhead: counters, profiling, and tracing.

■

■

Learn about observability sources, including: /proc, /sys, tracepoints, kprobes, uprobes,
USDT, and PMCs.
Learn how to configure sar(1) for archiving statistics.

In Chapter 1 I introduced different types of observability: counters, profiling, and tracing, as
well as static and dynamic instrumentation. This chapter explains observability tools and their
data sources in detail, including a summary of sar(1), the system activity reporter, and an introduction to tracing tools. This gives you the essentials for understanding Linux observability;
later chapters (6 to 11) use these tools and sources to solve specific issues. Chapters 13 to 15 cover
the tracers in depth.
This chapter uses the Ubuntu Linux distribution as an example; most of these tools are the same
across other Linux distributions, and some similar tools exist for other kernels and operating
systems where these tools originated.

130

