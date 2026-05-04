# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000009)

A.2.5 Chip design
Finally, it may be useful for networking readers to understand how chips for networking functions are
designed.
    After partitioning functions between chips, the box architect creates a design team for each chip and
works with the team to create chip specification. For each block within a chip, logic designers write
software register transfer level (RTL) descriptions using a hardware design language such as Verilog or
VHDL. Block sizes are estimated and a crude floor plan of the chip is done in preparation for circuit
design.
    At this stage, there is a fork in the road. In synthesized design the designer applies synthesis tools to
the RTL code to generate hardware circuits. Synthesis speeds the design process but generally produces
slower circuits than custom-designed circuits. If the synthesized circuit does not meet timing (e.g.,
8 nsec for OC-768 routers), the designer redoes the synthesis after adding constraints and tweaking
parameters. In custom design, on the other hand, the designer can design individual gates or drag-
and-drop cells from a standard library. If the chip does not meet timing, the designer must change the
design (Sutherland et al., 1999). Finally, the chip “tapes out” and is manufactured, and the first yield is
inspected.
    Even at the highest level, it helps to understand the chip design process. For example, systemwide
problems can be solved by repartitioning functions between chips. This is easy when the chip is being
specified, is an irritant after RTL is written, and causes blood feuds after the chip has taped out. A second
“spin” of a chip is something that any engineering manager would rather work around.

Interconnects, power, and packaging
Chips are connected using either point-to-high connections known as high-speed serial links, shared
links known as buses, or parallel arrays of buses known as crossbar switches. Instead of using N 2
point-to-point links to connect N chips, it is cheaper to use a shared bus. A bus is similar to any shared
media network, such as an Ethernet, and requires an arbitration protocol often implemented (unlike an
Ethernet) using a centralized arbiter. Once a sender has been selected in a time slot, other potential
senders must not send any signals. Electrically, this is done by having transmitters use a tristate output
device that can output a0 or a1 or be in a high-impedance state. In a high-impedance state there is no
path through the device to either the power supply or ground. Thus the selected transmitter sends 0’s or
1’s, while the nonselected transmitters stay in a high-impedance state.
    Buses are limited today to around 20 Gb/sec. Thus many routers today use parallel buses in the form
of crossbar switches (Chapter 13). A router can be built with a small number of chips, such as a link
interface chip, a packet-forwarding chip, memory chips to store lookup state, a crossbar switch, and a
queuing chip with associated DRAM memory for packet buffers.

Detailed models             539

A.3 Switching theory
This section provides some more details about matching algorithms for Clos networks and the dazzling
variety of interconnection networks.
