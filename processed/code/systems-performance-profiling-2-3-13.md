# Systems Performance — profiling (2.3.13) (PDF pages 72–75)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-profiling-2-3-13-scout-p72-75.md
- Slice: from `2.3.13 Profiling` up to before `2.3.14 Caching`

---

2.3.13      Profiling
Profiling builds a picture of a target that can be studied and understood. In the field of comput-
ing performance, profiling is typically performed by sampling the state of the system at timed
intervals and then studying the set of samples.

Unlike the previous metrics covered, including IOPS and throughput, the use of sampling pro-
vides a coarse view of the target’s activity. How coarse depends on the rate of sampling.

As an example of profiling, CPU usage can be understood in reasonable detail by sampling the
CPU instruction pointer or stack trace at frequent intervals to gather statistics on the code paths
that are consuming CPU resources. This topic is covered in Chapter 6, CPUs.
