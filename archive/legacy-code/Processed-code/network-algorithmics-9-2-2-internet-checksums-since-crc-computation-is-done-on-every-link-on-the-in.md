# Network Algorithmics — 9.2.2 Internet checksums Since CRC computation is done on every link on the Internet, it is done in hardware by link chips. (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 248
- Slice: from `9.2.2 Internet checksums Since CRC computation is done on every link on the Internet, it is done in hardware by link chips.` up to next detected section heading

---

9.2.2 Internet checksums
Since CRC computation is done on every link on the Internet, it is done in hardware by link chips.
However, the software algorithm, even shifting 8 bits at a time, is slow. Thus TCP chose to use a more
efficient error-detection hash function based on summing the message bits. Just as accountants calculate
sums of large sets of numbers by column and by row to check for errors, a checksum can catch errors
that change the resulting sum.
    It is natural to calculate the sum in units of the checksum size (16 bits in TCP), and some reasonable
strategy must be followed when the sum of the 16-bit units in the message overflows the checksum size.
Simply losing the MSB will, intuitively, lose information about 16-bit chunks computed early in the
summing process. Thus TCP follows the strategy of an end-around carry. When the MSB overflows,
the carry is added to the least significant bit (LSB). This is called one’s complement addition.
    The computation is straightforward. The specified portion of each TCP packet is summed in 16-bit
chunks. Each time the sum overflows, the carry is added to the LSB. Thus the main loop will naively
consist of three steps: Add the next chunk; test for carry; if carry, add to LSB. However, there are three
problems with the naive implementation.
• Byte swapping: First, in some machines, the 16-bit chunks in the TCP message may be stored
  byte-swapped. Thus it may appear that the implementation has to reverse each pair of bytes before
  addition.
• Masking: Second, many machines use word sizes of 32 bits or larger. Thus the naive computation
  may require masking out 16-bit portions.
• Check for carry: Third, the check for carry after every 16-bit word is added can potentially slow
  down the loop as compared to ordinary summation.


3 This is done by what is often called a SERDES chip, which stands for serializer–deserializer chip.

222       Chapter 9 Protocol processing




FIGURE 9.6
The 1’s complement addition of two 16-bit quantities stays the same (except for byte reversal) when the quantities
are represented in byte-reversed form. This is because carries from any bit position flow to the same next-bit position
in both original and byte-reversed formats. Consider, for example, how the MSB of B flows to the LSB of A in both
formats.


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
