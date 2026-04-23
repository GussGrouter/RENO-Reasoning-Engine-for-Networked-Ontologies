# network-algorithmics-5-1-why-data-copies-in-fig-a-1-in-the-appendix-we-describe-how-tcp-works-in (chunk 000002)

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
