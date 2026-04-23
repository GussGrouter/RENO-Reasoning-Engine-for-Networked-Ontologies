# network-algorithmics-6-9-exercises-1-packet-filters-and-upcalls-in-the-description-on-upcalls-fig (chunk 000001)

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
