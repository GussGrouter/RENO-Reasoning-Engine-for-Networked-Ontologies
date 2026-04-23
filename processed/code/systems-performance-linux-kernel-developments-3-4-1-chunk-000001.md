3.4.1 Linux Kernel Developments
Linux kernel developments, especially those related to performance, include the following
(many of these descriptions include the Linux kernel version where they were first introduced):
■

■

■

■

■

■

■

■

■

CPU scheduling classes: Various advanced CPU scheduling algorithms have been
developed, including scheduling domains (2.6.7) to make better decisions regarding nonuniform memory access (NUMA). See Chapter 6, CPUs.
I/O scheduling classes: Different block I/O scheduling algorithms have been developed,
including deadline (2.5.39), anticipatory (2.5.75), and completely fair queueing (CFQ)
(2.6.6). These are available in kernels up to Linux 5.0, which removed them to support
only newer multi-queue I/O schedulers. See Chapter 9, Disks.
TCP congestion algorithms: Linux allows different TCP congestion control algorithms to
be configured, and supports Reno, Cubic, and more in later kernels mentioned in this list.
See also Chapter 10, Network.
Overcommit: Along with the out-of-memory (OOM) killer, this is a strategy for doing
more with less main memory. See Chapter 7, Memory.
Futex (2.5.7): Short for fast user-space mutex, this is used to provide high-performing userlevel synchronization primitives.
Huge pages (2.5.36): This provides support for preallocated large memory pages by the
kernel and the memory management unit (MMU). See Chapter 7, Memory.
OProfile (2.5.43): A system profiler for studying CPU usage and other events, for both the
kernel and applications.
RCU (2.5.43): The kernel provides a read-copy update synchronization mechanism that
allows multiple reads to occur concurrently with updates, improving performance and
scalability for data that is mostly read.
epoll (2.5.46): A system call for efficiently waiting for I/O across many open file descriptors,
which improves the performance of server applications.

115

116

Chapter 3 Operating Systems

■

■

■

■

■

■

■

Modular I/O scheduling (2.6.10): Linux provides pluggable scheduling algorithms for
scheduling block device I/O. See Chapter 9, Disks.
DebugFS (2.6.11): A simple unstructured interface for the kernel to expose data to user
level, which is used by some performance tools.
Cpusets (2.6.12): exclusive CPU grouping for processes.
Voluntary kernel preemption (2.6.13): This process provides low-latency scheduling
without the complexity of full preemption.
inotify (2.6.13): A framework for monitoring file system events.
blktrace (2.6.17): A framework and tool for tracing block I/O events (later migrated into
tracepoints).
splice (2.6.17): A system call to move data quickly between file descriptors and pipes,
without a trip through user-space. (The sendfile(2) syscall, which efficiently moves data
between file descriptors, is now a wrapper to splice(2).)

■

Delay accounting (2.6.18): Tracks per-task delay states. See Chapter 4, Observability Tools.

■

IO accounting (2.6.20): Measures various storage I/O statistics per process.

■

DynTicks (2.6.21): Dynamic ticks allow the kernel timer interrupt (clock) to not fire
during idle, saving CPU resources and power.

■

SLUB (2.6.22): A new and simplified version of the slab memory allocator.

■

CFS (2.6.23): Completely fair scheduler. See Chapter 6, CPUs.

■

■

■

■

■

■

■

■

cgroups (2.6.24): Control groups allow resource usage to be measured and limited for
groups of processes.
TCP LRO (2.6.24): TCP Large Receive Offload (LRO) allows network drivers and hardware
to aggregate packets into larger sizes before sending them to the network stack. Linux also
supports Large Send Offload (LSO) for the send path.
latencytop (2.6.25): Instrumentation and a tool for observing sources of latency in the
operating system.
Tracepoints (2.6.28): Static kernel tracepoints (aka static probes) that instrument logical
execution points in the kernel, for use by tracing tools (previously called kernel markers).
Tracing tools are introduced in Chapter 4, Observability Tools.
perf (2.6.31): Linux Performance Events (perf) is a set of tools for performance observability, including CPU performance counter profiling and static and dynamic tracing. See
Chapter 6, CPUs, for an introduction.
No BKL (2.6.37): Final removal of the big kernel lock (BKL) performance bottleneck.
Transparent huge pages (2.6.38): This is a framework to allow easy use of huge (large)
memory pages. See Chapter 7, Memory.
KVM: The Kernel-based Virtual Machine (KVM) technology was developed for Linux by
Qumranet, which was purchased by Red Hat in 2008. KVM allows virtual operating system instances to be created, running their own kernel. See Chapter 11, Cloud Computing.

