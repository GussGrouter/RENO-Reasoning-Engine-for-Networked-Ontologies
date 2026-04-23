# systems-performance-static-performance-tuning-2-5-17 (chunk 000001)

# Systems Performance — static performance tuning (2.5.17) (PDF pages 96–104)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-drilldown-latency-methodr-scout-p96-104.md

---

2.5.17       Static Performance Tuning
Static performance tuning focuses on issues of the configured architecture. Other methodol-
ogies focus on the performance of the applied load: the dynamic performance [Elling 00]. Static
performance analysis can be performed when the system is at rest and no load is applied.

For static performance analysis and tuning, step through all the components of the system and
check the following:

    ■   Does the component make sense? (outdated, underpowered, etc.)
    ■   Does the configuration make sense for the intended workload?
    ■   Was the component autoconfigured in the best state for the intended workload?
    ■   Has the component experienced an error such that it is now in a degraded state?

Here are some examples of issues that may be found using static performance tuning:

    ■   Network interface negotiation: selecting 1 Gbits/s instead of 10 Gbit/s
    ■   Failed disk in a RAID pool
    ■   Older version of the operating system, applications, or firmware used
60   Chapter 2 Methodologies


         ■   File system nearly full (can cause performance issues)
         ■   Mismatched file system record size compared to workload I/O size
         ■   Application running with a costly debug mode accidentally left enabled
         ■   Server accidentally configured as a network router (IP forwarding enabled)
         ■   Server configured to use resources, such as authentication, from a remote data center
             instead of locally

     Fortunately, these types of issues are easy to check for; the hard part is remembering to do it!
