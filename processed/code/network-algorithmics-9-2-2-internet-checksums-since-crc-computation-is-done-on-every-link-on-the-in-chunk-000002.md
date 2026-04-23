# network-algorithmics-9-2-2-internet-checksums-since-crc-computation-is-done-on-every-link-on-the-in (chunk 000002)

All three problems can be solved by not being tied to the reference implementation (P8) and, instead,
by fitting the computation to the underlying hardware (P4c). The following ideas and Fig. 9.6 are taken
from Partridge (1993).
• Ignore byte order: Fig. 9.6 shows that swapping every word before addition on a byte-reversed
  machine is obvious waste (P1). The figure shows that whether or not AB is stored byte reversed as
  BA, any carry from the MSB of byte B still flows to the LSB of byte A. Similarly, in both cases,
  any carry from the MSB of byte A flows to the LSB of byte B. Thus any 1’s-complement addition
  done on the byte-reversed representation will have the same answer as in the original, except byte
  reversed. This in turn implies that it suffices to add in byte-reversed form and to do a final byte
  reversal only at the end.
• Use natural word length: If a machine has a 32- or 64-bit word, the most natural thing to do is to
  maintain the running sum in the natural machine word size. All that happens is that carries accumu-
  late in the higher-order 16 bits of the machine word, which need to be added back to the lower 16
  bits in a final operation.
• Lazy carry evaluation: Using a larger word size has the nice side effect of allowing lazy evaluation
  (P2b) of carry checking. For example, using a 32-bit word allows an unrolled loop that checks for
  carries only after every 16 additions (Stevens, 1994) because it takes 16 additions in the worst case
  to have the carry overflow from bit 32.
   In addition, as noted in Chapter 5, the overhead of reading in the checksum data into machine
registers can be avoided by piggybacking on the same requirement for copying data from the network
device into user buffers, and vice versa.

Header checksum
Finally, besides the TCP and UDP checksums on the data, IP computes an additional 1’s-complement
checksum on just the IP header. This is crucial for network routers and other hardware devices that
need to recompute Internet checksums.
    Hardware implementations of header checksum can benefit from parallel and incremental compu-
tation. One strategy for parallelism is to break up the data being checksummed into W 16-bit words and
to compute W different 1’s-complement sums in parallel, with a final operation to fold these W sums

9.2 Cyclic redundancy checks and checksums             223

into one 16-bit checksum. A complete hardware implementation of this idea with W = 2 is described
in Touch and Parham (1996).
    The strategy for incremental computation is defined precisely in RFC 1624 (Rijsinghani, 1994).
In essence, if a 16-bit field m in the header changes to m , the header checksum can be recalculated by
subtracting m and adding in m to the older checksum value. There is one subtlety, having to do with
the two representations of zero in 1’s-complement arithmetic (Rijsinghani, 1994), that is considered
further in the exercises.
