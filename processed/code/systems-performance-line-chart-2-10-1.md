# Systems Performance — line chart (2.10.1) (line-chart-2-10-1) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

2.10.1      Line Chart
     A line chart (also called line graph) is a well-known, basic visualization. It is commonly used for
     examining performance metrics over time, showing the passage of time on the x-axis.

     Figure 2.27 is an example, showing the average (mean) disk I/O latency for a 20-second period.
     This was measured on a production cloud server running a MySQL database, where disk I/O
     latency was suspected to be causing slow queries.




     Figure 2.27 Line chart of average latency

     This line chart shows fairly consistent average read latency of around 4 ms, which is higher than
     expected for these disks.

     Multiple lines can be plotted, showing related data on the same set of axes. With this example, a
     separate line may be plotted for each disk, showing whether they exhibit similar performance.

     Statistical values can also be plotted, providing more information on the distribution of data.
     Figure 2.28 shows the same range of disk I/O events, with lines added for the per-second median,
     standard deviation, and percentiles. Note that the y-axis now has a much greater range than the
     previous line chart (by a factor of 8).

     This shows why the average is higher than expected: the distribution includes higher-latency
     I/O. Specifically, 1% of the I/O is over 20 ms, as shown by the 99th percentile. The median also
     shows where I/O latency was expected, around 1 ms.
                                                                             2.10 Visualizations      81




Figure 2.28 Median, mean, standard deviation, percentiles
