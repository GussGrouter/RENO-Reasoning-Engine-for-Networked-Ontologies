# network-algorithmics-3-3-1-systems-principles (chunk 000005)

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
