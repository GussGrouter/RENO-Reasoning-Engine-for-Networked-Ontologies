# Systems Performance — Section 3.3.2 BSD (kernels-bsd-3-3-2) (PDF pages 118–170)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch3-background-p118-170.txt

---

3.3.2 BSD
The Berkeley Software Distribution (BSD) OS began as enhancements to Unix 6th Edition at
the University of California, Berkeley, and was first released in 1978. As the original Unix code
required an AT&T software license, by the early 1990s this Unix code had been rewritten in BSD
under a new BSD license, allowing free distributions including FreeBSD.
Major BSD kernel developments, especially performance-related, include:
■

■

■

■

■

■

■

Paged virtual memory: BSD brought paged virtual memory to Unix: instead of swapping
out entire processes to free main memory, smaller least-recently-used chunks of memory
could be moved (paged). See Chapter 7, Memory, Section 7.2.2, Paging.
Demand paging: This defers the mapping of physical memory to virtual memory to
when it is first written, avoiding an early and sometimes unnecessary performance and
memory cost for pages that may never be used. Demand paging was brought to Unix by
BSD. See Chapter 7, Memory, Section 7.2.2, Paging.
FFS: The Berkeley Fast File System (FFS) grouped disk allocation into cylinder groups,
greatly reducing fragmentation and improving performance on rotational disks, as well as
supporting larger disks and other enhancements. FFS became the basis for many other file
systems, including UFS. See Chapter 8, File Systems, Section 8.4.5, File System Types.
TCP/IP network stack: BSD developed the first high-performance TCP/IP network stack
for Unix, included in 4.2BSD (1983). BSD is still known for its performant network stack.
Sockets: Berkeley sockets are an API for connection endpoints. Included in 4.2BSD, they
have become a standard for networking. See Chapter 10, Network.
Jails: Lightweight OS-level virtualization, allowing multiple guests to share one kernel.
Jails were first released in FreeBSD 4.0.
Kernel TLS: As transport layer security (TLS) is now commonly used on the Internet,
kernel TLS moves much of TLS processing to the kernel, improving performance14
[Stewart 15].

While not as popular as Linux, BSD is used for some performance-critical environments, including for the Netflix content delivery network (CDN), as well as file servers from NetApp, Isilon,
and others. Netflix summarized FreeBSD performance on its CDN in 2019 as [Looney 19]:
“Using FreeBSD and commodity parts, we achieve 90 Gb/s serving TLS-encrypted
connections with ~55% CPU on a 16-core 2.6-GHz CPU.”
There is an excellent reference on the internals of FreeBSD, from the same publisher that brings
you this book: The Design and Implementation of the FreeBSD Operating System, 2nd Edition
[McKusick 15].

14

Developed to improve the performance of the Netflix FreeBSD open connect appliances (OCAs) that are the
Netflix CDN.

113

114

Chapter 3 Operating Systems

