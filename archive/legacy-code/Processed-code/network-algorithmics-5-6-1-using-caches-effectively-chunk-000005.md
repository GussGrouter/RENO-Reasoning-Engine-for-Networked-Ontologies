# network-algorithmics-5-6-1-using-caches-effectively (chunk 000005)

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
