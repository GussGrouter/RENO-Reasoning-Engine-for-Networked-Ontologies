# Network Algorithmics — 16.7 Reducing counters using threshold aggregation (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 491
- Slice: from `16.7 Reducing counters using threshold aggregation` up to next detected section heading

---

16.7 Reducing counters using threshold aggregation
The last two schemes reduce the width of the SRAM counter table shown in Fig. 16.1. The next two
approaches reduce the height of the SRAM counter table. They rely on the quote from Einstein (which
opened the chapter) that not all the information in the final counter table may be useful to an application,
at least for some applications. Effectively, by relaxing the specification (P3), the number of counters
that need to be maintained can be reduced.
    One simple way to compress the counter table is shown in Fig. 16.8. The idea is to pick a threshold,
say, 0.1% of the traffic, that can possibly be sent in the measurement interval and to keep counters only
for such “large” flows. Since, by definition, there can be at most 1000 such flows, the final table reduces
to 1000 flow ID, counter pairs, which can be indexed using a CAM. Note that small CAMs are perfectly
feasible at high speed.
    This form of compression is reasonable for applications that only want counters above a threshold.
For example, just as most cell phone plans charge a fixed price up to a threshold and a usage-based fee

                                  16.7 Reducing counters using threshold aggregation                    465




FIGURE 16.8
Using threshold compression to reduce the number of counters stored.

beyond the threshold, a router may only wish to keep track of the traffic sent by large flows. All other
flows are charged a fixed price. Similarly, ISPs wishing to reroute traffic hot spots or detect attacks are
only interested in large, “elephant” flows and not the “mice.”
    However, this idea gives rise to a technical problem. How can a chip detect the elephants above the
threshold without keeping track of all flows? The simplest approach would be to keep a counter for all
flows, as in Fig. 16.1, to determine which flows are above the threshold. However, doing so does not
save any memory.
    A trick (Estan and Varghese, 2002) to directly compute the elephants together with the traffic sent
by each elephant is shown in Fig. 16.9. The building blocks are hash stages that operate in parallel.
First, consider how the filter operates if it had only one stage. A stage is a table of counters indexed by
a hash function computed on a packet flow ID; all counters in the table are initialized to 0 at the start of
a measurement interval.
    When a packet comes in, a hash on its flow ID is computed and the size of the packet is added to the
corresponding counter. Since all packets belonging to the same flow hash to the same counter, if a flow
F sends more than threshold T , F ’s counter will exceed the threshold. If we add to the flow memory
all packets that hash to counters of T or more, we are guaranteed to identify all the large flows (no false
negatives).
    Unfortunately, since the number of counters we can afford is significantly smaller than the number
of flows, many flows will map to the same counter. This can cause false positives in two ways: First,
small flows can map to counters that hold large flows and get added to flow memory; second, several
small flows can hash to the same counter and add up to a number larger than the threshold.
    To reduce this large number of false positives, the algorithm uses multiple stages. Each stage
(Fig. 16.9) uses an independent hash function. Only the packets that map to counters of T or more
at all stages get added to the flow memory. For example, in Fig. 16.9, if a packet with a flow ID F ar-
rives that hashes to counters 3, 1, and 7, respectively, at the three stages, F will pass the filter (counters
that are over the threshold are shown darkened).
    On the other hand, a flow G that hashes to counters 7, 5, and 4 will not pass the filter because the
second-stage counter is not over the threshold. Effectively, the multiple stages attenuate the probability
of false positives exponentially in the number of stages. This is shown by the following simple analysis.
    Assume a 100-MB/sec link with 100,000 flows. We want to identify the flows above 1% of the link
during a 1-second measurement interval. Assume each stage has 1000 buckets and a threshold of 1 MB.
Let’s see what the probability is for a flow sending 100 KB to pass the filter. For this flow to pass one
stage, the other flows need to add up to 1 MB − 100 KB = 900 KB.

466       Chapter 16 Measuring network traffic




FIGURE 16.9
In a parallel multistage filter, a packet with a flow ID F is hashed using hash function h1 into a Stage 1 hash table,
h2 into a Stage 2 hash table, etc. Each of the hash buckets contains a counter that is incremented by the packet size.
If all the hash bucket counters are above the threshold (shown bolded), then flow F is passed to the flow memory for
more careful observation.


     There are at most 99,900/900 = 111 such buckets out of the 1000 at each stage. Therefore, the prob-
ability of passing one stage is at most 11.1%. With four independent stages, the probability that a small
flow no larger than 100 KB passes all four stages is the product of the individual stage probabilities,
which is at most 1.52 ∗ 10−4 .
     Note the potential scalability of the scheme. If the number of flows increases to one million, we
simply add a fifth hash stage to get the same effect. Thus, to handle 100,000 flows requires roughly
4000 counters and a flow memory of approximately 100 memory locations; to handle one million flows
requires roughly 5000 counters and the same size of flow memory. This is logarithmic scaling.
     The number of memory accesses at packet arrival time performed by the filter is exactly one read
and one write per stage. If the number of stages is small enough, this is affordable, even at high speeds,
since the memory accesses can be performed in parallel, especially in chip implementation. A simple
optimization called conservative update (see the exercises) can improve the performance of multistage
filtering even further. Multistage filters can be seen as an application of Principle P3a, trading certainty
(allowing some false positives and false negatives) for time and storage.
