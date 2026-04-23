# Systems Performance — Section 3.3.1 Unix (kernels-unix-3-3-1) (PDF pages 118–170)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch3-background-p118-170.txt

---

3.3.1 Unix
Unix was developed by Ken Thompson, Dennis Ritchie, and others at AT&T Bell Labs during
1969 and the years that followed. Its exact origin was described in The UNIX Time-Sharing System
[Ritchie 74]:
The first version was written when one of us (Thompson), dissatisfied with the available computer facilities, discovered a little-used PDP-7 and set out to create a more
hospitable environment.
The developers of UNIX had previously worked on the Multiplexed Information and Computer
Services (Multics) operating system. UNIX was developed as a lightweight multitasked operating
system and kernel, originally named UNiplexed Information and Computing Service (UNICS),
as a pun on Multics. From UNIX Implementation [Thompson 78]:
The kernel is the only UNIX code that cannot be substituted by a user to his own liking.
For this reason, the kernel should make as few real decisions as possible. This does not
mean to allow the user a million options to do the same thing. Rather, it means to
allow only one way to do one thing, but have that way be the least-common divisor of
all the options that might have been provided.
While the kernel was small, it did provide some features for high performance. Processes had
scheduler priorities, reducing run-queue latency for higher-priority work. Disk I/O was performed in large (512-byte) blocks for efficiency and cached in an in-memory per-device buffer
cache. Idle processes could be swapped out to storage, allowing busier processes to run in main
memory. And the system was, of course, multitasking—allowing multiple processes to run concurrently, improving job throughput.
To support networking, multiple file systems, paging, and other features we now consider standard, the kernel had to grow. And with multiple derivatives, including BSD, SunOS (Solaris), and
later Linux, kernel performance became competitive, which drove the addition of more features
and code.

3.3

Kernels

