# network-algorithmics-4-11-getting-rid-of-the-tcp-open-connection-list (chunk 000001)

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
