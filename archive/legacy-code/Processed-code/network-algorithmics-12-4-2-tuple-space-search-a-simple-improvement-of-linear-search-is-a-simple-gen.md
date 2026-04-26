# Network Algorithmics — 12.4.2 Tuple space search A simple improvement of linear search is a simple generalization of IP lookups using hash tables where (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 328
- Slice: from `12.4.2 Tuple space search A simple improvement of linear search is a simple generalization of IP lookups using hash tables where` up to next detected section heading

---

12.4.2 Tuple space search
A simple improvement of linear search is a simple generalization of IP lookups using hash tables where
prefixes were partitioned by length, and all prefixes of the same length are placed in a common hash
table. While this requires 32 memory accesses in the worst case for IPv4, recall that the previous chapter
described a major improvement, binary search on prefix lengths that could perform IPv4 lookups in
log2 32 = 5 memory accesses.
    While the use of binary search does not generalize from IP lookups to packet classification as far
as we know, the idea of using linear search on hash tables does and was first called tuple space search
(TSS) by Srinivasan et al. (1998). Consider a simple packet classifier with four rules on IPv4 Destination
(D) and Source (S) fields. Ignoring the directive fields, assume that R1 must match D = 01∗, S = 10∗;

302        Chapter 12 Packet classification



second, R2 must match D = 10∗, S = 00∗; third, R3 must match D = 0∗, S = 1∗; finally, R4 must
match D = 1∗, S = 0∗.
    While there are four rules, there are only 2 combinations of specified lengths or tuples in the table:
the tuple (2, 2) (length two specified in source and destination fields as in R1 and R2 ), and the tuple
(1, 1) (length 1 specified in source and destination fields as in R3 and R4 ). Thus the key idea is to
place all rules with the same tuple in a common hash table and do a linear search across all hash tables
corresponding to valid tuples. Each hash table is indexed by a key formed by concatenating the number
of bits in each field specified by the tuple. For example, the hash table corresponding to tuple (2, 2)
is indexed by a key formed by concatenating the first two bits of the Destination IP address and the
first two bits of the Source IP address of the packet to be classified. Note that one cannot stop after a
successful match because later tuples could have a lower cost match.
    In this simple example, tuple search requires only two memory accesses (assuming each hash table
takes one memory access to search) while linear search takes 4 memory access. However, if each
tuple has 1000’s of rules in the corresponding hash table, tuple space search can be 1000 times faster.
However, the worst case number of tuples can still be very large. For example, even for IPv4 and
considering only source and destination fields, the number of tuples (length combinations) can be as
bad as 32 * 32 = 1024.
    While there are more efficient schemes such as decision trees that are described later, tuple space
search has some important advantages. First, it has very fast update times because the time taken to add
(or delete) a new rule is O(1): we simply insert or delete the rule from the hash table corresponding
to its length tuple. Second, the memory required is O(n) where n is the number of rules. Third, tuple
space search easily generalizes to adding new fields as may be required in Software Defined Networks.
Perhaps for this reason, tuple space search is used in Open vSwitch (Pfaff et al., 2015) because in a
virtualized network new rules can be added several times every second (Pfaff et al., 2015).
    The actual use of Tuple Space search in Open vSwitch is much cleverer with several clever heuristics
to reduce the average lookup time, an important metric for software switches unlike hardware switches.
Two important ideas that speed up the average case in Open vSwitch (Pfaff et al., 2015) are the use
of caching and tuple priority sorting. We will discuss caching below, but priority sorting is a way of
stopping tuple search early by remembering the highest priority flow associated with each tuple hash
table. The details can be found in (Pfaff et al., 2015).
