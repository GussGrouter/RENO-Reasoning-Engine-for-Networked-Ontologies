# network-algorithmics-13-18-3-clos-networks-for-medium-sized-routers (chunk 000001)

# Network Algorithmics — 13.18.3 Clos networks for medium-sized routers (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 393
- Slice: from `13.18.3 Clos networks for medium-sized routers` up to next detected section heading

---

13.18.3 Clos networks for medium-sized routers
Despite the lack of current focus on crosspoints in VLSI technology, our survey of scalable fabrics
for routers begins by looking at the historically earliest proposal for a scalable switch fabric. Charles
Clos first proposed his idea in 1955 to reduce the expense of electromechanical switching in telephone
switches. Fortunately, the design also reduces the number of components and links required to connect
up a number of smaller switches. It is thus useful in a present-day context. Specifically, a Clos network
appears to be used in the Juniper Networks T-series multichassis router product, introduced 47 years
later, in 2002.
    The basic Clos network uses a simple divide-and-conquer (P15) approach to reducing crosspoints
by switching in three stages, as shown in Fig. 13.16. The first stage divides the N total inputs into
groups of n inputs each, and each group of n inputs is switched to the second stage by a small (n-by-k)
switch. Thus there are N/n “small” switches in the first stage.
    The second stage consists of k switches, each of which is an N/n-by-N/n switch. Each of the
k outputs of each first-stage switch is connected in order to all the k second-stage switches. More
precisely, output j of switch i in the first stage is connected to input i of switch j in the second stage.
The third stage is a mirror reversal of the first stage, and the interconnections between the second and
third stages are also the mirror reversal of those between the first and second stages. The view from

13.18 Scaling to larger and faster switches               367

outputs leftward to the middle stage is the same as the view from inputs to the middle stage. More
precisely, each of the N/n outputs of the first stage is connected in order to the inputs of the third stage.
    A switch is said to be nonblocking if, whenever the input and output are free, a connection can be
made through the switch using free resources. Thus a crossbar is always nonblocking by selecting the
crosspoint corresponding to the input–output pair, which is never used for any other pair. On the other
hand, in Fig. 13.16 every input switch has only k connections to the middle stage, and every middle
stage has only one path to any particular switch in the third stage. Thus for small k, it is easily possible
to block a new connection because there is no path from an input I to a middle-stage switch that has a
free line to an output O.
