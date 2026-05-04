# systems-performance-heat-maps-2-10-3 (chunk 000001)

# Systems Performance — heat maps (2.10.3) (heat-maps-2-10-3) (PDF pages 118–140)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch2-tail-scout-p118-140.md

---

2.10.3      Heat Maps
     Heat maps (more properly called a column quantization) can solve the scatter plot scalability prob-
     lems by quantizing x and y ranges into groups called buckets. These are displayed as large pixels,
     colored based on the number of events in that x and y range. This quantizing also solves the
     scatter plot visual density limit, allowing heat maps to show data from a single system or thou-
     sands of systems in the same way. Heat maps had previously been used for location such as disk
     offsets (e.g., TazTool [McDougall 06a]); I invented their use in computing for latency, utilization,
     and other metrics. Latency heat maps were first included in Analytics for the Sun Microsystems
     ZFS Storage appliance, released in 2008 [Gregg 10a][Gregg 10b], and are now commonplace in
     performance monitoring products such as Grafana [Grafana 20].

     The same dataset as plotted earlier is shown in Figure 2.30 as a heat map.




     Figure 2.30 Heat map

     High-latency outliers can be identified as blocks that are high in the heat map, usually of light
     colors as they span few I/O (often a single I/O). Patterns in the bulk of the data begin to emerge,
     which may be impossible to see with a scatter plot.

     The full range of seconds for this disk I/O trace (not shown earlier) is shown in the Figure 2.31
     heat map.
                                                                               2.10 Visualizations     83




Figure 2.31 Heat map: full range

Despite spanning nine times the range, the visualization is still very readable. A bimodal distri-
bution can be seen for much of the range, with some I/O returning with near-zero latency (likely
a disk cache hit), and others with a little less than 1 ms (likely a disk cache miss).

There are other examples of heat maps later in this book, including in Chapter 6, CPUs, Section 6.7,
Visualizations; Chapter 8, File Systems, Section 8.6.18, Visualizations; and Chapter 9, Disks,
Section 9.7.3, Latency Heat Maps. My website also has examples of latency, utilization, and
subsecond-offset heat maps [Gregg 15b].
