# network-algorithmics-8-5-pathfinder-factoring-out-common-checks (chunk 000003)

matching value corresponding to TCP. The value pointer leads to the TCP node, where the destination
port value in the packet is hashed to lead to the final matching filter.
    The Pathfinder data structure has a strong family resemblance to a common data structure called a
trie, which is more fully described in Chapter 11. Briefly, a trie is a tree in which each node contains an
array of pointers to subtries; each array contains one pointer for each possible value of a fixed-character
alphabet.
    To search the trie for a keyword, the keyword is broken into characters, and the ith character is used
to index into the ith node on the path, starting with the root. Searching in this way at node i yields a
pointer that leads to node i + 1, where search continues recursively. One can think of the Pathfinder
structure as generalizing a trie by using packet header fields (e.g., Ethernet type field) as the successive
characters used for search and by using hash tables to replace the arrays at each node.
    It is well known that tries provide fast insertions of new keys. Given this analogy, it is hardly
surprising that Pathfinder has a fast algorithm to insert or delete a filter. For instance, consider inserting
a new filter corresponding to TCP port 17. As in a trie, the insert algorithm starts with a search for the
longest matching prefix (Chapter 11) of this new filter.
    This longest match corresponds to the path Ethernet Type = IP and IP Protocol = TCP. Since
this path has already been created by the other two TCP filters, it need not be replicated. The insertion
algorithm only has to add branches (in this case a single branch) corresponding to the portion of the
new filter beyond the longest match. Thus the hash table in the TCP node need only be updated to add
a new pointer to the port 17 filter.
    More precisely, the basic atomic unit in Pathfinder is called a cell. A cell specifies a field of bits in
a packet header (using an offset, length, and a mask), a comparison value, and a pointer. For example,
ignoring the pointer, the cell that checks whether the protocol field in the IP header is (9, 1, 0xff,
6)—the cell specifies that the tenth byte of the IP header should be masked with all 1’s and compared
to the value 6, which specifies TCP.
    Cells of a given user are strung together to form a pattern for that user. Multiple patterns are super-
imposed to form the Pathfinder trie by not recreating cells that already exist. Finally, multiple cells that
specify identical bit fields but different values are coalesced using a hash table.
    Besides using hash tables in place of arrays, Pathfinder also goes beyond tries by making each node
contain arbitrary code. In effect, Pathfinder recognizes that a trie is a specialized state machine that can
be generalized by performing arbitrary operations at each node in the trie. For instance, Pathfinder can
handle fragmented packets by allowing loadable cells in addition to the comparison cells described
earlier. This is required because for a fragmented packet, only the first fragment specifies the TCP
headers; what links the fragments together is a common packet ID described in the first fragment.
    Pathfinder handles fragmentation by placing an additional loadable cell (together with the nor-
mal IP comparison cell specifying, say, a source address) that is loaded with the packet ID after the
first fragment arrives. A cell is specified as loadable by not specifying the comparison value in a
cell.
    The loadable cell is not initially part of the Pathfinder trie but is instead an attribute of the IP
cells. If the first fragment matches, the loaded cell is inserted into the Pathfinder trie and now matches
subsequent fragments based on the newly loaded packet ID. After all fragments have been removed,
this newly added cell can be removed. Finally, Pathfinder handles the case when the later fragments
arrive before the first fragment by postponing their processing until the first fragment arrives.
