# network-algorithmics-11-9-binary-search-on-ranges (chunk 000001)

# Network Algorithmics — 11.9 Binary search on ranges (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 302
- Slice: from `11.9 Binary search on ranges` up to next detected section heading

---

11.9 Binary search on ranges
So far, all our schemes (unibit tries, expanded tries, LC tries, Lulea tries, tree bitmaps) have been
trie variants. Are there other algorithmic paradigms (P15) to the longest-matching-prefix problem?
Now, exact matching is a special case of prefix matching. Both binary search and hashing (Cormen et
al., 1990) are well-known techniques for exact matching. Thus we should consider generalizing these
standard exact-matching techniques to handle prefix matching. In this section we examine an adaptation
of binary search; in the next section we look at an adaptation of hashing.
     In binary search on ranges (Lampson et al., 1998), each prefix is represented as a range, using the
start and end of the range. Thus the range endpoints for N prefixes partition the space of addresses
into 2N + 1 disjoint intervals. The algorithm (Lampson et al., 1998) uses binary search to find the
interval in which a destination address lies. Since each interval corresponds to a unique prefix match,
the algorithm precomputes this mapping and stores it with range endpoints. Thus prefix matching takes
log2 (2N ) memory accesses.
     Consider a tiny routing table with only two prefixes, P4 = 1* and P1 = 101*. This is a small subset
of the database used in Fig. 11.6. Fig. 11.15 shows how the binary search data structure is built as a
table (left) and as a binary tree (right).
     The starting point for this scheme is to consider a prefix as a range of addresses. To keep things
simple, imagine that addresses are 4 bits instead of 32 bits. Thus P4 = 1* is the range 1000 to 1111,
and P1 = 101* is the range 1010 to 1011. Next, after adding in the range for the entire address space
(0000 to 1111), the endpoints of all ranges are sorted into a binary search table, as shown on the left of
Fig. 11.15.
     In Fig. 11.15, the range endpoints are drawn vertically on the left. The figure also shows the ranges
covered by each of the prefixes. Next, two next-hop entries are associated with each endpoint. The
leftmost entry, called the > entry, is the next hop corresponding to addresses that are strictly greater
than the endpoint but strictly less than the next range endpoint in sorted order. The rightmost entry,
called the = entry, corresponds to addresses that are exactly equal to the endpoint.
     For example, it should be clear from the ranges covered by the prefixes that any addresses
greater than or equal to 0000 but strictly less than 1000 do not match any prefix. Hence the entries

276        Chapter 11 Prefix-match lookups

FIGURE 11.15
Binary search on values of a tiny subset of the sample database, consisting of only prefixes P4 = 1* and P1 = 101*.
