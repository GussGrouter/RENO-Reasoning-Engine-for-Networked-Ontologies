# Network Algorithmics — 6.9 Exercises 1. Packet Filters and Upcalls: In the description on upcalls (Fig. 6.2) we showed that the system (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 202
- Slice: from `6.9 Exercises 1. Packet Filters and Upcalls: In the description on upcalls (Fig. 6.2) we showed that the system` up to next detected section heading

---

6.9 Exercises
1. Packet Filters and Upcalls: In the description on upcalls (Fig. 6.2) we showed that the system
   figured out which application the packet was for by upcalling a transport routine. But if you can do
   that, who needs packet filters anyway? What hidden assumption is being made here?

176     Chapter 6 Transferring control



2. Comparing Web Server Structuring Models: In the text we compared various server structuring
   mechanisms with respect to simple metrics such as scheduling efficiency and CPU concurrency.
   Consider the following other metrics for comparison.
   • Disk Concurrency: Some systems employ multiple disks and do disk scheduling. Why might
     the event-driven approach have problems in such an environment, compared to a multithreaded
     approach? Does the event-driven approach with helper processes have the same problems?
   • Gathering Statistics: Web servers need to keep statistics on usage patterns for accounting. Why
     might gathering statistics be more complex in process-per-client and thread-per-client architec-
     tures? Why is it simpler in an event-driven architecture?
3. Algorithms versus Algorithmics in ufalloc() Reimplementation: In this exercise we will consider
   how to efficiently reimplement ufalloc() to find the lowest unallocated descriptor.
   • First consider using a binary heap. For N identifiers, how many memory accesses are required?
     How much space is required, in bits?
   • Assume that the machine has a W -bit (e.g., for the Alpha, W = 64) word and that there is an
     efficient instruction (or set of instructions) to find the rightmost zero in a W -bit word. Suppose
     the allocated descriptors are represented as set bits in a large bitmap (P14) of size N . Show how
     to augment this bitmap with some extra state (P12) to efficiently compute the lowest unallocated
     descriptor.
   • What are the space and time costs of this scheme compared to a simple heap? Can a simple heap
     be made faster by the (standard) trick of increasing the radix of the heap to have K > 1 elements
     in every heap node?
4. Modified Implementation of Fast select(): The text explains how elements are added to the sets
   I , H , and R but does not specify completely how they are removed. Explain how elements are
   removed, especially with respect to the hints set H .
5. Modified Implementation of Fast select(): In the fast select implementation of Banga and Mogul
   (1998), consider changing the implementation as follows:
   (a) First, Inew is set equal to S (and not to Iold ∪ S as before).
   (b) Rnew is computed as before.
   (c) What is returned to the user is Rnew (and not Rnew ∩ S) as before.
   Answer the following questions.
   • Explain in words what is different from this implementation and the one proposed by Banga and
     Mogul.
   • Explain why this implementation may require one to be careful about how it removes elements
     from the hints set H in order not to miss state changes due to newly arriving packets.
   • Explain how this scheme can be inferior to the existing implementation, assuming no application
     changes. Find a worst-case scenario.
   • Explain why this implementation can sometimes be better than the existing implementation if
     the application is smart enough not to choose a socket in its selecting set as long as it still has
     unread data. (In other words, if a socket has unconsumed data, the application is smart enough
     not to select it until all data has been consumed.)

                                                                             6.9 Exercises        177



