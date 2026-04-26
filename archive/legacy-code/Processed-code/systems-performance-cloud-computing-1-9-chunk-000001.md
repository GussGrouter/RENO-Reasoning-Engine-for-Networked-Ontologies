# systems-performance-cloud-computing-1-9 (chunk 000001)

# Systems Performance — 1.9 Cloud Computing (intro only) (PDF pages 52–54)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-experimentation-1-8-p52-54.md
- Slice: 1.9 Cloud Computing (intro only)

---

1.9 Cloud Computing
     Cloud computing, a way to deploy computing resources on demand, has enabled rapid scaling
     of applications by supporting their deployment across an increasing number of small virtual
     systems called instances. This has decreased the need for rigorous capacity planning, as more
     capacity can be added from the cloud at short notice. In some cases it has also increased the
     desire for performance analysis, because using fewer resources can mean fewer systems. Since
     cloud usage is typically charged by the minute or hour, a performance win resulting in fewer
     systems can mean immediate cost savings. Compare this scenario to an enterprise data center,
     where you may be locked into a fixed support contract for years, unable to realize cost savings
     until the contract has ended.

New difficulties caused by cloud computing and virtualization include the management of
     performance effects from other tenants (sometimes called performance isolation) and physical
     system observability from each tenant. For example, unless managed properly by the system,
     disk I/O performance may be poor due to contention with a neighbor. In some environments,
     the true usage of the physical disks may not be observable by each tenant, making identification
     of this issue difficult.

These topics are covered in Chapter 11, Cloud Computing.

5
      The output uses the term “Bandwidth,” a common misuse. Bandwidth refers to the maximum possible throughput,
     which iperf(1) is not measuring. iperf(1) is measuring the current rate of its network workload: its throughput.
                                                                                        1.10 Methodologies            15
