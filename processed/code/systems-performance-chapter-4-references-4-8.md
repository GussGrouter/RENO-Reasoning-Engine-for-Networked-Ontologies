<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (book PDF region ~171–220) -->

Exercises

Answer the following questions about observability tools (you may wish to revisit the introduction to some of these terms in Chapter 1):
1. List some static performance tools.
2. What is profiling?
3. Why would profilers use 99 Hertz instead of 100 Hertz?
4. What is tracing?
5. What is static instrumentation?
6. Describe why dynamic instrumentation is important.
7. What is the difference between tracepoints and kprobes?
8. Describe the expected CPU overhead (low/medium/high) from the following:
■

Disk IOPS counters (as seen by iostat(1))

■

Tracing per-event disk I/O via tracepoints or kprobes

■

Tracing per-event context switches (tracepoints/kprobes)

■

Tracing per-event process execution (execve(2)) (tracepoints/kprobes)

■

Tracing per-event libc malloc() via uprobes

9. Describe why PMCs are valuable for performance analysis.
10. Given an observability tool, describe how you could determine what instrumentation
sources it uses.

4.8 References
[Eigler 05] Eigler, F. Ch., et al. “Architecture of SystemTap: A Linux Trace/Probe Tool,”
http://sourceware.org/systemtap/archpaper.pdf, 2005.
[Drongowski 07] Drongowski, P., “Instruction-Based Sampling: A New Performance
Analysis Technique for AMD Family 10h Processors,” AMD (Whitepaper), 2007.
[Ayuso 12] Ayuso, P., “The Conntrack-Tools User Manual,” http://conntrack-tools.netfilter.org/