6. Comparing the APIC Approach to the ADC Approach: In the text we described the ADC ap-
   proach to application-level networking, thereby bypassing the kernel and avoiding system calls. We
   want to compare this approach to an approach used in the APIC chip. First use a search engine to
   locate and print out a paper called “The APIC Approach to High-Performance Network Interface
   Design: Protected DMA and Other Techniques” (Dittia et al., 1997). Read the paper carefully, and
   then answer the following questions about its particular twists to the ADC design for a practical
   system.
   • There are two types of memory the ADC approach protects: The device registers on the adaptor,
     and the buffer memory containing the data. The first is protected by overloading the virtual
     memory scheme; the second is protected by having the kernel hand the adaptor a list of pages
     that an application can read/write from. Contrast this to the APIC approach to protecting the
     device registers. Why is an access mask helpful? Why is each connection register mapped both
     into the application and kernel memory?
   • In the APIC, the buffer memory is protected by having the APIC read (from memory) a ker-
     nel descriptor that contains validation information about the buffer. In the ADC approach, the
     validating information is already in the adaptor. Why add this extra complexity?
   • In the APIC, there is a third kind of memory that needs to be protected: Buffer descriptors contain
     links to other descriptors, and this link memory needs to be validated. Why is this not needed in
     the ADC approach?
   • A different way to do link notarization is to have the kernel create an array of pointers to real
     buffers, one for each application. Only the kernel can read or write this array. The applications
     queue buffer descriptors as offsets into this array. This is a standard approach in systems called
     using one level of indirection. Compare this approach to the APIC link notarization approach.
   • A disadvantage of the APIC approach is that the adaptor has to do a number of Reads to main
     memory to do all its checks. How many such Reads are required in the worst case for a received
     packet? Why might this be insignificant?
   • The paper describes splitting a packet into two pieces. Why is this needed? What assumption
     does this method make about protocols (that an approach based on packet filters does not need)?

This page intentionally left blank

                                                                                                                       CHAPTER


Maintaining timers
                                                                                                                           7
                                                                           That was, is, and shall be: Time’s wheel runs back or stops.
                                                                                                                   —Robert Browning



A timer module in a system is analogous to a secretary who keeps track of all the appointments of
a busy executive. The executive tells the secretary to schedule appointments and sometimes to cancel
appointments before they occur. It is the secretary’s job to interrupt the executive with a warning just
before the scheduled time of an appointment. Many secretaries actually do this using a so-called tickler
file, which is a moving window over the next N days. When the day’s appointments are done, the tickler
file is rolled to bypass the current day. We will find a strong analogy between a tickler file and a timing
wheel, the main data structure of this chapter.
     The chapter is organized as follows. Section 7.1 describes why timers are needed. Section 7.2
describes a model of a timer routine and the relevant parameters that are critical for performance.
Section 7.3 describes the simplest techniques for maintaining timers, some of which are still appropri-
ate in some cases. Section 7.4 introduces the main data structure, called timing wheels. This is followed
by two specific instantiations of timing wheels called hashed wheels (in Section 7.5) and hierarchical
timing wheels (in Section 7.6). The chapter ends with a technique called soft timers (Section 7.9) that re-
duces timer overhead by amortizing timer maintenance across other system calls. Table 7.1 summarizes
the principles applied in the various timer schemes.
     When compared to the first edition, probably the most notable change has been the hundreds of
thousands of fine granularity timers (Saeed et al., 2017) that are now routinely used in hosts in clouds
to provide bandwidth isolation for Virtual Machine traffic via traffic shaping, and for modern congestion
control algorithms like BBR (Cardwell et al., 2017) that do fine-graining pacing to reduce packet drops.
These new applications make a stronger case for the use of the main data structure in this chapter (timing
wheels), and the need for even more streamlined timer implementations in multicore machines.


    Quick reference guide
    The most useful section for an implementor may be Section 7.5 on hashed timing wheels, versions of which have appeared
    in many operating systems, such as FreeBSD and in Google machines as part of the Carousel (Saeed et al., 2017) traffic
    shaping software. Linux used hierarchical timing wheels (Section 7.6) in early versions, as well as in a recent version that
    is more efficient but offers less precise timers (Corbet, 2015).




Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00013-0
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                                 179

180      Chapter 7 Maintaining timers



                      Table 7.1 Principles used by the timer schemes described
                      in this chapter.
                      Number             Principle               Timer technique
                      P14    Use array to store bounded timers Basic timing wheels
                      P2c, 4 Leverage off time-of-day update
                      P15    Using hashing or hierarchies      Hashed, hierarchical
                                                               timing wheels
                      P10    Pass handle to delete timer       Any timer scheme
                      P4     Leverage off system calls, etc.   Soft timers
                      P3     Relax need for accurate timers
                      P11    Optimize for fast timers



