# network-algorithmics-9-2-2-internet-checksums-since-crc-computation-is-done-on-every-link-on-the-in (chunk 000001)

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
