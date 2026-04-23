# network-algorithmics-17-4-3-scale-to-higher-link-speeds (chunk 000001)

# Network Algorithmics — 17.4.3 Scale to higher link speeds (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 529
- Slice: from `17.4.3 Scale to higher link speeds` up to next detected section heading

---

17.4.3 Scale to higher link speeds
When the link speeds continue to grow faster, a router cannot even afford to record a full Bloom filter
for every packet. It can however afford to record either a full Bloom filter for a small percentage of
packets or a “tiny fraction” of a Bloom filter for every packet. For example, when the SRAM budget is
only 0.4 bits (hash functions) per packet and each full Bloom filter is 12 bits (hash functions), a router
can record a full Bloom filter for only 3.3% of the packets. In this case the traceback by logging scheme
described above would not work. For example, if two neighboring routers along an attack path sample

17.4 IP traceback via logging             503

FIGURE 17.8
Hardware implementation of packet logging using Bloom filters. Note the use of two-level memory: SRAM for
random read-modify-writes and DRAM for large row writes.

packets independently uniformly at random each at such a low sampling rate, an attack packet seen by
one router is likely not seen by the other, making it hard to trace back even this single step.
    In Li et al. (2004) two significant enhancements are made to this scheme to make it perform well in
this more challenging environment. The first enhancement is a correlated sampling scheme called One-
Bit Random Marking and Sampling (ORMS), which is similar to that in trajectory sampling in spirit
but is more sophisticated to make it adversary-proof (necessary for this security application). This idea
can improve the correlation factor between the two sets of packets sampled (for Bloom filter logging)
at two neighboring routers to over 50%; in contrast, independent uniform random sampling by the two
neighboring routers would result in a correlation factor of only 3.3% in the example above. Intuitively,
a higher correlation factor between packets sampled by two neighboring routers makes it easier to trace
back to an attacker.
    The second enhancement is to fully develop the optimization theory concerning the optimal tradeoff
point between the sampling rate and the “size” of each full Bloom filter. Again suppose the budget is
0.4 bits per packet, as in the example above. For example, since 5% × 8 = 0.4, one possible way to use
this budget is to sample 5% of the packets and let each full Bloom filter be 8 bits (hash functions); but

504        Chapter 17 Network security
