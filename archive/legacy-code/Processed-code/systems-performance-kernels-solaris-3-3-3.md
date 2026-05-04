# Systems Performance — Section 3.3.3 Solaris (kernels-solaris-3-3-3) (PDF pages 118–170)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch3-background-p118-170.txt

---

3.3.3 Solaris
Solaris is a Unix and BSD-derived kernel and OS created by Sun Microsystems in 1982. It was originally named SunOS and optimized for Sun workstations. By the late 1980s, AT&T developed a new
Unix standard, Unix System V Release 4 (SVR4) based on technologies from SVR3, SunOS, BSD, and
Xenix. Sun created a new kernel based on SVR4, and rebranded the OS under the name Solaris.
Major Solaris kernel developments, especially performance-related, include:
■

■

■

■

■

■

■

VFS: The virtual file system (VFS) is an abstraction and interface that allows multiple file
systems to easily coexist. Sun initially created it so that NFS and UFS could coexist. VFS is
covered in Chapter 8, File Systems.
Fully preemptible kernel: This provided low latency for high-priority work, including
real-time work.
Multiprocessor support: In the early 1990s, Sun invested heavily in multiprocessor
operating system support, developing kernel support for both asymmetric and symmetric
multiprocessing (ASMP and SMP) [Mauro 01].
Slab allocator: Replacing the SVR4 buddy allocator, the kernel slab memory allocator
provided better performance via per-CPU caches of preallocated buffers that could be
quickly reused. This allocator type, and its derivatives, has become the standard for kernels including Linux.
DTrace: A static and dynamic tracing framework and tool providing virtually unlimited
observability of the entire software stack, in real time and in production. Linux has BPF
and bpftrace for this type of observability.
Zones: An OS-based virtualization technology for creating OS instances that share one
kernel, similar to the earlier FreeBSD jails technology. OS virtualization is now in widespread use as Linux containers. See Chapter 11, Cloud Computing.
ZFS: A file system with enterprise-level features and performance. It is now available for
other OSes, including Linux. See Chapter 8, File Systems.

Oracle purchased Sun Microsystems in 2010, and Solaris is now called Oracle Solaris. Solaris is
covered in more detail in the first edition of this book.

