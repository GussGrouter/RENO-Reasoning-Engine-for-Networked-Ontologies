even more instructions can make forward progress with each clock cycle. This CPU architecture is called superscalar and is typically used with pipelining to achieve a high instruction
throughput.
The instruction width describes the target number of instructions to process in parallel. Modern
processors are 3-wide or 4-wide, meaning they can complete up to three or four instructions per
cycle. How this works depends on the processor, as there may be different numbers of functional
units for each stage.

6.3.5 Instruction Size
Another instruction characteristic is the instruction size: for some processor architectures it is
variable: For example, x86, which is classified as a complex instruction set computer (CISC), allows
up to 15-byte instructions. ARM, which is a reduced instruction set computer (RISC), has 4 byte
instructions with 4-byte alignment for AArch32/A32, and 2- or 4-byte instructions for ARM
Thumb.


6.3

Concepts

6.3.6 SMT
Simultaneous multithreading makes use of a superscalar architecture and hardware multithreading support (by the processor) to improve parallelism. It allows a CPU core to run more
than one thread, effectively scheduling between them during instructions, e.g., when one
instruction stalls on memory I/O. The kernel presents these hardware threads as virtual CPUs,
and schedules threads and processes on them as usual. This was introduced and pictured in
Section 6.2.1, CPU Architecture.
An example implementation is Intel’s Hyper-Threading Technology, where each core often has
two hardware threads. Another example is POWER8, which has eight hardware threads per core.
The performance of each hardware thread is not the same as a separate CPU core, and depends
on the workload. To avoid performance problems, kernels may spread out CPU load across cores
so that only one hardware thread on each core is busy, avoiding hardware thread contention.
Workloads that are stall cycle-heavy (low IPC) may also have better performance than those that
are instruction-heavy (high IPC) because stall cycles reduce core contention.

6.3.7

IPC, CPI

Instructions per cycle (IPC) is an important high-level metric for describing how a CPU is spending its clock cycles and for understanding the nature of CPU utilization. This metric may also be
expressed as cycles per instruction (CPI), the inverse of IPC. IPC is more often used by the Linux
community and by the Linux perf(1) profiler, and CPI more often used by Intel and elsewhere. 3
A low IPC indicates that CPUs are often stalled, typically for memory access. A high IPC indicates that CPUs are often not stalled and have a high instruction throughput. These metrics
suggest where performance tuning efforts may be best spent.
Memory-intensive workloads, for example, may be improved by installing faster memory (DRAM),
improving memory locality (software configuration), or reducing the amount of memory I/O.
Installing CPUs with a higher clock rate may not improve performance to the degree expected,
as the CPUs may need to wait the same amount of time for memory I/O to complete. Put differently, a faster CPU may mean more stall cycles but the same rate of completed instructions
per second.
The actual values for high or low IPC are dependent on the processor and processor features and
can be determined experimentally by running known workloads. As an example, you may find
that low-IPC workloads run with an IPC at 0.2 or lower, and high IPC workloads run with an
IPC of over 1.0 (which is possible due to instruction pipelining and width, described earlier). At
Netflix, cloud workloads range from an IPC of 0.2 (considered slow) to 1.5 (considered good).
Expressed as CPI, this range is 5.0 to 0.66.
It should be noted that IPC shows the efficiency of instruction processing, but not of the instructions themselves. Consider a software change that added an inefficient software loop, which
operates mostly on CPU registers (no stall cycles): such a change may result in a higher overall
IPC, but also higher CPU usage and utilization.

3

In the first edition of this book I used CPI; I’ve since switched to working more on Linux, including switching to IPC.

225
