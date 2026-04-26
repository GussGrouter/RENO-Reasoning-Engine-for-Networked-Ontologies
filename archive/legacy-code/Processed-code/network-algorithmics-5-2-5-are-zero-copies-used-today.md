# Network Algorithmics — 5.2.5 Are zero copies used today? (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 152
- Slice: from `5.2.5 Are zero copies used today?` up to next detected section heading

---

5.2.5 Are zero copies used today?
Much has transpired since the first edition, and the general consensus so far has been that, at least
for general purpose operating systems like Linux, zero copy implementations are not worthwhile. The
overhead of page mapping seems too much compared to simply copying data from the application to the
kernel (A reworked TCP zero-copy receive API, 2018) for the same reasons that Druschel and Peterson
found many years ago. This is particularly true because early studies found that the major overhead was
protocol processing.
    However, things may be changing. A paper (Cai et al., 2021) shows that as we move to 100 Gbps
after doing all the major optimizations (e.g., large MTU sizes called jumbo frames and a form of batch-
ing called segmentation offload we will study in the next chapter), throughput for the Linux network
stack saturates at around 42 Gbps per core. The major bottleneck that remains is the data copy from the
kernel to user space and vice versa. The same paper (Cai et al., 2021) suggests that the time may be ripe


6 The Genie experiments were done on an ATM network, where the virtual circuit identifier can provide a quick mapping to the
path.

126      Chapter 5 Copying data



to reconsider recent zero-copy implementation proposals via page table mappings in Linux, both at the
receive side (A reworked TCP zero-copy receive API, 2018) and at the sender side (sendmsg, 2022).
    A sender side proposal for zero-copy by De Bruijn (sendmsg) uses the ideas described earlier in this
chapter. Once again, the assumption is that the application must lock and take care not to reuse a buffer
that is mapped while the kernel is using the buffer. The application can tell when it is safe to reuse
the buffer pages by a notification message that the kernel places in the error queue associated with the
socket, with sequence numbers allowing notifications to be matched to completed send calls.
    The proposed receive side fix is more complicated because the kernel must place the received packet
in a general buffer, determine the application it is destined for, and then map the buffer to the appli-
cation’s user space. As we have seen before in this chapter, this requires a network adaptor or NIC
to separate the headers from the data, and place the data aligned with a page. Dumazet’s patch (A
reworked TCP zero-copy receive API, 2018) sets the MTU to 61,512—this allows fifteen 4096-byte
pages of data, together with 40 bytes for IPv6 and 32 bytes for TCP. The interesting general idea in this
patch is that rather than using memory mapping (mmap()) for a file, it implements mmap() for TCP
sockets. Benchmarking in a controlled setting shows a potential reduction of 3X in the processing time
per Mbyte (A reworked TCP zero-copy receive API, 2018).
    Note that none of these recent proposals use the further optimizations suggested in this chapter such
as fbufs to amortize the cost of page mapping over a sequence of calls. Further, they are only being
considered, with no serious deployment at the time of writing. Zero-copy mechanisms are, however,
widely deployed today as part of two other more specialized techniques. The first is the DPDK (Data
Plane Data Kit) (2018) method for kernel bypass we will study in the next chapter. The second is
systems that incorporate remote DMA as we will study next.
