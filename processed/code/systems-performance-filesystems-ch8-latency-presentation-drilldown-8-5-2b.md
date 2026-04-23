Choosing the layer may depend on tool availability. Check the following:

Application documentation: Some applications already provide file system latency
metrics, or the ability to enable their collection.
Operating system tools: Operating systems may also provide metrics, ideally as separate
statistics for each file system or application.
Dynamic instrumentation: If your system has dynamic instrumentation (Linux kprobes
and uprobes, used by various tracers), all layers can be inspected via custom tracing programs, without restarting anything.

Latency may be presented as per-interval averages, distributions (e.g., histograms or heat maps:
see Section 8.6.18), or as a list of every operation and its latency. For file systems that have a high
cache hit rate (over 99%), per-interval averages can become dominated by cache hit latency. This
may be unfortunate when there are isolated instances of high latency (outliers) that are important to identify but difficult to see from an average. Examining full distributions or per-operation
latency allows such outliers to be investigated, along with the effect of different tiers of latency,
including file system cache hits and misses.
Once high latency has been found, continue with drill-down analysis into the file system to
determine the origin.

