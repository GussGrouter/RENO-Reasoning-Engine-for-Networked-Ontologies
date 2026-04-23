# network-algorithmics-4-15-video-conferencing-via-asynchronous-transfer-mode (chunk 000004)

and introduces a well-known technique called integrated layer processing. Section 5.6 broadens the
discussion beyond copying to show that without careful consideration of cache effects, performance
can suffer.
    The world has changed since the first edition of this book and this chapter reflects some of these
changes. The changes include the emergence of servers with multicore CPUs with NUMA (non-
uniform memory access, where groups of cores share an L3 cache), the rapid emergence of 100 Gbps
links, the ubiquity of solid state disks (NVM) that can saturate network links, and recent trends in re-
mote DMA techniques such as the popular RoCE (RDMA over converged Ethernet). We will fit these
trends into our framework, showing that the main ideas of the first edition still hold.
    Although this is the first chapter of the book that is devoted to techniques for overcoming a specific
bottleneck, the techniques are based on the principles described in Part I of the book. The techniques
and the corresponding principles are summarized in Table 5.1.

Quick reference guide
  The most useful sections for an implementor today are as follows. Section 5.3.1 on remote direct memory access (RDMA)
  describes techniques to avoid memory copying overheads in computing and storage clusters and modern incarnations
  of the idea like RoCE and Fibre Channel. RDMA is only useful for some applications, and so the remaining sections
  concentrate on avoiding copying overheads in general purpose operating systems. Section 5.2.5 summarizes the current
  thinking on zero-copy networking and some modern proposals in Linux that could benefit from a form of precomputation
  called fbufs that is introduced in Section 5.2.3. Section 5.4.3 describes a less radical but effective method called I/O
  splicing to directly connect I/O subsystems and send a file without copying. Finally, Section 5.6.1 describes techniques to
  improve cache performance.

5.1 Why data copies                  113

FIGURE 5.1
Redundant copies involved in handling a GET request at a server.
