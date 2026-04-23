# network-algorithmics-1-2-6-characteristics-of-network-algorithmics (chunk 000002)

Thus a feature of this book is an attempt to distill the system’s principles used in algorithmics
   into a set of 15 principles, which are cataloged inside the front cover of the book and are explored
   in detail in Chapter 3. This book attempts to explain and dissect all the network implementations
   described in this book in terms of these principles. The principles are also given numbers for easy
   reference, though for the most part, we will use both the number and the name. For instance, take a
   quick peek at the inside front cover and you will find that relaxing specification is principle P3 and
   lazy evaluation is P2b.
c. Network algorithmics can benefit from algorithmic thinking: While this book stresses the pri-
   macy of systems thinking to finesse problems wherever possible, there are many situations where
   systems constraints prevent any elimination of problems. In our example, after attempting to finesse
   the need for algorithmic thinking by relaxing the specification, the problem of false positives led
   to considering keeping track of the highest counter relative to its threshold value. As a second ex-
   ample, Chapter 11 shows that despite attempts to finesse Internet lookups using what is called tag
   switching, many routers resort to efficient algorithms for lookup.
      It is worth emphasizing, however, that because the models are somewhat different from stan-
   dard theoretical models, it is often insufficient to blindly reuse existing algorithms. For example,
   Chapter 13 discusses how the need to schedule a crossbar switch in 8 nsec leads to considering sim-
   pler maximal matching heuristics, as opposed to more complicated algorithms that produce optimal
   matchings in a bipartite graph.
      As a second example, Chapter 11 describes how the BSD implementation of lookups blindly
   reused a data structure called a Patricia trie, which uses a skip count, to do IP lookups. The resulting
   algorithm requires complex backtracking.1 A simple modification that keeps the actual bits that
   were skipped (instead of the count) avoids the need for backtracking. But this requires some insight
   into the black box (i.e., the algorithm) and its application.
      In summary, the uncritical use of standard algorithms can miss implementation breakthroughs be-
   cause of inappropriate measures (e.g., for packet filters such as BPF, the insertion of a new classifier
   can afford to take more time than search), inappropriate models (e.g., ignoring the effects of cache
   lines in software or parallelism in hardware), and inappropriate analysis (e.g., order-of-complexity
   results that hide constant factors crucial in ensuring wire-speed forwarding).
      Thus another purpose of this book is to persuade implementors that insight into algorithms and
   the use of fundamental algorithmic techniques such as divide-and-conquer and randomization is
   important to master. This leads us to the following.

Definition. Network algorithmics is the use of an interdisciplinary systems approach, seasoned with
algorithmic thinking, to design fast implementations of network processing tasks at servers, routers,
and other networking devices.

Part 1 of the book is devoted to describing the network algorithmics approach in more detail. An
overview of Part 1 is given in Fig. 1.8.

1 The algorithm was considered to be the state of the art for many years and was even implemented in hardware in several router
designs. In fact, a patent for lookups issued to a major router company appears to be a hardware implementation of BSD Patricia
tries with backtracking. Any deficiencies of the algorithm can, of course, be mitigated by fast hardware. However, it is worth
considering that a simple change to the algorithm could have simplified the hardware design.

1.3 Exercise           15

FIGURE 1.8
Preview of network algorithmics. Network algorithmics is introduced using a set of models, strategies, and sample
problems, which are described in Part 1 of the book.
