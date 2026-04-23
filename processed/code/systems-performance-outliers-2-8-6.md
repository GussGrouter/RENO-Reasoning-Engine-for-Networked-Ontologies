# Systems Performance — outliers (2.8.6) (outliers-2-8-6) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

2.8.6      Outliers
Another statistical problem is the presence of outliers: a very small number of extremely high or
low values that don’t appear to fit the expected distribution (single- or multimode).

Disk I/O latency outliers are an example—very occasional disk I/O that can take over 1,000 ms,
when the majority of disk I/O is between 0 and 10 ms. Latency outliers like these can cause
serious performance problems, but their presence can be difficult to identify from most metric
types, other than as a maximum. Another example is network I/O latency outliers caused by
TCP timer-based retransmits.

For a normal distribution, the presence of outliers is likely to shift the mean by a little, but not
the median (which may be useful to consider). The standard deviation and 99th percentile have
a better chance of identifying outliers, but this is still dependent on their frequency.

To better understand multimodal distributions, outliers, and other complex yet common
behaviors, inspect the full distribution, for example by using a histogram. See Section 2.10,
Visualizations, for more ways to do this.
