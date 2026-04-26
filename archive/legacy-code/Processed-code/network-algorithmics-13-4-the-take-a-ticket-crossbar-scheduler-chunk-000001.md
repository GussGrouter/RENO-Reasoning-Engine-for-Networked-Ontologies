# network-algorithmics-13-4-the-take-a-ticket-crossbar-scheduler (chunk 000001)

# Network Algorithmics — 13.4 The take-a-ticket crossbar scheduler (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 364
- Slice: from `13.4 The take-a-ticket crossbar scheduler` up to next detected section heading

---

13.4 The take-a-ticket crossbar scheduler
The simplest crossbar is an array of N input buses and N output buses, as shown in Fig. 13.3. Thus
if line card R wishes to send data to line card S, input bus R must be connected to output bus S. The
simplest way to make this connection is via a “pass” transistor, as shown in Fig. 13.4. For every pair
of input and output buses, such as R and S, there is a transistor that when turned on connects the two
buses. Such a connection is known as a crosspoint. Notice that a crossbar with N inputs and N outputs
has N 2 crosspoints, each of which needs a control line from the scheduler to turn it on or off.
     While N 2 crosspoints seem large, easy VLSI implementation via transistors makes pin counts, card
connector technologies, etc., still more limiting factors in building large switches. Thus most routers
and switches built before 2002 use simple crossbar-switch backplanes to support 16–32 ports. Notice
that multicast is trivially achieved by connecting input bus R to all the output buses that wish to receive
from R. However, scheduling multicast is tricky.
     In practice, only older crossbar designs use pass transistors. This is because the overall capacitance
(Chapter 2) grows very large as the number of ports increases. This in turn increases the delay to send a
signal, which becomes an issue at higher speeds. Modern implementations often use large multiplexer
trees per output or tristate buffers (Alleyne, 2002; Turner, 2002). Higher-performance systems even
pipeline the data flowing through the crossbar using some memory (i.e., a gate) at the crosspoints.
     Thus the design of a modern crossbar switch is actually quite tricky and requires careful attention to
physical-layer considerations. However, crossbar-design issues will be ignored in this chapter to con-
centrate on the algorithmic issues related to switch scheduling. But, what should scheduling guarantee?
     For correctness, the control logic must ensure that every output bus is connected to at most one
input bus (to prevent inputs from mixing). However, for performance, the logic must also maximize the
number of line-card pairs that communicate in parallel. While the ideal parallelism is achieved if all
N output buses are busy at the same time, in practice parallelism is limited by two factors. First, there
may be no data for certain output line cards. Second, two or more input line cards may wish to send
data to the same output line card. Since only one input can win at a time, this limits data throughput if
the other “losing” input cannot send data.

338       Chapter 13 Switching

FIGURE 13.4
Connecting input from Line Card R to Line Card S by turning the pass transistor connecting the two buses. Modern
crossbars replace this simplistic design by multiplexer trees to reduce capacitance.
