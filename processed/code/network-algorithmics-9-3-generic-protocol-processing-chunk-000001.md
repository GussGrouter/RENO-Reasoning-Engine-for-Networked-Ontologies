# network-algorithmics-9-3-generic-protocol-processing (chunk 000001)

# Network Algorithmics — 9.3 Generic protocol processing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 251
- Slice: from `9.3 Generic protocol processing` up to next detected section heading

---

9.3 Generic protocol processing
Section 9.1 described techniques for buffering a packet, and Section 9.2 described techniques to effi-
ciently compute packet checksums. The stage is now set to actually process such a packet. The reader
unfamiliar with TCP may wish first to consult the models in Chapter 2.
   Since TCP accounts for 90% of traffic (Braun, 1998) in most sites, it is crucial to efficiently process
TCP packets at close to wire speeds. Unfortunately, a first glance at TCP code is daunting. While the
TCP sender code is relatively simple, Stevens (1994) says:
   TCP input processing is the largest piece of code that we examine in this text. The function tcp_input
   is about 1100 lines of code. The processing of incoming segments is not complicated, just long and
   detailed.
    Since TCP appears to be complex, Greg Chesson and Larry Green formed Protocol Engines, Inc., in
1987, which proposed an alternative protocol called XTP (Chesson, 1989). XTP was carefully designed
with packet headers that were easy to parse and streamlined processing paths. With XTP threatening
to replace TCP, Van Jacobson riposted with a carefully tuned implementation of TCP in BSD UNIX
that is well described in Stevens (1994). This implementation was able to keep up with even 100-Mbps
links. As a result, while XTP is still used (Chesson, 1989), TCP proved to be a runaway success.
    Central to Jacobson’s optimized implementation is a mechanism called header prediction (Jacob-
son, 1993). Much of the complexity of the 1100 lines of TCP receive processing comes when handling
rare cases. Header prediction provides a fast path through the thicket of exceptions by optimizing the
expected case (P11).

TCP header prediction
The first operation on receiving a TCP packet is to find the protocol control block (PCB) that contains
the state (e.g., receive and sent sequence numbers) for the connection of which the packet is a part.
Assuming the connection is set up and that most workstations have only a few concurrent connections,
the few active connection blocks can be cached. The BSD UNIX code (Stevens, 1994) maintains a
one-behind cache containing the PCB of the last segment received; this works well in practice for
workstation implementations.
    After locating the PCB, the TCP header must be processed. A good way to motivate header pre-
diction, found in Partridge (1993), comes from looking at the fields in the TCP header, as shown in
Fig. 9.7.
    After a connection is set up, the destination and source ports are fixed. Since IP networks work
hard to send packets in order, the sequence number is likely to be the next in sequence after the last
packet received. The control bits, often called flag bits, are typically off, with the exception of the ack
bit, which is always set after the initial packet is sent. Finally, most of the time, the receiver does not
change its window size, and the urgent pointer is irrelevant. Thus the only two fields whose information
content is high are the ack number and checksum fields.
    Motivated by this observation, header prediction identifies the expected case as one of two possibil-
ities: receiving a pure acknowledgment (i.e., the received segment contains no data) or receiving a pure
data packet (i.e., the received segment contains an ack field that conveys no new information). In addi-
tion, the packet should also reflect business as usual in the following precise sense: no unexpected TCP
flags should be set, and the flow control window advertised in the packet should be no different from
what the receiver had previously advertised. In pseudocode (simplified from Ref. Jacobson, 1993):

9.3 Generic protocol processing                  225
