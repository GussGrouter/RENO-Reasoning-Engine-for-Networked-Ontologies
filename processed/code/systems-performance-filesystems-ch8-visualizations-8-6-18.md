8.6.18

Visualizations

The load applied to file systems can be plotted over time as a line graph, to help identify timebased usage patterns. It can be useful to plot separate graphs for reads, writes, and other file
system operations.
The distribution of file system latency is expected to be bimodal: one mode at low latency for
file system cache hits, and another at high latency for cache misses (storage device I/O). For this
reason, representing the distribution as a single value—such as a mean, mode, or median—is
misleading.
One way to solve this problem is to use a visualization that shows the full distribution, such as a
heat map. Heat maps were introduced in Chapter 2, Methodologies, Section 2.10.3, Heat Maps.
An example file system latency heat map is shown in Figure 8.13: it shows the passage of time on
the x-axis and I/O latency on the y-axis [Gregg 09a].
This heat map shows the difference enabling an L2ARC device makes to NFSv3 latency. An
L2ARC device is a secondary ZFS cache, after main memory, and typically uses flash memory (it
was mentioned in Section 8.3.2, Caching). The system in Figure 8.13 had 128 Gbytes of main
memory (DRAM) and 600 Gbytes of L2ARC (read-optimized SSDs). The left half of the heat map
shows no L2ARC device (the L2ARC was disabled), and the right half shows the latency with an
L2ARC device.

Figure 8.13 File system latency heat map
For the left half, file system latency is either low or high, separated by a gap. The low latencies are
the blue line at the bottom, around 0 milliseconds, which is likely main memory cache hits. The
high latencies begin at around 3 milliseconds and extended to the top, appearing as a “cloud,”
which is likely rotational disk latency. This bi-modal latency distribution is typical for file system
latency when backed by rotational disks.
For the right half, the L2ARC was enabled and latency is now often lower than 3 milliseconds,
and there are fewer higher disk latencies. You can see how the L2ARC’s latency filled in range
where there was a gap on the left of the heat map, reducing file system latency overall.