3.4 Linux

■

■

■

■

■

■

■

■

■

■

■

■

■

■

■

■

BPF JIT (3.0): A Just-In-Time (JIT) compiler for the Berkeley Packet Filter (BPF) to improve
packet filtering performance by compiling BPF bytecode to native instructions.
CFS bandwidth control (3.2): A CPU scheduling algorithm that supports CPU quotas and
throttling.
TCP anti-bufferbloat (3.3+): Various enhancements were made from Linux 3.3 onwards
to combat the bufferbloat problem, including Byte Queue Limits (BQL) for the transmission of packet data (3.3), CoDel queue management (3.5), TCP small queues (3.6), and the
Proportional Integral controller Enhanced (PIE) packet scheduler (3.14).
uprobes (3.5): The infrastructure for dynamic tracing of user-level software, used by other
tools (perf, SystemTap, etc.).
TCP early retransmit (3.5): RFC 5827 for reducing duplicate acknowledgments required
to trigger fast retransmit.
TFO (3.6, 3.7, 3.13): TCP Fast Open (TFO) can reduce the TCP three-way handshake to a
single SYN packet with a TFO cookie, improving performance. It was made the default in
3.13.
NUMA balancing (3.8+): This added ways for the kernel to automatically balance memory
locations on multi-NUMA systems, reducing CPU interconnect traffic and improving
performance.
SO_REUSEPORT (3.9): A socket option to allow multiple listener sockets to bind to the
same port, improving multi-threaded scalability.
SSD cache devices (3.9): Device mapper support for an SSD device to be used as a cache for
a slower rotating disk.
bcache (3.10): An SSD cache technology for the block interface.
TCP TLP (3.10): TCP Tail Loss Probe (TLP) is a scheme to avoid costly timer-based retransmits
by sending new data or the last unacknowledged segment after a shorter probe timeout, to
trigger faster recovery.
NO_HZ_FULL (3.10, 3.12): Also known as timerless multitasking or a tickless kernel, this
allows non-idle threads to run without clock ticks, avoiding workload perturbations
[Corbet 13a].
Multiqueue block I/O (3.13): This provides per-CPU I/O submission queues rather than
a single request queue, improving scalability especially for high IOPS SSD devices [Corbet
13b].
SCHED_DEADLINE (3.14): An optional scheduling policy that implements earliest deadline
first (EDF) scheduling [Linux 20b].
TCP autocorking (3.14): This allows the kernel to coalesce small writes, reducing the sent
packets. An automatic version of the TCP_CORK setsockopt(2).
MCS locks and qspinlocks (3.15): Efficient kernel locks, using techniques such as perCPU structures. MCS is named after the original lock inventors (Mellor-Crummey and
Scott) [Mellor-Crummey 91][Corbet 14].

117

118

Chapter 3 Operating Systems

■

■

■

■

■

■

■

■

■

■

■

■

■

■

■

