# Network Algorithmics — 16.10 Reducing reporting using sampled charging (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 496
- Slice: from `16.10 Reducing reporting using sampled charging` up to next detected section heading

---

16.10 Reducing reporting using sampled charging
A technique called sampled charging (Duffield et al., 2001) can be used to reduce the collection over-
head of NetFlow, at the cost of further errors. The idea is to start with a NetFlow log that is aggregated
by TCP or UDP connections and to reduce the overhead of sending this data to a collection station. The
goal is to reduce collection bandwidth and processing, as opposed to reducing the size of the router log.
    The idea, depicted in Fig. 16.11, is at first glance similar to threshold compression, described in Sec-
tion 16.7. The router reports only flow above a threshold to the collection station. The only additional
twist is that the router also reports a flow with size s that is less than the threshold with a probability
proportional to s.
    Thus the difference between this idea and simple threshold compression is that the final transmitted
bandwidth is still small, but some attention is paid to flows below the threshold as well. Why might this
be useful? Suppose all TCP individual connections in the aggregated log are small and below threshold
but that 50% of the connections are from subnet A to subnet B.
    If the router reported only the connections above threshold, the router would report no flows because
no individual TCP flow is large. Thus, the collection agency would be unable to determine this unusual
pattern in the destination and source addresses of the TCP connections. On the other hand, by reporting
flows below threshold with a probability proportional to their size, on average, half the flows the router
will report will be from A to B. Thus, the collection station can determine this unusual traffic pattern
and take steps (e.g., increase bandwidth between these two) accordingly.
    Thus the advantage of sampled charging over simple threshold compression is that it allows the
manager to infer potentially interesting traffic patterns that are not decided in advance while still reduc-
ing the bandwidth sent to the collection node.
    For example, sampled charging could also be used to detect an unusual number of packets sent by
Napster using the same data sent to the collection station. Its disadvantage is that it still requires a large
DRAM log. The large DRAM log scales poorly in size or accuracy as speeds increase.
    On the other hand, threshold compression removes the need for the large DRAM log while directly
identifying the large traffic flows. However, unless the manager knew in advance that he was interested
in traffic between source and destination subnets, one could not solve the earlier problem. For example,
one cannot use a log that is threshold compressed with respect to TCP flows to infer that traffic between

470        Chapter 16 Measuring network traffic



a pair of subnets is unusually large. Thus threshold compression has a more compact implementation
but is less flexible than sample charging.                                                           √
    More formally, it can be shown that the multistage memory solution in Fig. 16.9 requires M
memory, where M is the memory required by NetFlow or sampled charging for the same relative error.
On the other hand, this solution requires more packet processing. Threshold compression is also less
flexible than NetFlow and sampled charging in terms of being able to mine traffic patterns after the fact.
    Sampled charging is an example of using P3b, trading certainty for bandwidth (and time).
