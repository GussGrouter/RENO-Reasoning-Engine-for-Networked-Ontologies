<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

6.3.10

Saturation

A CPU at 100% utilization is saturated, and threads will encounter scheduler latency as they wait
to run on-CPU, decreasing overall performance. This latency is the time spent waiting on the
CPU run queue or other structure used to manage threads.
Another form of CPU saturation involves CPU resource controls, as may be imposed in a multitenant cloud computing environment. While the CPU may not be 100% utilized, the imposed
limit has been reached, and threads that are runnable must wait their turn. How visible this
is to users of the system depends on the type of virtualization in use; see Chapter 11, Cloud
Computing.

6.3

Concepts

A CPU running at saturation is less of a problem than other resource types, as higher-priority
work can preempt the current thread.

6.3.11 Preemption
Preemption, introduced in Chapter 3, Operating Systems, allows a higher-priority thread to
preempt the currently running thread and begin its own execution instead. This eliminates the
run-queue latency for higher-priority work, improving its performance.

