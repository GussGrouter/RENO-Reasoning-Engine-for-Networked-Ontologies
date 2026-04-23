# network-algorithmics-7-11-exercises-1-better-hash-functions-currently-hashed-wheels-use-a-very-sim (chunk 000003)

can be done (as we showed in Chapter 6) by packet steering mechanisms that check if the protocol is
TCP and IP (type field in Ethernet) and then demultiplexing based on the TCP 4-tuple.
     Recall that Linux does “early demultiplexing” in one of two ways: either by distributing load using
a hash of the TCP 4-tuple (Receive Packet Steering or RPS), or by sending the packet to the core the
application is running on (Receive Flow Steering or RFS). RFS also uses a hash of the 4-tuple but uses
it to index a table whose entry points to the core the packet should be steered to.
     While this simple hash-based mechanism works very well for TCP and IP, it does not solve the
problem of early demultiplexing for other protocols that the application can specify in real time such
as is needed for a traffic monitoring application. This is the subject of this chapter.
     This chapter is organized as follows. Section 8.1 delineates the reasons for early demultiplexing,
and Section 8.2 outlines the goals of an efficient demultiplexing solution. The rest of the chapter studies
various implementations of early demultiplexing. The chapter starts with the pioneering CMU/Stanford
packet filter (CSPF) (Section 8.3), moves on to the commonly used Berkeley packet filter (BPF) (Sec-
tion 8.4), and ends with more recent proposals, such as Pathfinder (Section 8.5) and DPF (Section 8.6).
     The demultiplexing techniques described in this chapter (and the corresponding principles used) are
summarized in Table 8.1.

Quick reference guide
   The Berkeley packet filter (BPF) is freely available. However, other demultiplexing algorithms are more efficient. The
   implementor who wishes to design a demultiplexing routine should consider PathFinder, described in Section 8.5. While
   dynamic packet filter (DPF, see Section 8.6) is even faster, many implementors may find the need for dynamic code
   generation in DPF to be an obstacle. Recall also that early demultiplexing for TCP connections is now standard and
   is available in Linux under various steering mechanisms. Thus the techiques in this chapter are only useful for flexible
   demultiplexing for say traffic monitoring.

8.1 Opportunities and challenges of early demultiplexing              197

Table 8.1 Principles used in the various demultiplexing
                     techniques discussed in this chapter.
                     Number                      Principle                      Used in
                     P9       Pass header specifications from user to kernel   CSPF
                     P1       Use CFG to avoid unnecessary tests               BPF
                     P4c      Use a register-based specification language
                     P15      Factor common checks using a generalized trie    Pathfinder
                     P2       Specialize code when classifier is modified      DPF
