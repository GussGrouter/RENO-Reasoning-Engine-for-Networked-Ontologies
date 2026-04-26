8.5.4 Performance Monitoring
Performance monitoring can identify active issues and patterns of behavior over time. Key
metrics for file system performance are:
■

Operation rate

■

Operation latency

The operation rate is the most basic characteristic of the applied workload, and the latency is the
resulting performance. The value for normal or bad latency depends on your workload, environment, and latency requirements. If you aren’t sure, micro-benchmarks of known-to-be-good
versus bad workloads may be performed to investigate latency (e.g., workloads that usually hit
the file system cache versus those that usually miss). See Section 8.7, Experimentation.
The operation latency metric may be monitored as a per-second average, and can include other
values such as the maximum and standard deviation. Ideally, it would be possible to inspect the
full distribution of latency, for example by using a histogram or heat map, to look for outliers
and other patterns.
Both rate and latency may also be recorded for each operation type (read, write, stat, open, close,
etc.). Doing this will greatly help investigations of workload and performance changes, by identifying differences in particular operation types.
For systems that impose file system-based resource controls, statistics can be included to show if
and when throttling was in use.
Unfortunately, in Linux there are usually no readily available statistics for file system operations
(exceptions include, for NFS, via nfsstat(8)).
