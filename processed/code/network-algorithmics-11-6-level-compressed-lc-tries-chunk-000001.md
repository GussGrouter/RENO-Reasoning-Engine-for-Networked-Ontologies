# network-algorithmics-11-6-level-compressed-lc-tries (chunk 000001)

# Network Algorithmics — 11.6 Level-compressed (LC) tries (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 294
- Slice: from `11.6 Level-compressed (LC) tries` up to next detected section heading

---

11.6 Level-compressed (LC) tries
An LC trie (Nilsson and Karlsson, 1998) is a variable-stride trie in which every trie node contains no
empty entries. An LC-trie is built by first finding the largest-root stride that allows no empty entries and
then recursively repeating this procedure on the child subtries. An example of this procedure is shown
in Fig. 11.10, starting with a 1-bit trie on the left and resulting in an LC trie on the right. Notice that P4
and P5 form the largest possible full-root subtrie—if the root stride is 2, then the first two array entries
will be empty. The motivation, of course, is to avoid empty array elements, to minimize storage.

268       Chapter 11 Prefix-match lookups

FIGURE 11.11
Array representation of LC tries.

However, general variable-stride tries are more tunable, allowing memory to be traded for speed.
For example, the LC trie representation using a 1997 snapshot of MAE-East has a trie height of 7 and
needs 700 KB of memory. By comparison, an optimal variable-stride trie (Srinivasan and Varghese,
1999) has a trie height of 4 using 400 KB. Recall also that the optimal variable-stride calculates the
best trie for a given target height and thus would indeed produce the LC trie if the LC trie were optimal
for its height.
    In its final form, the variable-stride LC trie nodes are laid out in breadth-first order (first the root,
then all the trie nodes at the second level from left to right, then third-level nodes, etc.), as shown on
the right of Fig. 11.11. Each pointer becomes an array offset. The array layout and the requirement
for full subtries make updates slow in the worst case. For example, deleting P5 in Fig. 11.10 causes a
change in the subtrie decomposition. Worse, it causes almost every element in the array representation
of Fig. 11.11 to be moved upward.
