7.4.4 Cycle Analysis
Memory bus load can be determined by inspecting the CPU performance monitoring counters
(PMCs), which can be programmed to count memory stall cycles, memory bus usage, and more.
A metric to begin with is the instructions per cycle (IPC), which reflects how memory-dependent
the CPU load is. See Chapter 6, CPUs.

7.4.5 Performance Monitoring
Performance monitoring can identify active issues and patterns of behavior over time. Key
metrics for memory are:
■

Utilization: Percent used, which may be inferred from available memory

■

Saturation: Swapping, OOM killing

For environments that implement memory limits or quotas (resource controls), statistics related
to the imposed limits may also need to be collected.
Errors can also be monitored (if available), as described with utilization and saturation in
Section 7.4.2, USE Method.
Monitoring memory usage over time, especially by process, can help identify the presence and
rate of memory leaks.
