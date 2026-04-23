# network-algorithmics-6-5-2-data-plane-development-kit-dpdk (chunk 000001)

# Network Algorithmics — 6.5.2 Data Plane Development Kit (DPDK) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 196
- Slice: from `6.5.2 Data Plane Development Kit (DPDK)` up to next detected section heading

---

6.5.2 Data Plane Development Kit (DPDK)
While there have been other open source proposals for Kernel Bypass and user space network im-
plementations such as netmap (Rizzo and Landi, 2011), the canonical kernel bypass mechanism is

170      Chapter 6 Transferring control

no longer VIA but DPDK (Data Plane Development kit) (DPDK, 2018). DPDK is a set of libraries
that high performance applications can include to bypass the kernel to realize the Application Device
Channel idea introduced earlier. However, DPDK goes further with several optimizations.
    First, DPDK relies on polling instead of interrupts to receive packets, an idea that we will see again
in Section 6.7. Second, DPDK does not use general purpose OS buffer mechanisms but preallocates
packet buffers so as not to incur the overhead of allocation or deallocation of memory as packets are
sent and received. Third, there is no copying of data between user and kernel memory spaces as a packet
is copied once to memory via DMA by the NIC, and this memory location is used by DPDK and the
applications—thus DPDK is also a zero-copy interface. Fourth, the overhead of processing packets can
be amortized over batches of packets with one API call on reception and sending. Fifth, DPDK uses
very large page table sizes (DPDK, 2018) (so-called “hugepages” of say 1GB in size) compared to
classical memory pages (4K in many platforms). This reduces the load on the cache used to translate
virtual to physical addresses—Translation Lookaside Buffers (TLBs). This in turn reduces TLB misses.
There are also several other optimizations, for instance to align memory cache lines. In addition, DPDK
has a host of libraries for network processing including for longest matching prefix and exact match.
    Note that while DPDK is now part of the Linux Foundation and is an open-source Linux project, it
is not the canonical Linux network stack analyzed in Cai et al. (2021). High performance applications
must choose to bypass the Linux stack using DPDK. Note also that many of the ideas in DPDK and
related schemes have flowed into the standard networking stack. For example, batching is done in
Linux using various batching mechanisms on the sending and the receiving sides like GSO (Generic
Sender Offload) (Ousterhout, 2021) where the transport protocol creates a single large packet to traverse
the stack and reduce system call overhead. Similarly, the Linux networking stack now uses NAPI (New
API) (Salim et al., 2001) to use some combination of polling and interrupts as we will see in Section 6.7.
    DPDK is also used in the storage space to improve performance with the advent of fast non-volatile
memories that have much lower latencies than classic disk storage. For such storage (e.g., SSDs or Solid
State Disks) the kernel overhead consumes a large fraction of media latency. Thus the SPDK (Storage
Processing Development Kit) (spdk, 2022) framework builds on DPDK to offer a set of storage specific
libraries that leverage DPDK for fast storage processing and kernel bypass.
