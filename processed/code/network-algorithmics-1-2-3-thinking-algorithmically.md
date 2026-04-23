# Network Algorithmics — 1.2.3 Thinking algorithmically (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 36
- Slice: from `1.2.3 Thinking algorithmically` up to next detected section heading

---

1.2.3 Thinking algorithmically
Intuitively, the second pass through the arrays C and T at the end seems like a waste. For example,
it suffices to alarm if any character is over the threshold. So why check all characters? This suggests
keeping track only of the largest character count c; at the end, perhaps the algorithm needs to check
only whether c is over threshold with respect to the total URL length L.

10        Chapter 1 Introducing network algorithmics




FIGURE 1.5
Avoiding the final loop through the threshold array by keeping track only of Max, the highest counter encountered so
far relative to its threshold value.


    This does not quite work. A nonsuspicious character such as “e” may well have a very high occur-
rence count. However, “e” is also likely to be specified with a high threshold. Thus if we keep track only
of “e” with, say, a count of 20, we may not keep track of “#” with, say, a count of 10. If the threshold of
“#” is much smaller, the algorithm may cause a false negative: The chip may fail to alarm on a packet
that should be flagged.
    The counterexample suggests the following fix. The chip keeps track in a register of the highest
counter relativized to the threshold value. More precisely, the chip keeps track of the highest relativized
counter Max corresponding to some character k, such that C[k]/T [k] = Max is the highest among all
characters encountered so far. If a new character i is read, the chip increments C[i]. If C[i]/T [i] > Max,
then the chip replaces the current stored value of Max with C[i]/T [i]. At the end of URL processing,
the chip alarms if Max ≥ L.
    Here’s why this works. If Max = C[k]/T[k] ≥ L, clearly the packet must be flagged, because char-
acter k is over threshold. On the other hand, if C[k]/T [k] < L, then for any character i, it follows that
C[i]/T [i] ≤ C[k]/T [k] < L. Thus if Max falls below threshold, then no character is above threshold.
Thus there can be no false negatives. This solution is shown in Fig. 1.5.
