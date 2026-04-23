# network-algorithmics-13-18-1-measuring-switch-cost (chunk 000001)

# Network Algorithmics — 13.18.1 Measuring switch cost (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 391
- Slice: from `13.18.1 Measuring switch cost` up to next detected section heading

---

13.18.1 Measuring switch cost
Before studying switch scaling, it helps to understand the most important cost metrics of a switch.
We identify two key cost metrics: the number of crosspoints in the crossbar and the complexities of
the matching algorithm. They correspond to the complexities of the crossbar hardware and software,
respectively.

Metric #1: the number of crosspoints
In the early days of telephone switching, crosspoints were electromagnetic switches, and thus the N 2
crosspoints of a crossbar were a major cost. Even today, this is a major cost for very large switches of
size 1000. But, because crosspoints can be thought of as just transistors, they take up very little space
on a VLSI die.3
    The real limits for electronic switches are pin limits on ICs. For example, given current pin limits
of around 1000, of which a large number of pins must be devoted to other factors, such as power and
ground, even a single bit slice of a 500-by-500 switch is impossible to package in a single chip. Of
course, one could multiplex several crossbar inputs on a single pin, but that would slow down the speed
of each input to half the I/O speed possible on a pin.
    Thus while the crossbar does indeed require N 2 crosspoints (and this indeed does matter for large
enough N), for values of N up to 200, much of the crosspoint complexity is contained within chips.
Thus one places the largest crossbar one can implement within a chip and then one interconnects these
chips to form a larger switch. Thus the dominant cost of the composite switch is the cost of the pins and
the number of links between chips. Since these last two are related (most of the pins are for input and
output links), the total number of pins is a reasonable cost measure. More refined cost measures take
into account the type of pins (backplane, chip, board, etc.) because they have different costs.
    Other factors that limit the building of large monolithic crossbar switches are the capacitive loading
on the buses, scheduler complexity, and issues of rack space and power. First, if one tries to build a
256-by-256 switch using the crossbar approach of 256 input and output buses, the loading will prob-
ably result in not meeting the speed requirements for the buses. Second, note that some centralized
algorithms, such as iSLIP, that require N 2 bits of scheduling state will not scale well to large N .

3 However, over time, the number of crosspoints again may begin to matter for optical switches!

13.18 Scaling to larger and faster switches              365

Third, many routers are limited by availability requirements to placing only a few (or often one)
ports in a line card. Similarly, for power and other reasons, there are often strict requirements on the
number of line cards that can be placed in a rack. Thus a router with a large port count is likely to
be limited by packaging requirements to use a multirack, multichassis solution consisting of several
smaller fabrics connected together to form a larger composite router.
