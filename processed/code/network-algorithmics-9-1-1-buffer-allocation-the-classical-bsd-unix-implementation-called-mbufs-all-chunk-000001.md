# network-algorithmics-9-1-1-buffer-allocation-the-classical-bsd-unix-implementation-called-mbufs-all (chunk 000001)

# Network Algorithmics — 9.1.1 Buffer allocation The classical BSD UNIX implementation, called mbufs, allowed a single packet to be stored as a linear (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 239
- Slice: from `9.1.1 Buffer allocation The classical BSD UNIX implementation, called mbufs, allowed a single packet to be stored as a linear` up to next detected section heading

---

9.1.1 Buffer allocation
The classical BSD UNIX implementation, called mbufs, allowed a single packet to be stored as a linear
list of smaller buffers, where a buffer is a contiguous area of memory.1 The motivation for this technique

1 Craig Partridge attributes the invention of mbufs to Rob Gurwitz (Partridge et al., 2004).

9.1 Buffer management             213

is to allow the space allocated to the packet to grow and shrink (for example, as it passes up and down
the stack). For instance, it is easy to grow a packet by prepending a new mbuf to the current chain of
mbufs. For even more flexibility, BSD mbufs come in three flavors: two small sizes (100 and 108 bytes)
and one large size (2048 bytes, called a cluster).
    Besides allowing dynamic expansion of a packet’s allocated memory, mbufs make efficient use
of memory, something that was important around 1981, when mbufs were invented. For example, a
packet of 190 bytes would be allocated two mbufs (wasting around 20 bytes), while a packet of 450
bytes would be allocated five mbufs (wasting around 50 bytes).
    However, dynamic expansion of a packet’s size may be less important than it sounds because the
header sizes for important packet paths (e.g., Ethernet, IP, TCP) are well known and can be preallocated.
Similarly, saving memory may be less important in workstations today than increasing the speed of
packet processing. On the other hand, the mbuf implementation makes accessing and copying data
much harder because it may require traversing the list.
    Thus very early on, Van Jacobson designed a prototype kernel that used what we called pbufs. As
Jacobson puts it in an email note (Jacobson, 1993): “There is exactly one, contiguous, packet per pbuf
(none of that mbuf chain stupidity).”
    While pbufs have sunk into oblivion, the Linux operating system currently uses a very similar idea
(Cox, 1996) for network buffers called sk_buf. These buffers, like pbufs, are linear buffers with space
saved in advance for any packet headers that need to be added later. At times, this will incur wasted
space to handle the worst-case headers, but the simpler implementation makes this worthwhile. Both
sk_bufs and pbufs relax the specification of a buffer to avoid unnecessary generality (P7) and trade
memory for time (P4b).
    Given that the use of linear buffer sizes, as in Linux, is a good idea, how do we allocate memory for
packets of various sizes? Dynamic memory allocation is a hard problem in general because users (e.g.,
TCP connections) deallocate at different times, and these deallocations can fragment memory into a
patchwork of holes of different sizes.
    The standard textbook algorithms, such as First-Fit and Best-Fit (Wilson et al., 1995), effectively
stroll through memory, looking for a hole of the appropriate size. Any implementor of a high-speed net-
working implementation, say, TCP, should be filled with horror at the thought of using such allocators.
Instead, the following three allocators should be considered.
