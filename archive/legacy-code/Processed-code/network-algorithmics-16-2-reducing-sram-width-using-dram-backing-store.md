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


largest SRAM counter. With this strategy, Shah et al. (2002a) show that the SRAM counter width c can
be significantly smaller than M, the width of a DRAM counter.
                                             log b(N −1)
    More precisely, they show that 2c ≈ log(b/(b−1))     , where N is the total number of counters. Note
that this means that the SRAM counter width grows approximately as log log bN since b/(b − 1) can
be ignored for large b. For example, with three 64-bit counters, every 8 nanoseconds (OC-768) for N
equal to a million requires only 8 Mbit of 2.5 microseconds SRAM with 51.2 microseconds DRAM.
Note that in this case the value of b is 51.2/2.5 ≈ 21.
    The bottom line is that the naive method would have required 192 Mbit of SRAM compared to
8 Mbit, a factor of 24 savings in expensive SRAM. Overall, this provides roughly a factor of 24 savings
in cost since DRAM is roughly two orders of magnitude cheaper than SRAM.
    But this begs the question: How do the chip processing counters find the largest counter? Bhagwan
and Lin (2000) describe an implementation of a pipelined heap structure that can determine the largest
value at a fairly high expense in hardware complexity and space. Their heap structure requires pointers
of size log2 N for each counter just to identify the counter to be evicted. Unfortunately, log2 N addi-
tional bits per counter can be large (20 for N = 1 million) and can defeat the overall goal that was to
reduce the required SRAM bits from 64 to say 10.
    The need for a pointer per heap value seems hard to avoid. This is because the counters must be in
a fixed place to be updated when packets arrive, but values in a heap must keep moving to maintain
the heap property. On the other hand, when the largest value arrives at the top of the heap, one has to
correlate it to the counter index to reset the appropriate counter and to banish its contents to DRAM.
Notice also that all values in the heap, including pointers and values, must be in SRAM for speed.
    The following LR algorithm (Ramabhadran and Varghese, 2003) simplifies the largest count first
(LCF) algorithm of Shah et al. (2002a) and is easier to implement. Let j be the index of the counter
with the largest value among the counters incremented in the last cycle of b updates to SRAM. Ties may
be broken arbitrarily. If cj ≥ b, the algorithm updates counter cj to DRAM. If cj < b, the algorithm
updates any counter with value at least b to DRAM. If no such counter exists, LR(T ) updates counter
Cj to DRAM.
    It can be shown that LR (Ramabhadran and Varghese, 2003) is also conditionally optimal (within
the “pick-a-counter-to-flush” algorithmic framework) and produces SRAM counter width c, which is
equal to that of LCF. The maintaining of all counters above the threshold b can be done using a size-N
bitmap in which a 1 implies that the corresponding position has a counter no less than b.

                                                    16.3 A randomized counter scheme                 455



    This leaf structure can be augmented with a simple tree that maintains the position of the first 1 (see
the end-of-chapter exercises). The tree can be easily pipelined for speed, and only roughly 2 bits per
counter are required for this additional data structure; thus c is increased from its optimal value, say, x
to x + 2, a reasonable cost.
    Thus, the final LR algorithm is a better algorithm (P15) and one that is easier to implement, provides
a new data structure to efficiently find the first bit set in a bitmap (P15), and adds pipelining hardware
(P5) to gain speed.
    The overall approach could be considered superficially similar to the usual use of the memory hier-
archy, in which a faster memory acts as a cache for a slower memory. However, unlike a conventional
cache, this design ensures worst-case performance and not expected case performance. The goals of the
two algorithms are also different: Counter management stores an entry for all items but seeks to reduce
the width of cache entries, while standard caching stores full widths for only some frequent items.
