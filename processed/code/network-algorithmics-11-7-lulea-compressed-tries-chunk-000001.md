# network-algorithmics-11-7-lulea-compressed-tries (chunk 000001)

# Network Algorithmics — 11.7 Lulea-compressed tries (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 295
- Slice: from `11.7 Lulea-compressed tries` up to next detected section heading

---

11.7 Lulea-compressed tries
Though LC tries and variable-stride tries attempt to compress multibit tries by varying the stride at
each node, both schemes have problems. While the use of full arrays allows LC tries not to waste any
memory because of empty array locations, it also increases the height of the trie, which cannot then be
tuned. On the other hand, variable-stride tries can be tuned to have short height, at the cost of wasted
memory because of empty array locations in trie nodes. The Lulea approach (Degermark et al., 1997),
which we now describe, is a multibit-trie scheme that uses fixed-stride trie nodes of large stride but uses
bitmap compression to reduce storage considerably.
   We know that a string with repetitions (e.g., AAAABBAAACCCCC) can be compressed using a
bitmap denoting repetition points (i.e., 10001010010000) together with a compressed sequence (i.e.,

11.7 Lulea-compressed tries             269

FIGURE 11.12
Compressing the root node of Fig. 11.7 (after leaf pushing) using the Lulea bitmap compression scheme.
