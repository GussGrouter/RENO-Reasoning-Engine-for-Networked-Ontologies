# network-algorithmics-12-5-1-fast-searching-using-set-pruning-tries (chunk 000001)

# Network Algorithmics — 12.5.1 Fast searching using set-pruning tries (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 332
- Slice: from `12.5.1 Fast searching using set-pruning tries` up to next detected section heading

---

12.5.1 Fast searching using set-pruning tries
Consider the two-dimensional rule set in Fig. 12.3. The simplest idea is first to build a trie on the des-
tination prefixes in the database and then to hang a number of source tries off the leaves of the
destination trie. Fig. 12.4 illustrates the construction for the rules in Fig. 12.3. Each valid prefix in
the destination trie points to a trie containing some source prefixes. The question is: Which source
prefixes should be stored in the source trie corresponding to each destination prefix?
    For instance, consider D = 00∗. Both rules R4 and R5 have this destination prefix, and so the trie
at D clearly needs to store the corresponding source prefixes 1∗ and 11∗. But storing only these source
prefixes is insufficient. This is because the destination prefix 0∗ in rules R1 , R2 , and R3 also matches
any destination that D matches. In fact, the wildcard destination prefix ∗ of R7 also matches what-
ever D matches. This suggests that the source trie at D = 00 must contain the source prefixes for
{R1 , R2 , R3 , R4 , R5 , R7 }, because these are the set of rules whose destination is a prefix of D.
    Fig. 12.4 shows a schematic representation of this data structure for the database of Fig. 12.3. Note
that S1 denotes the source prefix of rule R1 , S2 of rule R2 , and so on. Thus each prefix D in the
destination trie prunes the set of rules from the entire set of rules down to the set of rules compatible

306       Chapter 12 Packet classification

FIGURE 12.4
The set-pruning trie data structure in two dimensions corresponding to the database of Fig. 12.3. Destination trie is
a trie for the destination prefixes. The nodes corresponding to a valid destination prefix in the database are shown as
filled circles; others are shown as empty circle. Each valid destination prefix D has a pointer to a trie containing the
source prefixes that belong to rules whose destination field is a prefix of D.
