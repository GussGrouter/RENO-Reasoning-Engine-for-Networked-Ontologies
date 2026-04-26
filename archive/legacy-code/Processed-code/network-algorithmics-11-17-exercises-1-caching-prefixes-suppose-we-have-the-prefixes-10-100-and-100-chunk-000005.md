# network-algorithmics-11-17-exercises-1-caching-prefixes-suppose-we-have-the-prefixes-10-100-and-100 (chunk 000005)

13. Rope Search: Binary search on prefix lengths can be improved by what is called rope search in
    Waldvogel et al. (1997). If we ever get a match with some entry M at length m, we only search
    further among the set of lengths corresponding to prefixes that are extensions of M. The basic
    technique we studied earlier will continue to search among all lengths greater than m in the current
    set of lengths R. However, many of the lengths l > m may not have a prefix that is an extension
    of M. Thus this optimization can result in more than halving the set of possible lengths on each
    match. It may not help the worst case, but it can considerably help the average case. Try to work
    out the details of such a scheme. In particular, a naive approach would keep a list of all potentially
    matching lengths (O(W ) space, where W is the length of an address) with each prefix. Find a way
    to reduce the state kept with each marker to O(log W ). Details can be found in Waldvogel et al.
    (1997).
14. Invariant for Binary Search on Prefix Ranges: Designing and proving algorithms that correct via
    invariants is a useful technique even in network algorithmics. The standard invariant for ordinary
    binary search when searching for key K is: “K is not in the table, or K is in the current range R.”
    Standard binary search starts with R equal to the entire table and constantly halves the range while
    maintaining the invariant. Find a similar invariant for binary search on prefix ranges.
15. Semiperfect Hashing: Hardware chips can fetch up to 1000 bits at a time using wide buses.
    Exploit this observation to allow up to X collisions in each hash table entry, where the X colliding
    entries are stored at adjacent locations. Code up a perfect hashing implementation (of 1000 IP
    addresses using a set of random hash functions), and compare the amount of memory needed with
    an implementation based on semiperfect hashing.
16. Removing Redundancies in Lookup Tables: Besides the use of compressed structures, another
    technique to reduce the size of IP lookup tables (especially when the tables are stored in on-chip
    SRAM) is to remove redundancy. One simple example of redundancy is when a prefix P is longer
    than a prefix P  and they both have the same next hop. Which prefix can be removed from the
    table? Can you think of other examples of removing redundancy? How would you implement such
    compression? Draves et al. (1999) describe a dynamic programming algorithm for compression,
    but even simpler alternatives can be effective.
17. Alternative SAIL implementation: Since there are 4 cases considered in the description of SAIL,
    the basic SAIL algorithm uses pivot pushing and an extra lookup to the netx hop array at the pivot
    level to manage with a bitmap (that has only 1 bit and hence 2 possibilities for each bit). Suppose
    we use 2 bits for each possible prefix P at the pivot length. Can we avoid pivot pushing? What are
    the tradeoffs in terms of on-chip memory, speed of lookup and insertion costs.
18. Implementing Lookups in P4: Go to https://github.com/p4lang/ and download the latest P4 com-
    piler and behavioral model and Mininet if necessary. Implement the DXR, SAIL, Tree bitmap, and
    Mashup Algorithms and compare them. Can CAM be used to simplify or make more efficient the
    SAIL and DXR algorithms? Compare these algorithms with respect to a P4 implementation both
    for IPv4 and IPv6.
19. Implementing Tries for Best Matching Prefix: (Due to V. Srinivasan.) The problem is to use
    tries to implement a file name completion routine in C or C++, similar to ones found in many
    shells. Given a unique prefix, the query should return the entire string. For example, with the
    words angle, epsilon, and eagle: Search(a) should return angle, Search(e) should return “No unique
    completion,” Search(ea), Search(eag), etc. should return eagle; and Search(b) should return “No
    matching entries found.” Assume all lowercase alphabets. To obtain an index into a trie array, use:
