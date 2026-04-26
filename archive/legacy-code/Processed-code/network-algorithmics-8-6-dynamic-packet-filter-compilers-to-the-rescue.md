# Network Algorithmics — 8.6 Dynamic packet filter: compilers to the rescue (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 232
- Slice: from `8.6 Dynamic packet filter: compilers to the rescue` up to next detected section heading

---

8.6 Dynamic packet filter: compilers to the rescue
The Pathfinder story ends with an appeal to hardware to handle demultiplexing at high speeds. Since
it is unlikely that most workstations and PCs today can afford dedicated demultiplexing hardware, it
appears that implementors must choose between the flexibility afforded by early demultiplexing and
the limited performance of a software classifier. Thus it is hardly surprising that high-performance
TCP (Clark et al., 1989), active messages (von Eicken et al., 1992b), and remote procedure call (RPC)
(Thekkath et al., 1993) implementations use hand-crafted demultiplexing routines.
     Dynamic packet filter (DPF) (Engler and Kaashoek, 1996) attempts to have its cake (gain flexibility)
and eat it (obtain performance) at the same time. DPF starts with the Pathfinder trie idea. However,
it goes on to eliminate indirections and extra checks inherent in cell processing by recompiling the
classifier into machine code each time a filter is added or deleted. In effect, DPF produces separate,
optimized code for each cell in the trie, as opposed to generic, unoptimized code that can parse any cell
in the trie.
     DPF is based on dynamic code generation technology (Engler, 1996), which allows code to be
generated at run time instead of when the kernel is compiled. DPF is an application of Principle P2,
shifting computation in time. Note that by run time we mean classifier update time and not packet
processing time.
     This is fortunate because this implies that DPF must be able to recompile code fast enough so as not
to slow down a classifier update. For example, it may take milliseconds to set up a connection, which
in turn requires adding a filter to identify the endpoint at the same time. By contrast, it can take a few

206      Chapter 8 Demultiplexing



microseconds to receive a minimum-size packet at gigabit rates. Despite this leeway, submillisecond
compile times are still challenging.
   To understand why using specialized code per cell is useful, it helps to understand two generic
causes of cell-processing inefficiency in Pathfinder:
• Interpretation Overhead: Pathfinder code is indeed compiled into machine instructions when kernel
  code is compiled. However, the code does, in some sense, “interpret” a generic Pathfinder cell. To see
  this, consider a generic Pathfinder cell C that specifies a 4-tuple: offset, length, mask, value.
  When a packet P arrives, idealized machine code to check whether the cell matches the packet is as
  follows:
   LOAD R1, C(Offset); (* load offset specified in cell into register R1 *)
   LOAD R2, C(length); (* load length specified in cell into register R2 *)
   LOAD R3, P(R1, R2); (* load packet field specified by offset into R3 *)
   LOAD R1, C(mask); (* load mask specified in cell into register R1 *)
   AND R3, R1; (* mask packet field as specified in cell *)
   LOAD R2, C(value); (* load value specified in cell into register R2 *)
   BNE R2, R3; (* branch if masked packet field is not equal to value *)

  Notice the extra instructions and extra memory references in Lines 1, 2, 4, and 6 that are used to
  load parameters from a generic cell in order to be available for later comparison.
• Safety-Checking Overhead: Because packet filters written by users cannot be trusted, all implemen-
  tations must perform checks to guard against errors. For example, every reference to a packet field
  must be checked at run time to ensure that it stays within the current packet being demultiplexed.
  Similarly, references need to be checked in real time for memory alignment; on many machines,
  a memory reference that is not aligned to a multiple of a word size can cause a trap. After these
  additional checks, the code fragment shown earlier is more complicated and contains even more
  instructions.
    By specializing code for each cell, DPF can eliminate these two sources of overhead by exploiting
information known when the cell is added to the Pathfinder graph.
• Exterminating Interpretation Overhead: Since DPF knows all the cell parameters when the cell is
  created, DPF can generate code in which the cell parameters are directly encoded into the machine
  code as immediate operands. For example, the earlier code fragment to parse a generic Pathfinder
  cell collapses to the more compact cell-specific code:
   LOAD R3, P(offset, length); (* load packet field into R3 *)
   AND R3, mask; (* mask packet field using mask in instruction *)
   BNE R3, value; (* branch if field not equal to value *)

  Notice that the extra instructions and (more importantly) extra memory references to load parameters
  have disappeared, because the parameters are directly placed as immediate operands within the
  instructions.
