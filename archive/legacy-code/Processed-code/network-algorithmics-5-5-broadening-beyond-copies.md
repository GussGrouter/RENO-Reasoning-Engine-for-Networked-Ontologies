# Network Algorithmics — 5.5 Broadening beyond copies (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 161
- Slice: from `5.5 Broadening beyond copies` up to next detected section heading

---

5.5 Broadening beyond copies
There are several data manipulations in the network beyond copying that can be made more efficent if
done at the same time, avoiiding multiple passes over the data. This leverages the principle of avoiding

                                                                 5.5 Broadening beyond copies                  135




FIGURE 5.10
In I/O splicing, all the indirection caused by copying to and from user-space buffers is removed by a single system
call that “splices” together the I/O stream from the disk with the I/O stream to the network. As always, Copy 1 can
be removed for files in the cache.



obvious waste (P1), and expense sharing (P2c). We describe two such ideas, integrated layer processing
(ILP) and in-network computing.
    ILP: Clark and Tennehouse, in a landmark paper, suggested generalizing Van Jacobson’s idea (de-
scribed earlier) of integrating checksums and copying. In more detail the Jacobson idea is based on the
following observation. When copying a packet word from a location (say, W 10 in adaptor memory in
Fig. 5.11) to a location in memory (say, M9 in memory in Fig. 5.11), the processor has to load W 10 into
a register and then store that register to M9. Typically, most RISC processors require that, between a
load and a store, the compiler insert a so-called delay slot, or empty cycle, to keep the pipeline working
correctly (never mind why!). That empty cycle can be used for other computation. For example, it can
be used to add the word just read to a register that holds the current checksum. Thus with no extra cost
the copy loop can often be augmented to be the checksum loop as well.
    But there are other data-intensive manipulations, such as encrypting data and doing format conver-
sions. Why not, Clark and Tennenhouse (1990) argued, integrate all such manipulations into the copy
loop? For example, in Fig. 5.11 the CPU could read W 10 and then decrypt W 10 and write the decrypted
word to M9 rather than have that done in another loop. They called this idea integrated layer process-
ing, or ILP. The essential idea is to avoid obvious waste (P1), in terms of reading (and possibly) writing
the bytes of a packet several times for multiple data-manipulation operations on the same packet.

136      Chapter 5 Copying data




FIGURE 5.11
Integrating checksumming and copying.


   Thus ILP is a generalization of copy-checksum integration to other manipulations (e.g., encryption,
presentation formatting). However, it has several challenges.
• Challenge 1: Information needed for manipulations is typically at different layers (e.g., encryption
  is at the application layer, and checksumming is done at the TCP layer). Integrating the code from
  different layers without sacrificing modularity is hard.
• Challenge 2: Each manipulation may operate on different-size chunks and different portions of the
  packet. For example, TCP works in 16-bit quantities for a 16-bit checksum, while the popular DES
  encryption works in 64-bit quantities. Thus while working with one 32-bit word, the ILP loop has
  to deal with two TCP checksum words and half a DES word.
• Challenge 3: Some manipulations may be dependent on each other. For example, one should prob-
  ably not decrypt a packet if the TCP checksum fails.
• Challenge 4: ILP can increase cache miss rate because it can reduce locality within a single ma-
  nipulation. If we did TCP separately and DES separately instead of in a single loop, the code we’d
  use at each instant is smaller for the two single loops as opposed to the single loop. This makes it
  more likely that the code will be found in the instruction cache in the more naive implementation.
  Increasing integration beyond a certain point can destroy code locality so much that it may even
  have adverse effects. Some studies have shown this to be a major issue.
   The first three challenges show that ILP is hard to do. The fourth challenge suggests that integrating
more than a few operations can possibly even reduce performance. Finally, if the packet data is used
multiple times, it could well reside in the data cache (even in a naive implementation), making all the
bother about integrating loops unnecessary. Possibly for these reasons, ILP has remained a tantalizing
idea. Beyond the copy–checksum combination, there has been little follow-up work in integrating other
manipulations in academic or commercial systems.
   In-Network Computing and SHARP: In contrast to in-network computing, recent Infiniband hard-
ware (SHARP, 2019) has made the very old idea of in-network computing a practical reality at very high
speeds. The idea is that many High Performance Computing applications synchronize multiple com-
putations using mechanisms such as barriers and reduction, and reduce data using constructs such as

                                           5.6 Broadening beyond data manipulations                  137



AllReduce. Further, many distributed machine learning algorithms need aggregate computations such
as summing or finding the minimum of a large number of variables. If aggregate operations can be per-
formed while data is travelling through the network, host computation can be saved. More importantly,
in-network computing can reduce latency and even network bandwidth.
    SHARP (2019) (Scalable Hierarchical Aggregation and Reduction Protocol) does precisely that. In
some sense, SHARP does integrated processing of the application and network layers, a form of ILP.
The problem of breaking layer abstraction is mitigated by the network offering a set of abstractions
for these commonly used functions. SHARP technology has been incorporated into the classic MPI
(Message Passing Interface for parallel computers), and is used in several supercomputers.
