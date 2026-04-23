# network-algorithmics-11-5-multibit-tries-most-large-memories-use-dram-dram-has-a-large-latency-say (chunk 000001)

# Network Algorithmics — 11.5 Multibit tries Most large memories use DRAM. DRAM has a large latency (say 30 nanoseconds) when compared to (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 289
- Slice: from `11.5 Multibit tries Most large memories use DRAM. DRAM has a large latency (say 30 nanoseconds) when compared to` up to next detected section heading

---

11.5 Multibit tries
Most large memories use DRAM. DRAM has a large latency (say 30 nanoseconds) when compared to
register access times (2 nanoseconds). Since a unibit trie may have to make 32 accesses for a 32-bit
prefix, the worst-case search time of a unibit trie is at least 32 * 30 = 0.96 microseconds. This clearly
motivates multibit trie search. The number of bits one can search at a time is a degree of freedom
algorithmic techniques (P13) we can exploit.
    To search a trie in strides of say 4 bits, the main problem is dealing with prefixes like 10101*
(length 5), whose lengths are not a multiple of the chosen stride length, 4. If we search 4 bits at a time,
how can we ensure that we do not miss prefixes like 10101*? Controlled prefix expansion solves this
problem by transforming an existing prefix database into a new database with fewer prefix lengths but
with potentially more prefixes. By eliminating all lengths that are not multiples of the chosen stride
length, expansion allows faster multibit trie search, at the cost of increased database size.
    For example, removing odd prefix lengths reduces the number of prefix lengths from 32 to 16 and
would allow trie search 2 bits at a time. To remove a prefix like 101* of length 3, observe that 101*
represents addresses that begin with 101, which in turn represents addresses that begin with 1010* or
1011*. Thus 101* (of length 3) can be replaced by two prefixes of length 4 (1010* and 1011*), both of
which inherit the next hop forwarding entries of 101*.
    However, the expanded prefixes may collide with an existing prefix at the new length. In that case,
the expanded prefix is removed. The existing prefix is given priority because it was originally of longer
length.
    In essence, expansion trades memory for time (P4b). The same idea can be used to remove any
chosen set of lengths except length 32. Since trie search speed depends linearly on the number of
lengths, expansion reduces search time.
    Consider the sample prefix database shown in Fig. 11.4, which has nine prefixes, P1 to P9. The
same database is repeated on the left of Fig. 11.6. The database on the right of Fig. 11.6 is an equivalent
database, constructed by expanding the original database to contain prefixes of lengths 3 and 6 only.
Notice that of the four expansions of P6 = 1000* to 6 bits, one collides with P7 = 100000* and is thus
removed.
