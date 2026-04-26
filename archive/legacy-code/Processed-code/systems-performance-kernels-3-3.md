# Systems Performance — Section 3.3 Kernels (kernels-3-3) (PDF pages 118–170)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch3-background-p118-170.txt

---

3.3 Kernels
The following sections discuss Unix-like kernel implementation details with a focus on performance. As background, the performance features of earlier kernels are discussed: Unix, BSD, and
Solaris. The Linux kernel is discussed in more detail in Section 3.4, Linux.
Kernel differences can include the file systems they support (see Chapter 8, File Systems), the
system call (syscall) interfaces, network stack architecture, real-time support, and scheduling
algorithms for CPUs, disk I/O, and networking.
Table 3.3 shows Linux and other kernel versions for comparison, with syscall counts based on
the number of entries in section 2 of the OS man pages. This is a crude comparison, but enough
to see some differences.

Table 3.3

Kernel versions with documented syscall counts

Kernel Version

Syscalls

UNIX Version 7

48

SunOS (Solaris) 5.11

142

FreeBSD 12.0

222

Linux 2.6.32-21-server

408

Linux 2.6.32-220.el6.x86_64

427

Linux 3.2.6-3.fc16.x86_64

431

Linux 4.15.0-66-generic

480

Linux 5.3.0-1010-aws

493

111

112

Chapter 3 Operating Systems

These are just the syscalls with documentation; more are usually provided by the kernel for
private use by operating system software.
UNIX had twenty system calls at the very first, and today Linux—which is a direct
descendant—has over a thousand . . . I just worry about the complexity and the size of
things that grow.
Ken Thompson, ACM Turing Centenary Celebration, 2012
Linux is growing in complexity and exposing this complexity to user-land by adding new system calls or through other kernel interfaces. Extra complexity makes learning, programming,
and debugging more time-consuming.

