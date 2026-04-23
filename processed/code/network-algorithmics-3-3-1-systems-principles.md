# Network Algorithmics — fifteen principles: systems principles (3.3.1) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 84 -l 111 -layout
- Slice: from `3.3.1 Systems principles` up to (excluding) `3.3.2 Principles for modularity with efficiency`

---

3.3.1 Systems principles
The first five principles exploit the fact that we are building systems.

P1: Avoid obvious waste in common situations
In a system, there may be wasted resources in special sequences of operations. If these patterns occur
commonly, it may be worth eliminating the waste. This reflects an attitude of thriftiness toward system
costs.
    For example, Chef Charlie has to make a trip to the pantry to get the ice cream maker to make ice
cream and to the pantry for a pie plate when he makes pies. But when he makes pie à la mode, he has
learned to eliminate the obvious waste of two separate trips to the pantry.
    Similarly, optimizing compilers look for obvious waste in terms of repeated subexpressions. For
example, if a statement calculates i = 5.1 ∗ n + 2 and a later statement calculates j := (5.1 ∗ n + 2) ∗ 4,
the calculation of the common subexpression 5.1 ∗ n + 2 is wasteful and can be avoided by computing
the subexpression once, assigning it to a temporary variable t, and then calculating i := t and j := t ∗ 4.
A classic networking example, described in Chapter 5, is avoiding making multiple copies of a packet
between the operating system and user buffers.
    Notice that each operation (e.g., walk to pantry, line of code, single packet copy) considered by
itself has no obvious waste. It is the sequence of operations (two trips to the pantry, two statements
that recompute a subexpression, two copies) that have obvious waste. Clearly, the larger the exposed
context, the greater the scope for optimization. While the identification of certain operation patterns as
being worth optimizing is often a matter of designer intuition, optimizations can be tested in practice
using benchmarks.

P2: Shift computation in time
Systems have an aspect in space and time. The space aspect is represented by the subsystems, possibly
geographically distributed, into which the system is decomposed. The time aspect is represented by
the fact that a system is instantiated at various time scales, from fabrication time to compile time to
parameter-setting times to run time. Many efficiencies can be gained by shifting computation in time.
Here are three generic methods that fall under time-shifting.
• P2a: Precompute. This refers to computing quantities before they are actually used, to save time at
  the point of use. For example, Chef Charlie prepares crushed garlic in advance to save time during
  the dinner rush. A common systems example is table-lookup methods, where the computation of an
  expensive function f in run time is replaced by the lookup of a table that contains the value of f
  for every element in the domain of f . A networking example is the precomputation of IP and TCP
  headers for packets in a connection; because only a few header fields change for each packet, this
  reduces the work to write packet headers (Chapter 9).
• P2b: Evaluate Lazily. This refers to postponing expensive operations at critical times, hoping that
  either the operation will not be needed later or a less busy time will be found to perform the opera-

---

## PDF page 86

             3.3 Fifteen implementation principles—categorization and description                               59




FIGURE 3.8
Easing the implementation of Subsystem 1 by weakening its specification from S to, say, W , at the cost of making
Subsystem 2 do more work.


  tion. For example, Chef Charlie postpones dishwashing to the end of the day. While precomputation
  is computing before the need, lazy evaluation is computing only when needed.
  A famous example of lazy evaluation in systems is copy-on-write in the Mach operating system. Sup-
  pose we have to copy a virtual address space A to another space, B, for process migration. A general
  solution is to copy all pages in A to B to allow for pages in B to be written independently. Instead,
  copy-on-write makes page table entries in B’s virtual address space point to the corresponding page
  in A. When a process using B writes to a location, then a separate copy of the corresponding page in
  A is made for B, and the write is performed. Since we expect the number of pages that are written
  in B to be small compared to the total number of pages, this avoids unnecessary copying.
  A simple networking example occurs when a network packet arrives at an endnode X in a different
  byte order than X’s native byte order. Rather than swap all bytes immediately, it can be more efficient
  to wait to swap the bytes that are actually read.
• P2c: Share Expenses. This refers to taking advantage of expensive operations done by other parts
  of the system. An important example of expense sharing is batching, where several expensive op-
  erations can be done together more cheaply than doing each separately. For example, Charlie bakes
  several pies in one batch. Computer systems have used batch processing for years, especially in the
  early days of mainframes, before time sharing. Batching trades latency for throughput. A simple
  networking example of expense sharing is timing wheels (Chapter 7), where the timer data structure
  shares expensive per-clock-tick processing with the routine that updates the time-of-day clock.

