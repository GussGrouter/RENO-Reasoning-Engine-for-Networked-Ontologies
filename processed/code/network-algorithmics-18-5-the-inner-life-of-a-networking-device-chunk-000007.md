# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000007)

Programmable logic arrays and programmable array logics
A programmable logic array (PLA) has the generality of a software lookup table but is more compact.
Any binary function can be written as the OR of a set of product terms, each of which is the AND of a
subset of (possibly complemented) inputs. The PLA thus has all the inputs pass through an AND plane,
where the desired product terms are produced by making the appropriate connections. The products are
then routed to an OR plane. A designer produces specific functions by making connections within the
PLA. A more restrictive but simpler form of PLA is a PAL (programmable array logic).

536       Detailed models

FIGURE A.5
To store the output of an inverter indefinitely in the absence of writes, the output is fed back to the input after a
second inversion. Two further transistors are used to allow writes and to block the feedback refresh.

Standard cells
Just as software designers reuse code, so also do hardware designers reuse a repertoire of commonly
occurring functions, such as multiplexers and adders.
    The functional approach to design is generally embodied in standard cell libraries and gate array
technologies, in which a designer must map his or her specific problem to a set of building blocks
offered by the technology. At even higher abstraction levels, designers use synthesis tools to write
higher-level language code in Verilog or VHDL for the function they wish to implement. The VHDL
code is then synthesized into hardware by commercial tools. The trade-off is reduced design time, at
some cost in performance. Since a large fraction of the design is not on the critical path, synthesis can
greatly reduce time to market. This section ends with a networking example of the use of reduction for
a critical path function.

A.2.4 Memories: the inside scoop
This section briefly describes implementation models for registers, static random access memories
(SRAMs), and dynamic RAMs (DRAMs).

Registers
How can a bit be stored such that in the absence of writes and power failures, the bit stays indefinitely?
Storing a bit as the output of the inverter shown in Fig. A.3 will not work, because, left to itself, the
output will discharge from a high to a low voltage via “parasitic” capacitances. A simple solution is to
use feedback: in the absence of a write the inverter output can be fed back to the input and “refresh” the
output. Of course, an inverter flips the input bit, and so the output must be inverted a second time in the
feedback path to get the polarity right, as shown in Fig. A.5. Rather than show the complete inverter
(Fig. A.3), a standard triangular icon is used to represent an inverter.
   Input to the first transistor must be supplied by the write input when a write is enabled and by the
feedback output when a write is disabled. This is accomplished by two more “pass” transistors. The

Detailed models          537

FIGURE A.6
A DRAM cell stores a bit using charge on a capacitor that leaks away slowly and must be refreshed periodically.

pass transistor whose gate is labeled “Refresh Enable” is set to high when a write is disabled, while the
pass transistor whose gate is labeled “Write Enable” is set to high when a write is enabled. In practice,
refreshes and writes are done only at the periodic pulses of a systemwide signal called a clock. Fig. A.5
is called a flip-flop.
    A register is an ordered collection of flip-flops. For example, most modern processors (e.g., the Pen-
tium series) have a collection of 32- or 64-bit on-chip registers. A 32-bit register contains 32 flip-flops,
each storing a bit. Access from logic to a register on the same chip is extremely fast, say, 0.5–1 nanosec-
ond. Access to a register off-chip is slightly slower because of the delay to drive larger off-chip loads.
