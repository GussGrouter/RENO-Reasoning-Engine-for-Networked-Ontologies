# Systems Performance — Section 3.5.3 Microkernels and Hybrid Kernels (microkernels-hybrid-3-5-3) (PDF pages 118–170)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch3-background-p118-170.txt

---

3.5.3 Microkernels and Hybrid Kernels
Most of this chapter discusses Unix-like kernels, also described as monolithic kernels, where all
the code that manages devices runs together as a single large kernel program. For the microkernel
model, kernel software is kept to a minimum. A microkernel supports essentials such as memory
management, thread management, and inter-process communication (IPC). File systems, the
network stack, and drivers are implemented as user-mode software, which allows those usermode components to be more easily modified and replaced. Imagine not only choosing which
database or web server to install, but also choosing which network stack to install. The microkernel is also more fault-tolerant: a crash in a driver does not crash the entire kernel. Examples
of microkernels include QNX and Minix 3.
A disadvantage with microkernels is that there are additional IPC steps for performing I/O
and other functions, reducing performance. One solution for this is hybrid kernels, which combine the benefits of microkernels and monolithic kernels. Hybrid kernels move performancecritical services back into kernel space (with direct function calls instead of IPC) as they are
with a monolithic kernel, but retains the modular design and fault tolerance of a micro kernel.
Examples of hybrid kernels include the Windows NT kernel and the Plan 9 kernel.

