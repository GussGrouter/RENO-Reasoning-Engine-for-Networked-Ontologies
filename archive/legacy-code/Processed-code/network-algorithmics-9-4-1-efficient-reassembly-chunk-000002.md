# network-algorithmics-9-4-1-efficient-reassembly (chunk 000002)

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
