# network-algorithmics-15-4-2-rescuing-reliability (chunk 000001)

# Network Algorithmics — 15.4.2 Rescuing reliability (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 470
- Slice: from `15.4.2 Rescuing reliability` up to next detected section heading

---

15.4.2 Rescuing reliability
A panic reaction to the counterexample of Fig. 15.4 might be to jettison single-copy update and re-
treat to the safety of two copies. However, all the counterexample demonstrates is that a search must
complete without intervening update operations. If so, the binary search invariants hold and correctness
follows. The counterexample does not imply the converse: that an entire update must complete without
intervening search operations. The converse property is restrictive and would considerably slow down
search.
    There are simple ways to ensure that a search completes without intervening updates. The first is
to change the architectural model, algorithmics, after all, is the art of changing the problem to fit our
limited ingenuity, so that all update writes are centralized through the search chip. When update wishes
to perform a write, it posts the write to search and waits for an acknowledgment. After finishing its
current search cycle, search does the required write and sends an acknowledgment. Search can then
work on the next search task.
    A second way, more consonant with the bridge implementation, is to observe that the route pro-
cessor does packet forwarding. The route processor asks the chip to do search, and it waits for a few
microseconds to get the answer. Finally, the route processor does updates only when no packets are
being forwarded and hence no searches are in progress. Thus an update can be interrupted by a search,
but not vice versa.
    The final solution relies on search tolerating duplicates, and it avoids locking by changing the model
to centralize updates and searches. Note that centralizing updates are insufficient by itself (without also
relaxing the specification to allow duplicates) because this would require performing a complete update
without intervening searches.