Extended BPF (3.18+): An in-kernel execution environment for running secure kernelmode programs. The bulk of extended BPF was added in the 4.x series. Support for
attached to kprobes was added in 3.19, to tracepoints in 4.7, to software and hardware
events in 4.9, and to cgroups in 4.10. Bounded loops were added in 5.3, which also
increased the instruction limit to allow complex applications. See Section 3.4.4,
Extended BPF.
Overlayfs (3.18): A union mount file system included in Linux. It creates virtual file systems
on top of others, which can also be modified without changing the first. Often used for
containers.
DCTCP (3.18): The Data Center TCP (DCTCP) congestion control algorithm, which aims
to provide high burst tolerance, low latency, and high throughput [Borkmann 14a].
DAX (4.0): Direct Access (DAX) allows user space to read from persistent-memory storage
devices directly, without buffer overheads. ext4 can use DAX.
Queued spinlocks (4.2): Offering better performance under contention, these became the
default spinlock kernel implementation in 4.2.
TCP lockless listener (4.4): The TCP listener fast path became lockless, improving
performance.
cgroup v2 (4.5, 4.15): A unified hierarchy for cgroups was in earlier kernels, and considered stable and exposed in 4.5, named cgroup v2 [Heo 15]. The cgroup v2 CPU controller
was added in 4.15.
epoll scalability (4.5): For multithreaded scalability, epoll(7) avoids waking up all threads
that are waiting on the same file descriptors for each event, which caused a thunderingherd performance issue [Corbet 15].
KCM (4.6): The Kernel Connection Multiplexor (KCM) provides an efficient messagebased interface over TCP.
TCP NV (4.8): New Vegas (NV) is a new TCP congestion control algorithm suited for
high-bandwidth networks (those that run at 10+ Gbps).
XDP (4.8, 4.18): eXpress Data Path (XDP) is a BPF-based programmable fast path for
high-performance networking [Herbert 16]. An AF_XDP socket address family that can
bypass much of the network stack was added in 4.18.
TCP BBR (4.9): Bottleneck Bandwidth and RTT (BBR) is a TCP congestion control algorithm that provides improved latency and throughput over networks suffering packet loss
and bufferbloat [Cardwell 16].
Hardware latency tracer (4.9): An Ftrace tracer that can detect system latency caused by
hardware and firmware, including system management interrupts (SMIs).
perf c2c (4.10): The cache-to-cache (c2c) perf subcommand can help identify CPU cache
performance issues, including false sharing.
Intel CAT (4.10): Support for Intel Cache Allocation Technology (CAT) allowing tasks to
have dedicated CPU cache space. This can be used by containers to help with the noisy
neighbor problem.

3.4 Linux

■

■

■

■

■

■

■

■

■

■

■

■

■

■

Multiqueue I/O schedulers: BPQ, Kyber (4.12): The Budget Fair Queueing (BFQ) multiqueue I/O scheduler provides low latency I/O for interactive applications, especially for
slower storage devices. BFQ was significantly improved in 5.2. The Kyber I/O scheduler is
suited for fast multiqueue devices [Corbet 17].
Kernel TLS (4.13, 4.17): Linux version of kernel TLS [Edge 15].
MSG_ZEROCOPY (4.14): A send(2) flag to avoid extra copies of packet bytes between an
application and the network interface [Linux 20c].
PCID (4.14): Linux added support for process-context ID (PCID), a processor MMU feature
to help avoid TLB flushes on context switches. This reduced the performance cost of the
kernel page table isolation (KPTI) patches needed to mitigate the meltdown vulnerability.
See Section 3.4.3, KPTI (Meltdown).
PSI (4.20, 5.2): Pressure stall information (PSI) is a set of new metrics to show time spent
stalled on CPU, memory, or I/O. PSI threshold notifications were added in 5.2 to support
PSI monitoring.
TCP EDT (4.20): The TCP stack switched to Early Departure Time (EDT): This uses a
timing-wheel scheduler for sending packets, providing better CPU efficiency and smaller
queues [Jacobson 18].
Multi-queue I/O (5.0): Multi-queue block I/O schedulers became the default in 5.0, and
classic schedulers were removed.
UDP GRO (5.0): UDP Generic Receive Offload (GRO) improves performance by allowing
packets to be aggregated by the driver and card and passed up stack.
io_uring (5.1): A generic asynchronous interface for fast communication between applications and the kernel, making use of shared ring buffers. Primary uses include fast disk and
network I/O.
MADV_COLD, MADV_PAGEOUT (5.4): These madvise(2) flags are hints to the kernel that
memory is needed but not anytime soon. MADV_PAGEOUT is also a hint that memory can
be reclaimed immediately. These are especially useful for memory-constrained embedded
Linux devices.
MultiPath TCP (5.6): Multiple network links (e.g., 3G and WiFi) can be used to improve
the performance and reliability of a single TCP connection.
Boot-time tracing (5.6): Allows Ftrace to trace the early boot process. (systemd can provide timing information on the late boot process: see Section 3.4.2, systemd.)
Thermal pressure (5.7): The scheduler accounts for thermal throttling to make better
placement decisions.
perf flame graphs (5.8): perf(1) support for the flame graph visualization.

Not listed here are the many small performance improvements for locking, drivers, VFS, file systems, asynchronous I/O, memory allocators, NUMA, new processor instruction support, GPUs,
and the performance tools perf(1) and Ftrace. System boot time has also been improved by the
adoption of systemd.

119

120

Chapter 3 Operating Systems

The following sections describe in more detail three Linux topics important to performance:
systemd, KPTI, and extended BPF.

