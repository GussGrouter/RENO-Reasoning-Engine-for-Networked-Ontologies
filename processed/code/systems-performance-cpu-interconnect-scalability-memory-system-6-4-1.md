<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

Interconnects
For multiprocessor architectures, processors are connected using either a shared system bus or a
dedicated interconnect. This is related to the memory architecture of the system, uniform memory access (UMA) or NUMA, as discussed in Chapter 7, Memory.
A shared system bus, called the front-side bus, used by earlier Intel processors is illustrated by the
four-processor example in Figure 6.9.

235

236

Chapter 6 CPUs

Figure 6.9 Example Intel front-side bus architecture, four-processor
The use of a system bus has scalability problems when the processor count is increased, due to
contention for the shared bus resource. Modern servers are typically multiprocessor, NUMA,
and use a CPU interconnect instead.
Interconnects can connect components other than processors, such as I/O controllers. Example
interconnects include Intel’s Quick Path Interconnect (QPI), Intel’s Ultra Path Interconnect
(UPI), AMD’s HyperTransport (HT), ARM’s CoreLink Interconnects (there are three different
types), and IBM’s Coherent Accelerator Processor Interface (CAPI). An example Intel QPI architecture for a four-processor system is shown in Figure 6.10.

Figure 6.10 Example Intel QPI architecture, four-processor

6.4

Architecture

The private connections between processors allow for non-contended access and also allow
higher bandwidths than the shared system bus. Some example speeds for Intel FSB and QPI are
shown in Table 6.4 [Intel 09][Mulnix 17].

Table 6.4

Intel CPU interconnect example bandwidths

Intel

Transfer Rate

Width

Bandwidth

FSB (2007)

1.6 GT/s

8 bytes

12.8 Gbytes/s

QPI (2008)

6.4 GT/s

2 bytes

25.6 Gbytes/s

UPI (2017)

10.4 GT/s

2 bytes

41.6 Gbytes/s

To explain how transfer rates can relate to bandwidth, I will explain the QPI example, which is
for a 3.2 GHz clock. QPI is double-pumped, performing a data transfer on both rising and falling
edges of the clock.4 This doubles the transfer rate (3.2 GHz × 2 = 6.4 GT/s). The final bandwidth
of 25.6 Gbytes/s is for both send and receive directions (6.4 GT/s × 2 byte width × 2 directions =
25.6 Gbytes/s).
An interesting detail of QPI is that its cache coherency mode could be tuned in the BIOS, with
options including Home Snoop to optimize for memory bandwidth, Early Snoop to optimize
for memory latency, and Directory Snoop to improve scalability (it involves tracking what is
shared). UPI, which is replacing QPI, only supports Directory Snoop.
Apart from external interconnects, processors have internal interconnects for core
communication.
Interconnects are typically designed for high bandwidth, so that they do not become a systemic
bottleneck. If they do, performance will degrade as CPU instructions encounter stall cycles for
operations that involve the interconnect, such as remote memory I/O. A key indicator for this is
a drop in IPC. CPU instructions, cycles, IPC, stall cycles, and memory I/O can be analyzed using
CPU performance counters.

