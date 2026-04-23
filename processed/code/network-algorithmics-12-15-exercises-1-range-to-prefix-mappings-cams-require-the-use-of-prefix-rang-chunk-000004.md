# network-algorithmics-12-15-exercises-1-range-to-prefix-mappings-cams-require-the-use-of-prefix-rang (chunk 000004)

without the use of randomization. iSLIP is found in a number of router products, including the Cisco
GSR.
     Neither PIM nor its derandomized version iSLIP can achieve close to 100% throughput under all
traffic patterns. In addition, if implemented as a centralized algorithm, both PIM and its derandomized
version iSLIP have a fairly high time complexity of O(N log2 N ), where N is the number of input
and output ports. Section 13.11 introduces an incremental learning-based approach to computing bipar-
tite matchings, which is taken by the four algorithms we describe next: sample-and-compare SERENA,
QPS, and Sliding-Window QPS (SW-QPS). Section 13.12 describes an extremely simple centralized al-
gorithm, called sample-and-compare, that can provably achieve 100% throughput and has a lower time
complexity of O(N ). Its delay performance under heavy loads, however, is poor. Section 13.13 de-
scribes an improved algorithm called SERENA that, like sample-and-compare, also can achieve 100%
throughput and has O(N ) time complexity, but has much better delay performance under heavy loads
than sample-and-compare. SERENA is only a slight modification of sample-and-compare that replaces
the “compare” operation with a “merge” operation. Section 13.14 introduces a new sampling strategy
called queue-proportional sampling (QPS), that, if used to replace the “sample” operation in SERENA
or to generate a starter matching for iSLIP, can further improve their delay performances. Using QPS,
an input port can, in O(1) time, sample and propose to match with an output port, with a probability
that is proportional to the number of packets (currently in the queue of the input port) destined for that
output port. The data structure that enables this O(1) time complexity is described in Section 13.15.
The pursuit for better monolithic bipartite matching algorithms culminates in a late-breaking paral-
lel iterative algorithm called sliding-window QPS (SW-QPS), to be described in Section 13.16, that
achieves overall better throughput and delay performances than iLSIP, yet has only a O(1) time com-
plexity per input or output port. Finally, in Section 13.17, we describe the Combined Input and Output
Queueing (CIOQ) proposal that advocates combining switching with packet scheduling for providing
QoS guarantees.
     As various hurdles exist for existing monolithic switching schemes to scale to a large number of
ports, Section 13.18 describes two approaches to that end. Each achieves the scalability objective by
reducing a different switching cost. One reduces the overall size of the switch circuitry through the

13.1 Router versus telephone switches                          333

use of more space-efficient switch fabrics than a monolithic crossbar, such as the Clos and the Benes
fabrics. The other, called load-balanced switching (LBS), reduces the algorithmic cost of matching
computation to virtually zero, as it requires no such computation at all. However, it does so by using
two crossbars instead of one.
    Section 13.19 shows how to scale switches to faster link speeds by using bit-slice parallelism and
by using shorter fabric links as implemented in the Avici TSR.
    The literature on switching is vast, and this chapter can hardly claim to be representative. In the
first edition, this section mostly covers switch designs that had been built, analyzed in the literature,
and actually used in the networking industry. They include DEC’s GigaSwitch, Cisco’s GSR, Juniper’s
T-series, and Avici’s TSR. In this edition, we have added several new switching schemes that emerged
after the early 2000s, such as SERENA, QPS, SW-QPS, and the LBS algorithms. With these updates,
we believe this section now strikes a better balance between the practical and the theoretical issues that
arise in designing switch fabrics for high-speed routers.
    The switching techniques described in this chapter (and the corresponding principles invoked) are
summarized in Table 13.1.
