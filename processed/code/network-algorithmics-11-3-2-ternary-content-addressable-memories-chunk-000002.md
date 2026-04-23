# network-algorithmics-11-3-2-ternary-content-addressable-memories (chunk 000002)

11.4 Unibit tries
It is helpful to start a survey of algorithmic techniques (P15) for prefix lookup with the simplest tech-
nique: a unibit trie. Consider the sample prefix database of Fig. 11.4. This database will be used to
illustrate many of the algorithmic solutions in this chapter. It contains nine prefixes, called P1 to P9,
with the bit strings shown in the figure.
     In practice there is a next hop associated with each prefix omitted from the figure. To avoid clutter,
prefix names are used to denote the next hops. Thus in the figure, an address D that starts with 1
followed by a string of 31 zeroes will match P4, P6, P7, and P8. The longest match is P7.
     Fig. 11.5 shows a unibit trie for the sample database of Fig. 11.4. A unibit trie is based on the simple
algorithmic technique (P15) of divide and conquer based on the bits in the destination address, starting

260       Chapter 11 Prefix-match lookups

FIGURE 11.5
The one-bit trie for the sample database of Fig. 11.4.

with the most significant. A unibit trie is a tree in which each node is an array containing a 0-pointer and
a 1-pointer. At the root all prefixes that start with 0 are stored in the subtrie pointed to by the 0-pointer
and all prefixes that start with a 1 are stored in the subtrie pointed to by the 1-pointer.
    Each subtrie is then constructed recursively in a similar fashion using the remaining bits of the
prefixes allocated to the subtrie. For example, in Fig. 11.5 notice that P1 = 101 is stored in a path
traced by following a 1-pointer at the root, a 0-pointer at the right child of the root, and a 1-pointer at
the next node in the path.
    There are two other fine points to note. In some cases, a prefix may be a substring of another prefix.
For example, P4 = 1* is a substring of P2 = 111*. In that case, the smaller string, P4, is stored inside
a trie node on the path to the longer string. For example, P4 is stored at the right child to the root; note
that the path to this right child is the string 1, which is the same as P4.
    Finally, in the case of a prefix such as P3 = 11001, after we follow the first three bits, we might
naively expect to find a string of nodes corresponding to the last two bits. However, since no other
prefixes share more than the first 3 bits with P3, these nodes would only contain one pointer apiece.
Such a string of trie nodes with only one pointer each is called a one-way branch.
    Clearly one-way branches can greatly increase wasted storage by using whole nodes (containing at
least two pointers) when only a single bit suffices. (The exercises will help you quantify the amount

11.4 Unibit tries        261
