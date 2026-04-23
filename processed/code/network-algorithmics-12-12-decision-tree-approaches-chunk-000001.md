# network-algorithmics-12-12-decision-tree-approaches (chunk 000001)

# Network Algorithmics — 12.12 Decision tree approaches (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 350
- Slice: from `12.12 Decision tree approaches` up to next detected section heading

---

12.12 Decision tree approaches
This chapter ends with a description of a very simple scheme that performs well in practice, better even
than RFC and comparable to or better than the extended grid of tries. This scheme was introduced by
Woo (2000). A similar idea, with range tests replacing bit tests, was independently described by Gupta
and McKeown (1999b).
    The basic idea is extremely close to the simple set-pruning tries described in Section 12.5.1, with
the addition of some important degrees of freedom. Recall that set-pruning tries work one field at a
time; thus in Fig. 12.7, the algorithm tests all the bits for the destination address before testing all the
bits for the source address. The extension to multiple fields in Decasper et al. (1998) similarly tests all
the bits of one field before moving on to another field. The set-pruning trie can be seen as an instance
of a general decision tree.
    Clearly, an obvious degree of freedom (P13) not considered in set-pruning tries is to arbitrarily
interleave the bit tests for all fields. Thus the root of the trie could test for (say) bit 15 of the source field;
if the bit is 0, this could lead to a node that tests for, say, bit 22 of the port number field. Clearly, there
is an exponential number of such decision trees. The schemes in Woo (2000) and Gupta and McKeown
(1999b) build the final decision tree using local optimization decisions at each node to choose the next
bit to test. A simple criterion used in Gupta and McKeown (1999b) is to balance storage and time.
    A second important degree of freedom considered in Woo (2000) is to use multiple decision trees.
For example, for examples such as Fig. 12.5, it may help to place all the rules with wildcards in the
source field in one tree and the remainder in a second tree. While this can increase overall search time,
it can greatly reduce storage.
    A third degree of freedom exploited in both Woo (2000) and Gupta and McKeown (1999b) is to
allow a small amount of linear searching after traversing the decision tree. This is similar to the common
strategy of using an insert. Consider a decision tree with 10,000 leaves where each leaf is associated
with one of four rules. While it may be possible to distinguish these four rules by lengthening the
decision tree in height, this lengthened decision tree could add 40,000 extra nodes of storage.

324       Chapter 12 Packet classification

FIGURE 12.15
The HiCuts data structure is essentially a range tree that has pointers corresponding to some ranges of some dimen-
sion variable with linear search at the end.
