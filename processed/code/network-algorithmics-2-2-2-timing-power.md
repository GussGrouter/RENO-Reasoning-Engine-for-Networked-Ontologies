# Network Algorithmics — 2.2.2 Timing and power (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 49 -l 60 -layout
- Slice: from `2.2.2 Timing and power` up to (excluding) `2.2.3 Raising the abstraction level of hardware design`

---

## PDF page 50

2.2.2 Timing and power
To forward a 40-byte packet at OC-768 speeds, any networking function on the packet must complete
in 8 nsec. Thus the maximum signal transmission delay from inputs to outputs on any logic path must
not exceed 8 nsec.2 To ensure this constraint, a model of signal transmission delay in a transistor is
needed.
    Roughly speaking, each logic gate, such as a NAND or NOT gate, can be thought of as a set of
capacitors and resistors that must be charged (when input values change) in order to compute output
values. Worse, charging one input gate can cause the outputs of later gates to charge further inputs,
and so on. Thus for a combinatorial function, the delay to compute the function is the sum of the
charging and discharging delays over the worst-case path of transistors. Such path delays must fit within
a minimum packet arrival time. Besides the time to charge capacitors, another source of delay is wire
delay. More details can be found in Section A.2.2.
    It also takes energy to charge capacitors, where the energy per unit time (power) scales with the
square of the voltage, the capacitance, and the clock frequency at which inputs can change; P = CV 2 f .
While new processes shrink voltage levels and capacitance, higher-speed circuits must increase clock
frequency. Similarly, parallelism implies more capacitors being charged at a time. Thus many high-
speed chips dissipate a lot of heat, requiring nontrivial cooling techniques such as heat sinks. ISPs and
colocation facilities are large consumers of power. While our level of abstraction precludes understand-
ing power trade-offs, it is good to be aware that chips and routers are sometimes power limited. Some
practical limits today are 30 watts per square centimeter on a single die and 10,000 watts per square
foot in a data center.
Example 2. Priority Encoder Design: Consider the problem of estimating timing for the priority en-
coder of Example 1 for an OC-768 link using 40-byte packets. Thus the circuit has 8 nsec to produce
the output. Assume the input I and outputs O are N -bit vectors such that O[j ] = 1 if and only if
I [j ] = 1 and I [k] = 0 for all k < j . Notice that the output is represented in unary (often called 1-hot
representation) rather than binary. The specification leads directly to the combinational logic equation
O[j ] = I [1] . . . I [j − 1]I [j ] for j > 0.
     This design can be implemented directly using N AND gates, one for each output bit, where the N
gates take a number of inputs that range from 1 to N . Intuitively, since N input AND gates take O(N )
transistors, we have a design, Design 1, with O(N 2 ) transistors that appears to take O(1) time.3 Even
this level of design is helpful, though one can do better.
     A more area-economical design is based on the observation that every output bit O[j ] requires
the AND of the complement of the first j − 1 input bits. Thus we define the partial results P [j ] =
I [1] . . . I [j − 1] for j = 2 . . . N. Clearly, O[j ] = I [j ]P [j ]. But P [j ] can be constructed recursively us-
ing the equation P [j ] = P [j − 1]I [j − 1], which can be implemented using N two-input AND gates,
connected in series. This produces a design, Design 2, that takes O(N ) transistors but takes O(N ) time.
     Design 1 is fast and fat, and Design 2 is slow and lean. This is a familiar time–space trade-off
and suggests we can get something in between. The computation of P [j ] in Design 2 resembles an
unbalanced binary tree of height N . However, it is obvious that P [N ] can be computed using a fully


2 Alternatively, parts of the function can be parallelized/pipelined, but then each part must complete in 8 nsec.
3 A more precise argument, due to David Harris, using the method of Sutherland et al. (1999), shows the delay scales as
log(N log N ) because of the effort required to charge a tree of N transistors in each AND gate.

---

## PDF page 51

24       Chapter 2 Network implementation models



balanced binary of 2-input AND gates of height log N . A little thought then shows that the partial
results of the binary tree can be combined in simple ways to get P [j ] for all j < N using the same
binary tree (Wang and Huang, 2000).
    For example, if N = 8, to compute P [8] we compute X = I [0] . . . I [3] and Y = I [4] . . . I [7] and
compute the AND of X and Y at the root. Thus, it is easy to calculate P [5], for instance, using one
more AND gate by computing X · I [4]. Such a method is very commonly used by hardware designers
to replace apparently long O(N) computation chains with chains of length 2 log N . Since it was first
used to speed up carry chains in addition, it is known as carry look-ahead or simply look-ahead. While
look-ahead techniques appear complex, even software designers can master them because, at their core,
they use divide-and-conquer.
