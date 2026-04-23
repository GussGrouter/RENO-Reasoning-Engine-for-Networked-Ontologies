# Network Algorithmics — 3.7 Exercises 1. Batching, Disk Locality, and Logs: Most serious databases use log files for performance. Because (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 98
- Slice: from `3.7 Exercises 1. Batching, Disk Locality, and Logs: Most serious databases use log files for performance. Because` up to next detected section heading

---

3.7 Exercises
1. Batching, Disk Locality, and Logs: Most serious databases use log files for performance. Because
   writes to disk are expensive, it is cheaper to update only a memory image of a record. However,
   because a crash can occur at any time, the update must also be recorded on disk. This can be done
   by directly updating the record location on disk, but random writes to disk are expensive (see P4a).
   Instead, information on the update is written to a sequential log file. The log entry contains the
   record location, the old value (undo information), and the new value (redo information).
   • Suppose a disk page of 4000 bytes can be written using one disk I/O and that a log record is
     50 bytes. If we apply batching (2c), what is a reasonable strategy for updating the log? What
     fraction of a disk I/O should be charged to a log update?
   • Before a transaction that does the update can commit (i.e., tell the user it is done), it must be
     sure the log is written. Why? Explain why this leads to another form of batching, group commit,
     where multiple transactions are committed together.

72       Chapter 3 Fifteen implementation principles



   • If the database represented by the log gets too far ahead of the database represented on disk,
     crash recovery can take too long. Describe a strategy to bound crash recovery times.
2. Relaxing Consistency Requirements in a Name Service: The Grapevine system (Birell et al.,
   1982) offers a combination of a name service (to translate user names to inboxes) and a mail service.
   To improve availability, Grapevine name servers are replicated. Thus any update to a registration
   record (e.g., Joe → MailSlot3) must be performed on all servers implementing replicas of that
   record. Standard database techniques for distributed databases require that each update be atomic;
   that is, the effect should be as if updates were done simultaneously on all replicas. Because atomic
   updates require that all servers be available, and registration information is not as important as,
   say, bank accounts, Grapevine provides only the following loose semantics (P3): All replicas will
   eventually agree if updates stop. Each update is timestamped and passed from one replica to the
   other in arbitrary order. The highest timestamped update wins.
   • Give an example of how a user could detect inconsistency in Joe’s registration during the con-
     vergence process.
   • If Joe’s record is deleted, it should eventually be purged from the database to save storage. Sup-
     pose a server purges Joe’s record immediately after receiving a Delete update. Why might Add
     updates possibly cause a problem? Suggest a solution.
   • The rule that the latest timestamp wins does not work well when two administrators try to create
     an entry with the same name. Because a later creation could be trapped in a crashed server,
     the administrator of the earlier creation can never know for sure that his creation has won. The
     Grapevine designers did not introduce mechanisms to solve this problem but relied on “some
     human-level centralization of name creation.” Explain their assumption clearly.
3. Replacing General-Purpose Routines with Special-Purpose Routines and Efficient Storage
   Allocators: Consider the design of a general storage allocator that is given control of a large contigu-
   ous piece of memory and may be asked by applications for smaller, variable-size chunks. A general
   allocator is quite complex: As time goes by, the available memory fragments and time must be spent
   finding a piece of the requested size and coalescing adjacent released pieces into larger free blocks.
   • Briefly sketch the design of a general-purpose allocator. Consult a textbook such as Horowitz
     and Sahni (1978) for examples of allocators.
   • Suppose a profile has shown that a large fraction of the applications ask for 64 bytes of storage.
     Describe a more efficient allocator that works for the special case (P6) of allocating just 64-byte
     quantities.
   • How would you optimize the expected case (P11) and yet handle requests for storage other than
     64 bytes?
4. Passing Information in Interfaces: Consider a file system that is reading or writing files from
   disk. Each random disk Read/Write involves positioning the disk over the correct track (seeking).
   If we have a sequence of, say, three Reads to Tracks 1, 15, and 7, it may pay to reorder the second
   and third Reads to reduce waste in terms of seek times. Clearly, as in P1, the larger the context of
   the optimization (e.g., the number of Reads or Writes considered for reordering), the greater the
   potential benefits of such seek optimization.

                                                                                3.7 Exercises          73



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



The previous chapter outlined 15 principles for efficient network protocol implementation. Part 2 of the
book begins a detailed look at specific network bottlenecks such as data copying and control transfer.
While the principles are used in these later chapters, the focus of these later chapters is on the specific
bottleneck being examined. Given that network algorithmics is as much a way of thinking as it is a
set of techniques, it seems useful to round out Part 1 by seeing the principles in action on small, self-
contained, but nontrivial network problems.
    Thus this chapter provides examples of applying the principles in solving specific networking prob-
lems. The examples are drawn from real problems, and some of the solutions are used in real products.
Unlike subsequent chapters, this chapter is not a collection of new material followed by a set of exer-
cises. Instead, this chapter can be thought of as an extended set of exercises.
    In Sections 4.1 to 4.15 15 problems are motivated and described. Each problem is followed by a
hint that suggests specific principles, which is then followed by a solution sketch. There are also a few
exercises after each solution. In classes and seminars on the topic of this chapter, the audience enjoyed
inventing solutions by themselves (after a few hints were provided), rather than directly seeing the final
solutions.


    Quick reference guide
    In an ideal world, each problem should have something interesting for every reader. For those readers pressed for time,
    however, here is some guidance. Hardware designers looking to sample a few problems may wish to try their hand at
    designing an Ethernet monitor (Section 4.4) or doing a binary search on long identifiers (Section 4.14). Systems people
    looking for examples of how systems thinking can finesse algorithmic expertise may wish to tackle a problem on applica-
    tion device channels (Section 4.1) or a problem on compressing the connection table (Section 4.11). Algorithm designers
    may be interested in the problem of identifying a resource hog (Section 4.10) and a problem on the use of protocol design
    changes to simplify an implementation problem in link state routing (Section 4.8).




Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00009-9
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                            75

76        Chapter 4 Principles in action
