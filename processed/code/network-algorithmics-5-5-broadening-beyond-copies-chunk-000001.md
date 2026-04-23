# network-algorithmics-5-5-broadening-beyond-copies (chunk 000001)

# Network Algorithmics — 5.5 Broadening beyond copies (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 161
- Slice: from `5.5 Broadening beyond copies` up to next detected section heading

---

5.5 Broadening beyond copies
There are several data manipulations in the network beyond copying that can be made more efficent if
done at the same time, avoiiding multiple passes over the data. This leverages the principle of avoiding

5.5 Broadening beyond copies                  135

FIGURE 5.10
In I/O splicing, all the indirection caused by copying to and from user-space buffers is removed by a single system
call that “splices” together the I/O stream from the disk with the I/O stream to the network. As always, Copy 1 can
be removed for files in the cache.

obvious waste (P1), and expense sharing (P2c). We describe two such ideas, integrated layer processing
(ILP) and in-network computing.
    ILP: Clark and Tennehouse, in a landmark paper, suggested generalizing Van Jacobson’s idea (de-
scribed earlier) of integrating checksums and copying. In more detail the Jacobson idea is based on the
following observation. When copying a packet word from a location (say, W 10 in adaptor memory in
Fig. 5.11) to a location in memory (say, M9 in memory in Fig. 5.11), the processor has to load W 10 into
a register and then store that register to M9. Typically, most RISC processors require that, between a
load and a store, the compiler insert a so-called delay slot, or empty cycle, to keep the pipeline working
correctly (never mind why!). That empty cycle can be used for other computation. For example, it can
be used to add the word just read to a register that holds the current checksum. Thus with no extra cost
the copy loop can often be augmented to be the checksum loop as well.
    But there are other data-intensive manipulations, such as encrypting data and doing format conver-
sions. Why not, Clark and Tennenhouse (1990) argued, integrate all such manipulations into the copy
loop? For example, in Fig. 5.11 the CPU could read W 10 and then decrypt W 10 and write the decrypted
word to M9 rather than have that done in another loop. They called this idea integrated layer process-
ing, or ILP. The essential idea is to avoid obvious waste (P1), in terms of reading (and possibly) writing
the bytes of a packet several times for multiple data-manipulation operations on the same packet.

136      Chapter 5 Copying data

FIGURE 5.11
Integrating checksumming and copying.
