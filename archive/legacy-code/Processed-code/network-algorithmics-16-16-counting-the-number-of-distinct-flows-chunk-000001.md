# network-algorithmics-16-16-counting-the-number-of-distinct-flows (chunk 000001)

# Network Algorithmics — 16.16 Counting the number of distinct flows (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 504
- Slice: from `16.16 Counting the number of distinct flows` up to next detected section heading

---

16.16 Counting the number of distinct flows
We start with a simple data-streaming algorithm, called the min-hash algorithm or sketch (Cohen,
2016), for counting the number of distinct flows. This problem is equivalent to counting the number
of distinct elements in a data stream because we can view each packet as an element identified by
its flow identifier (which, as explained earlier, can be a source IP address, a source-destination IP
address pair, or a four-tuple). Hence, two different packets are considered two copies of the same
element if they belong to the same flow. The min-hash algorithm can be considered a variant of the
HyperLogLog algorithm (Flajolet and Martin, 1985) described in Section 16.8. Although it is slightly
less cost-effective than HyperLogLog, it is much easier to describe and understand.
