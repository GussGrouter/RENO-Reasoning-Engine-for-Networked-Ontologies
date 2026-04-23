# network-algorithmics-8-6-dynamic-packet-filter-compilers-to-the-rescue (chunk 000001)

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