7.1 Why timers?
Why do systems need timers? Systems need timers for failure recovery and also to implement al-
gorithms in which the notion of time or relative time is integral. Several kinds of failures cannot be
detected asynchronously. Some can be detected by periodic checking (e.g., disk watchdog timers), and
such timers always expire. Other failures can only be inferred by the lack of some positive action (e.g.,
message acknowledgment) within a specified period. If failures are infrequent, these timers rarely ex-
pire.
     Many systems also implement algorithms that use time or relative time. Examples include algo-
rithms that control the rate of production of some entity (e.g., rate-based flow control in networks) and
scheduling algorithms. These timers almost always expire.
     The performance of algorithms to implement a timer module becomes an issue when any of the
following are true. First, performance becomes an issue if the algorithm is implemented by a processor
that is interrupted each time a hardware clock ticks and the interrupt overhead is substantial. Second,
it becomes an issue if fine-granularity timers are required. Third, it becomes an issue if the average
number of active timers is large. All three factors are becoming increasingly critical in cloud servers
running at 100 Gbps that do fine-grained traffic shaping of hundreds of thousands of flows (Saeed et
al., 2017).
     If the hardware clock interrupts the host every tick and the interval between ticks is on the order
of microseconds, then the interrupt overhead is substantial. Most host operating systems offer timers
of coarse granularity (milliseconds or seconds). Alternatively, in some systems finer-granularity timers
reside in special-purpose hardware. In either case the performance of the timer algorithms will be an
issue because they determine the latency incurred in starting or stopping a timer and the number of
timers that can be simultaneously outstanding.
     As an example, consider communications between members of a distributed system. Since messages
can be lost in the underlying network, timers are needed at some level to trigger retransmissions. A
host in a distributed system can have several timers outstanding. Consider, for example, a server with
50,000 connections and three timers per connection. Further, as networks scale to 100 gigabit speeds
and beyond, both the required resolution and the rate at which timers are started and stopped will
increase.
     Some network implementations do not use a timer per packet; instead, only a few timers are used
for the entire networking package. Such TCP implementation gets away with two timers because the

                                                  7.2 Model and performance measures                  181



TCP implementation maintains its own timers for all outstanding packets and uses a single kernel timer
as a clock to run its own timers. TCP maintains its packet timers in the simplest fashion: Whenever its
single kernel timer expires, it ticks away at all its outstanding packet timers. For example, many TCP
implementations use two timers: a 200-millisecond timer and a 500-millisecond timer.
    The naive method works reasonably well if the granularity of timers is low and losses are rare.
However, it is desirable to improve the resolution of the retransmission timer to allow speedier recovery.
For example, the University of Arizona has a TCP implementation called TCP Vegas (Brakmo et al.,
1994) that performs better than the commonly used TCP Reno. One of the reasons TCP Reno has bad
performance when experiencing losses is the coarse granularity of the timeouts.
    Besides faster error recovery, fine-granularity timers also allow network protocols to more accu-
rately measure small intervals of time. For example, accurate estimates of round trip delay are important
for the TCP congestion-control algorithm (Jacobson, 1988) and the SRM (scalable reliable multicast)
framework (Floyd et al., 1995) that is implemented in the Web conferencing tool (McCanne, 1992).
    More recently, beyond accurate round trip delay measurements, recent congestion algorithms have
been using fine grained timers. Google’s BBR algorithm (Cardwell et al., 2017), for instance, uses fine
grained pacing to reduce packet drops in the network, especially for video.
    Finally, many multimedia applications routinely use timers, and the number of such applications is
increasing. An early example can be found in Siemens’ CHANNELS run-time system for multimedia
(Boecking et al., 1995), where each audio stream uses a timer with granularity that lies between 10
and 20 milliseconds. For multimedia and other real-time applications, it is important to have worst-case
bounds on the processing time to start and stop timers.
    Besides networking applications, process control and other real-time applications will benefit from
large numbers of fine-granularity timers. Also, the number of users on a system may grow large enough
to lead to a large number of outstanding timers. This is the reason cited for redesigning the timer facility
by the developers of the IBM VM/XA SP1 operating system (Davison, 1989).
    In the following sections we will describe a family of schemes for efficient timer implementations
based on a data structure called a timing wheel. We will also survey some of the systems that have
implemented timer packages based on the ideas in this chapter.
