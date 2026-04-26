# network-algorithmics-16-4-1-motivation-and-design-objectives (chunk 000001)

# Network Algorithmics — 16.4.1 Motivation and design objectives (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 484
- Slice: from `16.4.1 Motivation and design objectives` up to next detected section heading

---

16.4.1 Motivation and design objectives
While passive counters are good enough for many network monitoring applications, a number of other
applications require the maintenance of active counters, in which the values of counters need to be
read out as frequently as they are incremented, typically on a per packet basis. In many network data-
streaming algorithms (Cormode and Muthukrishnan, 2005; Estan and Varghese, 2002; Krishnamurthy
et al., 2003; Kumar et al., 2004b; Zhang et al., 2004; Zhao et al., 2005), upon the arrival of each packet,
values need to be read out from some counters to decide on actions that need to be taken; we will
provide a brief introduction to network data streaming and sketching in Section 16.15.
    A paper on approximate active counters (Stanojevic, 2007) identifies several other data-streaming
algorithms that need to maintain active counters, including multistage filters for elephant detection (Es-
tan and Varghese, 2002) and online hierarchical heavy hitter identification (Zhang et al., 2004). All these
data-streaming algorithms that use exact active counters implement them as full-size SRAM counters.
An efficient solution for exact active counters can significantly reduce SRAM cost for all such applica-
tions, as we will show next.
    BRICK (Bucketized Rank Index Counter) (Hua et al., 2008b) is an early solution to the problem
of efficiently maintaining exact active counters. BRICK allows extremely fast read and increment (by
1) accesses at on-chip SRAM speeds, yet is much more SRAM-efficient than the naive solution of
maintaining full-size SRAM counters, in the following sense.
    Suppose at the end of a measurement interval, the sum of the values of all N counters in the array,
which is equal to the total number of increments during the interval, is M. When the naive solution
is used, every SRAM counter has to be at least log2 M bits long since, in the worst case, all the
M increments can hit this counter. When BRICK is used, however, the average size of each SRAM
counter only needs to be slightly larger than log2 (M/N ) bits, the minimum length needed to encode

458      Chapter 16 Measuring network traffic

FIGURE 16.3
BRICK wall (conceptual baseline scheme) (Hua et al., 2008b).

the average counter value M/N. Hence, roughly speaking, BRICK pays the average cost (P11), not the
worst-case cost.
    We emphasize that the average cost log2 (M/N ) can be much smaller than the worst-case cost
log2 M. For example, let the total counts be M = 15 million and the number of counters be N =
1 million. In this case, the average cost log2 (M/N ) is only 4 bits, but the worst-case cost log2 M
is 24 bits, which is six times larger.
