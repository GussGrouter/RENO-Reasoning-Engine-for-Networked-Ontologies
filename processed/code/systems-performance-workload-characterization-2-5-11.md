# Systems Performance — workload characterization (2.5.11) (PDF pages 90–96)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-diagnosis-cycle-tools-method-scout-p90-96.md

---

2.5.11 Workload Characterization
     Workload characterization is a simple and effective method for identifying a class of issues:
     those due to the load applied. It focuses on the input to the system, rather than the resulting
     performance. Your system may have no architectural, implementation, or configuration issues
     present, but be experiencing more load than it can reasonably handle.

     Workloads can be characterized by answering the following questions:

         ■   Who is causing the load? Process ID, user ID, remote IP address?
         ■   Why is the load being called? Code path, stack trace?
         ■   What are the load characteristics? IOPS, throughput, direction (read/write), type? Include
             variance (standard deviation) where appropriate.
         ■   How is the load changing over time? Is there a daily pattern?

     It can be useful to check all of these, even when you have strong expectations about what the
     answers will be, because you may be surprised.

     Consider this scenario: You have a performance issue with a database whose clients are a pool of
     web servers. Should you check the IP addresses of who is using the database? You already expect
     them to be the web servers, as per the configuration. You check anyway and discover that the
     entire Internet appears to be throwing load at the databases, destroying their performance. You
     are actually under a denial-of-service (DoS) attack!

     The best performance wins are the result of eliminating unnecessary work. Sometimes unnec-
     essary work is caused by applications malfunctioning, for example, a thread stuck in a loop
     creating unnecessary CPU work. It can also be caused by bad configurations—for example,
     system-wide backups that run during peak hours—or even a DoS attack as described previously.
     Characterizing the workload can identify these issues, and with maintenance or reconfiguration
     they may be eliminated.

     If the identified workload cannot be eliminated, another approach may be to use system
     resource controls to throttle it. For example, a system backup task may be interfering with a
     production database by consuming CPU resources to compress the backup, and then network
     resources to transfer it. This CPU and network usage may be throttled using resource controls (if
     the system supports them) so that the backup runs more slowly without hurting the database.

     Apart from identifying issues, workload characterization can also be input for the design of
     simulation benchmarks. If the workload measurement is an average, ideally you will also collect
     details of the distribution and variation. This can be important for simulating the variety of
     workloads expected, rather than testing only an average workload. See Section 2.8, Statistics, for
     more about averages and variation (standard deviation), and Chapter 12, Benchmarking.

     Analysis of the workload also helps separate problems of load from problems of architecture,
     by identifying the former. Load versus architecture was introduced in Section 2.3.8, Load vs.
     Architecture.

     The specific tools and metrics for performing workload characterization depend on the target.
     Some applications record detailed logs of client activity, which can be the source for statistical
     analysis. They may also already provide daily or monthly reports of client usage, which can be
     mined for details.
                                                                               2.5 Methodology        55
