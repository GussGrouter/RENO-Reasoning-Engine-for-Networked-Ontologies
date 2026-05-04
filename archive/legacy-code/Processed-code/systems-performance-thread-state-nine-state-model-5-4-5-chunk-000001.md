
5.4.5 Thread State Analysis
This is the first methodology I use for every performance issue, but it is also an advanced activity
on Linux. The goal is to identify at a high level where application threads are spending their
time, which solves some issues immediately, and directs the investigation of others. You can do
this by dividing each application’s thread time into a number of meaningful states.

193


194

Chapter 5 Applications

At a minimum, there are two thread states: on-CPU and off-CPU. You can identify if threads are
in the on-CPU state using standard metrics and tools (e.g., top(1)), and follow with CPU profiling or off-CPU analysis as appropriate (see Sections 5.4.1, CPU Profiling, and 5.4.2, Off-CPU
Analysis). This methodology is more effective with more states.

Nine States
This is a list of nine thread states I’ve chosen to give better starting points for analysis than the
two earlier states (on-CPU and off-CPU):
■

User: On-CPU in user mode

■

Kernel: On-CPU in kernel mode

■

Runnable: And off-CPU waiting for a turn on-CPU

■

Swapping (anonymous paging): Runnable, but blocked for anonymous page-ins

■

Disk I/O: Waiting for block device I/O: reads/writes, data/text page-ins

■

Net I/O: Waiting for network device I/O: socket reads/writes

■

Sleeping: A voluntary sleep

■

Lock: Waiting to acquire a synchronization lock (waiting on someone else)

■

Idle: Waiting for work

This nine-state model is pictured in Figure 5.6.

Figure 5.6 Nine-state thread model
Performance for an application request is improved by reducing the time in every state except
idle. Other things being equal, this would mean that application requests have lower latency,
and the application can handle more load.
