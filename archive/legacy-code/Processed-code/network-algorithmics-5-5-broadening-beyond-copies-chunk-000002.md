# network-algorithmics-5-5-broadening-beyond-copies (chunk 000002)

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
