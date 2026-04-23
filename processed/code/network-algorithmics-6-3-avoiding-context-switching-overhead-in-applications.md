# Network Algorithmics — 6.3 Avoiding context-switching overhead in applications (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 180
- Slice: from `6.3 Avoiding context-switching overhead in applications` up to next detected section heading

---

6.3 Avoiding context-switching overhead in applications
The last section concentrated on removing process-scheduling overhead for processing a single packet
received by the network by effectively limiting the processing to fielding one interrupt (which, as we
discuss in Section 6.7, can also be removed or amortized over several packets) and dispatching the
packet to the final process in which the application (that processes the packet) resides. If the desti-
nation process is currently running, then there is even no process-scheduling overhead. Thus after all
optimizations there can be close to no control overhead for processing a packet.
    This is analogous to Chapter 5, in which the first few sections showed how to process a received
packet with zero copies. However, in that chapter after broadening one’s viewpoint to see the com-
plete application processing, it became apparent that there were further redundant copies caused by
interactions with the file system.
    In a similar fashion this section broadens beyond the processing of a single packet to consider how
an application processes packets. Once again, as in Chapter 5, we consider a Web server (Fig. 6.1)
because it is a canonical example of a server that needs to be made more efficient and because of its
importance in practice.
    In what follows, we will use a Web server as an example of a canonical server that may require the
handling of a large number of connections. In another example Barile (2004) describes a TCP-to-UDP
proxy server for a telephony server that can handle 100,000 concurrent connections.
    How should a Web server be structured? Before tackling this question, it helps to understand the
potential concurrency within a single Web server. Readers familiar with operating systems may wish to
skim over the next three paragraphs. These are included for readers not as familiar with the secret life
of a workstation.1
    Even with a single CPU and a single disk head, there are opportunities for concurrency. For example,
assume that in processing a read for File 1, File 1 is not in cache. Thus the CPU initiates a disk read.
Since this may take a few milliseconds to complete, and the CPU can do an instruction almost every
nanosecond, it is obvious waste to idle the CPU during this read. Thus a more sensible strategy is to
have the CPU switch to processing another client while Client 1’s disk read is in progress. This allows
processing by the disk on behalf of Client 1 to be overlapped with processing by the CPU for Client 2.
    A second example of concurrency between the CPU and a device (that is relevant to a Web server)
is overlapping between network I/O (as performed by the adaptor) and the CPU. For example, after
a server accepts a connection, it may do a Read to an accepted connection for Client 1. If the CPU
waits for the Read to complete it may wait a long time, potentially also several milliseconds. This is


1 Recall that the intent of network algorithmics and of this book is to allow all constituencies, for example, hardware designers,
to understand the relevant issues.

154        Chapter 6 Transferring control



because the remote client has to send a packet that has to make its way through the network and finally
be written by the adaptor to the socket corresponding to Client 1 at the server.
    By switching to another client, processing by the network on behalf of Client 1 is overlapped with
processing by the CPU on behalf of some other client. Similarly, when doing a Write to the network,
the Write may be blocked because of the lack of buffer space in the socket buffer. This buffer space
may be released much later when acknowledgments arrive from the destination.
    The last three paragraphs show that for a Web server to be efficient, every opportunity for concur-
rency must be exploited to increase effective throughput. Thus a CPU in a Web server must switch
between clients when one client is blocked waiting for I/O. We now consider various ways to structure
a server application and their effects on concurrency and scheduling overhead.
