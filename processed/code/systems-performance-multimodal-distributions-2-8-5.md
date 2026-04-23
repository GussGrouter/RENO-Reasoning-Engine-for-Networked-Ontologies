# Systems Performance — multimodal distributions (2.8.5) (multimodal-distributions-2-8-5) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

2.8.5 Multimodal Distributions
     There is a problem with means, standard deviations, and percentiles, which may be obvious
     from the previous chart: they are intended for normal-like or unimodal distributions. System
     performance is often bimodal, returning low latencies for a fast code path and high latencies for
     a slow one, or low latencies for cache hits and high latencies for cache misses. There may also be
     more than two modes.

     Figure 2.23 shows the distribution of disk I/O latency for a mixed workload of reads and writes,
     which includes random and sequential I/O.




     Figure 2.23 Latency distribution

     This is presented as a histogram, which shows two modes. The mode on the left shows laten-
     cies of less than 1 ms, which is for on-disk cache hits. The right, with a peak around 7 ms, is for
                                                                                      2.9    Monitoring     77


on-disk cache misses: random reads. The average (mean) I/O latency is 3.3 ms, which is plotted
as a vertical line. This average is not the index of central tendency (as described earlier); in fact, it
is almost the opposite. As a metric, the average for this distribution is seriously misleading.

     Then there was the man who drowned crossing a stream with an average depth of
     six inches. —W. I. E. Gates

Every time you see an average used as a performance metric, especially an average latency, ask:
What is the distribution? Section 2.10, Visualizations, provides another example and shows how
effective different visualizations and metrics are at showing this distribution.
