# network-algorithmics-15-3-2-rescuing-reliability (chunk 000001)

# Network Algorithmics — 15.3.2 Rescuing reliability (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 466
- Slice: from `15.3.2 Rescuing reliability` up to next detected section heading

---

15.3.2 Rescuing reliability
The solution advocated in Iyer’s thesis (and first explained in a seminal paper (Sundar et al., 2008)) is to
use SRAM as a cache front-end to an array of DRAM banks. Using clever algorithms and the “staging
SRAM,” it is possible to provably emulate the behavior of a single large SRAM.
    Of course, this is very similar to the use of an SRAM cache for measurement counters we will study
later in the measurement chapter (Section 16.2). This is not surprising because both ideas are described
in Iyer’s thesis (Sundar, 2008). However, in that idea the low order bits of each counter are stored in an
SRAM cache and the high order bits of each counter are stored in DRAM. In this idea, some portion
of the head and tail of each queue are stored in SRAM (for fast read out of packets, and for acceptance

440      Chapter 15 Routers as distributed systems
