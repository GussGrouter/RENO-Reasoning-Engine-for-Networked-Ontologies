# systems-performance-visual-identification-2-6-2 (chunk 000001)

# Systems Performance — visual identification (2.6.2) (visual-identification-2-6-2) (PDF pages 98–114)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-modeling-scout-p98-106.md + processed/code/systems-performance-modeling-scout-p104-114.md

---

2.6.2     Visual Identification
     When enough results can be collected experimentally, plotting them as delivered performance
     versus a scaling parameter may reveal a pattern.

     Figure 2.15 shows the throughput of an application as the number of threads is scaled. There
     appears to be a knee point around eight threads, where the slope changes. This can now be
     investigated, for example by looking at the application and system configuration for any setting
     around the value of eight.
                                                                                      2.6   Modeling   63




Figure 2.15 Scalability test results

In this case, the system was an eight-core system, each core having two hardware threads. To
further confirm that this is related to the CPU core count, the CPU effects at fewer than and
more than eight threads can be investigated and compared (e.g., IPC; see Chapter 6, CPUs). Or,
this can be investigated experimentally by repeating the scaling test on a system with a different
core count and confirming that the knee point moves as expected.

There are a number of scalability profiles to look for that may be identified visually, without
using a formal model. These are shown in Figure 2.16.

For each of these, the x-axis is the scalability dimension, and the y-axis is the resulting perfor-
mance (throughput, transactions per second, etc.). The patterns are:

    ■   Linear scalability: Performance increases proportionally as the resource is scaled. This
        may not continue forever and may instead be the early stages of another scalability
        pattern.
    ■   Contention: Some components of the architecture are shared and can be used only
        serially, and contention for these shared resources begins to reduce the effectiveness of
        scaling.
    ■   Coherence: The tax to maintain data coherency including propagation of changes begins
        to outweigh the benefits of scaling.
64   Chapter 2 Methodologies


         ■   Knee point: A factor is encountered at a scalability point that changes the scalability
             profile.
         ■   Scalability ceiling: A hard limit is reached. This may be a device bottleneck, such as a
             bus or interconnect reaching maximum throughput, or a software-imposed limit (system
             resource control).




     Figure 2.16 Scalability profiles

     While visual identification can be easy and effective, you can learn more about system scalabil-
     ity by using a mathematical model. The model may deviate from the data in an unexpected way,
     which can be useful to investigate: either there is a problem with the model, and hence with
     your understanding of the system, or the problem is in the real scalability of the system. The next
     sections introduce Amdahl’s Law of Scalability, the Universal Scalability Law, and queueing
     theory.
