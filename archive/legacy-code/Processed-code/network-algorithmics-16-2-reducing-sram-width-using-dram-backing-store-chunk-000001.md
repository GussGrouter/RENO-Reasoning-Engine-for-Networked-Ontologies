# network-algorithmics-16-2-reducing-sram-width-using-dram-backing-store (chunk 000001)

# Network Algorithmics — 16.2 Reducing SRAM width using DRAM backing store (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 480
- Slice: from `16.2 Reducing SRAM width using DRAM backing store` up to next detected section heading

---

16.2 Reducing SRAM width using DRAM backing store
The next few sections ignore the general measurement problem and concentrate on the specific problem
of packet counting. The simplest way to implement packet counting is shown in Fig. 16.1. One SRAM
location is used for each of, say, 1 million 64-bit counters. When a packet arrives, the corresponding
flow counter (say, based on the destination) is incremented.
    Given that such large amounts of SRAM are expensive and infeasible, is it required? If a packet ar-
rives, say, every 8 nanoseconds, some SRAM counter must be accessed, as opposed to, say, 40 nanosec-
onds DRAM. However, intuitively keeping a full 64-bit SRAM location is an obvious waste (P1).
    Instead, the best hardware features of DRAM and SRAM can be combined (P5c). DRAM is cur-
rently roughly two orders of magnitude cheaper costly. On the other hand, DRAM is slow. This is
exactly analogous to the memory hierarchy in a computer. The analogy suggests that DRAM and SRAM
can be combined to provide a solution that is both cheap and fast.
    Observe that, if the router keeps a 64-bit DRAM backing location for each counter and a much
smaller width (say, 12 bits) for each SRAM counter, then the counter system will be accurate as long as
every SRAM counter is backed up (i.e., flushed) to DRAM before the smaller SRAM counter overflows.
This scheme is depicted in Fig. 16.2. What is missing, however, is a good algorithm (P15) for deciding
when and how to flush SRAM counters.
    Assume that the chip maintaining counters is allowed to dump some SRAM counter to DRAM every
b SRAM accesses. b is chosen to be large enough that b SRAM access times correspond to 1 DRAM
access time. In other words, b is the ratio of DRAM access speed to SRAM access speed. In terms of
the smallest SRAM width required, Shah et al. (2002a) show that, under this algorithmic framework
of “pick-a-counter-to-flush,” the conditionally optimal counter-management algorithm is to flush the

454       Chapter 16 Measuring network traffic

FIGURE 16.2
Using large DRAM counters as a backing store for small SRAM counters, reducing overall cost. For correctness, an
SRAM counter must be flushed to DRAM before it overflows.
