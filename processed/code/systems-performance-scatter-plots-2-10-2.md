# Systems Performance — scatter plots (2.10.2) (scatter-plots-2-10-2) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

2.10.2      Scatter Plots
Figure 2.29 shows disk I/O events for the same time range as a scatter plot, which enables all data
to be seen. Each disk I/O is drawn as a point, with its completion time on the x-axis and latency
on the y-axis.




Figure 2.29 Scatter plot

Now the source of the higher-than-expected average latency can be understood fully: there are
many disk I/O with latencies of 10 ms, 20 ms, even over 50 ms. The scatter plot has shown all the
data, revealing the presence of these outliers.
