# network-algorithmics-13-16-1-batch-switching-algorithms (chunk 000001)

# Network Algorithmics — 13.16.1 Batch switching algorithms (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 386
- Slice: from `13.16.1 Batch switching algorithms` up to next detected section heading

---

13.16.1 Batch switching algorithms
Since SB-QPS is a batch switching algorithm (Aggarwal et al., 2003; Neely et al., 2007; Wang et
al., 2018), we first provide some background on batch switching. Unlike in a regular switching al-
gorithm, where a matching decision is computed for every time slot, in a batch-switching algorithm,
multiple (say T ) consecutive time slots are grouped as a batch and these T matching decisions are batch-
computed (P2c). Hence, in a batch-switching algorithm, each of the T matchings being computed in a
batch has a period of T time slots to find opportunities to have the quality of the matching improved by
the underlying bipartite matching algorithm, whereas, in a regular switching algorithm, each matching
has only a single time slot to find such opportunities. As a result, a batch-switching algorithm can usu-
ally produce matchings of higher quality than a regular switching algorithm using the same underlying
bipartite matching algorithm. However, the flip side of the coin is that all batch-switching algorithms
suffer an average batching delay of at least T /2 time slots since any packet belonging to the current
batch has to wait till at least the beginning of the next batch to be switched. A key contribution of
SB-QPS, described next, is to make this T much smaller than in all other batch-switching algorithms,
for attaining a similar or better throughput performance.
    As just explained, in a batch-switching algorithm, the T matchings for a batch of T future time slots
are batch-computed. These T matchings form a joint calendar (schedule) of the N output ports that can
be encoded as a T × N table with T N cells in it, as illustrated by an example shown in Fig. 13.14. Each
column corresponds to the calendar of an output port and each row a time slot. The content of the cell at

360      Chapter 13 Switching

FIGURE 13.14
A joint calendar. “–” means unmatched. (Adapted from Meng et al., 2020.)

the intersection of the tth row and the j th column is the input port that Oj is to pair with during the tth
time slot in this batch. Hence, each cell also corresponds to an edge (between the input and the output
port pair) and each row also corresponds to a matching (under computation for the corresponding time
slot). In the example shown in Section 13.14 output port O1 is to pair with I3 during the first time slot
(in this batch), I5 during the second time slot, and is unmatched during the T th time slot.
