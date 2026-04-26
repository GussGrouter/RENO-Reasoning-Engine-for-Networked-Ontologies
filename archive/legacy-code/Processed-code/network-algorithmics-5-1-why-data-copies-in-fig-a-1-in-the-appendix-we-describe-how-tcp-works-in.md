# Network Algorithmics — 5.1 Why data copies In Fig. A.1 in the Appendix we describe how TCP works in the context of a Web server. Fig. A.1 only (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 140
- Slice: from `5.1 Why data copies In Fig. A.1 in the Appendix we describe how TCP works in the context of a Web server. Fig. A.1 only` up to next detected section heading

---

5.1 Why data copies
In Fig. A.1 in the Appendix we describe how TCP works in the context of a Web server. Fig. A.1 only
shows the sending of the GET request for a file, followed by the file data itself in two TCP segments.
What Fig. A.1 does not show is how the Web server processes the GET request. In this chapter we
ignore the control transfer required to transfer the request to some application server process. Instead,
Fig. 5.1 shows the sequence of data transfers involved in reading file data from the disk (in the worst
case) to the sending of the corresponding segments via the network adaptor.
    The main hardware players in Fig. 5.1 are the CPU, the memory bus, the I/O bus, the disk, and the
network adaptor. The main software players are the Web server application and the kernel. There are
two main kernel subsystems involved, the file system and the networking system. For simplicity, the
picture shows only one CPU in the server (many servers are multiprocessors and particularly multicore
machines) and focuses only on requests for static content (many requests are for dynamic content that
is served by a Common Gateway Interface (CGI) process).1
    Intuitively, the story is simple. The file is read from disk into the application buffer via, say, a read()
system call. The combination of the HTTP response and the application buffer is then sent to the


1 The picture makes it appear that the code for the file system and the TCP/IP code is on the processor. In reality the code is also
stored in memory and is fetched by the processor. However, the portion of the code that fits into the processor instruction cache
indeed can be considered to be in the processor.

114      Chapter 5 Copying data



network over the TCP connection to the client by, say, a write() system call. The TCP code in the
network subsystem of the kernel breaks up the response data into bite-size segments and transmits
them to the network adaptor after adding a TCP checksum to each segment.
    In practice the story is often more messy in the details. First, the file is typically read into a piece of
kernel memory, called the file cache, in what we call Copy 1. This is a good idea because subsequent
requests to a popular file can be served from main memory without slow disk I/O. The file is then
copied from the file cache into the Web server application buffer in Copy 2 shown in Fig. 5.1. Since the
application buffer and the file cache buffer are in different parts of main memory, this copy can only be
done by the CPU’s reading the data from the first memory location and writing into the second location
across the memory bus.
    The Web server then does a write() to the corresponding socket. Since the application can freely
reuse its buffer (or even deallocate it) at any time after the write(), the network subsystem in the kernel
cannot simply transmit out of the application buffer. In particular the TCP software may need to re-
transmit part of the file after an unpredictable amount of time, by which time the application may wish
to use the buffer for other purposes.
    Thus UNIX (and many other operating systems) provides what is known as copy semantics. The
application buffer specified in the write() call is copied to a socket buffer (another buffer within the
kernel, at a different address in memory than either the file cache or the application buffer). This is
called Copy 3 in Fig. 5.1. Finally, each segment is sent out to the network (after IP and link headers
have been pasted) by copying the data from the socket buffer to memory within the network adaptor.
This is called Copy 4.
    In between, before transmission to the network, the TCP software in the kernel must make a pass
over the data to compute the TCP checksum. Techniques for efficiently implementing the TCP check-
sum are described in Chapter 9, but for now it suffices to think of the TCP checksum as essentially
computing the sum of 16-bit words in each TCP segment’s data.
    Each of the four copies and the checksum consume resources. All four copies and the checksum
calculation consume bandwidth on the memory bus. The copies between memory locations (Copies 2
and 3) are actually worse than the others because they require one Read and one Write across the bus
for every word of memory transferred. The TCP checksum requires only one Read for every word and a
single Write to append the final checksum. Finally, Copies 1 and 4 can be as expensive as Copies 2 and
3 if the CPU does the heavy lifting for the copy (so-called programmed I/O); however, if the devices
themselves do the copy (so-called DMA), the cost is only a single Read or Write per word across the
bus.
    The copies also consume I/O bus bandwidth and ultimately memory bandwidth itself. A memory
that supplies a word of size W bits every x nanoseconds has a fundamental limit on throughput of W/x
bits per nanosecond. For example, even assuming DMA, these copies ensure that the memory bus is
used seven times for each word in the file sent out by the server. Thus the Web server throughput cannot
exceed T /7, where T is the smaller of the speed of the memory and the memory bus.
    Second, and more basically, the extra copies consume memory. The same file (Fig. 5.1) could be
stored in the file cache, the application buffer, and the socket buffer. While memory seems to be cheap
and plentiful (especially when buying a PC!), it does have some limits, and Web servers would like
to use as much as possible for the file cache to avoid slow disk I/O. Thus triply replicating a file can
reduce the file cache by a factor of 3, which in turn can dramatically reduce the cache hit rate and,
hence, overall server performance.

                                          5.2 Reducing copying via local restructuring              115



    In summary redundant copies hurt performance in two fundamental and orthogonal ways. First,
by using more bus and memory bandwidth than strictly necessary, the Web server runs slower than
bus speeds, even when serving documents that are in memory. Second, by using more memory than it
should, the Web server will have to read an unduly large fraction of files from disk instead of from the
file cache.
    Note also that we have only described the scenario in which static content is served. In reality the
SPECweb benchmarks assume that 30% of the requests are for dynamic content. Dynamic content
is often served by a separate CGI process (other than the server application) that communicates this
content to the server via some interprocess communication mechanism, such as a UNIX pipe, which
often involves another copy.
    Ideally, all these pesky extra bus traversals should be removed. Clearly, Copy 1 is not required if
the data is in cache and so we can ignore it. If it’s not in cache, the server runs at disk speed, which
is too slow anyway (though the use of fast non-volatile memory changes this equation). Copy 2 seems
unnecessary. Why can’t the data be sent directly from the file cache memory location to the network?
Similarly, Copy 3 seems unnecessary. Copy 4 is unavoidable.
