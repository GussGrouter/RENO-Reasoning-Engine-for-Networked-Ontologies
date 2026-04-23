# Network Algorithmics — 5.6.1 Using caches effectively (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 164
- Slice: from `5.6.1 Using caches effectively` up to next detected section heading

---

5.6.1 Using caches effectively
The architectural model of Fig. 5.1 avoids two important details that were described in Chapter 2.
Recall that the processor keeps one or more data caches (D-caches), and one or more instruction caches
(I-caches). The data cache is a table that maps from memory addresses to data contents; if there are
repeated reads and writes to the same location L in memory and L is cached, then these reads and writes
can be served directly out of the data cache without incurring bus or memory bandwidth. Similarly,
recall that programs are stored in memory; every line of code executed by the CPU has to be fetched
from main memory unless it is cached in the instruction cache.

138      Chapter 5 Copying data



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

                                                5.6 Broadening beyond data manipulations                        139




FIGURE 5.12
The figure on the left shows networking code that is laid out in memory so that frequently used (white) and infre-
quently used (black) code is arbitrarily intermixed. Using a direct-mapped cache of half the size of the total code
can lead two frequently used instructions, such as X and Y , to collide. This problem can be avoided by relocating all
frequently used code to be contiguous, as shown on the right.



Code arrangement
It is hard to realize when one is writing networking code that the actual layout of code in memory (and
hence in the I-cache) is a degree of freedom that can be exploited (P13) with some effort. The key idea
in code arrangement (Mosberger et al., 1996) is to lay out code in memory to optimize the common
case (P11) such that commonly used code fits in the I-cache and the effort of loading the I-cache is not
wasted.
     At first glance, this seems to require no extra work. Since a cache should favor frequently used code
over infrequently used code, this should happen automatically. Unfortunately, this is incorrect because
of the following two aspects of the way I-caches are implemented.
• Direct mapping: An I-cache is a mapping of memory addresses to contents; the mapping is usually
  implemented by a simple hash function that optimizes for the case of sequential access. Thus most
  processors use direct-mapped I-caches, where the low-order bits of a memory address are used to
  index the I-cache array. If the high-order bits match, the contents are returned directly from cache;
  otherwise, a Read to memory is done across the bus, and the new data value and high-order bits are
  stored in the same location.
  Fig. 5.12 shows the effect of this implementation artifact. The figure on the left shows the memory
  layout of code for two networking functions, with black code denoting infrequently used code. Since
  the I-cache size is only half the total size of the code, it is possible for two frequently accessed lines
  of code (such as X and Y , with addresses that are the same modulo the I-cache size) to map to the
  same location in the I-cache. Thus if both X and Y are used to process every packet, they will keep
  evicting each other from the cache even though they are both frequently used.

140      Chapter 5 Copying data



• Multiple instructions per block: Many I-caches can be thought of as an array of blocks, where
  multiple instructions (say, eight) are stored in a block. Thus when an instruction is fetched, all eight
  instructions in the same block are also fetched on the assumption of spatial locality: With sequential
  access, it seems probable that the other seven instructions will also be fetched, and it is cheaper to
  read multiple instructions from memory at the same time.
  Unfortunately, much of networking code contains error checks such as “If error E do X, else do Z.”
  Z is hardly ever executed, but a compiler will often arrange the code for Z immediately after X. For
  example, in Fig. 5.12 imagine that code for Z immediately follows X. If X and Z fall in the same
  block of eight instructions, then fetching frequently accessed X also results in fetching infrequently
  used Z. This makes loading the cache less efficient (more useless work) and makes the cache less
  useful after loading (less useful code in cache).
    Note that both of these effects are caused by the fact that real caches imperfectly reflect tempo-
ral locality. The first is caused by an imperfect hash function that can cause collisions between two
frequently used addresses. The second is caused by the fact that the cache also optimizes for spatial
locality.
    Both effects can be mitigated by reorganizing networking code (Mosberger et al., 1996) so that all
frequently used code is contiguous (see right of Fig. 5.12). For example, in the case “If error E do X,
else do Z,” the code for Z can be moved far away from X. This does require an extra jump instruction
to be added to the code for Z so that it can jump back to the code that followed Z in the unoptimized
version. However, this extra jump is taken only in the error case, and so it is not much of a cost.
    This is an example of realizing that the memory location of code is a degree of freedom that can
