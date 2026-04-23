# Systems Performance — 2.3.8 Load vs. Architecture (PDF pages 68–72)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-concepts-2-3-6-to-2-3-8-p68-72.md
- Slice: 2.3.8 Load vs. Architecture

---

2.3.8     Load vs. Architecture
     An application can perform badly due to an issue with the software configuration and hardware
     on which it is running: its architecture and implementation. However, an application can also
     perform badly simply due to too much load being applied, resulting in queueing and long laten-
     cies. Load and architecture are pictured in Figure 2.5.




     Figure 2.5 Load versus architecture

     If analysis of the architecture shows queueing of work but no problems with how the work is per-
     formed, the issue may be too much load applied. In a cloud computing environment, this is the
     point where more server instances can be introduced on demand to handle the work.

     For example, an issue of architecture may be a single-threaded application that is busy on-CPU,
     with requests queueing while other CPUs are available and idle. In this case, performance is
                                                                                   2.3   Concepts     31


limited by the application’s single-threaded architecture. Another issue of architecture may be
a multi-threaded program that contends for a single lock, such that only one thread can make
forward progress while others wait.

An issue of load may be a multithreaded application that is busy on all available CPUs, with
requests still queueing. In this case, performance is limited by the available CPU capacity, or put
differently, by there being more load than the CPUs can handle.
