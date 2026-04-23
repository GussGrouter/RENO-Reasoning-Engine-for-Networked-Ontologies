# Network Algorithmics — 9.4.1 Efficient reassembly (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 255
- Slice: from `9.4.1 Efficient reassembly` up to next detected section heading

---

9.4.1 Efficient reassembly
Fig. 9.8 shows a simple data structure, akin to the one used in BSD UNIX, for reassembling a data
packet. Assume that three fragments for the packet with ID 1080 have arrived. The fragments are
sorted in a list by their starting offset number. Notice that there are overlapping bytes because the first
fragment contains bytes 1–10, while the second contains 2–21.

                                                                                      9.4 Reassembly              229




FIGURE 9.9
This implementation is similar to that of Fig. 9.8, except it optimizes for the case that the fragments are nonoverlap-
ping and arrive in order.


     Thus if a new fragment with packet ID 1080 arrives containing offsets 25–30, the implementation
will typically search through the list, starting from the head, to find the correct position. The correct
position is between start offsets 2 and 40 and so is after the second list item.
     Each time a fragment is placed in the list, the implementation can check during list traversal if all
required bytes have been received up to this fragment. If so, it continues checking to the end of the
list to see if all bytes have been received and the last fragment has the last fragment bit set. If these
conditions are met, then all required fragments have arrived; the implementation then traverses the list
again, copying the data of each fragment into another buffer at the specified offset, potentially avoiding
copying overlapping portions.
     The resulting implementation is quite complex and slow and typically requires an extra copy. Note
that to insert a fragment, one has to locate the packet ID’s list and then search within the list. This
requires two linear searches. Is IP reassembly fundamentally hard?
     Oddly enough, there exists a counterexample reassembly protocol that has been implemented in
hardware at gigabit speeds: the ATM AAL-5 cell reassembly protocol (Partridge, 1993), which basically
describes how to chop up IP packets into 53-byte ATM cells while allowing reassembly at the cells into
packets at the receiver. What makes the AAL-5 reassembly algorithm simple to implement in hardware
is not the fixed-length cell (the implementation can be generalized to variable-length cells) but the fact
that cells can only arrive in FIFO order.
     If cells can arrive only in FIFO order, it is easy to paste each successive cell into a buffer just after
where the previous cell was placed. When the last cell arrives carrying a last cell bit (just as in IP), the
packet’s CRC is checked. If the CRC computes, the packet is successfully reassembled. Note that ATM
does not require any offset fields because packets arrive in order on ATM virtual circuits.
     Unlike ATM cells, IP datagrams can arrive (theoretically) in any order because IP uses a datagram
(post office) model as opposed to a virtual circuit (telephony) model. However, we have just seen that
header prediction, and, in fact, the fast retransmission algorithm, depends crucially on the fact that
in the expected case, IP segments arrive in order (P11, optimizing the expected case). Combining this
observation with that of the AAL-5 implementation suggests that one can obtain an efficient reassembly
algorithm, even in hardware, by optimizing for the case of FIFO arrival of fragments, as shown in
Fig. 9.9.
     Fig. 9.9 maintains the same sorted list as in Fig. 9.8 but also keeps a pointer to the end of the
list. Optimizing for the case that fragments arrive in order and are nonoverlapping, when a fragment
containing bytes 22–30 arrives, the implementation checks the ending byte number of the last received
fragment (stored in a register, equal to 21) against the start offset of the new fragment. Since 22 is

230      Chapter 9 Protocol processing



21 + 1, all is well. The new end byte is updated to the end byte of the new fragment (30), and the
pointer is updated to point to the newly arrived fragment after linking it at the end of the list. Finally, if
the newly arriving fragment is a last fragment, reassembly is done.
    Compared to the implementation in Fig. 9.8, the check for completion as well as the check to find
out where to place a fragment takes constant and not linear time. Similarly, one can cache the expected
packet ID (as in the TCP or UDP PCB lookup implementations) to avoid a list traversal when searching
for the fragment list. Finally, using data structures such as pbufs instead of mbufs, even the need for
an extra copy can be avoided by directly copying a received fragment into the buffer at the appropriate
offset.
    If the expected case fails, the implementation can revert to the standard BSD processing. For exam-
ple, Chandranmenon and Varghese (1998) describe this expected-case optimization in which the code
keeps two lists and directly reuses the existing BSD code (which is hard to get right!) when the expected
case fails. The expected case is reported by Chandranmenon and Varghese (1998) as taking 38 SPARC
instructions, which is comparable with Jacobson’s TCP estimates.
    As with header prediction, it is worth applying Caveat Q8 and examining the sensitivity of this
