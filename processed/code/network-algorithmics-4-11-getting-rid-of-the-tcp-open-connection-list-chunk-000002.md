# network-algorithmics-4-11-getting-rid-of-the-tcp-open-connection-list (chunk 000002)

Problem
Can you get rid of the waste caused by the explicit connection list while retaining the hash table? It is
reasonable to add a small amount of extra information to the hash table. When doing so, observe that
the original connection list was made doubly linked to allow easy deletion when connections terminate.
But this adds storage and dilutes the data cache. How can a singly linked list be used without slowing
down deletion?
Hint: The first part is easy to fix by linking the valid hash table entries in a list. The second part
(avoiding the doubly linked list, which would require two pointers per hash table entry) is a bit
harder.
   A connection list consists of nodes, each of which contains a connection ID (96 bits for IP)
plus two pointers (say, 32 bits each) for easy deletion. Since the hash table is needed for fast
demultiplexing, the connection list can be removed if the valid hash table entries are linked together
as shown in Fig. 4.21 and a pointer is kept to the head of the list. On a timer tick, the retransmit
routine will periodically scan this list. Scanning the complete hash table is less efficient because
the hash table may have many empty locations.

98        Chapter 4 Principles in action

FIGURE 4.21
Linking the valid hash table entries using forward pointers and lazy deletion. The dashed lines imply connection
records that have been marked as deleted but that will be processed only in the next iteration.

The naive solution would add two pointers to each valid hash table entry to implement a doubly
linked list. Since these pointers can be hash table indexes instead of arbitrary pointers to memory,
the indexes need not be larger than the size of the hash table: Even the largest hash table storing
connections should require no more than 16 bits, often much less. The naive solution does well,
adding at most 32 bits per entry instead of 160 bits per entry, savings of 128 bits. However, it is
possible to do better and to add only 16 bits per entry. Consider using lazy evaluation (P2b) and
relaxing the specification (P3).

Solution
A doubly linked list is useful only for efficient deletions. When a connection (say, Connection C3 in
Fig. 4.21) is terminated, the delete routine would ideally like to find the previous valid entry (i.e., the
list containing Connection C1 in Fig. 4.21) in order to link the previous list to the next list (i.e., the list
containing C2). This would require each hash table entry to store a pointer to the previous valid entry
in the list.
     Instead, consider principle P3, which asks whether the system requirements can be relaxed. Nor-
mally, one assumes that when a connection terminates, its storage must be reclaimed immediately. To
reclaim storage, the hash table entry should be placed in a free list, where it can be used by another
connection. However, if the hash table is a little larger than strictly necessary, it is not essential that the
storage used by a terminated connection be reused immediately.
     Given this relaxation of requirements, the implementation can lazily delete the connection state.
When a connection is terminated, the entry must be marked as unused. This requires an extra bit of
state, as in P12, but is cheap. The actual deletion of unused hash table entry E involves linking the

4.12 Acknowledgment withholding                  99

entry before E to the entry after E and also requires returning E to a free list. However, this deletion
can be done on the next list traversal when the traversal encounters an unused entry.

Exercises
