# network-algorithmics-3-3-1-systems-principles (chunk 000002)

tion. For example, Chef Charlie postpones dishwashing to the end of the day. While precomputation
  is computing before the need, lazy evaluation is computing only when needed.
  A famous example of lazy evaluation in systems is copy-on-write in the Mach operating system. Sup-
  pose we have to copy a virtual address space A to another space, B, for process migration. A general
  solution is to copy all pages in A to B to allow for pages in B to be written independently. Instead,
  copy-on-write makes page table entries in B’s virtual address space point to the corresponding page
  in A. When a process using B writes to a location, then a separate copy of the corresponding page in
  A is made for B, and the write is performed. Since we expect the number of pages that are written
  in B to be small compared to the total number of pages, this avoids unnecessary copying.
  A simple networking example occurs when a network packet arrives at an endnode X in a different
  byte order than X’s native byte order. Rather than swap all bytes immediately, it can be more efficient
  to wait to swap the bytes that are actually read.
• P2c: Share Expenses. This refers to taking advantage of expensive operations done by other parts
  of the system. An important example of expense sharing is batching, where several expensive op-
  erations can be done together more cheaply than doing each separately. For example, Charlie bakes
  several pies in one batch. Computer systems have used batch processing for years, especially in the
  early days of mainframes, before time sharing. Batching trades latency for throughput. A simple
  networking example of expense sharing is timing wheels (Chapter 7), where the timer data structure
  shares expensive per-clock-tick processing with the routine that updates the time-of-day clock.

P3: Relax system requirements
When a system is first designed top-down, functions are partitioned among subsystems. After fixing
subsystem requirements and interfaces, individual subsystems are designed. When implementation dif-
ficulties arise, the basic system structure may have to be redone, as shown in Fig. 3.8.
    As shown in Chapter 1, implementation difficulties (e.g., implementing a divide) can sometimes be
solved by relaxing the specification requirements for, say, Subsystem 1. This is shown in the figure by
weakening the specification of Subsystem 1 from, say, S to W , but at the cost of making Subsystem 2
obey a stronger property, Q, compared to the previous property, P .
    Three techniques that arise from this principle are distinguished by how they relax the original
subsystem specification.

---

## PDF page 87

60        Chapter 3 Fifteen implementation principles
