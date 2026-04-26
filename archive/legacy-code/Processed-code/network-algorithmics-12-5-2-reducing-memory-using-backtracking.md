# Network Algorithmics — 12.5.2 Reducing memory using backtracking (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 334
- Slice: from `12.5.2 Reducing memory using backtracking` up to next detected section heading

---

12.5.2 Reducing memory using backtracking
The previous scheme pays in memory in order to reduce search time. The dual idea is to pay with time
in order to reduce memory. In order to avoid the memory blowup of the simple trie scheme, observe
that rules associated with a destination prefix D are copied into the source trie of D  whenever D  is a
prefix of D. For instance, in Fig. 12.4, the prefix D = 00∗ has two rules associated with it: R4 and R5 .
The other rules, R1 , R2 , R3 , are copied into D’s trie because their destination field 0∗ is a prefix of D.
    The copying can be avoided by having each destination prefix D point to a source trie that stores
the rules whose destination field is exactly D. This requires modifying the search strategy as follows:
Instead of just searching the source trie for the best-matching destination prefix D, the search algorithm
must now search the source tries associated with all ancestors of D.
    In order to search for the least-cost rule, the algorithm first traverses the destination trie and finds
the longest destination prefix D  matching the header. The algorithm then searches the source trie of
D  and updates the least-cost-matching rule. Unlike set-pruning tries, however, the search algorithm is
not finished at this point.
    Instead, the search algorithm must now work its way back up the destination trie and search the
source trie associated with every prefix of D  that points to a nonempty source trie.3


3 Note that backtracking search can actually search the source tries corresponding to destination prefixes in any order; this
particular order was used only to motivate the grid-of-tries scheme. Another search order that minimizes the state required for
backtracking is described in Qiu et al. (2001).

308       Chapter 12 Packet classification




FIGURE 12.6
Avoiding the memory blowup by storing each rule in exactly one trie.


    Since each rule now is stored exactly once, the memory requirement for the new structure is
O(N W ), which is a significant improvement over the previous scheme. Unfortunately, the lookup cost
for backtracking is worse than for set-pruning tries: In the worst case, the lookup costs (W 2 ), where
W is the maximum number of bits specified in the destination or source fields.
    The (W 2 ) bound on the search cost follows from the observation that, in the worst case, the
algorithm may end up searching W source tries, each at the cost of O(W ), for a total of O(W 2 ) time.
For W = 32 and using 1-bit tries, this is 1024 memory accesses. Even using 4-bit tries, this scheme
requires 64 memory accesses.
    While backtracking can be very slow in the worst case, it turns out that all classification algorithms
exhibit pathological worst-case behavior. For databases encountered in practice, backtracking can work
very well. Qiu et al. (2001) describe experimental results using backtracking and also describe potential
hardware implementations on pipelined processors.
