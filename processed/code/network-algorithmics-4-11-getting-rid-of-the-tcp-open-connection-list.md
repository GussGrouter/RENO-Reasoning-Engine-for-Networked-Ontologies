# Network Algorithmics — 4.11 Getting rid of the TCP open connection list (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 123
- Slice: from `4.11 Getting rid of the TCP open connection list` up to next detected section heading

---

4.11 Getting rid of the TCP open connection list
A transport protocol such as TCP (Stevens, 1994) in computer X keeps state for every concurrent
conversation that X has with other computers. Recall from Chapter 2 that the technical name for the
shared state between the two endpoints of a conversation is a connection. Thus if a user wishes to
send mail from X to another workstation, Y , the mail program in X must first establish a connection
(shared state) to the mail program in Y . A busy server like a Web server may have lots of concurrent
connections.
    The state in a connection consists of things like the numbers of packets sent by X that have not been
acknowledged by Y . Any packets that have not been acknowledged for a long time must be retrans-
mitted by X. To do retransmission, transport protocols typically have a periodic timer that triggers the
retransmission of any packets whose acknowledgments have been outstanding for a while.
    The freely available BSD TCP code (Stevens, 1994) keeps a list of open connections (Fig. 4.20) to
examine on timer ticks in order to perform any needed retransmissions. However, when a packet arrives
at X, TCP at X must also quickly determine which connection the packet belongs to in order to update
the state for the connection. Each connection is identified by a connection identifier that is carried in
every packet.
    Relying on the list to determine the connection for a packet would require searching the entire list,
in the worst case; this could be slow for servers with large numbers of connections. Thus the x-kernel

                                         4.11 Getting rid of the TCP open connection list                          97




FIGURE 4.20
The x-kernel implementation uses a hash table mapping connections to state (for packet dispatching) as well as a
linked list of connections (for timer processing). The redundant state causes dilution of the data cache.


implementation (Hutchinson and Peterson, 1991) added a hash table to the BSD implementation (P15)
to efficiently map from connection identifiers in packets to the corresponding state for the connection.
The hash table is an array of pointers indexed by hash value that points to lists of connections that hash
to the same value. In addition, the original linked list of connections was retained for timer processing,
while the hash table was supposed to speed up packet processing.
    Oddly enough, measurements of the new implementation actually showed a slowdown! Careful
measurements traced the problem to the fact that information about connections was stored redun-
dantly, and this reduced the efficiency of the data cache when implemented on modern processors (see
Chapter 2 for a model of a modern processor). This illustrates question Q3 in Chapter 3, where an ob-
vious improvement to one part of the system can affect other parts of the system. Note that while main
memory may be cheap, fast memory such as the data cache is often limited. Commonly used structures
such as the connection list should float into the data cache as long as they are small enough to fit.
    The obvious solution is to avoid redundancy. The hash table is needed for fast lookups. The timer
routine must also periodically and efficiently scan through all connections. This leads to the following
problem.

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

• Write pseudocode for the addition of a new connection, the termination of a connection, and the
  timer-based traversal.
• How can we get away with singly linked lists for the lists of connections in each hash table list?
• Hugh Hopeful is always interested in clever tricks that he never thinks through completely. He
  suggests a way to avoid back pointers in any doubly linked list. Suppose a node X needs to be
  deleted. Normally, the deletion routine is passed a handle to retrieve X, which is typically a pointer
  to node X. Instead, Hugh suggests that the handle be a pointer to the node before X in the linked
  list (except when X is the head of the list when the handle is a null pointer). Hugh claims that this
  allows his implementation to efficiently locate both the node prior to X and the node after X using
  only forward pointers. Present a counter-example to stop Hugh before he writes some buggy code.
