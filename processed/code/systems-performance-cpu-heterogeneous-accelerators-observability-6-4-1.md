<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

GPUs
Graphics processing units (GPUs) were created to support graphical displays, and are now
finding use in other workloads including artificial intelligence, machine learning, analytics,
image processing, and cryptocurrency mining. For servers and cloud instances, a GPU is a
processor-like resource that can execute a portion of a workload, called the compute kernel, that
is suited to highly parallel data processing such as matrix transformations. General-purpose
GPUs from Nvidia using its Compute Unified Device Architecture (CUDA) have seen widespread
adoption. CUDA provides APIs and software libraries for using Nvidia GPUs.
While a processor (CPU) may contain a dozen cores, a GPU may contain hundreds or thousands
of smaller cores called streaming processors (SPs),5 which each can execute a thread. Since GPU
workloads are highly parallel, threads that can execute in parallel are grouped into thread blocks,
where they may cooperate among themselves. These thread blocks may be executed by groups of
SPs called streaming multiprocessors (SMs) that also provide other resources including a memory
cache. Table 6.6 further compares processors (CPUs) with GPUs [Ather 19].

Table 6.6

CPUs versus GPUs

Attribute

CPU

GPU

Package

A processor package plugs into
a socket on the system board,
connected directly to the system
bus or CPU interconnect.

A GPU is typically provided as an expansion
card and connected via an expansion bus (e.g.,
PCIe). They may also be embedded on a system
board or in a processor package (on-chip).

Package
scalability

Multi-socket configurations,
connected via a CPU interconnect
(e.g., Intel UPI).

Multi-GPU configurations are possible,
connected via a GPU-to-GPU interconnect (e.g.,
NVIDIA's NVLink).

Cores

A typical processor of today
contains 2 to 64 cores.

A GPU may have a similar number of streaming
multiprocessors (SMs).

Threads

A typical core may execute two
hardware threads (or more,
depending on the processor).

An SM may contain dozens or hundreds of
streaming processors (SPs). Each SP can only
execute one thread.

Caches

Each core has L2 and L2 caches,
and may share an L3 cache.

Each SM has a cache, and may share an L2
cache between them.

Clock

High (e.g., 3.4 GHz).

Relatively lower (e.g., 1.0 GHz).

Custom tools must be used for GPU observability. Possible GPU performance metrics include the
instructions per cycle, cache hit ratios, and memory bus utilization.

Other Accelerators
Apart from GPUs, be aware that other accelerators may exist for offloading CPU work to faster
application-specific integrated circuits. These include field-programmable gate arrays (FPGAs)

5

Nvidia also calls these CUDA cores [Verma 20].

6.4

Architecture

and tensor processing units (TPUs). If in use, their usage and performance should be analyzed
alongside CPUs, although they typically require custom tooling.
GPUs and FPGAs are used to improve the performance of cryptocurrency mining.
