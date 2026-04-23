# Systems Performance — perspectives (2.4) (PDF pages 75–82)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-profiling-caching-scout-p75-82.md
- Slice: from `2.4 Perspectives` up to before `2.5 Methodology`

---

2.4        Perspectives
There are two common perspectives for performance analysis, each with different audiences,
metrics, and approaches. They are workload analysis and resource analysis. They can be thought
of as either top-down or bottom-up analysis of the operating system software stack, as shown in
Figure 2.10.
38   Chapter 2 Methodologies




     Figure 2.10 Analysis perspectives

     Section 2.5, Methodology, provides specific strategies to apply for each. These perspectives are
     introduced here in more detail.


     2.4.1      Resource Analysis
     Resource analysis begins with analysis of the system resources: CPUs, memory, disks, network
     interfaces, buses, and interconnects. It is most likely performed by system administrators—those
     responsible for the physical resources. Activities include
         ■   Performance issue investigations: To see if a particular type of resource is responsible
         ■   Capacity planning: For information to help size new systems, and to see when existing
             system resources may become exhausted

     This perspective focuses on utilization, to identify when resources are at or approaching their
     limit. Some resource types, such as CPUs, have utilization metrics readily available. Utilization
     for other resources can be estimated based on available metrics, for example, estimating network
     interface utilization by comparing the send and receive megabits per second (throughput) with
     the known or expected maximum bandwidth.

     Metrics best suited for resource analysis include:

         ■   IOPS
         ■   Throughput
         ■   Utilization
         ■   Saturation

     These measure what the resource is being asked to do, and how utilized or saturated it is for a
     given load. Other types of metrics, including latency, are also useful to see how well the resource
     is responding for the given workload.
                                                                                2.4 Perspectives       39


Resource analysis is a common approach to performance analysis, in part thanks to the widely
available documentation on the topic. Such documentation focuses on the operating system
“stat” tools: vmstat(8), iostat(1), mpstat(1). It’s important when you read such documentation to
understand that this is one perspective, but not the only perspective.


2.4.2      Workload Analysis
Workload analysis (see Figure 2.11) examines the performance of applications: the workload
applied and how the application is responding. It is most commonly used by application devel-
opers and support staff—those responsible for the application software and configuration.




Figure 2.11 Workload analysis

The targets for workload analysis are:

    ■   Requests: The workload applied
    ■   Latency: The response time of the application
    ■   Completion: Looking for errors

Studying workload requests typically involves checking and summarizing their attributes: this is
the process of workload characterization (described in more detail in Section 2.5, Methodology). For
databases, these attributes may include the client host, database name, tables, and query string.
This data may help identify unnecessary work, or unbalanced work. Even when a system is perform-
ing its current workload well (low latency), examining these attributes may identify ways to reduce
or eliminate the work applied. Keep in mind that the fastest query is the one you don’t do at all.

Latency (response time) is the most important metric for expressing application performance.
For a MySQL database, it’s query latency; for Apache, it’s HTTP request latency; and so on. In
these contexts, the term latency is used to mean the same as response time (refer to Section 2.3.1,
Latency, for more about context).

The tasks of workload analysis include identifying and confirming issues—for example, by
looking for latency beyond an acceptable threshold—then finding the source of the latency and
confirming that the latency is improved after applying a fix. Note that the starting point is the
application. Investigating latency usually involves drilling down deeper into the application,
libraries, and the operating system (kernel).

System issues may be identified by studying characteristics related to the completion of an
event, including its error status. While a request may complete quickly, it may do so with an
error status that causes the request to be retried, accumulating latency.
40   Chapter 2 Methodologies


     Metrics best suited for workload analysis include:

        ■    Throughput (transactions per second)
        ■    Latency

     These measure the rate of requests and the resulting performance.
