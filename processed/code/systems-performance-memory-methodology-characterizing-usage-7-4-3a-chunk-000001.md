7.4.3 Characterizing Usage
Characterizing memory usage is an important exercise when capacity planning, benchmarking, and simulating workloads. It can also lead to some of the largest performance gains from
finding and correcting misconfigurations. For example, a database cache may be configured too
small and have low hit rates, or too large and cause system paging.
For memory, characterizing usage involves identifying where and how much memory is used:
■

System-wide physical and virtual memory utilization

■

Degree of saturation: swapping and OOM killing

■

Kernel and file system cache memory usage

■

Per-process physical and virtual memory usage

■

Usage of memory resource controls, if present

This example description shows how these attributes can be expressed together:
The system has 256 Gbytes of main memory, which has 1% in use (utilized) by processes
and 30% in the file system cache. The largest process is a database, consuming 2 Gbytes
of main memory (RSS), which is its configured limit from the previous system it was
migrated from.
These characteristics can vary over time as more memory is used to cache working data. Kernel
or application memory may also grow continually over time due to a memory leak—a software
error—aside from regular cache growth.
