# Systems Performance — standard deviation, percentiles, median (2.8.3) (standard-deviation-percentiles-median-2-8-3) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

2.8.3     Standard Deviation, Percentiles, Median
Standard deviations and percentiles (e.g., 99th percentile) are statistical techniques to provide
information on the distribution of data. The standard deviation is a measure of variance, with
larger values indicating greater variance from the average (mean). The 99th percentile shows the
point in the distribution that includes 99% of the values. Figure 2.22 pictures these for a normal
distribution, along with the minimum and maximum.




Figure 2.22 Statistical values

Percentiles such as 90th, 95th, 99th, and 99.9th are used in performance monitoring of request
latency to quantify the slowest in the population. These may also be specified in service-level
agreements (SLAs) as a way to measure that performance is acceptable for most users.

The 50th percentile, called the median, can be examined to show where the bulk of the data is.
76   Chapter 2 Methodologies
