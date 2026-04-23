# Network Algorithmics — 2.2.3 Raising abstraction level of hardware design (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 49 -l 60 -layout
- Slice: from `2.2.3 Raising the abstraction level of hardware design` up to (excluding) `Example 3.`

---

## PDF page 51

2.2.3 Raising the abstraction level of hardware design
Hand designing each transistor in a network chip design consisting of 1 million transistors would be
time consuming. The design process can be reduced to a few months using building blocks. A quick
description of building block technologies, such as PLAs, PALs, and standard cells, can be found in
Section A.2.5.
    The high-order bit, however, is that just as software designers reuse code, so also hardware designers
reuse a repertoire of commonly occurring functions. Besides common computational blocks, such as
adders, multipliers, comparators, and priority encoders, designs also use decoders, barrel shifters, mul-
tiplexers, and demultiplexers. It is helpful to be familiar with these “arrows” in the hardware designer’s
quiver.
    A decoder converts a log N -bit binary value to an N -bit unary encoding of the same value; while
binary representations are more compact, unary representations are more convenient for computation.
A barrel shifter shifts an input I by s positions to the left or right, with the bits shifted off from an end
coming around to the other end.
    A multiplexer (mux) connects one of several inputs to a common output, while its dual, the de-
multiplexer, routes one input to one of several possible outputs. More precisely, a multiplexer (mux)
connects one of n input bits Ij to the output O if a log n-bit select signal S encodes the value j in
binary. Its dual, the demultiplexer, connects input I to output Oj if the signal S encodes the value j in
binary.
    Thus the game becomes one of decomposing a complex logic function into instances of the standard
functions, even using recursion when needed. This is exactly akin to reduction and divide-and-conquer
and is easily picked up by software designers. For example, Fig. 2.3 shows the typical Lego puzzle faced
by hardware designers: Build a 4-input multiplexer from 2-input multiplexers. Start by choosing one of
I0 and I1 using a 2-input mux and then choosing one of I2 and I3 by another 2-input mux. Clearly, the
outputs of the 2-input muxes in the first stage must be combined using a third 2-input mux; the only
cleverness required is to realize that the select signal for the first two muxes is the least significant bit
S0 of the 2-bit select signal, while the third mux chooses between the upper and lower halves and so
uses S1 as the select bit.
    The following networking example shows that reduction is a powerful design tool for designing
critical networking functions.
