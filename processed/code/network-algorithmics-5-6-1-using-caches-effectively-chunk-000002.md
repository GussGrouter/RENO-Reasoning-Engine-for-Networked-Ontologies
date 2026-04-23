# network-algorithmics-5-6-1-using-caches-effectively (chunk 000002)

Data Cache Optimization
Now, one might think packet data benefits little from a data cache, for there is little reuse of the data
and copying involves writing to a new memory address, as opposed to repeated reads and writes from
the same memory address. However, what if when packet data is received into memory by DMA, it is
also sent to the processor cache? This is not as hard to do as it seems because the bus is a broadcast
bus and the cache can “snoop” on transactions on the bus (Huggahalli et al., 2005). But if the data is
already in the processor cache, then the copy from the socket buffer to application memory becomes a
cache access. There is also a reduction in memory bandwidth and bus bandwidth.
    But the presence of modern multicore machines complicates direct cache access. Which processor
cache should the packet be sent by DMA to? One possibility is to send the packet to the cache corre-
sponding to the core on which the receive application is running. This is called Receive Flow Steering
(RFS); if the mechanism can be done in hardware it is referred to as aRFS (for accelerated Receive
Flow Steering) (Cai et al., 2021).
    Direct Cache Access (DCA) is standard in many processors and is often enabled by default (Cai
et al., 2021). Unfortunately, the combination of high link speeds (100 Gbps) and increased end-to-end
latencies implies that the number of bytes in flight (the so-called bandwidth delay product) is high. If
this number is higher than the size of data cache, then cache can be overwritten before the application
reads from the cache, negating the benefits of DCA, resulting in significant drop in the throughput
per core (Cai et al., 2021). The same paper suggests that window size tuning in TCP should take into
account cache sizes to avoid this effect.
    There are two other items stored in memory that can benefit from caches. First, the program execut-
ing the protocol code to process a packet must be fetched from memory, unless it is stored in the I-cache.
Second, the state required to process a packet (e.g., TCP connection state tables) must be fetched from
memory, unless it is stored in the D-cache.
    Of these two other possible contenders for memory bandwidth, the code to be executed is potentially
a more serious threat. This is because the state, in bytes, required to process a packet (say, one connec-
tion table entry, one routing table entry) is generally small. However, for a small, 40-byte packet, even
this can be significant. Thus avoiding the use of redundant state (which tends to pollute the D-cache)
wherever possible can improve performance, as was described in Problem 11 of Chapter 4.
    However, the code required to execute all of the networking stack (Data Link, TCP, IP, socket layer,
and kernel entry and exit) can be much larger. For example, measurements in Blackwell (1996) show a
total code size of 34 KB using a 1995 NetBSD TCP implementation. Given that even large packets on
an Ethernet are at most 1.5 KB, the effort to load the code from memory can easily dwarf the effort to
copy the packet multiple times.
    In particular, if the I-cache is 8 KB (typical for older machines, such as the early Alpha machines
used in Blackwell, 1996), this means that at most a quarter of the networking stack can fit in the cache.
This in turn could imply that all or most of the code has to be fetched from memory every time a
packet needs to be processed. Modern machines have not improved their I-cache sizes significantly.
The Pentium III uses 16 KB. Thus effective use of the I-cache could be a key to improved performance,
especially for small packets.
    We now describe two techniques that can be used to improve I-cache effectiveness: code arrange-
ment and locality-driven-layer processing.
