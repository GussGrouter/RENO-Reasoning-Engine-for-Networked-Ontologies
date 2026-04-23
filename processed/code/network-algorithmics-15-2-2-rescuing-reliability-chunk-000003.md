# network-algorithmics-15-2-2-rescuing-reliability (chunk 000003)

438      Chapter 15 Routers as distributed systems

this is a powerful technique, the example of Fig. 15.1 shows that perhaps the soft state approach, at
least as currently expressed, works only if the protocol invariants are one-way.
    For load balancing, besides the one-way invariants on each channel that relate sender and receiver
round numbers, there is also a global invariant that ensures that, assuming no packet loss, channel round
numbers never differ by more than 1. This node invariant is enforced, after a violation due to loss, by
skipping at the receiver.
    Even in the case when sequence numbers can be added to cells, logical reception can help simplify
the resequencing implementation. Some resequencers use fast parallel hardware sorting circuits to re-
assemble packets. If logical reception is used, this circuitry is overkill. Logical reception is adequate
for the expected case, and a slow scan looking for a matching sequence number is sufficient in the
rare error case. Recall that, on chip-to-chip links, errors should be very rare. Notice that, if sequence
numbers are added, FIFO delivery is guaranteed, unlike the protocol of Fig. 15.3.
