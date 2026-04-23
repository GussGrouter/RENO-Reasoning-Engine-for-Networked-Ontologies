# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000006)

FIGURE A.3
A transistor is a voltage-controlled switch allowing the source-to-drain path to conduct current when the gate voltage
is high. An inverter is a transistor whose source is connected to ground and whose drain is connected to a power
supply.

output to the power supply (i.e., O = 1). Thus an inverter output flips the input bit, implementing the
NOT operation. Although omitted in our pictures, real gates also add a resistance in the path to avoid
“shorting” the power supply when I = 1, by connecting it directly to ground.
    The inverter generalizes to a NAND gate (Fig. A.4) of two inputs, I1 and I2, using two transistors
whose source-drain paths are connected in series. The output O is pulled down to ground if and only
if both transistors are on, which happens if and only if both I 1 and I 2 are 1. Similarly, a NOR gate is
formed by placing two transistors in parallel.

A.2.2 Timing delays
Fig. A.3 assumes that the output changed instantaneously when the input changed. In practice, when
I is turned from 0 to 1, it takes time for the gate to accumulate enough charge to allow the source-
drain path to conduct. This is modeled by thinking of the gate input as charging a gate capacitor (C) in
series with a resistor (R). If you don’t remember what capacitance and resistance are, think of charge
as water, voltage as water pressure, capacitance as the size of a container that must be filled with water,
and resistance as a form of friction impeding water flow. The larger the container capacity and the larger
the friction, the longer the time to fill the container. Formally, the voltage at time t after the input I is
set to V is V (1 − e−t/RC ). The product RC is the charging time constant; within one time constant, the
output reaches 1 − 1/e = 63.2% of its final value.
    In Fig. A.3 notice also that if I is turned off, output O pulls up to the power supply voltage. But to
do so, the output must charge one or more gates to which it is connected, each of which is a resistance
and a capacitance (the sum of which is called the output load). For instance, in a typical 0.18-micron
process,2 the delay through a single inverter driving an output load of four identical inverters is 60
picoseconds.

2 Semiconductor processes are graded by the smallest gate lengths they can produce. Shrinking process width decreases capaci-
tances and resistances and so increases speed.

Detailed models        535

FIGURE A.4
Using two transistors in series to create a NAND gate.

Charging one input can cause further outputs to charge further inputs, and so on. Thus for a combi-
natorial function, the delay is the sum of the charging and discharging delays over the worst-case path
of transistors. Such path delays must fit within a minimum packet arrival time. Logic designs are sim-
ulated to see if they meet timing using approximate analysis as well as accurate circuit models, such as
Spice. Good designers have intuition that allows them to create designs that meet timing. A formaliza-
tion of such intuition is the method of logical effort (Sutherland et al., 1999), which allows a designer
to make quick timing estimates. Besides the time to charge capacitors, another source of delay is wire
delay.

A.2.3 Hardware design building blocks
This section describes some standard terminology for higher-level building blocks used by hardware
designers that can be useful to know.
