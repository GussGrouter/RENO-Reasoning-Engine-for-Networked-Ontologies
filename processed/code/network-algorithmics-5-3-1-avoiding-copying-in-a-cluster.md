# Network Algorithmics — 5.3.1 Avoiding copying in a cluster (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 154
- Slice: from `5.3.1 Avoiding copying in a cluster` up to next detected section heading

---

5.3.1 Avoiding copying in a cluster
In the last few years clusters of workstations have become accepted as a cheaper and more effective
substitute for large computers. Thus many Web servers are really server farms. While this appears
to be recent technology, 20 years ago Digital Equipment Corporation (DEC) introduced a successful
commercial product called VAX Clusters to provide a platform for scalable computing for, say, database
applications. The heart of the system was a 140-Mbit network called the computer interconnect, or CI,
which used an Ethernet-style protocol. To this interconnect, customers could connect a number of VAX
computers and network-attached disks. The issue of efficient copying was motivated by the need to
transfer large amounts of data between the remote disk and the memory of a VAX. RDMA was born
from this need.
    RDMA requires that packet data containing part of a large file go into its final destination when it
gets to the destination adaptor. This is trickier than it sounds. In traditional networking when the packet
arrives the processor is involved in at least examining the packet and deciding where the packet is to
go. Even if the CPU looks at headers, it can only tell based on the destination application which queue
of receive buffers to use.
    Suppose the receiving application queues Pages 1, 2, and 3 to the receiving adaptor for Application
1. Suppose the first packet arrives and is sent to Page 1, the third packet arrives out of order and is put
in Page 2 instead of Page 3. Assume that Pages 1, 2, and 3 should store the receiving file. The CPU can
always remap pages at the end, but remapping all the pages at the end of the transfer for a large file can
be painful. Out-of-order arrival can always happen, even on a FIFO link, because of packet loss.
    Instead, the idea in VAX Clusters is first to have the destination application lock a number of physi-
cal pages (such as Pages 11 and 16 in Fig. 5.8) that comprise the destination memory for the file transfer.
The logical view presented, however, is a buffer of consecutive logical pages (e.g., Pages 1 and 2 in
Fig. 5.8) called, say, B. This buffer name B is passed to the sending application.
    The source now passes (P10, pass information in protocol headers) the buffer name and offset with
each packet it sends. Thus when sending Packet 3 out of order in our last example, Packet 3 will contain
B and Page 3 and so can get stored in Page 3 of the buffer even though it arrives before Packet 2. Thus
after all packets arrive there is no need for any further page remapping. This is an example of P10:
passing information, such as a buffer name, in message headers.
    To realize the ideal of not bothering the processor on every packet arrival, there are several additional
requirements. First, the adaptor must implement the transport protocol (and do all the checking for
duplicates, etc.), as in TCP processing. Second, the adaptor must be able to determine where the data
begins and where the headers stop so as only to copy the data into the destination buffer.

128      Chapter 5 Copying data




FIGURE 5.8
Doing DMA across the network.


    Finally, it is somewhat cavalier to allow any packet carrying a buffer ID from the network to be
written directly into memory. This could be a security hole. To mitigate against this, the buffer IDs
contain a random string that is hard to guess. More importantly, VAX Clusters are used only between
trusted hosts in a cluster. It is more difficult to imagine scaling this approach to Internet data transfers.
