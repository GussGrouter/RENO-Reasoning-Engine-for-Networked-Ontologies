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



    Compared to PIM and iSLIP, SW-QPS is a mind-blowing result. Its per-port time complexity is
strictly O(1) without using any hardware support. Its per-port communication complexity is also O(1),
as compared to O(N ) in the cases of PIM and iSLIP. Yet, it delivers overall better throughput and delay
performance than iSLIP. It achieves all these by exploiting all relevant algorithmics techniques to the
fullest extent: randomization, hardware parallelism, and extreme pipelining (which the sliding-window
technique can arguably be viewed as).
    Larger port counts can also be handled by algorithmic techniques based on the divide-and-conquer
approach. An understanding of the actual costs of switching shows that even a simple three-stage Clos
switch works well for port sizes up to 256. However, for larger switch sizes, the Benes network, with
its combination of (2log N ) depth Delta networks, is better suited for the job. The main issue in both
these scalable fabrics is scheduling. And, in both cases, as in PIM, a complex deterministic algorithm
is finessed using simple randomization. In both the Clos and Benes networks the essential similarity
of structure allows the use of an initial randomized load-balancing step followed by deterministic path
selection from the randomized intermediate destination.
    Similar ideas are also used to reduce memory needs by either picking a random intermediate line
card or a random choice of DRAM bank to send a given packet (cell) to. The knockout switch uses
trees of randomized 2-by-2 concentrators to provide k-out-of-N fairness. Thus randomization is a sur-
prisingly important idea in switch implementations.
    It is interesting to note that almost every new switch idea described in this chapter has led to the
creation of a company. For example, Kanakia worked on shared-memory switches at Bell Labs and
then left to found Torrent. Juniper seems to have been started with Sindhu’s idea for a new fabric
based, perhaps, on the use of staging via a random intermediate line card. McKeown founded Abrizio
after the success of iSLIP. Growth Networks was started by Turner, Parulkar, and Cox to commercialize
Turner’s Benes switch idea, and it was later sold to Cisco. Dally took his ideas for deadlock-free routing
on low-dimensional meshes and moved them successfully from Cray Computers to Avici’s TSR.
    Thus, if you, dear reader, have an idea for a new folded Banyan or an inverted Clos, you, too, may be
the founder of the next great thing in networking. Perhaps some venture capitalist will soon be meeting
you in a coffee shop in Silicon Valley to make you an offer you cannot refuse.
    In conclusion for a router designer it’s better to switch than to fight, with the difficulties of designing
a high-speed bus.
