# network-algorithmics-1-2-5-cleaning-up-we-have-postponed-one-thorny-issue-to-this-point-the-termina (chunk 000003)

URL or a non-URL byte. Clearly, the designer can gain more slack, if needed, by increasing the bits in
the generation number, at the cost of slightly increased storage in the array.
    The chip, then, must have two states: one for processing URL bytes and one for processing non-
URL bytes. When the URL is completely processed, the chip switches to the “Scrub” state. The chip
maintains another register, which points to the next array entry s to be scrubbed. In the scrub state,
when a non-URL character is received, the chip reads entry s in the coalesced array. If G[s] = g, G[s]
is reset to g and C[s] is initialized to 0.
    Thus the use of 3 extra bits of generation number per array entry has reduced initialization process-
ing cycles, trading processing for storage. Altogether a coalesced array entry is now only 32 bits, 15
bits for a counter, 14 bits for a threshold shift value, and 3 bits for a generation number. Note that the
added initialization check needed during URL byte processing does not increase memory references
(the bottleneck) but adds slightly to the processing logic. In addition, it requires two more chip registers
to hold g and s, a small additional expense.
