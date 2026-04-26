# network-algorithmics-6-3-avoiding-context-switching-overhead-in-applications (chunk 000002)

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
