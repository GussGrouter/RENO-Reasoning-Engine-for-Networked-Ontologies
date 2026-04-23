8.5.3 Workload Characterization
Characterizing the load applied is an important exercise when capacity planning, benchmarking, and simulating workloads. It can also lead to some of the largest performance gains by
identifying unnecessary work that can be eliminated.
Here are the basic attributes that characterize the file system workload:
■

Operation rate and operation types

■

File I/O throughput

■

File I/O size

■

Read/write ratio

■

Synchronous write ratio

■

Random versus sequential file offset access

Operation rate and throughput are defined in Section 8.1, Terminology. Synchronous writes and
random versus sequential were described in Section 8.3, Concepts.
These characteristics can vary from second to second, especially for timed application tasks that
execute at intervals. To better characterize the workload, capture maximum values as well as
averages. Better still, examine the full distribution of values over time.
Here is an example workload description, to show how these attributes can be expressed
together:
On a financial trading database, the file system has a random read workload,
averaging 18,000 reads/s with an average read size of 4 Kbytes. The total operation
rate is 21,000 ops/s, which includes reads, stats, opens, closes, and around 200
synchronous writes/s. The write rate is steady while the read rate varies, up to a peak
of 39,000 reads/s.
These characteristics may be described in terms of a single file system instance, or all instances
on a system of the same type.