P3: Relax system requirements
When a system is first designed top-down, functions are partitioned among subsystems. After fixing
subsystem requirements and interfaces, individual subsystems are designed. When implementation dif-
ficulties arise, the basic system structure may have to be redone, as shown in Fig. 3.8.
    As shown in Chapter 1, implementation difficulties (e.g., implementing a divide) can sometimes be
solved by relaxing the specification requirements for, say, Subsystem 1. This is shown in the figure by
weakening the specification of Subsystem 1 from, say, S to W , but at the cost of making Subsystem 2
obey a stronger property, Q, compared to the previous property, P .
    Three techniques that arise from this principle are distinguished by how they relax the original
subsystem specification.

---

## PDF page 87

60        Chapter 3 Fifteen implementation principles



• P3a: Trade Certainty for Time. Systems designers can fool themselves into believing that their
  systems offer deterministic guarantees, when in fact we all depend on probabilities. For example,
  quantum mechanics tells us there is some probability that the atoms in your body will rearrange
  themselves to form a hockey puck, but this is clearly improbable.2 This opens the door to consider
  randomized strategies when deterministic algorithms are too slow.
  In systems, randomization is used by millions of Ethernets worldwide to sort out packet-sending
  instants after collisions occur. A simple networking example of randomization is Cisco’s NetFlow
  traffic measurement software: If a router does not have enough processing power to count all arriving
  packets, it can count random samples and still be able to statistically identify large flows. A second
  networking example is stochastic fair queuing (Chapter 14), where, rather than keep track exactly
  of the networking conversations going through a router, conversations are tracked probabilistically
  using hashing.
• P3b: Trade Accuracy for Time. Similarly, numerical analysis cures us of the illusion that comput-
  ers are perfectly accurate. Thus it can pay to relax accuracy requirements for speed. In systems,
  many image compression techniques, such as MPEG, rely on lossy compression using interpolation.
  Chapter 1 used approximate thresholds to replace divides by shifts. In networking, some packet-
  scheduling algorithms at routers (Chapter 14) require sorting packets by their departure deadlines;
  some proposals to reduce sorting overhead at high speeds suggest approximate sorting, which can
  slightly reduce quality-of-service bounds but reduce processing.
• P3c: Shift Computation in Space. Notice that all the examples given for this principle relaxed re-
  quirements: Sampling may miss some packets, and the transferred image may not be identical to the
  original image. However, other parts of the system (e.g., Subsystem 2 in Fig. 3.8) have to adapt to
  these looser requirements. Thus we prefer to call the general idea of moving computation from one
  subsystem to another (“robbing Peter to pay Paul”) shifting computation in space. In networking, for
  example, the need for routers to fragment packets has recently been avoided by having end systems
  calculate a packet size that will pass all routers.

P4: Leverage off system components
A black-box view of system design is to decompose the system into subsystems and then to design
each subsystem in isolation. While this top-down approach has a pleasing modularity, in practice
performance-critical components are often constructed partially bottom-up. For example, algorithms
are designed to fit the features offered by the hardware. Here are some techniques that fall under this
principle.
• P4a: Exploit Locality. Chapter 2 showed that memory hardware offers efficiencies if related data
  is laid out contiguously, e.g., same sector for disks, or same DRAM page for DRAMs. Disk-search
  algorithms exploit this fact by using search trees of high radix, such as B-trees. IP-lookup algorithms
  (Chapter 11) use the same trick to reduce lookup times by placing several keys in a wide word, as
  did the example in Chapter 1.
• P4b: Trade Memory for Speed. The obvious technique is to use more memory, such as lookup tables,
  to save processing time. A less obvious technique is to compress a data structure to make it more
  likely to fit into cache, because cache accesses are cheaper than memory accesses; in this case,


2 Quote due to Tony Lauck.

---

## PDF page 88

              3.3 Fifteen implementation principles—categorization and description                                            61



  both memory and speed may be improved. The Lulea IP-lookup algorithm described in Chapter 11
  uses this idea by using sparse arrays that can still be looked up efficiently using space-efficient
  bitmaps.