optimization of this implementation to the assumptions. Actually, it turns out to be pretty bad. This is
because measurements indicate that many recent implementations, including Linux, have senders send
out fragments in reverse order! Thus fragments arrive in reverse order 9% of the time (Shannon et al.,
2001).
    This seemingly eccentric behavior is justified by the fact that it is only the last fragment that carries
the length of the entire packet; by sending it first the sender allows the receiver to know what length
buffer to allocate after the first fragment is received, assuming the fragments arrive in FIFO order.
Note that the FIFO assumption still holds true. However, Fig. 9.9 has a concealed but subtle additional
assumption: that fragments will be sent in offset order. Before reading further, think how you might
modify the implementation of Fig. 9.9 to handle this case.
    The solution, of course, is to use the first fragment to decide which of two expected cases to optimize
for. If the first fragment is the first fragment (offset 0), then the implementation uses the mode described
in Fig. 9.9. If the first fragment is the last (last bit set), the implementation jumps to a different state,
where it expects fragments in reverse order. This is just the dual of Fig. 9.9, where the next fragment
should have its last byte number to be 1 less (as opposed to 1 more) than the start offset of the previous
fragment. Similarly, the next fragment is expected to be pasted at the start of the list and not the end.



9.5 Conclusions
This chapter describes techniques for efficient buffer allocation, CRC and checksum calculation, pro-
tocol processing such as TCP, and finally reassembly.
    For buffer allocation, techniques such as the use of segregated pools and batch allocation promise
fast allocation with potential trade-offs: the lack of storage efficiency (for segregated pools) versus the
difficulty of coalescing noncontiguous holes (for batch allocation). Buffer sharing is important to use
memory efficiently and can be done by efficiently stealing buffers from large users or by using dynamic
thresholds.
    For CRC calculation, efficient multibit remainder calculation finesses the obvious waste (P1) of
calculating CRCs one bit at a time, even using LFSR implementations. For checksum calculation, the

                                                                               9.6 Exercises        231



main trick is to fit the computation to the underlying machine architecture, using large word lengths,
lazy checks for carries, and even parallelism. The optimizations for TCP, UDP, and reassembly are all
based on optimizing simple expected cases (e.g., FIFO receipt, no errors) that cut through a welter of
corner cases that the protocol must check for but rarely occur. Table 9.1 presents a summary of the
techniques used in this chapter together with the major principles involved.
    Beyond the specific techniques, there are some general lessons to be gleaned. First, when consider-
ing the buffer-stealing algorithm, it is tempting to believe that finding the user with the largest buffer
allocation requires a heap, which requires logarithmic time. However, as with timing wheels in Chap-
ter 7, McKenney’s algorithm exploits the special case that buffer sizes only increase and decrease by 1.
    The general lesson is that for algorithmics, special cases matter. Theoreticians know this well; for
example, the general problem of finding a Hamiltonian cycle (Cormen et al., 1990) is hard for general
graphs but is trivial if the graph is a ring. In fact, the practitioner of algorithmics should look for
opportunities to change the system to permit special cases that permit efficient algorithms.
    Second, the dynamic threshold scheme shows how important it is to optimize one’s degrees of
freedom (P13), especially when considering dynamic instead of static values for parameters. This is a
very common evolutionary path in many protocols: for example, collision-avoidance protocols evolved
from using fixed backoff times to using dynamic backoff times in Ethernet; transport protocols evolved
from using fixed window sizes to using dynamic window sizes to adjust to congestion; finally, the
dynamic threshold scheme of this chapter shows the power of allowing dynamic buffer thresholds.
    Third, the discussion of techniques for buffer sharing shows why algorithmics, at least in terms of
abstracting common networking tasks and understanding a wide spectrum of solutions for these tasks,
can be useful. For example, when writing this chapter, it became clear that buffer sharing is also part of
many credit-based protocols, such as Ozveren et al. (1994) (see the protocol in Chapter 15), except that
in such settings a sender is allocating buffer space at a distant receiver. Isolating the abstract problem
is helpful because it shows, for instance, that the dynamic threshold scheme of Choudhury and Hahne
can provide finer grain buffer sharing than the technique of Ozveren et al. (1994).
    Finally, the last lesson from header prediction and fast reassembly is that attempts to design new
protocols for faster implementation can often be countered by simpler implementations. In particu-
lar, arguing that a protocol is “complex” is often irrelevant if the complexities can be finessed in the
expected case.
    As a second example, a transport protocol (Sabnani and Netravali, 1989) was designed to allow
efficient sequence number processing for protocols that used large windows and could handle out-of-
order delivery. The protocol embedded concepts such as chunks of contiguous sequence numbers into
the protocol for this purpose. Simple implementation tricks described in the patent (Thomas et al.,
1992) can achieve much the same effect, using large words to effectively represent chunks without
redesigning the protocol.
    Thus history teaches that attempts to redesign protocols for efficiency (as opposed to more func-
tionality) should be viewed with some skepticism.
