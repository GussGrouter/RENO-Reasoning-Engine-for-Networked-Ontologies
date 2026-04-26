# network-algorithmics-18-2-3-algorithmic-thinking (chunk 000001)

# Network Algorithmics — 18.2.3 Algorithmic thinking (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 549
- Slice: from `18.2.3 Algorithmic thinking` up to next detected section heading

---

18.2.3 Algorithmic thinking
Algorithmic thinking refers to thinking about networking bottlenecks the way algorithm designers ap-
proach problems. Overall, algorithmic approaches are less important than other systems approaches, as
embodied by Principles P1 through P10. Also, it is dangerous to blindly reuse existing algorithms.
    The first problem that must be confronted in using algorithmic thinking is how to frame the problem
that must be solved. By changing the problem, one can often find more effective solutions. Consider
the following problem, which we avoided in Chapter 11.
Example (Pipelining and Memory Allocation). A lookup engine is using a trie. The lookup engine
must be pipelined for speed. The simplest solution is to pipeline the trie by level. The root is at the first
stage, the children of the root are assigned to the second stage, the nodes at height 2 to the third stage,
etc. Unfortunately, the memory needs for each stage can vary as prefixes are inserted and deleted. There
is the following spectrum of approaches.

• Centralized memory: All the processing stages share a single memory. Memory allocation is easy,
  but the centralized memory becomes a bottleneck.
• One memory per stage: Each processing stage has its own memory, minimizing memory contention.
  However, since the memory is statically allocated at fabrication time, any memory unused by a stage
  cannot be used by another stage.
• Dynamically allocate small 1-port memories to stages: As suggested in Chapter 11, on-chip memory
  is divided into M SRAMs, which are connected to stage processors via a crossbar. As a processor
  requires more or less memory, crossbar connections can be changed to allocate more or fewer mem-
  ories to each stage. This scheme requires a large M to avoid wasting memory, but a large M can
  lead to high capacitive loads.
• Dynamically allocate medium-size 2-port memories to stages: The setting is identical to the last
  approach, except that each memory is now a 2-port memory that can be allocated to two processors.
  Using this, it is possible to show that N memories are sufficient for N processors, with almost no
  memory wastage.
• Dynamically change the starting point in the pipeline: In a conventional linear pipeline all lookups
  start at the first stage and leave at the last. Florin Baboescu has suggested an alternative: Using
  a lookup table indexed on the first few bits, assign each address to a different first processor in
  the pipeline. Thus different addresses have different start and end processors. However, this gives
  considerably more flexibility in allocating memory to processors by changing the assignment of
  addresses to processors.
• Pipeline by depth: Instead of pipelining a tree by height, consider pipelining by depth. All leaves
  are assigned to the last stage, K, all parents of the leaves to stage K − 1, etc.

These approaches represent the interplay between Principles P13 (optimizing degrees of freedom)
and P5 (add hardware). However, each approach results in a different algorithmic problem! Thus a far
more important skill than solving a hard problem is the skill required to frame the right problems that
balance overall system needs.
   Principles P11 and P13 help choose the right problem to solve. The pipelining example shows that
choosing the degrees of freedom (P13) can change the algorithmic problem solved.
   Similarly, Principle P11, optimizing the expected case, can sometimes help decide what the right
measure is to optimize. This in turn influences the choice of algorithm. For example, simple TCP

18.2 What network algorithmics is about               523
