# network-algorithmics-16-3-a-randomized-counter-scheme (chunk 000001)

# Network Algorithmics — 16.3 A randomized counter scheme (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 482
- Slice: from `16.3 A randomized counter scheme` up to next detected section heading

---

16.3 A randomized counter scheme
Both LCF and LR are deterministic algorithms and both guarantee that no counter update will be
lost. However, in most real-world network measurement operations, missing some counter updates
“occasionally” (say once a few billion years) is acceptable (P3). This has motivated Zhao et al. to
design a randomized algorithm (P3a) that is better than both LCF and LR in virtually all aspects (Zhao
et al., 2006b). We call this algorithm RS (random seeding) for reasons that will become clear shortly.
RS can be proved to be unconditionally (among all possible schemes and not restricted to the “pick-a-
counter-to-flush” framework) near-optimal in terms of SRAM consumption, yet has very simple control
logic. RS has been used on Huawei router products since 2010.
     With the same assumption (that the SRAM/DRAM speed difference b ≈ 21), RS requires only 5 + 
bits per counter, where each SRAM counter consumes 5 bits and its control logic consumes  bits per
counter. Here,  is typically a small number (e.g., 0.01). Clearly, in this case 5 bits per counter is the
absolute minimum for any algorithm/scheme since using 4 bits per counter would necessarily lead to
one DRAM access every 16 SRAM accesses, which would exceed the DRAM bandwidth (as b ≈ 21).
More generally, it can be shown that this absolute minimum is log2 (b + 1).
     Note that reducing the SRAM counter size from 8 to 5 bits per counter is 28−5 = 8 times harder
since overflows from an SRAM counter happen 8 times faster with the smaller overflow threshold (25
as compared to 28 ), requiring the “flushing” mechanism to operate 8 times more efficiently. Fortunately,
this improvement in the efficiency of RS is achieved with a simple counter-flushing technique that costs
only a small fraction of bits per counter, as compared to 20 bits per counter in LCF and 2 bits per
counter in LR.
     Like LCF and LR, the performance (in terms of not losing a counter update) guarantee of RS is
still worst case in nature in the sense that this guarantee holds under all possible sequences of counter
indices (to increment). Unlike LCF and LR, however, the guarantee is not with probability 1: With an
extremely small yet nonzero probability, RS may miss some increments to the counters.
     However, in practice, this probability can be made so small that even if a router operates continu-
ously for billions of years, the probability that a single loss of increment happens is less than one in a
billion. Note that router software/hardware failures and other unexpected or catastrophic events (e.g.,
earthquakes) that may disable a router happen with a probability many orders of magnitude higher.

456      Chapter 16 Measuring network traffic
