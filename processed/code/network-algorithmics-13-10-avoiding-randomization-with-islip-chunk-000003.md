# network-algorithmics-13-10-avoiding-randomization-with-islip (chunk 000003)

13.10 Avoiding randomization with iSLIP          349

FIGURE 13.8
One-and-a-half rounds of a sample iSLIP scenario.

The second iteration (middle row of Fig. 13.8) starts with only inputs unmatched on previous itera-
tions (i.e., B) requesting and only to hitherto unmatched outputs. Thus B requests to 2 and 3 (and not
to 1, although B has a cell destined for 1 as well). Both 2 and 3 grant B, and B chooses 2 (the lowest
one that is greater than or equal to its accept pointer of 1). One might think that B should increment its
accept pointer to 3 (1 plus the last accepted, which was 2). However, to avoid starvation, iSLIP does
not increment pointers on iterations other than the first, for reasons that will be explained.
    Thus even after B is connected to 2, 2’s grant pointer remains at A, and B’s accept pointer remains
at 1. Since this is the final iteration, all matched pairs, including pairs, such as A, 1, matched in prior
iterations, are all connected and data transfer (solid lines) occurs.
    The third row provides some insight into how the initial synchronization of grant-and-accept point-
ers gets broken. Because only one output port has granted to A, that port (i.e., 1) gets to move on and
this time to provide priority to ports beyond A. Thus even if A had a second packet destined for 1
(which it does not in this example), 1 would still grant to B.
    The remaining rows in Figs. 13.8 and 13.9 should be examined carefully by the reader to check for
the updating rules for the grant-and-accept pointers and to check which packets are switched at each
round. The bottom line is that by, the end of the third row of Fig. 13.9, the only cell that remains to be
switched is the cell from B to 3. This can clearly be done in a fourth time slot.

350       Chapter 13 Switching

FIGURE 13.9
Last one-and-a-half rounds of the sample iSLIP scenario shown in Fig. 13.8.

FIGURE 13.10
How iSLIP avoids HOL blocking to increase throughput in the scenario of Fig. 13.6.

Fig. 13.10 shows a summary of the final scheduling (abstracted from the internal mechanics) of the
iSLIP scenario and should be compared in terms of scheduling density with Fig. 13.6. While these are
just isolated examples, they do suggest that iSLIP (and similarly PIM) tends to waste fewer slots by
avoiding HOL blocking and computing pretty-good bipartite matchings. Note that both iSLIP and PIM
finish the same input backlog in four time slots, as opposed to six.
    Note also that, when we compare Fig. 13.8 with Fig. 13.7, iSLIP looks worse than PIM because
it requires two iterations per match for iSLIP to achieve the same match sizes as PIM does using one

13.10 Avoiding randomization with iSLIP                 351
