<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs begins in this extract) -->

Chapter 6 CPUs

Figure 6.2 CPU cache sizes

6.2.3

CPU Run Queues

Figure 6.3 shows a CPU run queue, which is managed by the kernel scheduler.

Figure 6.3 CPU run queue
The thread states shown in the figure, ready to run and on-CPU, are covered in Figure 3.8 in
Chapter 3, Operating Systems.
The number of software threads that are queued and ready to run is an important performance
metric indicating CPU saturation. In this figure (at this instant) there are four, with an additional thread running on-CPU. The time spent waiting on a CPU run queue is sometimes called
run-queue latency or dispatcher-queue latency. In this book, the term scheduler latency is often used,
as it is appropriate for all schedulers, including those that do not use queues (see the discussion
of CFS in Section 6.4.2, Software).
For multiprocessor systems, the kernel typically provides a run queue for each CPU, and aims to
keep threads on the same run queue. This means that threads are more likely to keep running
on the same CPUs where the CPU caches have cached their data. These caches are described as
having cache warmth, and this strategy to keep threads running on the same CPUs is called CPU