be optimized (P13) and an example of optimizing the expected case (P11) despite increasing the code
path for infrequently used code.

Locality-driven layer processing
Code reorganization can help up to a point but fails if the working set (i.e., the set of instructions actually
accessed for almost every packet) exceeds the I-cache size. For example, in Fig. 5.12, if the size of the
white, frequently used instructions is larger than the I-cache, code reorganization will still help (fewer
loads from memory are required because each load loads only useful instructions). However, every
instruction will still have to be fetched from memory.
    While the working set of the networking stack may fit into a modern I-cache (which is getting
bigger), it is possible that more complicated protocols (that run over TCP/IP) may not. The idea behind
locality-driven layer processing (Blackwell, 1996) is to be able to use the I-cache effectively as long
as the code for each layer of the networking stack fits into the I-cache. By repeatedly processing the
code for the same layer across multiple packets, the expense of loading the I-cache is shared (P2c) over
multiple packets.
    Consider the top timeline in Fig. 5.13. In a conventional processing timeline (shown from left to
right in the figure), all the networking layers of packet P 1 are processed before those of packet P 2.
Imagine that two packets P 1 and P 2 arrive at a server. In a conventional implementation, all the pro-
cessing of P 1 is finished, starting with the data link layer (e.g., Ethernet driver) and ending with the
transport (e.g., TCP) layer. Only then is the processing of packet P 2 started.
    The main idea in locality-driven processing is to exploit another degree of freedom (P13) and to
process all the layer code for as many received packets as possible before moving on to the next layer.
Thus in the bottom timeline, after the data link layer code for P 1 is finished, the CPU moves on to

                                                5.6 Broadening beyond data manipulations                         141




FIGURE 5.13
In a conventional processing timeline (shown from left to right), all the networking layers of packet P 1 are pro-
cessed before those of packet P 2. In locality-driven receiver processing, each layer code is executed multiple times
for multiple received packets (two in the picture) before moving on to the next layer.


execute the data link layer code for P 2, not the network layer code for P 1. This should not affect cor-
rectness because code for a layer should not depend on the state of lower layers. By contrast, integrated
layer processing has more subtle dependencies and failure cases.
    Thus if the code for each layer (e.g., the data link layer) fits into the I-cache while the code for all
layers does not, then this optimization amortizes the cost of loading the I-cache over multiple packets.
This is effectively using batch processing (P2c, expense sharing). The larger the size of the batch, the
more effective the use of the I-cache.
    The implementation can be made to tune the size of the batch dynamically (Blackwell, 1996).
The code can batch-process up to, say, k packets from the queue of arrived packets, where k is a
parameter that limits the latency. If the system is lightly loaded, then only one message at a time will
be processed. On the other hand, if the system is heavily loaded, the batch size increases to make more
effective use of memory bandwidth when it is most needed.

Software engineering considerations
Optimizations such as code restructuring (Fig. 5.12) and locality-driven processing (Fig. 5.13) also
need to be evaluated by their effects on code modularity and maintenance. After all, one could rewrite
the kernel and all applications using assembly language to more perfectly optimize memory bandwidth.
But it would be difficult to get the code to work or be maintainable.
    Code restructuring is best done by a compiler. For example, error-handling code can be annotated
with hints (Mosberger et al., 1996) suggesting which branches are more frequently taken (generally
obvious to the programmer), and a specially augmented compiler can restructure the code for I-cache
locality. Algorithms for this purpose are described in Mosberger et al. (1996).
    On the other hand, locality-driven processing preserves modularity within layers. Communication
between layers must be changed as follows. If each layer code passes a packet to the code for a higher
layer with a procedure call, this code must be modified to add packets to a queue for the higher layer.
Similarly, when a layer is called, it removes packets from its read queue until the queue is exhausted;
after processing each packet, it places it on the queue for its next-higher layer. This strategy works well
when each layer can reuse buffers from other layers, as is the case for UNIX mbufs. Overall, the code
changes may not be severe.

142      Chapter 5 Copying data
