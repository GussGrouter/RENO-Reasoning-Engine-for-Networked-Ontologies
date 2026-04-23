# Network Algorithmics — 1.2.6 Characteristics of network algorithmics (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 40
- Slice: from `1.2.6 Characteristics of network algorithmics` up to next detected section heading

---

1.2.6 Characteristics of network algorithmics
The example of scenting an evil packet illustrates three important aspects of network algorithmics.
a. Network algorithmics is interdisciplinary: Given the high rates at which network processing must
   be done, a router designer would be hard pressed not to use hardware. The example exploited several
   features of hardware: It assumed that wide words of arbitrary size were easily possible; it assumed
   that shifts were easier than divides; it assumed that memory references were the bottleneck; it as-
   sumed that a 256-element array contained in fast on-chip memory was feasible; it assumed that
   adding a few extra registers was feasible; and finally it assumed that small changes to the logic to
   combine URL processing and initialization were trivial to implement.
      For the reader unfamiliar with hardware design, this is a little like jumping into a game of cards
   without knowing the rules and then finding oneself finessed and trumped in unexpected ways. A con-
   tention of this book is that mastery of a few relevant aspects of hardware design can help even a
   software designer understands at least the feasibility of different hardware designs. A further con-
   tention of this book is that such interdisciplinary thinking can help produce the best designs.
      Thus Chapter 2 presents the rules of the game. It presents simple models of hardware that point
   out opportunities for finessing and trumping troublesome implementation issues. It also presents
   simple models of operating systems. This is done because end systems such as clients and Web
   servers require tinkering with and understanding operating system issues to improve performance,
   just as routers and network devices require tinkering with hardware.
b. Network algorithmics recognizes the primacy of systems thinking: The specification was relaxed
   to allow approximate thresholds in powers of 2, which simplified the hardware. Relaxing specifica-
   tions and moving work from one subsystem to another is an extremely common systems technique,
   but it is not encouraged by current educational practice in universities, in which each area is taught
   in isolation.
      Thus today, one has separate courses in algorithms, in operating systems, and in networking.
   This tends to encourage “black box” thinking instead of holistic or systems thinking. The example
   alluded to other systems techniques, such as the use of lazy evaluation and trading memory for
   processing in order to scrub the Count array.

14         Chapter 1 Introducing network algorithmics



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


    While this book concentrates on networking, the general algorithmics approach holds for the im-
plementation of any computer system, whether a database, a processor architecture, or a software
application. This general philosophy is alluded to in Chapter 3 by providing illustrative examples
from the field of computer system implementation. The reader interested only in networking should
rest assured that the remainder of the book, other than Chapter 3, avoids further digressions beyond
networking.
    While Parts 2 and 3 provide specific techniques for important specific problems, the main goal of
this book is to allow the reader to be able to tackle arbitrary packet-processing tasks at high speeds
in software or hardware. Thus the implementor of the future may be given the task of speeding up
XML processing in a Web server (likely, given current trends) or even the task of computing the chi-
square statistic in a router (possible because chi-square provides a test for detecting observed abnormal
frequencies for tasks such as intrusion detection). Despite being assigned a completely unfamiliar task,
the hope is that the implementor would be able to craft a new solution to such tasks using the models,
principles, and techniques described in this book.
