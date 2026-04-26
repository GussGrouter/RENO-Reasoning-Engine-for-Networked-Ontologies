7.2.10 Working Set Size
Working set size (WSS) is the amount of main memory a process frequently uses to perform
work. It is a useful concept for memory performance tuning: performance should greatly
improve if the WSS can fit into the CPU caches, rather than main memory. Also, performance
will greatly degrade if the WSS exceeds the main memory size, and the application must swap
to perform work.
While useful as a concept, it is difficult to measure in practice: there is no WSS statistic in
observability tools (they commonly report RSS, not WSS). Section 7.4.10, Memory Shrinking,
describes an experimental methodology for WSS estimation, and Section 7.5.12, wss, shows an
experimental working set size estimation tool, wss(8).
