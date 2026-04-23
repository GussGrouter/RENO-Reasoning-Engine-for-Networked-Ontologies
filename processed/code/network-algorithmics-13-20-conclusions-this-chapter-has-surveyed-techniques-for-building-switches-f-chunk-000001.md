# network-algorithmics-13-20-conclusions-this-chapter-has-surveyed-techniques-for-building-switches-f (chunk 000001)

# Network Algorithmics — 13.20 Conclusions This chapter has surveyed techniques for building switches, from small shared-memory switches to (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 405
- Slice: from `13.20 Conclusions This chapter has surveyed techniques for building switches, from small shared-memory switches to` up to next detected section heading

---

13.20 Conclusions
This chapter has surveyed techniques for building switches, from small shared-memory switches to
input-queued switches used in the Cisco GSR, to larger, more scalable switch fabrics used in the Juniper
T130 and Avici TSR Routers.
    Since this is a book about algorithmics, it is important to focus on the techniques and not get lost in
the mass of product names. These are summarized in Table 13.1. Fundamentally, the major idea in PIM
and iSLIP is to realize that, by using VOQs, one can feasibly (with O(N 2 ) bits in total or O(N) bits
in per-port communication complexity) communicate all the desired communication patterns to avoid
HOL blocking. These schemes go further and show that maximal matching can be done in N log N time
using randomization (PIM) or approximately (iSLIP) using round-robin pointers per port for fairness.
Here we assume this randomization and the round-robin pointer mechanism can be performed with
O(1) time complexity using hardware such as the priority encoder described in Section 2.2.2.
    While N log N is a large number, by showing that this can be done in parallel by each of N ports,
the time reduces to log N (in PIM) and to a small constant (in iSLIP). Given that log N is small, even
this delay can be pipelined away to run in a minimum packet time. The fundamental lesson is that even
algorithms that appear complex, such as matching, can, with randomization and hardware parallelism,
be made to run in a minimum packet time. Further scaling in speed can be done using bit slices.

4 The cost premium of DRAM versus SRAM is hard to pin down because DRAM prices sometimes fall dramatically.

13.21 Exercises           379
