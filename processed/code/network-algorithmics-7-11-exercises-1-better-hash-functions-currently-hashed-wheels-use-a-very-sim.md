# Network Algorithmics — 7.11 Exercises 1. Better Hash Functions: Currently hashed wheels use a very simple and primitive hash function (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 220
- Slice: from `7.11 Exercises 1. Better Hash Functions: Currently hashed wheels use a very simple and primitive hash function` up to next detected section heading

---

7.11 Exercises
1. Better Hash Functions: Currently hashed wheels use a very simple and primitive hash function
   (low-order bits). Find a way to use your favorite hash function to do hashed wheels. (Hint: Consider

194      Chapter 7 Maintaining timers



   working with absolute time and not relative time.) What particular aspect of performance of a timer
   module would a better hash function improve? (This idea is due to Travis Newhouse.)
2. Hierarchical Wheels Versus Hashed Wheels and Heaps: Current implementations of timing
   wheels use hashed wheels.
   • What is one possible advantage of hierarchical wheels over hashed wheels? Can you quantify the
     difference precisely?
   • Suppose we do hierarchical wheels by dividing a 32-bit timer into four chunks of 8 bits apiece.
     What is the difference between such a timing wheel and a 256-way d-heap? When might the
     heap be a better solution?

                                                                                                         CHAPTER


Demultiplexing
                                                                                                             8
                  Biologically the species is the accumulation of the experiments of all its successful individuals since
                                                                                                           the beginning.
                                                                                                            —H.G. Wells



A protocol, like a copy center or an ice cream parlor, should be able to serve multiple clients. The
clients of a protocol could be end-users (as in the case of the file transfer protocol), software programs
(for example, when the tool traceroute uses the Internet protocol), or even other protocols (as in the
case of the email protocol SMTP, which uses TCP).
    Thus when a message arrives, the receiving protocol must dispatch the received message to the
appropriate client. This function is called demultiplexing. Demultiplexing is an integral part of data link,
routing, and transport protocols. It is a fundamental part of the abstract protocol model of Chapter 2.
    Traditionally, demultiplexing is done layer by layer using a demultiplexing field contained in each
layer header of the received message. Called layered demultiplexing, this is shown in Fig. 8.1. For ex-
ample, working from bottom to top in the picture, a packet may arrive on the Ethernet at a workstation.
The packet is examined by the Ethernet driver, which looks at a so-called protocol type field to decide
what routing protocol (e.g., IP, IPX) is being used. Assuming the type field specifies IP, the Ethernet
driver may upcall the IP software.
    After IP processing, the IP software inspects the protocol ID field in the IP header to determine
the transport protocol (e.g., TCP or UDP?). Assuming it is TCP, the packet will be passed to the TCP
software. After doing TCP processing, the TCP software will examine the port numbers in the packet
to demultiplex the packet to the right client, say, to a process implementing HTTP.
    Traditional demultiplexing is fairly straightforward because each layer essentially does an exact
match on some field or fields in the layer header. This can be done easily, using, say, hashing, as we
describe in Chapter 10. Of course, the lookup costs add up at each layer.
    By contrast, this chapter concentrates on early demultiplexing, which is a much more challenging
task at high speeds. Referring back to Fig. 8.1, early demultiplexing determines the entire path of
protocols taken by the received packet in one operation when the packet first arrives. In the last example
early demultiplexing would determine in one fell swoop that the path of the Web packet was Ethernet,
IP, TCP, Web. A possibly better term is layered demultiplexing. However, this book uses the more
accepted name of early demultiplexing.
    What makes early demultiplexing hard in general is to also allow applications to flexibly specify the
lower layer protocols they wish to run over or whose packets they wish to receive. This is particularly
useful for traffic monitoring or security applications. However, if the early demultiplexing is confined
to TCP connections that have become standard in the last 20 years, the problem is much simpler and
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00014-2
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                   195

196       Chapter 8 Demultiplexing




FIGURE 8.1
Traditional layered demultiplexing has each layer demultiplex a packet to the next layer software above using a field
in the layer header.

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
