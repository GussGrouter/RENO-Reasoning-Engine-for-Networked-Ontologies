# Systems Performance — scalability (2.3.9) (PDF pages 70–75)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-scalability-scout-p70-75.md
- Slice: from `2.3.9 Scalability` up to before `2.3.10 Metrics`

---

2.3.9     Scalability
The performance of the system under increasing load is its scalability. Figure 2.6 shows a typical
throughput profile as a system’s load increases.




Figure 2.6 Throughput versus load

For some period, linear scalability is observed. A point is then reached, marked with a dotted
line, where contention for a resource begins to degrade throughput. This point can be described
as a knee point, as it is the boundary between two functions. Beyond this point, the throughput
profile departs from linear scalability, as contention for the resource increases. Eventually the
overheads for increased contention and coherency cause less work to be completed and through-
put to decrease.

This point may occur when a component reaches 100% utilization: the saturation point. It may
also occur when a component approaches 100% utilization and queueing begins to be frequent
and significant.

An example system that may exhibit this profile is an application that performs heavy com-
putation, with more load added as additional threads. As the CPUs approach 100% utilization,
response time begins to degrade as CPU scheduler latency increases. After peak performance, at
100% utilization, throughput begins to decrease as more threads are added, causing more con-
text switches, which consume CPU resources and cause less actual work to be completed.

The same curve can be seen if you replace “load” on the x-axis with a resource such as CPU cores.
For more on this topic, see Section 2.6, Modeling.

The degradation of performance for nonlinear scalability, in terms of average response time or
latency, is graphed in Figure 2.7 [Cockcroft 95].
32   Chapter 2 Methodologies




     Figure 2.7 Performance degradation

     Higher response time is, of course, bad. The “fast” degradation profile may occur for memory
     load, when the system begins moving memory pages to disk to free main memory. The “slow”
     degradation profile may occur for CPU load.

     Another “fast” profile example is disk I/O. As load (and the resulting disk utilization) increases,
     I/O becomes more likely to queue behind other I/O. An idle rotational (not solid state) disk may
     serve I/O with a response time of about 1 ms, but when load increases, this can approach 10 ms.
     This is modeled in Section 2.6.5, Queueing Theory, under M/D/1 and 60% Utilization, and disk
     performance is covered in Chapter 9, Disks.

     Linear scalability of response time could occur if the application begins to return errors when
     resources are unavailable, instead of queueing work. For example, a web server may return 503
     “Service Unavailable” instead of adding requests to a queue, so that those requests that are
     served can be performed with a consistent response time.
