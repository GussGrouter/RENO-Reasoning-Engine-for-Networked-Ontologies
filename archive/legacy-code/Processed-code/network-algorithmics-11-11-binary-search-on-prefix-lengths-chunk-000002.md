# network-algorithmics-11-11-binary-search-on-prefix-lengths (chunk 000002)

Binary search must start at the median prefix length, and each hash must divide the possible prefix
lengths in half. A hash search gives only two values: found and not found. If a match is found at length
m, then lengths strictly greater than m must be searched for a longer match. Correspondingly, if no
match is found, search must continue among prefixes of lengths strictly less than m.
    For example, in Fig. 11.16, part (A), suppose search begins at the median length-2 hash table for an
address that starts with 101. Clearly, the hash search does not find a match. But there is a longer match
in the length-3 table. Since only a match makes search move to the right half, an “artificial match,” or
marker, must be introduced to force the search to the right half when there is a potentially longer match.
    Thus part (B) introduces a bolded marker entry 10, corresponding to the first two bits of prefix P1
= 101, in the length-2 table. In essence, state has been added for speed (P12). The markers allow probe
failures in the median to rule out all lengths greater than the median.
    Search for an address D that starts with 101 works correctly. Search for 10 in the length-2 table
(in part (B) of Fig. 11.16) results in a match; search proceeds to the length-3 table, finds a match with

280      Chapter 11 Prefix-match lookups