• P4c: Exploit Hardware Features. Compilers use strength reduction to optimize away multipli-
  cations in loops; for example, in a loop where addresses are 4 bytes and the index i increases
  by 1 each time, instead of computing 4 ∗ i, the compiler calculates the new array index as be-
  ing 4 higher than its previous value. This exploits the fact that multiplies are more expensive
  than additions on many modern processors. Similarly, it pays to manipulate data in multiples of
  the machine word size, as we will see in the fast IP-checksum algorithms described in Chap-
  ter 9.
    If this principle is carried too far, the modularity of the system will be in jeopardy. Two techniques
alleviate this problem. First, if we exploit other system features only to improve performance, then
changes to those system features can only affect performance and not correctness. Second, we use this
technique only for system components that profiling has shown to be a bottleneck.

P5: Add hardware to improve performance
When all else fails, goes the aphorism, use brute force. Adding new hardware,3 such as buying a faster
processor, can be simpler and more cost effective than using clever techniques. Besides the brute-force
approach of using faster infrastructure (e.g., faster processors, memory, buses, links), there are cleverer
hardware–software trade-offs. Since hardware is less flexible and has higher design costs, it pays to add
the minimum amount of hardware needed.
    Thus baking at the Greasy Spoon was sped up using microwave ovens. In computer systems, dra-
matic improvements each year in processor speeds and memory densities suggest doing key algorithms
in software and upgrading to faster processors for speed increases. But computer systems abound with
cleverer hardware–software trade-offs.
    For example, in a multiprocessor system, if a processor wishes to write data, it must inform any
“owners” of cached versions of the data. This interaction can be avoided if each processor has a piece
of hardware that watches the bus for write transactions by other processors and automatically inval-
idates the cached location when necessary. This simple hardware snoopy cache controller allows the
remainder of the cache-consistency algorithm to be efficiently performed in software.
    Decomposing functions between hardware and software is an art in itself. Hardware offers several
benefits. First, there is no time required to fetch instructions: Instructions are effectively hardcoded.
Second, common computational sequences (which would require several instructions in software) can
be done in a single hardware clock cycle. For example, finding the first bit set in, say, a 32-bit word
may take several instructions on a RISC machine but can be computed by a simple priority encoder, as
shown in the previous chapter.
    Third, hardware allows you to explicitly take advantage of parallelism inherent in the problem.
Finally, hardware manufactured in volume may be cheaper than a general-purpose processor. For ex-
ample, a Pentium may cost $100, while an ASIC in volume with similar speeds may cost $10.


3 By contrast, Principle P4 talks about exploiting existing system features, such as the existing hardware. Of course, the distinc-
tion between principles tends to blur and must be taken with a grain of salt.

---

## PDF page 89

62       Chapter 3 Fifteen implementation principles



    On the other hand, a software design is easily transported to the next generation of faster chips.
Hardware, despite the use of programmable chips, is still less flexible. Despite this, with the advent of
design tools such as VHDL synthesis packages, hardware design times have decreased considerably.
Thus in the last few years chips performing fairly complex functions, such as image compression and
IP lookups, have been designed.
    Besides specific performance improvements, new technology can result in a complete paradigm
shift. A visionary designer may completely redesign a system in anticipation of such trends. For exam-
ple, the invention of the transistor and fast digital memories certainly enabled the use of digitized voice
in the telephone network.
    Increases in chip density have led computer architects to ponder what computational features to add
to memories to alleviate the processor-memory bottleneck. In networks, the availability of high-speed
links in the 1980s led to the use of large addresses and large headers. Ironically, the emergence of
laptops in the 1990s led to the use of low-bandwidth wireless links and to a renewed concern for header
compression. Technology trends can seesaw!
    The following specific hardware techniques are often used in networking ASICs and are worth
mentioning. They were first described in Chapter 2 and are repeated here for convenience.
• P5a: Use Memory Interleaving and Pipelining. Similar techniques are used in IP lookup, in classi-
  fication, and in scheduling algorithms that implement QoS. The multiple banks can be implemented
  using several external memories, a single external memory such as a RAMBUS, or on-chip SRAM
  within a chip that also contains processing logic.
• P5b: Use Wide Word Parallelism. A common theme in many networking designs, such as the
  Lucent bit vector scheme (Chapter 12), is to use wide memory words that can be processed in
  parallel. This can be implemented using DRAM and exploiting page mode or by using SRAM and
  making each memory word wider.
• P5c: Combine DRAM and SRAM. We have explained in Chapter 2 and will explain in Chapter 16
  two clever applications of this principle.
