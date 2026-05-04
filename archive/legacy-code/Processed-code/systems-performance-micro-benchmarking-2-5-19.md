# Systems Performance — micro-benchmarking (2.5.19) (micro-benchmarking-2-5-19) (PDF pages 98–106)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-cache-microbench-mantras-scout-p98-106.md

---

2.5.19 Micro-Benchmarking
     Micro-benchmarking tests the performance of simple and artificial workloads. This differs from
     macro-benchmarking (or industry benchmarking), which typically aims to test a real-world and
     natural workload. Macro-benchmarking is performed by running workload simulations and can
     become complex to conduct and understand.

     With fewer factors in play, micro-benchmarking is less complicated to conduct and understand.
     A commonly used micro-benchmark is Linux iperf(1), which performs a TCP throughput test:
     this can identify external network bottlenecks (which would otherwise be difficult to spot) by
     examining TCP counters during a production workload.
                                                                             2.5 Methodology       61


Micro-benchmarking can be performed by a micro-benchmark tool that applies the workload and
measures its performance, or you can use a load generator tool that just applies the workload,
leaving measurements of performance to other observability tools (example load generators are
in Chapter 12, Benchmarking, Section 12.2.2, Simulation). Either approach is fine, but it can be
safest to use a micro-benchmark tool and to double-check performance using other tools.

Some example targets of micro-benchmarks, including a second dimension for the tests, are:
   ■   Syscall time: For fork(2), execve(2), open(2), read(2), close(2)
   ■   File system reads: From a cached file, varying the read size from one byte to one Mbyte
   ■   Network throughput: Transferring data between TCP endpoints, for varying socket
       buffer sizes

Micro-benchmarking typically conducts the target operation as quickly as possible and measures
the time for a large number of these operations to complete. The average time can then be calcu-
lated (average time = runtime/operation count).

Later chapters include specific micro-benchmarking methodologies, listing the targets and attri-
butes to test. The topic of benchmarking is covered in more detail in Chapter 12, Benchmarking.
