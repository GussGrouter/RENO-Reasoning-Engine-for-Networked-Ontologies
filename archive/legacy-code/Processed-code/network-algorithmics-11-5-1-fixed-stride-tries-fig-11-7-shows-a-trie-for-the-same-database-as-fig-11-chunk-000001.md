# network-algorithmics-11-5-1-fixed-stride-tries-fig-11-7-shows-a-trie-for-the-same-database-as-fig-11 (chunk 000001)

# Network Algorithmics — 11.5.1 Fixed-stride tries Fig. 11.7 shows a trie for the same database as Fig. 11.6, using expanded tries with a fixed stride length (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 289
- Slice: from `11.5.1 Fixed-stride tries Fig. 11.7 shows a trie for the same database as Fig. 11.6, using expanded tries with a fixed stride length` up to next detected section heading

---

11.5.1 Fixed-stride tries
Fig. 11.7 shows a trie for the same database as Fig. 11.6, using expanded tries with a fixed stride length
of 3. Thus each trie node uses 3 bits. The replicated entries within trie nodes in Fig. 11.7 correspond

11.5 Multibit tries           263

FIGURE 11.6
Controlled expansion of the original prefix database shown on the left (which has five prefix lengths, 1, 3, 4, 5, and
6) to an expanded database (which has only 2 prefix lengths, 3 and 6).

exactly to the expanded prefixes on the right of Fig. 11.6. For example, P6 in Fig. 11.6 has three
expansions (100001, 100010, 100011).
    These three expanded prefixes are pointed to by the 100 pointer in the root node of Fig. 11.7 (because
all three expanded prefixes start with 100) and are stored in the 001, 010, and 011 entries of the right
child of the root node. Notice also that the entry 100 in the root node has a stored prefix P8 (besides the
pointer pointing to P6’s expansions), because P8 = 100* is itself an expanded prefix.
    Thus each trie node element is a record containing two entries: a stored prefix and a pointer. Trie
search proceeds 3 bits at a time. Each time a pointer is followed, the algorithm remembers the stored
prefix (if any). When search terminates at an empty pointer, the last stored prefix in the path is returned.
    For example, if address D begins with 1110, search for D starts at the 111 entry at the root node,
which has no outgoing pointer but a stored prefix (P2). Thus search for D terminates with P2. A search
for an address that starts with 100000 follows the 100 pointer in the root (and remembers P8). This
leads to the node on the lower right, where the 000 entry has no outgoing pointer but a stored prefix
(P7). The search terminates with result P7. Both the pointer and stored prefix can be retrieved in one
memory access using wide memories (P5b).
    A special case of fixed-stride tries, described in Gupta et al. (1998), uses fixed strides of 24, 4, and
4. The authors observe that DRAMs with more than 224 locations are becoming available, making even
24-bit strides feasible.
