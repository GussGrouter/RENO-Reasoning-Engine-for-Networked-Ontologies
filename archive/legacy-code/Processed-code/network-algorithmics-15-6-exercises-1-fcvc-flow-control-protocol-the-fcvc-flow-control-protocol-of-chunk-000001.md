# network-algorithmics-15-6-exercises-1-fcvc-flow-control-protocol-the-fcvc-flow-control-protocol-of (chunk 000001)

# Network Algorithmics — 15.6 Exercises 1. FCVC flow control protocol: The FCVC flow control protocol of Kung et al. (1994) provides (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 471
- Slice: from `15.6 Exercises 1. FCVC flow control protocol: The FCVC flow control protocol of Kung et al. (1994) provides` up to next detected section heading

---

15.6 Exercises
1. FCVC flow control protocol: The FCVC flow control protocol of Kung et al. (1994) provides
   an important alternative to the credit protocols described in Section 15.1. In the FCVC protocol,
   shown in Fig. 15.5, the sender keeps a count of cells sent H , while the receiver keeps a count
   of cells received R and cells dequeued D. The receiver periodically sends its current value of D,
   which is stored at the sender as estimate L. The sender is allowed to send if H − L > Max. More
   importantly, if the sender periodically sends H to the receiver, the receiver can deal with errors due
   to cell loss.

• Assume cells are lost and that the sender periodically sends H to the receiver. How can the
     receiver use the values of H and R to detect how many cells have been lost?
   • How can the receiver use this estimate of cell loss to fix D and so correct the sender?

15.6 Exercises           445

FIGURE 15.5
The FCVC protocol uses a count H of cells sent by the sender and an estimated L of the cells dequeued at the re-
ceiver; flow control is achieved by limiting the difference between H and L. More importantly, the use of absolute
packet numbers instead of incremental credits allows the periodic sending of counts to fix errors due to cell loss.

• Can this protocol be made self-stabilizing without using the full machinery of a snapshot and
     reset?
   • Compare the general features of this method of achieving reliability to the method used in the
     load-balancing algorithm described in the chapter.
