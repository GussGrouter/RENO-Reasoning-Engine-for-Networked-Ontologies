# network-algorithmics-9-4-1-efficient-reassembly (chunk 000001)

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
