# network-algorithmics-3-7-exercises-1-batching-disk-locality-and-logs-most-serious-databases-use-l (chunk 000003)

A normal file system only has an interface to open, read, and write a single file. However, suppose
   an application is reading multiple files and can pass that information (P9) in the file system call.
   • What information about the pattern of file accesses would be useful for the file system to perform
     seek optimization? What should the interface look like?
   • Give examples of applications that process multiple files and could benefit from this optimization.
     For more details, see the paper by Patterson et al. (1995). They call this form of tip a disclosure.
5. Optimizing the Expected Case, Using Algorithmic Ideas, and Scavenging Files: The Alto com-
   puter used a scavenging system (Lampson, 1989) that scans the disk after a crash to reconstruct file
   system indexes that map from file names and blocks to disk sectors. This can be done because each
   disk sector that contains a file block also contains the corresponding file identifier. What complicates
   matters is that the main memory is not large enough to hold information for every disk sector. Thus
   a single scan that builds a list in memory for each file will not work. Assume that the information
   for a single file will fit into memory. Thus a way that will work is to make a single scan of the disk
   for each file, but that would be obvious waste (P1) and too slow.
   Instead, observe that in the expected case, most files are allocated contiguously. Thus suppose File
   X has pages 1–1000 located on disk sectors 301–1300. Thus the information about 1000 sectors can
   be compactly represented by three integers and a file name. Call this a run node.
   • Assume the expected case holds and that all run nodes can fit in memory. Assume also that the
     file index for each file is an array (stored on disk) that maps from file block number to disk sector
     number. Show how to rebuild all the file indexes.
   • Now suppose the expected case does not hold and that the run nodes do not all fit into memory.
     Describe a technique, based on the algorithmic idea of divide-and-conquer (P15), that is guaran-
     teed to work (without reverting to the naive idea of building the index for one file at a time unless
     strictly necessary).

This page intentionally left blank

CHAPTER

Principles in action
                                                                                                                   4
                              System architecture and design, like any art, can only be learned by doing. . . . The space of
                                                                      possibilities unfolds only as the medium is worked.
                                                                                           —Carver Mead and Lynn Conway

Having rounded up my horses, I now set myself to put them through their paces.
                                                                                                            —Arnold Toynbee