• Mitigating Safety-Checking Overhead: Alignment checking can be reduced in the expected case
  (P11) by inferring at compile time that most references are word aligned. This can be done by
  examining the complete filter. If the initial reference is word aligned and the current reference (offset

                                   8.6 Dynamic packet filter: compilers to the rescue                207



   plus the length of all previous headers) is a multiple of the word length, then the reference is word
   aligned. Real-time alignment checks need only be used when the compile time inference fails, for
   example, when indirect loads are performed (e.g., a variable-size IP header). Similarly, at compile
   time the largest offset used in any cell can be determined and a single check can be placed (before
   packet processing) to ensure that the largest offset is within the length of the current packet.
   Once one is onto a good thing, it pays to push it for all it is worth. DPF goes on to exploit compile
time knowledge in DPF to perform further optimizations as follows. A first optimization is to combine
small accesses to adjacent fields into a single large access. Other optimizations are explored in the
exercises.
   DPF has the following potential disadvantages that are made manageable through careful design.
• Recompilation Time: Recall that when a filter is added to the Pathfinder trie (Fig. 8.5), only cells
  that were not present in the original trie need to be created. DPF optimizes this expected case (P11)
  by caching the code for existing cells and copying this code directly (without recreating them from
  scratch) to the new classifier code block. New code must be emitted only for the newly created cells.
  Similarly, when a new value is added to a hash table (e.g., the new TCP port added in Fig. 8.5),
  unless the hash function changes, the code is reused and only the hash table is updated.
• Code Bloat: One of the standard advantages of interpretation is more compact code. Generating
  specialized code per cell appears to create excessive amounts of code, especially for large numbers
  of filters. A large code footprint can, in turn, result in degraded instruction cache performance. How-
  ever, a careful examination shows that the number of distinct code blocks generated by DPF is only
  proportional to the number of distinct header fields examined by all filters. This should scale much
  better than the number of filters. Consider, for example, 10,000 simultaneous TCP connections, for
  which DPF may emit only three specialized code blocks: one for the Ethernet header, one for the IP
  header, and one hash table for the TCP header.
    The final performance numbers for DPF are impressive. DPF demultiplexes messages 13–26 times
faster than Pathfinder on a comparable platform (Engler and Kaashoek, 1996). The time to add a filter,
however, is only three times slower than Pathfinder. Dynamic code generation accounts for only 40%
of this increased insertion overhead.
    In any case, the larger insertion costs appear to be a reasonable way to pay for faster demultiplexing.
Finally, DPF demultiplexing routines appear to rival or beat hand-crafted demultiplexing routines; for
instance, a DPF routine to demultiplex IP packets takes 18 instructions, compared to an earlier value,
reported in Clark (1985), of 57 instructions. While the two implementations were on different machines,
the numbers provide some indication of DPF quality.
    The final message of DPF is twofold. First, DPF indicates that one can obtain both performance
and flexibility. Just as compiler-generated code is often faster than hand-crafted code, DPF code ap-
pears to make hand-crafted demultiplexing no longer necessary. Second, DPF indicates that hardware
support for demultiplexing at line rates may not be necessary. In fact, it may be difficult to allow
dynamic code generation on filter creation in a hardware implementation. Software demultiplexing
allows cheaper workstations; it also allows demultiplexing code to benefit from processor speed im-
provements.

208      Chapter 8 Demultiplexing



                       Technology changes can invalidate design assumptions
      There are several examples of innovations in architecture and operating systems that were
  discarded after initial use and then returned to be used again. While this may seem like the whims
  of fashion (“collars are frilled again in 1995”) or reinventing the wheel (“there is nothing new
  under the sun”), it takes a careful understanding of current technology to know when to dust off
  an old idea, possibly even in a new guise.
      Take, for example, the core of the telephone network used to send voice calls via analog sig-
  nals. With the advent of fiber optics and the transistor, much of the core telephone network now
  transmits voice signals in digital formats using the T1 and SONET hierarchies. However, with the
  advent of wavelength-division multiplexing in optical fiber, there is at least some talk of returning
  to analog transmission.
      Thus the good system designer must constantly monitor available technology to check whether
  the system design assumptions have been invalidated. The idea of using dynamic compilation was
  mentioned by the CSPF designers in Mogul et al. (1987) but was not considered further. The CSPF
  designers assumed that tailoring code to specific sets of filters (by recompiling the classifier code
  whenever a filter was added) was too “complicated.”
      Dynamic compilation at the time of the CSPF design was probably slow and also not portable
  across systems; the gains at that time would have also been marginal because of other bottlenecks.
  However, by the time DPF was being designed, a number of systems, including VCODE (Engler,
  1996), had designed fairly fast and portable dynamic compilation infrastructure. The other clas-
  sifier implementations in DPF’s lineage had also eliminated other bottlenecks, which allowed the
  benefits of dynamic compilation to stand out more clearly.
