# network-algorithmics-13-15-2-the-qps-data-structure (chunk 000001)

# Network Algorithmics — 13.15.2 The QPS data structure (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 384
- Slice: from `13.15.2 The QPS data structure` up to next detected section heading

---

13.15.2 The QPS data structure
We show that the two steps of the QPS proposing strategy can be performed in O(1) time, at any input
port, via a main and an auxiliary data structures, that are the same for all input ports. Fig. 13.13(A)
and (B) present the data structures, at a single input port, before and after the HOL packet of its j th
VOQ is chosen for (switching) service. The top half and bottom half of the figures show the main and
the auxiliary data structures, respectively.
The main data structure. The main data structure is an array of N records, corresponding to the N
VOQs at the input port. Each record j (i.e., array entry j ) is associated with a linked list that corresponds
to (pointers to) packets queued at a VOQ in the order they arrived, starting with the HOL packet. Each
node in the linked list contains two pointers encoded as “letter” (e.g., A); one points to the actual
packet (e.g., packet A) in the packet buffer (not shown in the figure) and the other to the corresponding
entry (e.g., entry A) in the auxiliary data structure, which we refer to as a back pointer.
    For simplicity Fig. 13.13 shows only record j (corresponding to VOQ j ). Each record contains a
head and tail pointers that point to the head node and the tail node of the linked list, respectively. The

358       Chapter 13 Switching

FIGURE 13.13
Illustrating the action of the QPS data structures on a single-input port. (Adapted from Gong et al., 2017.)
