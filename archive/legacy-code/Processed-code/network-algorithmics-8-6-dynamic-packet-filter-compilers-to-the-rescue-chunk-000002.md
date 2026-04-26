# network-algorithmics-8-6-dynamic-packet-filter-compilers-to-the-rescue (chunk 000002)

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
