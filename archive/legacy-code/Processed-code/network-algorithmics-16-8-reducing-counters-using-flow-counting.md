# Network Algorithmics — 16.8 Reducing counters using flow counting (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 493
- Slice: from `16.8 Reducing counters using flow counting` up to next detected section heading

---

16.8 Reducing counters using flow counting
A second way to reduce the number of counters even further, beyond even threshold compression, is
to realize that many applications do not even require identifying flows above a threshold. Some only
need a count of the number of flows. For example, the Snort ( www.snort.org) intrusion-detection tool
detects port scans by counting all the distinct destinations sent to by a given source and warning if this
amount is over a threshold.

                                           16.8 Reducing counters using flow counting                  467



     On the other hand, to detect a denial-of-service attack, one might want to count the number of
sources sending to a destination because many such attacks use multiple forged addresses. In both
examples it suffices to count flows, where a flow identifier is a destination (port scan) or a source
(denial of service).
     A naive method to count source-destination pairs would be to keep a counter together with a hash
table (such as Fig. 16.1, except without the counter) that stores all the distinct 64-bit source–destination
address pairs seen thus far. When a packet arrives with source and destination addresses S, D, the
algorithm searches the hash table for S, D; if there is no match, the counter is incremented, and S, D is
added to the hash table. Unfortunately, this solution takes too much memory.
     An algorithm called HyperLogLog (Flajolet and Martin, 1985) can considerably reduce the memory
needed by the naive solution at the cost of some accuracy in counting flows. The intuition behind
probabilistic counting is to compute a metric of how uncommon a certain pattern within a flow ID is.
It then keeps track of the degree of “uncommonness” across all packets seen. If the algorithm sees very
uncommon patterns, the algorithm concludes it saw a large number of flows.
     More precisely, for each packet seen, the algorithm computes a hash function on the flow ID. It then
counts the number of consecutive zeroes, starting from the least significant position of the hash result;
this is the measure of uncommonness used. The algorithm keeps track of X, i.e., the largest number of
consecutive zeroes seen (starting from the least significant position) in the hashed flow ID values of all
packets seen so far.
     At the end of the interval, the algorithm converts X, the largest number of trailing zeroes seen, into
an estimate 2X for the number of flows. Intuitively, if the stream contains two distinct flows, on average
one flow will have the least significant bit of its hashed value equal to zero; if the stream contains eight
flows, on average, one flow will have the last three bits of its hashed value equal to zero, and so on.
     Note that hashing is essential for two reasons. First, implementing the algorithm directly on the
sequence of flow IDs itself could make the algorithm susceptible to flow ID assignments where the
traffic stream contains a flow ID F with many trailing zeroes. If F is in the traffic stream, then even
if the stream has only a few flows, the algorithm without hashing will wrongly report a large number
of flows. Notice that adding multiple copies of the same flow ID to the stream will not change the
algorithm’s final result because all copies hash to the same value.
     A second reason for hashing is that accuracy can be boosted using multiple independent hash
functions. The basic idea with one hash function can guarantee at most 50% accuracy. By using N-
independent hash functions in parallel to compute N separate estimates of X, probabilistic counting
greatly reduces the error of its final estimate. It does so by keeping the average value of X (as a floating-
point number, not an integer) and then computing 2X . Better algorithms for networking purposes are
described in Estan et al. (2002).
     The bottom line is that a chip can count approximately the number of flows with small error but
with much less memory than required to track all flows. The computation of each hash function can be
done in parallel. Flow counting can be seen as an application of Principle P3b, trading accuracy in the
estimate for low storage and time.

468       Chapter 16 Measuring network traffic




FIGURE 16.10
Using sampling to reduce packet processing while maintaining a packet log for later analysis.
