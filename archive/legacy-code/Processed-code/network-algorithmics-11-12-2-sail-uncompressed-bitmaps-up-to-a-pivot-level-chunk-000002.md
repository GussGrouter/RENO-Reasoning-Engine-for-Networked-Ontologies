# network-algorithmics-11-12-2-sail-uncompressed-bitmaps-up-to-a-pivot-level (chunk 000002)

off-chip DRAM. Note that we need 256 element trie nodes for these rare cases because the expansion
of a 24-bit prefix results in up to 256 32-bit entries.
    Because SAIL is also designed to work in software, SAIL starts lookup at length 24. SAIL first
determines whether the longest match is exactly 24 bits, less than 24 bits, or possibly greater than 24
bits. If the match is 24 bits, SAIL terminates by a lookup into the 24-bit next hop table in DRAM. If the
match is less than 24 bits, search continues sequentially from 23 to 1, trying each bitmap on-chip until
the longest match length is found at say W ; this is followed by a lookup to the W length hash table in
DRAM. Finally, if the match is greater than 24 (this should occur rarely), SAIL uses the last 8 bits of
the IP address to index into the corresponding multibit trie node in DRAM corresponding to the first
24-bits of the address.
    The key mechanism then is to efficiently implement a predicate that determines whether the longest
match is equal to 24, < 24, or possibly greater than 24. This is trickier than it may seem. Consider the
conceptual unibit trie level corresponding to the pivot length 24. Let the first 24 bit prefix of the address
being looked up be P .
    There are four cases to consider. If there is no trie node corresponding to the path P , then the
longest match must be less than 24. Second, if there is a trie node but it is a pure pointer, then search
must continue at levels greater than 24. But Case 2 can fail as a match is not guaranteed to be found at
longer lengths (as in binary search on prefix lengths). The third case is that the corresponding trie node
is a stored prefix but not a pointer; but in this case search terminates with a 24-bit match). The fourth
case is that the corresponding trie node is both a stored prefix and a pointer.
    For example, consider a smaller version of our earlier database with P 4 = 1∗, P 2 = 101∗, P 3 =
11001∗, P 7 = 1000000∗ and a new prefix P 10 = 100∗. If we assume the pivot level is 3, Case 1 occurs
say when the first bits of the address are 000, and Case 2 occurs when the first 3 bits are 110 (a pure
pointer pointing to P 3). Further, Case 3 occurs when the first 3 bits being matched are 101 (they match
P 2 and no longer prefix. Finally, Case 4 occurs when the first 3 bits being matched are 100 (they match
P 10 and also potentially the longer match P 7.
    A single bitmap at the pivot level cannot distinguish these four cases because a single indexed bit
has only 2 possible values. Thus SAIL uses an idea called pivot pushing to reduce four cases to three
cases. For example, case 4 (which should be rare) can be eliminated by pushing the stored prefix to
length 25 by expansion; thus, the prefix can be stored in an off-chip multibit trie node. That still leaves
3 cases. Case 1 is distinguished by a corresponding 0 in the 24-bit on-chip bitmap. However, Case 2
and Case 3 both correspond to a 1 in the bitmap. They are distinguished by one more lookup to the
corresponding next hop array of Length 24 bit prefixes. If there is a match (Case 3), search terminates
with a 24-bit match.
    If there is no match in the 24-bit next hop array and there is a 1 in the corresponding bit in the Length
24 bitmap, we are in Case 2 (pure pointer) and search must proceed to an off-chip multibit trie node.
But as in binary search on prefix lengths this can cause us to hare off on a wild goose chase when the
best match is actually at lengths less than 24. SAIL fixes this problem as usual using precomputation.
The longest match corresponding to the pointer is pushed to Level 25 in case no other longer match
works. Again just as in Case 4, such pushing should be done rarely, because prefixes greater than 24
are rare.
    The overall performance of SAIL in a hardware model requires 2 DRAM accesses in the (rare)
worst case for a match that is longer than 24-bits. This is because it requires a DRAM access into the
