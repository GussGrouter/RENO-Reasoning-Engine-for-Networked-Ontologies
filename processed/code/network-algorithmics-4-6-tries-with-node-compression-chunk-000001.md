# network-algorithmics-4-6-tries-with-node-compression (chunk 000001)

# Network Algorithmics — 4.6 Tries with node compression (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 112
- Slice: from `4.6 Tries with node compression` up to next detected section heading

---

4.6 Tries with node compression
A trie is a data structure that is a tree of nodes, where each node is an array of M elements. Fig. 4.10
shows a simple example with M = 8. Each array can hold either a key (e.g., KEY 1, KEY 2, or KEY 3
in Fig. 4.10) or a pointer to another trie node (e.g., the first element in the topmost trie node of Fig. 4.10,
which is the root). The trie is used to search for exact matches (and longest-prefix matches) with an
input string. Tries are useful in networking for such varied tasks as IP address lookups (Chapter 11),
bridge lookups (Chapter 10), and demultiplexing filters (Chapter 8).

FIGURE 4.10
Trie storing three keys. Notice the wasted space in the trie nodes.

86       Chapter 4 Principles in action

The exact trie algorithms do not concern us here. All one needs to know is how a trie is searched.
Let c = log2 M be the chunk size of a trie. To search the trie, search first breaks the input string into
chunks of size c. Search uses successive chunks, starting from the most significant, to index into nodes
of the trie, starting with the root node. When search uses chunk j to index into position i of the current
trie node, position i could contain either a pointer or a key. If position i contains a nonnull pointer to
node N , the search continues at node N with chunk j + 1; otherwise, the search terminates.
    To summarize, each node is an array of pointers or keys, and the search process needs to index
into these arrays. However, if many trie nodes are sparse, there is considerable wasted space (P1). For
example, in Fig. 4.10, only 4 out of 16 locations contain useful information. In the worst case, each
trie node could contain 1 pointer or key and there could be a factor of M in wasted memory. Assume
M ≤ 32 in what follows. Even if M is this small, a 32-fold increase in memory can greatly increase the
cost of the design.
    An obvious approach is to replace each trie node by a linear list of pairs of the form (i, val), where
val is the nonempty value (either pointer or key) in position i of the node. For example, the root trie
node in Fig. 4.10 could be replaced by the list (1, ptr1); (7, KEY 1), where ptr1 is the pointer to the
bottom trie node. Unfortunately, this can slow down trie search by a factor of M, because the search
of each trie node may now have to search through a list of M locations, instead of a single indexing
operation. This leads to the following problem.

Problem
How can trie nodes be compressed to remove null pointers without slowing down search by more than
a small factor?
Hint: Despite compressing the nodes, array indexing needs to be efficient. If the nodes are com-
pressed, how might information about which array elements are removed be represented? Consider
leveraging off the fact that M is small by following P14 (exploit the small integer size) and P4a
(exploit locality).
