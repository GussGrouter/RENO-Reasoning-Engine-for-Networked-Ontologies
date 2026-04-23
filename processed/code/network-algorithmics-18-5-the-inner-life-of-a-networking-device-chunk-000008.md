# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000008)

Static RAM
A SRAM contains N registers addressed by log N address bits A. SRAM is so named because the
underlying flip-flops refresh themselves and so are “static.” Besides flip-flops, an SRAM needs a de-
coder that decodes A into a unary value used to select the right register. Accessing an SRAM on-chip
is only slightly slower than accessing a register because of the added decode delay. At the time of
writing, it was possible to obtain on-chip SRAMs with 0.5 nanoseconds access times. Access times of
1–2 nanoseconds for on-chip SRAM and 5–10 nanoseconds for off-chip SRAM are common. On-chip
SRAM is limited to around 64 Mbits today.

Dynamic RAM
The SRAM bit cell of Fig. A.5 requires at least five transistors. Thus SRAM is always less dense or
more expensive than memory technology based on DRAM. In Fig. A.6 a DRAM cell uses only a single
transistor connected to an output capacitance. The transistor is only used to connect the write input to
the output when the write enable signal on the gate is high. The output voltage is stored on the output
capacitance, which is significantly larger than the gate capacitance; thus the charge leaks, but slowly.
Loss due to leakage is fixed by refreshing the DRAM cell externally within a few milliseconds.
    To obtain high densities, DRAMs use “pseudo-three-dimensional trench or stacked capacitors”
(Fromm et al., 1997); together with the factor of 5–6 reduction in the number of transistors, a DRAM
cell is roughly 16 times smaller than an SRAM cell (Fromm et al., 1997).
    The compact design of a DRAM cell has another important side effect: a DRAM cell requires
higher latency to read or write than the SRAM cell of Fig. A.5. Intuitively, if the SRAM cell of Fig. A.5

538      Detailed models

is selected, the power supply quickly drives the output bit line to the appropriate threshold. On the
other hand, the capacitor in Fig. A.6 has to drive an output line of higher capacitance. The resulting
small voltage swing of a DRAM bit line takes longer to sense reliably. In addition, DRAMs need extra
delay for two-stage decoding and for refresh. DRAM refreshes are done automatically by the DRAM
controller’s periodically enabling RAS for each row R, thereby refreshing all the bits in R.
